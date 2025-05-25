#
# This file is part of gumicorn released under the MIT license.
# See the NOTICE for more information.
#
# Example code from Eventlet sources

from gumicorn import __version__


def app(environ, start_response):
    """Simplest possible application object"""

    if environ['REQUEST_METHOD'].upper() != 'POST':
        data = b'Hello, World!\n'
    else:
        data = environ['wsgi.input'].read()

    status = '200 OK'

    response_headers = [
        ('Content-type', 'text/plain'),
        ('Content-Length', str(len(data))),
        ('X-Gumicorn-Version', __version__)
    ]
    start_response(status, response_headers)
    return iter([data])
