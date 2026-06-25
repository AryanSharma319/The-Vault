import hashlib
import json


def hashed(password):
    hashed=hashlib.sha256(password.encode()).hexdigest()
    return hashed


def create_master(password):
    password=hashed(password)

    with open('master.json','w') as file:
        json.dump({'master':password},file)


def verify_master(password):
    password=hashed(password)
    try:
        with open('master.json','r') as file:
            data=json.load(file)

        if password==data['master']:
            return True

        return False
    except FileNotFoundError:
        return False