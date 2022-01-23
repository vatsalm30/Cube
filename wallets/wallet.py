from bitcoin import *


def create_keys():
    priv_key = random_key()
    address = pubtoaddr(privtopub(priv_key))
    return priv_key, address


def sign_txn(address, priv_key):
    if len(priv_key) != 64:
        print("error")
        return False
    check_add = pubtoaddr(privtopub(priv_key))
    if check_add == address:
        return True
    else:
        return False


priv_key, address = create_keys()

print(sign_txn(address, "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))
