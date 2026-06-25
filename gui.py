from tkinter import *
from master import *
from security import decrypt
import os
from tkinter import messagebox 


class Mainwindow:
    def __init__(self, vault):
        self.bg="#1e1e1e"
        self.panel="#252526"
        self.text="#d4d4d4"
        self.accent="#007acc"
        self.entry="#3c3c3c"

        self.vault=vault
        self.clogin=Tk()
        self.clogin.title("Login")
        self.clogin.geometry("350x350")
        self.clogin.configure(bg=self.bg)
        self.icon=PhotoImage(file="vault.png")
        self.clogin.iconphoto(True,self.icon)
        self.create_login()
        self.clogin.mainloop()


    def CreateMaster(self,password,confirm,slogin):
        if password!=confirm:
            return
        create_master(password)
        slogin.destroy()
        self.password_entry.delete(0,END)
        self.password_entry.focus()


    def Dashboard(self):
        self.root=Toplevel()
        self.root.title("Password Manager")
        self.root.geometry("700x500")
        self.root.configure(bg=self.bg)
        self.root.iconphoto(True,self.icon)

        left=Frame(self.root,bg=self.panel)
        left.pack(side=LEFT,fill=Y,padx=15,pady=15)

        right=Frame(self.root,bg=self.bg)
        right.pack(side=RIGHT,fill=BOTH,expand=True,padx=15,pady=15)

        add=Button(left,text="Add",width=10,bg=self.accent,fg="white",command=self.Form)
        add.pack(pady=(0,10))

        edit=Button(left,text="Edit",width=10,bg=self.accent,fg="white",command=self.Edit)
        edit.pack(pady=10)

        delete=Button(left,text="Delete",width=10,bg=self.accent,fg="white",command=self.Delete)
        delete.pack(pady=10)

        top=Frame(right,bg=self.bg)
        top.pack(fill=X)

        show=Button(left, text="Show",width=10,bg=self.accent,fg="white",command=self.Show)
        show.pack(pady=10)

        self.search_entry=Entry(top,bg=self.entry,fg=self.text,insertbackground=self.text)
        self.search_entry.pack(side=LEFT,fill=X,expand=True,padx=(0,10))
        search=Button(top,text="Search",width=10,bg=self.accent,fg="white",command=self.Search)
        search.pack(side=RIGHT)
        self.listbox=Listbox(right,bg=self.panel,fg=self.text,selectbackground=self.accent)
        self.listbox.pack(fill=BOTH,expand=True,pady=(15,0))
        self.LoadData()
        self.root.protocol("WM_DELETE_WINDOW",self.root.destroy)
    

    def Show(self):
        selection=self.listbox.curselection()
        if selection==():
            return
        index=selection[0]
        accounts=self.vault.getall_account()
        account=accounts[index]
        password=decrypt(account['encrypted_pswd'])
        messagebox.showinfo("Password",password)


    def Login(self):
        password=self.password_entry.get()
        if verify_master(password):
            self.clogin.withdraw()
            self.Dashboard()


    def create_login(self):
        self.login_image=self.icon.subsample(13,13)
        image=Label(self.clogin,image=self.login_image,bg=self.bg)
        image.grid(row=0,column=0,columnspan=2,pady=(20,30))

        password=Label(self.clogin,text="Enter Password:",bg=self.bg,fg=self.text)
        password.grid(row=1,column=0,padx=10,pady=10)

        self.password_entry=Entry(self.clogin,width=25,show="*",bg=self.entry,fg=self.text,insertbackground=self.text)
        self.password_entry.grid(row=1,column=1,padx=10,pady=10)

        login=Button(self.clogin,text="Login",width=12,bg=self.accent,fg="white",command=self.Login)
        login.grid(row=2,column=0,pady=30)

        if not os.path.exists('master.json'):
            signin=Button(self.clogin,text="Sign In",width=12,bg=self.accent,fg="white",command=self.Sign_in)
            signin.grid(row=2,column=1,pady=30)


    def Sign_in(self):
        slogin=Toplevel(self.clogin)

        slogin.title("Sign In")
        slogin.geometry("450x250")

        slogin.configure(bg=self.bg)
        slogin.iconphoto(True, self.icon)

        password=Label(slogin,text="Enter Password:",bg=self.bg,fg=self.text)
        password.grid(row=0,column=0,padx=10,pady=20)

        password_entry=Entry(slogin,width=25,show="*",bg=self.entry,fg=self.text,insertbackground=self.text,relief=FLAT)
        password_entry.grid(row=0,column=1,padx=10,pady=20)

        confirm=Label(slogin,text="Confirm Password:",bg=self.bg,fg=self.text)
        confirm.grid(row=1,column=0,padx=10,pady=20)

        confirm_entry=Entry(slogin,width=25,show="*",bg=self.entry,fg=self.text,insertbackground=self.text,relief=FLAT)
        confirm_entry.grid(row=1,column=1,padx=10,pady=20)

        signin=Button(slogin,text="Sign In",width=15,bg=self.accent,fg="white",relief=FLAT,command=lambda:self.CreateMaster(password_entry.get(),confirm_entry.get(),slogin))
        signin.grid(row=2,column=0,columnspan=2,pady=30)


    def Form(self,index=None,account=None):

        form=Toplevel(self.root)
        form.iconphoto(True,self.icon)
        form.configure(bg=self.bg)

        web_label=Label(form,text="Website:",padx=10,pady=10,bg=self.bg,fg=self.text)
        web_label.grid(row=0,column=0)

        web_entry=Entry(form,bg=self.entry,fg=self.text,insertbackground=self.text,relief=FLAT)
        web_entry.grid(row=0,column=1)

        user_label=Label(form,text="Username:",padx=10,pady=10,bg=self.bg,fg=self.text)
        user_label.grid(row=1,column=0)

        user_entry=Entry(form,bg=self.entry,fg=self.text,insertbackground=self.text,relief=FLAT)
        user_entry.grid(row=1,column=1)

        pasw_label=Label(form,text="Password:",padx=10,pady=10,bg=self.bg,fg=self.text)
        pasw_label.grid(row=2,column=0)

        pasw_entry=Entry(form,bg=self.entry,fg=self.text,insertbackground=self.text,relief=FLAT)
        pasw_entry.grid(row=2,column=1)

        if account:
            web_entry.insert(0,account['website'])
            user_entry.insert(0,account['username'])
            pasw_entry.insert(0,decrypt(account['encrypted_pswd']))
            save_butt=Button(form,text="Save",padx=20,pady=10,bg=self.accent,fg="white",relief=FLAT,command=lambda:self.SaveEdit(form,index,web_entry.get(),user_entry.get(),pasw_entry.get()))

        else:
            save_butt=Button(form,text="Save",padx=20,pady=10,bg=self.accent,fg="white",relief=FLAT,command=lambda:self.SaveNew(form,web_entry.get(),user_entry.get(),pasw_entry.get()))

        save_butt.grid(row=3,column=0,columnspan=2)
 

    def SaveNew(self,form,web,user,pasw):
        self.vault.add_account(web,user,pasw)
        self.LoadData()
        form.destroy()


    def SaveEdit(self,form,index,web,user,pasw):
        self.vault.update_account(index,web,user,pasw)
        self.LoadData()
        form.destroy()


    def LoadData(self):
        accounts=self.vault.getall_account()

        self.listbox.delete(0,END)

        for account in accounts:
            self.listbox.insert(END,f"{account['website']}:{account['username']}")


    def Search(self):
        search=self.search_entry.get()

        result=self.vault.search_account(search)

        self.listbox.delete(0,END)

        for account in result:
            self.listbox.insert(END,f"{account['website']}:{account['username']}")


    def Delete(self):
        selection=self.listbox.curselection()
        if selection==():
            return
        index=selection[0]
        self.vault.delete_account(index)
        self.LoadData()


    def Edit(self):
        selection=self.listbox.curselection()
        if selection==():
            return

        index=selection[0]

        accounts=self.vault.getall_account()

        account=accounts[index]

        self.Form(index,account)
