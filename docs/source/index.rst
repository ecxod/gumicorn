======================
Gunicorn - WSGI server
======================

.. image:: _static/gumicorn.png

:Website: http://gumicorn.org
:Source code: https://github.com/ecxod/gumicorn
:Issue tracker: https://github.com/ecxod/gumicorn/issues
:IRC: ``#gumicorn`` on Libera Chat
:Usage questions: https://github.com/ecxod/gumicorn/issues

Gunicorn 'Green Unicorn' is a Python WSGI HTTP Server for UNIX. It's a pre-fork
worker model ported from Ruby's Unicorn project. The Gunicorn server is broadly
compatible with various web frameworks, simply implemented, light on server
resources, and fairly speedy.

Features
--------

* Natively supports WSGI, Django, and Paster
* Automatic worker process management
* Simple Python configuration
* Multiple worker configurations
* Various server hooks for extensibility
* Compatible with Python 3.x >= 3.7


Contents
--------

.. toctree::
    :maxdepth: 2

    install
    run
    configure
    settings
    instrumentation
    deploy
    signals
    custom
    design
    faq
    community
    news
