from datetime import datetime
import hashlib


class Transaction():
    def __init__(self, sender, reciver, amt, txn_location):
        self.sender = sender
        self.reciver = reciver
        self.time = datetime.now()
        self.amt = amt
        self.txn_location = txn_location
        self.hash = self.calculate_hash()

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

    def __str__(self):
        return "Transaction Hash: " + str(self.hash) + "\nReciver: " + str(self.reciver) + "\nSender: " + str(self.sender) + "\nAmount: " + str(self.amt) + "\n--------------"
