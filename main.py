from vault import Vault
from gui import Mainwindow
from storage import *
from security import *
import os

create_database()

if not os.path.exists('secret.key'):
    generate_key()

vault=Vault()

app=Mainwindow(vault)
