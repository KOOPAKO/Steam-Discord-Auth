from steam.guard import SteamAuthenticator
import json


def get_code():
    secrets = json.load(open('./mysecrets.json'))
    sa = SteamAuthenticator(secrets)
    TFAcode = sa.get_code()
    return TFAcode
