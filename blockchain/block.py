import hashlib
from datetime import datetime


class Block():
    def __init__(self, block_location, prev_hash, transactions):
        self.block_location = block_location
        self.prev_hash = prev_hash
        self.nonce = 0
        self.time = datetime.now()
        self.time = int(self.time.timestamp())
        self.transactions = transactions
        self.hash = self.calculate_hash()
        self.is_valid = False

    def find_encoded_string_of_transactions(self):
        result = b''
        for txn in self.transactions:
            result = str(txn.hash).encode('utf-8') + str(txn.sender).encode('utf-8') + str(txn.reciver).encode('utf-8') + str(txn.time).encode(
                'utf-8') + str(txn.amt).encode('utf-8') + str(txn.txn_location).encode('utf-8')
        return result

    def calculate_hash(self):
        h = hashlib.sha256()
        h.update(
            str(self.nonce).encode('utf-8') +
            str(self.prev_hash).encode('utf-8') +
            str(self.time).encode('utf-8') +
            str(self.block_location).encode('utf-8') +
            self.find_encoded_string_of_transactions()
        )
        return h.hexdigest()

    def __str__(self):
        return "Block Hash: " + str(self.hash) + "\nPrevious Block Hash: " + str(self.prev_hash) + "\nBlockNo: " + str(self.block_location) + "\nNonce: " + str(self.nonce) + "\n--------------"

    def mineBlock(self):
        hash_puzzle = "ac312"
        while self.hash[0:len(hash_puzzle)] != hash_puzzle:
            self.nonce += 1
            self.hash = self.calculate_hash()

        print("Block Mined!")
        return True
