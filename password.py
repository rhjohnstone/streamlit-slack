import hashlib


def hash_password(password: str) -> str:
    m = hashlib.sha256()
    m.update(password.encode())
    return m.hexdigest()


if __name__ == "__main__":

    import sys

    with open("hash.txt", "w") as outf:
        outf.write(hash_password(sys.argv[1]))
