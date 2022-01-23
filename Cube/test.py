import sys
import chilkat

rsa = chilkat.CkRsa()

#  Generate a 2048-bit key.  Chilkat RSA supports
#  key sizes ranging from 512 bits to 8192 bits.
success = rsa.GenerateKey(2048)
if (success != True):
    print(rsa.lastErrorText())
    sys.exit()

# privKey is a CkPrivateKey
privKey = rsa.ExportPrivateKeyObj()

#  Get the private key in PKCS8 Base64 format
privKeyPkcs8Base64 = privKey.getPkcs8ENC("base64")

#  The key in base64 format will start similar to this:
#  MIIEvAIBADANBgkqhkiG9w0BA...
print(privKeyPkcs8Base64)
