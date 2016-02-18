#!/usr/bin/env python
import os
from flup.server.fcgi import WSGIServer
import server

wsgi = WSGIServer(server.app,
    bindAddress="/var/www/run/starroamer.sock", umask=0002)

print("running as process %s" % os.getpid())

while wsgi.run():
    reload(server)
    wsgi.application = server.app
    print("application reloaded")
