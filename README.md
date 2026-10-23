# Secure Login

A small Python login program that never stores the real password. It saves only a salted SHA-256 hash and locks after 3 failed attempts.

## Features

- Passwords are hashed with SHA-256 (`hashlib`) and never stored in plain text
- A salt is added before hashing, so the same password does not give the standard, precomputed hash
- 3 attempts allowed, with a "tries left" message
- The program locks after the third wrong password

## How it works

1. A salt is joined to the password: `salt + password`
2. The result is hashed with SHA-256
3. The hash is compared with the stored hash
4. If they match, access is granted. Otherwise, one attempt is used up.

## How to run

1. Install Python 3
2. Download `secure_login.py`
3. Run it: `python secure_login.py`
4. Enter the password when asked

## Example output

```
Password:a
wrong password, 2 tries left
Password:b
wrong password, 1 tries left
Password:c
wrong password, 0 tries left
locked
```

## Limitations

This is a learning project, not production code:

- It uses one fixed salt for everyone. Real systems use a random salt per user.
- SHA-256 is fast, which helps attackers guess passwords. Real systems use slow hashes such as scrypt, bcrypt or argon2.
- Failed attempts reset when the program restarts.

## What I learned

Hashing, salting, loops, `if/else`, and why plain-text password storage is dangerous.
