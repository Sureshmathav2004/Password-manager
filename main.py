from tkinter import *
from tkinter import messagebox

def Add():
    username=user.get()
    password=password1.get()
    
    if username and password:
        with open("simple.txt",'a') as f:
            f.write(f"{username} {password}\n")
        messagebox.showinfo("Success","Password added !!")
    else:
        messagebox.showinfo("Error","Please Enter Both Fields")

def Get():
    username=user.get()
    password={}
    try:
        with open("simple.txt","r") as f:
            for k in f:
                s=k.split(" ")
                password[s[0]]=s[1]
    except:
        print("Error in Getting data")
    
    if password:
        mess="your password"
        for i in password:
            if i==username:
                mess+=f"{username} {password[i]}\n"
                break
            else:
                mess+="No such username Exist"
        messagebox.showinfo("Password is: ",mess)
    else:
        messagebox.showinfo("Password is:","Empty List!!")
        
def Getlist():
    username=user.get()
    password={}
    try:
        with open("simple.txt","r") as f:
            for k in f:
                s=k.split(" ")
                password[s[0]]=s[1]
    except:
        print("NO Password Found")
    
    if password:
        mess="your password"
        for i in password:
            if i==username:
                mess+=f"{username} {password[i]}\n"
            else:
                mess+="No such username Exist"
            messagebox.showinfo("Password is:",mess)
    else:
        messagebox.showinfo("Password is:","Empty List!!")

def Delete():
    username=user.get()
    
    temp=[]
    
    try:
        with open("simple.txt","r") as f:
            for i in f:
                s=i.split(" ")
                if s[0] != username:
                    temp.append(f"{s[0]} {s[1]}")
        with open("simple.txt","w") as f:
            for line in temp:
                f.write(line)
        messagebox.showerror("Success", f"User {username} deleted successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Error deleting user {username}: {e}")
        


if __name__=="__main__":
    a=Tk()
    a.geometry('900x600')
    a.title("Password Manager")
    
    '''username'''
    Label(a,text='USERNAME').grid(row=0,column=0,padx=15,pady=15)
    user=Entry(a)
    user.grid(row=0,column=1,padx=15,pady=15)
    
    '''password'''
    Label(a,text='PASSWORD').grid(row=1,column=0,padx=15,pady=15)
    password1=Entry(a)
    password1.grid(row=1,column=1,padx=15,pady=15)
    
    '''add button'''
    b=Button(a,text='ADD',command=Add)
    b.grid(row=5,column=0,padx=15,pady=15)
    
    '''Get button'''
    c=Button(a,text='GET',command=Get)
    c.grid(row=5,column=5,padx=20,pady=20)
    
    '''List button'''
    d=Button(a,text='LIST',command=Getlist)
    d.grid(row=6,column=0,padx=15,pady=15)
    
    '''Delete button'''
    e=Button(a,text='DELETE',command=Delete)
    e.grid(row=6,column=5,padx=15,pady=15)
    
    a.mainloop()
    
