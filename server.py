#!/usr/bin/env python

import json
import pickle

from flask import Flask
from flask import abort, jsonify, redirect, session, url_for
from flask import request as req
from oauth2client import client
import httplib2

from user import User
from utils import templated, SessionCredStorage

app = Flask(__name__)
app.config['DEBUG'] = True
app.secret_key = 'DEV_SECRET_KEY'

ROOT_URL = "https://crest-tq.eveonline.com"

client.REFRESH_STATUS_CODES = (400,)
oa2flow = client.OAuth2WebServerFlow(
    client_id = "350c3b990af74ce58c2713e6e8a95c2c",
    client_secret = "3e4rOgOsLjnrn5KfgkBZQ6l9UnI7uBfbqHRGjGOz",
    auth_uri = "https://login.eveonline.com/oauth/authorize",
    token_uri = "https://login.eveonline.com/oauth/token",
    redirect_uri = "https://starroamer.mattic.org/auth",
    scope="publicData characterFittingsRead characterLocationRead",
)

@app.route('/', endpoint="index")
@templated()
def hello():
    user = pickle.loads(session.get('user'))
    return {'user': user}
    try:
        cred = SessionCredStorage().get()
        return {"auth": "ok"}
    except TypeError:
        pass

@app.route('/api')
@templated()
def api():
    pass

@app.route('/api/get')
def api_get():
    cred = SessionCredStorage().get()
    path = req.args.get('path')
    if not path:
        return abort(400)
    http = httplib2.Http()
    http = cred.authorize(http)
    (header, content) = http.request("%s%s" % (ROOT_URL, path), "GET")
    return jsonify(header=header, data=json.loads(content))
    return "<pre>%s<hr>%s" % (
        json.dumps(header, indent=4),
        json.dumps(json.loads(content), indent=4)
    )

@app.route('/cred')
def cred():
    cred = SessionCredStorage().get()
    return "<pre>%s</pre>" % (
        json.dumps(json.loads(cred.to_json()), indent=4)
    )

@app.route('/verify')
def verify():
    cred = SessionCredStorage().get()
    path = "https://login.eveonline.com/oauth/verify"
    http = httplib2.Http()
    http = cred.authorize(http)
    (header, content) = http.request("%s" % (path), "GET")
    data = json.loads(content)
    print(data.get("CharacterName", "Unknown"))
    return "<pre>%s<hr>%s" % (
        json.dumps(header, indent=4),
        json.dumps(json.loads(content), indent=4)
    )

@app.route('/refresh')
def refresh():
    pass

@app.route('/auth/go', endpoint="auth.start")
def auth_start():
    return redirect(oa2flow.step1_get_authorize_url())

@app.route('/auth', endpoint="auth.back")
def auth_back():
    code = req.args.get('code')
    SessionCredStorage().put(oa2flow.step2_exchange(code))
    # Grabbing and storing user identity
    cred = SessionCredStorage().get()
    path = "https://login.eveonline.com/oauth/verify"
    http = httplib2.Http()
    http = cred.authorize(http)
    (header, content) = http.request("%s" % (path), "GET")
    session['user'] = pickle.dumps(User.from_json(content))
    # Back home
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
