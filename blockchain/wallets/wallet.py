from bitcoin import *


def create_keys():
    priv_key = random_key()
    address = pubtoaddr(privtopub(priv_key))
    return priv_key, address


def sign_txn(address, priv_key):
    check_add = pubtoaddr(privtopub(priv_key))
    if check_add == address:
        return True
    return False


def check_length(key, public):
    if public:
        if len(key) != 34:
            return False
        return True

    if (public != True):
        if len(key) != 64:
            return False
        return True
