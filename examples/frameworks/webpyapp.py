# Run with
#
# $ gumicorn webpyapp:app
#

import web

urls = (
    '/', 'index'
)

class index:
    def GET(self):
        return "Hello, world!"

app = web.application(urls, globals()).wsgifunc()
