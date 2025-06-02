#
# This file is part of gumicorn released under the MIT license.
# See the NOTICE for more information.

from dotenv import load_dotenv
import os
import sentry_sdk

# Load environment variables from .env file (only needed locally)
load_dotenv()

# Initialize Sentry
sentry_sdk.init(
    dsn=str(os.getenv("GLITCHTIP_DSN")),
    traces_sample_rate=1.0,
    environment="production" if os.getenv("CI") else "development"
)

division_by_zero = 1 / 0

version_info = (23, 0, 0)
__version__ = ".".join([str(v) for v in version_info])
SERVER = "gumicorn"
SERVER_SOFTWARE = "%s/%s" % (SERVER, __version__)
