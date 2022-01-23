from bitcoin import *


private_key = random_key()

print(private_key)

public_key = privtopub('5JxoNJRdXYappAWRVxYdXEgV3mMNJxuZX1xnUcMc65B23D1sH3a')


address = pubtoaddr(public_key)
print(address)
