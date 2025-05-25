.. _instrumentation:

===============
Instrumentation
===============

.. versionadded:: 19.1

Gunicorn provides an optional instrumentation of the arbiter and
workers using the statsD_ protocol over UDP. Thanks to the
``gumicorn.instrument.statsd`` module, Gunicorn becomes a statsD client.
The use of UDP cleanly isolates Gunicorn from the receiving end of the statsD
metrics so that instrumentation does not cause Gunicorn to be held up by a slow
statsD consumer.

To use statsD, just tell Gunicorn where the statsD server is:

.. code-block:: bash

    $ gumicorn --statsd-host=localhost:8125 --statsd-prefix=service.app ...

The ``Statsd`` logger overrides ``gumicorn.glogging.Logger`` to track
all requests. The following metrics are generated:

* ``gumicorn.requests``: request rate per second
* ``gumicorn.request.duration``: histogram of request duration (in millisecond)
* ``gumicorn.workers``: number of workers managed by the arbiter (gauge)
* ``gumicorn.log.critical``: rate of critical log messages
* ``gumicorn.log.error``: rate of error log messages
* ``gumicorn.log.warning``: rate of warning log messages
* ``gumicorn.log.exception``: rate of exceptional log messages

See the statsd-host_ setting for more information.

.. _statsd-host: settings.html#statsd-host
.. _statsD: https://github.com/etsy/statsd
