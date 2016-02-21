#!/usr/bin/env python

import json

from flask import Flask
from flask import redirect, url_for, session
from flask import request as req
from oauth2client.client import OAuth2WebServerFlow
import httplib2

from utils import templated, SessionCredStorage

app = Flask(__name__)
app.config['DEBUG'] = True
app.secret_key = 'DEV_SECRET_KEY'

ROOT_URL = "https://crest-tq.eveonline.com"

oa2flow = OAuth2WebServerFlow(
    client_id = "350c3b990af74ce58c2713e6e8a95c2c",
    client_secret = "3e4rOgOsLjnrn5KfgkBZQ6l9UnI7uBfbqHRGjGOz",
    auth_uri = "https://login.eveonline.com/oauth/authorize",
    token_uri = "https://login.eveonline.com/oauth/token",
    redirect_uri = "https://starroamer.mattic.org/auth",
    scope="",
)

@app.route('/', endpoint="index")
@templated()
def hello():
    try:
        cred = SessionCredStorage().get()
        return {"auth": "ok"}
    except TypeError:
        pass

@app.route('/api')
def api():
    cred = SessionCredStorage().get()
    path = req.args.get('path')
    http = httplib2.Http()
    http = cred.authorize(http)
    (header, content) = http.request("%s%s" % (ROOT_URL, path), "GET")
    return "<pre>%s<hr>%s" % (
        json.dumps(header, indent=4),
        json.dumps(json.loads(content), indent=4)
    )

@app.route('/auth/go', endpoint="auth.start")
def auth_start():
    return redirect(oa2flow.step1_get_authorize_url())

@app.route('/auth', endpoint="auth.back")
def auth_back():
    code = req.args.get('code')
    SessionCredStorage().put(oa2flow.step2_exchange(code))
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
