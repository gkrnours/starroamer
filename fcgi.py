#!/usr/bin/env python
from flup.server.fcgi import WSGIServer
from server import app

WSGIServer(app, bindAddress="/var/www/run/starroamer.sock").run()
