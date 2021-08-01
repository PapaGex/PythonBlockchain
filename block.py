class Block:
    """
    Unit of storage
    storing transactions in the blockchain
    """
    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f'Block - data: {self.data}' 

def main():

    block = Block('blood')        
    print(block)
    print(f'block.py __name__: {__name__}')

if __name__ == '__main__':
    main()    