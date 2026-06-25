import sqlite3

def create_database():
    conn=sqlite3.connect("storeroom.db")
    cur=conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                website TEXT,
                username TEXT NOT NULL,
                encrypted_pswd TEXT NOT NULL
                )""")
    conn.commit()
    conn.close()

def save_acc(web, user, pswd):
    conn=sqlite3.connect("storeroom.db")
    cur=conn.cursor()
    cur.execute("""INSERT INTO data (website, username, encrypted_pswd)
                VALUES(?,?,?)""",(web,user,pswd))
    conn.commit()
    conn.close()

def load_acc():
    conn=sqlite3.connect("storeroom.db")
    cur=conn.cursor()
    cur.execute("""SELECT * FROM data""")
    records=cur.fetchall()
    accounts=[]
    for id,website,username,encrypted_pswd in records:
        accounts.append({'id':id,'website':website, 'username':username, 'encrypted_pswd':encrypted_pswd})
    conn.close()
    return accounts

def delete_acc(account):
    conn=sqlite3.connect("storeroom.db")
    cur=conn.cursor()
    cur.execute("""DELETE FROM data
                WHERE id=?""",
                (account['id'],))

    conn.commit()
    conn.close()

def update_acc(index, website, username, encrypted):
    conn=sqlite3.connect("storeroom.db")
    cur=conn.cursor()
    accounts=load_acc()
    old=accounts[index]
    cur.execute("""UPDATE data
                SET website=?,
                username=?,
                encrypted_pswd=?
                WHERE website=?
                AND username=?
                AND encrypted_pswd=?""",
                (website,
                username,
                encrypted,
                old['website'],
                old['username'],
                old['encrypted_pswd']))
    conn.commit()
    conn.close()
