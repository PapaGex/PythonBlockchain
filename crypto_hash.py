import hashlib
import json

def crypto_hash(*args):
    """
    returns a sha-256 hash of the given argument
    """
    stringified_args = sorted(map(lambda data: json.dumps(data), args))

    joined_data = ''.join(stringified_args)

    return hashlib.sha256(joined_data.encode('utf-8')).hexdigest()
   
def main():
    print(f"crypto_hash('blood', 7, [42]): {crypto_hash('blood', 7, [42])}")
    print(f"crypto_hash(7, [42], 'blood'): {crypto_hash(7, [42], 'blood')}")

if __name__ == '__main__':
    main()    