from tkinter import *
from tkinter .font import Font
from tkinter import messagebox
sai=Tk()
sai.geometry("500x500")
sai.resizable(height="false",width="false")
sai.title("Login page")
myfont=Font(family="times",size=20,weight="bold")
subf=Font(family="time",size=40,weight='bold')
sai.config(bg='white')
sai.iconbitmap("icon.ico")
def reset():
    print('reset all')
    messagebox.showinfo('Message','reset all your datas')

def submit():
    variable=Label(sai,text='success',fg='green',font=myfont)
    variable.pack()

lab=Label(sai,text="Registration form",font=myfont,bg="#0a3d62",fg='white',padx=120,pady=0,relief="raised")
lab.pack()

sub=Button(sai,text="submit",bg='red',fg='white',padx=50,pady=10,font=subf,command=submit)
sub.pack(side='bottom')
re=Button(sai,text="Reset",bg='blue',fg='white',width=20,font=myfont,activebackground='#009432',activeforeground='white',command=reset)
re.pack(fill='x')


sai.mainloop()


# text box


from tkinter import *
from tkinter  import  messagebox
form=Tk()
form.wm_geometry('500x500')
def ok():
    data=Name.get()
    # lam=Label(form,text=data,font=('time',30),fg='red')
    # lam.pack()
    messagebox.showinfo("message",data)

def no():
    Name.delete(0,END)

def submit():
    if(c1.get()==1):
        # val=chk1.cget('text')
          val=c1.get()
          messagebox.showinfo(val)


def clear():
    messagebox.showinfo()



#text box

Name=Entry(form,width=50,font=('time',10),bg='red',fg='white',selectbackground='black',selectforeground='yellow',show='*****')
Name.pack()

but=Button(form,text='submit',font=('times',16),width=10,padx=50,bg='yellow',command=ok)
but.pack()

cle=Button(form,text='clear',command=no)
cle.pack()
form.mainloop()
