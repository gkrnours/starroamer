from os import environ as nv

try:
    client_id = nv['EVE_CLIENT_ID']
    client_secret = nv['EVE_CLIENT_SECRET']
except KeyError as e:
    print("Missing key %s" % str(e))
    exit(1)

server = {
    "auth_uri": "https://login.eveonline.com/oauth/authorize",
    "token_uri": "https://login.eveonline.com/oauth/token",
    "redirect_uri": "https://starroamer.mattic.org/auth",
}

singularity = {
    "auth_uri": "https://sisilogin.testeveonline.com/oauth/authorize",
    "token_uri": "https://sisilogin.testeveonline.com/oauth/token",
    "redirect_uri": "https://starroamer.mattic.org/auth",
}

