from wallets.wallet import *
from datetime import datetime
import hashlib


class Transaction():
    def __init__(self, sender, reciver, amt, txn_location):
        self.sender = sender
        self.reciver = reciver
        self.time = datetime.now()
        self.time = int(self.time.timestamp())
        self.amt = amt
        self.txn_location = txn_location
        self.hash = self.calculate_hash()
        self.is_valid = self.check_txn(self.sender, self.test_user_prompt())

    def calculate_hash(self):
        h = hashlib.sha256()
        h.update(
            str(self.sender).encode('utf-8') +
            str(self.reciver).encode('utf-8') +
            str(self.time).encode('utf-8') +
            str(self.amt).encode('utf-8') +
            str(self.txn_location).encode('utf-8')
        )
        return h.hexdigest()

    def test_user_prompt(self):
        return input("Private Key: ")

    def check_txn(self, address, private_key):
        if check_length(address, True) != True:
            print("fail 1")
            return False

        if check_length(private_key, False) != True:
            print("fail 2")
            return False

        if(sign_txn(address, private_key) == False):
            print("fail 3")

        return sign_txn(address, private_key)

    def __str__(self):
        return "Transaction Hash: " + str(self.hash) + "\nReciver: " + str(self.reciver) + "\nSender: " + str(self.sender) + "\nAmount: " + str(self.amt) + "\n--------------"
