class Block:
    """
    Unit of storage
    storing transactions in the blockchain
    """
    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f'Block - data: {self.data}' 
    

class Blockchain:
    """
    Blockchain is a public ledgers of transactions.
    Implemented as a list of blocks - data sets of transactions
    """
    def __init__(self):
        self.chain = []

    def add_block(self, data):
        self.chain.append(Block(data))

    def __repr__(self):
        return f'Blockchain: {self.chain}'

blockchain = Blockchain()
blockchain.add_block('one')
blockchain.add_block('two')
blockchain.add_block('three')
blockchain.add_block('four')
blockchain.add_block('five')
blockchain.add_block('six')
blockchain.add_block('seven')

print(blockchain)
