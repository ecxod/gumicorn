#
# This file is part of gumicorn released under the MIT license.
# See the NOTICE for more information.

import pytest
import sys

def test_import():

    try:
        import eventlet
    except AttributeError:
        if (3,13) > sys.version_info >= (3, 12):
            pytest.skip("Ignoring eventlet failures on Python 3.12")
        raise
    __import__('gumicorn.workers.geventlet')
