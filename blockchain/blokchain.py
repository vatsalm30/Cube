import json
from block import Block
from transaction import Transaction
import time


class Blockchain():
    def __init__(self):
        self.blockchain = []
        self.transactions = []
        self.can_add_txn = False
        self.can_create_block = True
        self.transactions_for_block = []
        self.pending_transaction = []

    def create_block(self, txn):
        self.can_add_txn = True
        self.can_create_block = False
        time.sleep(1)
        self.can_add_txn = False
        self.can_create_block = True
        self.transactions_for_block.append(txn)
        block = Block(len(self.blockchain) + 1,
                      self.blockchain[len(self.blockchain)-1].hash, self.transactions_for_block)

        self.minePendingTransactions("", block)
        for txn in self.transactions_for_block:
            self.transactions.append(txn)
        self.transactions_for_block = []
        self.can_create_block = True

    def minePendingTransactions(self, miner, newBlock):

        # transactionSlice = self.pendingTransactions[i:end]

        # newBlock = Block(transactionSlice, datetime.now().strftime(
        # "%m/%d/%Y, %H:%M:%S"), len(self.chain))
        # print(type(self.getLastBlock()));
        newBlock.mineBlock()
        self.blockchain.append(newBlock)

        # payMiner = Transaction("Miner Rewards", miner, self.minerRewards)
        # self.pendingTransactions = [payMiner]
        return True

    def txn(self, sender, reciver, amt):
        txn = Transaction(sender, reciver, amt, len(self.transactions) + 1)
        if self.can_create_block and self.can_add_txn == False:
            self.create_block(txn)
            return
        if self.can_add_txn and self.can_create_block == False:
            self.transactions_for_block.append(txn)
            return

    def create_genesis(self):
        block = Block(1, '', [])
        block.nonce
        self.minePendingTransactions("", block)
        self.blockchain.append(block)

    def json_encode(self):
        blocks = {}

        for block in self.blockchain:
            blocks['block'+str(block.block_location)] = {
                'hash': block.hash
            }

        s = json.dumps(blocks)

        print(s)

        self.blockchain = []


b = Blockchain()
b.create_genesis()
b.txn("Billy", "Bobby", 10)
b.txn("Vatsal", "Maira", 15)
b.json_encode()

for block in b.blockchain:
    print(block.__str__())
    for txn in block.transactions:
        print(txn.__str__())
    print()
    print()
print(b.transactions[1].__str__())
