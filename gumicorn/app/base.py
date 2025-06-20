#
# This file is part of gumicorn released under the MIT license.
# See the NOTICE for more information.
import importlib.util
import importlib.machinery
import os
import sys
import traceback

from gumicorn import util
from gumicorn.arbiter import Arbiter
from gumicorn.config import Config, get_default_config_file
from gumicorn import debug


class BaseApplication:
    """
    An application interface for configuring and loading
    the various necessities for any given web framework.
    """
    def __init__(self, usage=None, prog=None):
        self.usage = usage
        self.cfg = None
        self.callable = None
        self.prog = prog
        self.logger = None
        self.do_load_config()

    def do_load_config(self):
        """
        Loads the configuration
        """
        try:
            self.load_default_config()
            self.load_config()
        except Exception as e:
            print("\nError: %s" % str(e), file=sys.stderr)
            sys.stderr.flush()
            sys.exit(1)

    def load_default_config(self):
        # init configuration
        self.cfg = Config(self.usage, prog=self.prog)

    def init(self, parser, opts, args):
        raise NotImplementedError

    def load(self):
        raise NotImplementedError

    def load_config(self):
        """
        This method is used to load the configuration from one or several input(s).
        Custom Command line, configuration file.
        You have to override this method in your class.
        """
        raise NotImplementedError

    def reload(self):
        self.do_load_config()
        if self.cfg and self.cfg.spew:
            debug.spew()

    def wsgi(self):
        if self.callable is None:
            self.callable = self.load()
        return self.callable

    def run(self):
        try:
            Arbiter(self).run()
        except RuntimeError as e:
            print("\nError: %s\n" % e, file=sys.stderr)
            sys.stderr.flush()
            sys.exit(1)


class Application(BaseApplication):

    # 'init' and 'load' methods are implemented by WSGIApplication.
    # pylint: disable=abstract-method

    def chdir(self):
        # chdir to the configured path before loading,
        # default is the current dir
        if self.cfg : os.chdir(self.cfg.chdir)

        # add the path to sys.path
        if self.cfg and self.cfg.chdir not in sys.path:
            sys.path.insert(0, self.cfg.chdir)

    def get_config_from_filename(self, filename):

        if not os.path.exists(filename):
            raise RuntimeError("%r doesn't exist" % filename)

        ext = os.path.splitext(filename)[1]

        try:
            module_name = '__config__'
            if ext in [".py", ".pyc"]:
                spec = importlib.util.spec_from_file_location(module_name, filename)
            else:
                msg = "configuration file should have a valid Python extension.\n"
                util.warn(msg)
                loader_ = importlib.machinery.SourceFileLoader(module_name, filename)
                spec = importlib.util.spec_from_file_location(module_name, filename, loader=loader_)
            if spec is not None:
                mod = importlib.util.module_from_spec(spec)
                sys.modules[module_name] = mod
                if spec and spec.loader is not None: 
                    spec.loader.exec_module(mod)
        except Exception:
            print("Failed to read config file: %s" % filename, file=sys.stderr)
            traceback.print_exc()
            sys.stderr.flush()
            sys.exit(1)

        return vars(mod)

    def get_config_from_module_name(self, module_name):
        return vars(importlib.import_module(module_name))

    def load_config_from_module_name_or_filename(self, location):
        """
        Loads the configuration file: the file is a python file, otherwise raise an RuntimeError
        Exception or stop the process if the configuration file contains a syntax error.
        """

        if location.startswith("python:"):
            module_name = location[len("python:"):]
            cfg = self.get_config_from_module_name(module_name)
        else:
            if location.startswith("file:"):
                filename = location[len("file:"):]
            else:
                filename = location
            cfg = self.get_config_from_filename(filename)

        for k, v in cfg.items():
            # Ignore unknown names
            if self.cfg: 
                if k not in self.cfg.settings:
                    continue
                try:
                    self.cfg.set(k.lower(), v)
                except Exception:
                    print("Invalid value for %s: %s\n" % (k, v), file=sys.stderr)
                    sys.stderr.flush()
                    raise

        return cfg

    def load_config_from_file(self, filename):
        return self.load_config_from_module_name_or_filename(location=filename)

    def load_config(self):
        if self.cfg is not None:
            # parse console args
            parser = self.cfg.parser()
            args = parser.parse_args()

            # optional settings from apps
            cfg = self.init(parser, args, args.args)

            # set up import paths and follow symlinks
            self.chdir()

            # Load up the any app specific configuration
            if cfg:
                for k, v in cfg.items():
                    self.cfg.set(k.lower(), v)

            env_args = parser.parse_args(self.cfg.get_cmd_args_from_env())

            if args.config:
                self.load_config_from_file(args.config)
            elif env_args.config:
                self.load_config_from_file(env_args.config)
            else:
                default_config = get_default_config_file()
                if default_config is not None:
                    self.load_config_from_file(default_config)

            # Load up environment configuration
            for k, v in vars(env_args).items():
                if v is None:
                    continue
                if k == "args":
                    continue
                self.cfg.set(k.lower(), v)

            # Lastly, update the configuration with any command line settings.
            for k, v in vars(args).items():
                if v is None:
                    continue
                if k == "args":
                    continue
                self.cfg.set(k.lower(), v)

            # current directory might be changed by the config now
            # set up import paths and follow symlinks
            self.chdir()

    def run(self):
        if self.cfg is not None:
            if self.cfg.print_config:
                print(self.cfg)

            if self.cfg.print_config or self.cfg.check_config:
                try:
                    self.load()
                except Exception:
                    msg = "\nError while loading the application:\n"
                    print(msg, file=sys.stderr)
                    traceback.print_exc()
                    sys.stderr.flush()
                    sys.exit(1)
                sys.exit(0)

            if self.cfg.spew:
                debug.spew()

            if self.cfg.daemon:
                # if os.environ.get('NOTIFY_SOCKET'):
                #     msg = "Warning: you shouldn't specify `daemon = True`" \
                #           " when launching by systemd with `Type = notify`"
                #     print(msg, file=sys.stderr, flush=True)

                util.daemonize(self.cfg.enable_stdio_inheritance)

            # set python paths
            if self.cfg.pythonpath:
                paths = self.cfg.pythonpath.split(",")
                for path in paths:
                    pythonpath = os.path.abspath(path)
                    if pythonpath not in sys.path:
                        sys.path.insert(0, pythonpath)

            super().run()
