#
# This file is part of gumicorn released under the MIT license.
# See the NOTICE for more information.

# supported gumicorn workers.
SUPPORTED_WORKERS = {
    "sync": "gumicorn.workers.sync.SyncWorker",
    "eventlet": "gumicorn.workers.geventlet.EventletWorker",
    "gevent": "gumicorn.workers.ggevent.GeventWorker",
    "gevent_wsgi": "gumicorn.workers.ggevent.GeventPyWSGIWorker",
    "gevent_pywsgi": "gumicorn.workers.ggevent.GeventPyWSGIWorker",
    "tornado": "gumicorn.workers.gtornado.TornadoWorker",
    "gthread": "gumicorn.workers.gthread.ThreadWorker",
}
