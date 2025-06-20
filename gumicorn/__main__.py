#
# This file is part of gumicorn released under the MIT license.
# See the NOTICE for more information.

from gumicorn.app.wsgiapp import run

if __name__ == "__main__":
    # see config.py - argparse defaults to basename(argv[0]) == "__main__.py"
    # todo: let runpy.run_module take care of argv[0] rewriting
    run(prog="gumicorn")
