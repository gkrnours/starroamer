from __future__ import print_function
import sys

with open("secret.py") as f:
    c = compile(f.read(), "secret.py", "exec")
data = {}
exec(c, {}, data)

if data["client_id"] == "secret" and data["secret_key"] == "terces":
    print("Did you updated secret.py with your application settings ?",
        file=sys.stderr)
    print("See https://developers.eveonline.com", file=sys.stderr)
    exit(1)

tranquility = {
    "auth": {
        "client_id": data["client_id"],
        "client_secret": data["secret_key"],
    },
    "client": {
        "auth_uri": "https://login.eveonline.com/oauth/authorize",
        "token_uri": "https://login.eveonline.com/oauth/token",
        "redirect_uri": "https://starroamer.mattic.org/auth",
    },
}

