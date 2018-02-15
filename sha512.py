import hashlib

def main():
    resultHash = hashlib.sha512("jiangang92").hexdigest()
    print resultHash

if __name__ == "__main__":
    main()
