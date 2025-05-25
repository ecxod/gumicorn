#
# This file is part of gumicorn released under the MIT license.
# See the NOTICE for more information.

def test_import():
    __import__('gumicorn.workers.ggevent')
