from security import *
from storage import *

class Vault:
    def add_account(self, website, username, password):
        encrypted=encrypt(password)
        save_acc(website, username, encrypted)
    
    def delete_account(self, index):
        accounts=load_acc()
        account=accounts[index]
        delete_acc(account)
    
    def search_account(self, search):
        accounts=load_acc()
        result=[]
        for account in accounts:
            if search.lower() in account['website'].lower():
                result.append(account)

        return result
    
    def update_account(self, index, website, username, password):
        encrypted=encrypt(password)
        update_acc(index, website, username, encrypted)
    
    def getall_account(self):
        accounts=load_acc()
        return accounts