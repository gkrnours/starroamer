from __future__ import print_function
import sys
from os import environ as nv

no_tranquility = False
no_singularity = False

try:
    eve_client_id = nv['EVE_CLIENT_ID']
    eve_client_secret = nv['EVE_CLIENT_SECRET']
except KeyError as e:
    no_tranquility = True
try:
    test_client_id = nv['TEST_CLIENT_ID']
    test_client_secret = nv['TEST_CLIENT_SECRET']
except KeyError as e:
    no_singularity = True

if no_tranquility and no_singularity:
    print("Missing env variable.", file=sys.stderr)
    print("Require EVE_CLIENT_{ID,SECRET} or TEST_CLIENT_{ID,SECRET}",
        file=sys.stderr)
    exit(1)

if not no_tranquility:
    tranquility = {}
    tranquility['auth'] = {
        "client_id": eve_client_id,
        "client_secret": eve_client_secret
    }
    tranquility['client'] = {
        "auth_uri": "https://login.eveonline.com/oauth/authorize",
        "token_uri": "https://login.eveonline.com/oauth/token",
        "redirect_uri": "https://starroamer.mattic.org/auth",
    }

if not no_singularity:
    singularity = {}
    singularity['auth'] = {
        "client_id": test_client_id,
        "client_secret": test_client_secret
    }
    singularity['client'] = {
        "auth_uri": "https://sisilogin.testeveonline.com/oauth/authorize",
        "token_uri": "https://sisilogin.testeveonline.com/oauth/token",
        "redirect_uri": "https://starroamer.mattic.org/auth",
    }

