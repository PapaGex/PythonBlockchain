import hashlib
import json

def crypto_hash(data):
    """
    returns a sha-256 hash of the given data
    """
    stringified_data = json.dumps(data)

    return hashlib.sha256(stringified_data.encode('utf-8')).hexdigest()

def main():
    print(f"crypto_hash('blood'): {crypto_hash('blood')}")

if __name__ == '__main__':
    main()    