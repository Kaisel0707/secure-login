import hashlib
salt = "x9f2k"
stored_hash ="2cb613e4af717581d87f845502658ab9267675d69e37e02c870c5e81b8405180"
failed = 0
while failed < 3:
    attempt = input("Password:")
    attempt_hash = hashlib.sha256((salt + attempt).encode()).hexdigest()
    if attempt_hash == stored_hash:
        print("access granted")
        break
    else:
        failed += 1
        print(f"wrong password, {3-failed} tries left")
if failed == 3:
    print("locked")
