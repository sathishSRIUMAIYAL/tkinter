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

# check button

from tkinter import *
from tkinter import messagebox
sai=Tk()
sai.geometry('500x500')
sai.title('sathiahkumar')
sai.iconbitmap('icon.ico')

def success():
    if (c1.get()==1):
        val=c1.get()
        messagebox.showinfo('message',val)

    if (c2.get()==1):
        va=c2.get()
        messagebox.showinfo('message',va)

    if c3.get()==1:
        val=c3.get()
        messagebox.showinfo('message',val)


def clear():
    cc1.deselect()
    messagebox.showinfo()



c1=IntVar()
c2=IntVar()
c3=IntVar()

l=Label(sai,text='chooes',bg='red',fg='white',font=('time',10),padx=10,pady=10,width=10).grid(row=0,column=0)

cc1=Checkbutton(sai,text='Amma',variable=c1,onvalue=1,offvalue=0).grid(row=1,column=0)
cc2=Checkbutton(sai,text='Appa',variable=c2,onvalue=1,offvalue=0).grid(row=1,column=1)
cc3=Checkbutton(sai,text='Me',variable=c3,onvalue=1,offvalue=0).grid(row=1,column=2)

sub=Button(sai,text='submit',bg='blue',padx=40,pady=10,width=30,command=success).grid(row=2,column=0)
cle=Button(sai,text='clear',command=clear).grid(row=4,column=2)

sai.mainloop()


# radio box

from tkinter import *
sai=Tk()
sai.geometry('500x500')
l=Label(sai,text='Radio Button',relief="raised",width=30)
l.pack()
gender=IntVar()

Bmale=Radiobutton(sai,text='Male',variable=gender,value=1)
Fmale=Radiobutton(sai,text='Fmale',variable=gender,value=2)
Bmale.pack()
Fmale.pack()


sai.mainloop()


#combobox

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

sai=Tk()
sai.geometry('500x500')
sai.title('combo box')

def comboclick(event):
    data=cb.get()
    messagebox.showinfo('message',data)


l=Label(sai,text='combo box',relief='raised',bg='blue')
l.pack(fill=X)

cb=ttk.Combobox(sai,width=30)
cb['values']=('c','c++','java','python')
cb.current(3)
cb.bind('<<ComboboxSelected>>',comboclick)
cb.pack(pady=30)

sai.mainloop()


# grid

from tkinter import *
sai=Tk()
sai.geometry('500x500')
sai.title('Login page...')
sai.iconbitmap('icon.ico')

l=Label(sai,text='Registration...',font=('time',16,'bold'),fg='green',pady=10).grid(columnspan=2)
l1=Label(sai,text='Username',font=('time',16,'bold')).grid(row=1,column=0,pady=10)
txName=Entry(sai,font=('time',14,'bold')).grid(row=1,column=1)
l2=Label(sai,text='Password',font=('time',16,'bold')).grid(row=2,column=0,pady=10)
txPassword=Entry(sai,font=('time',14,'bold')).grid(row=2,column=1)
l3=Label(sai,text='E-mail',font=('time',16,'bold')).grid(row=3,column=0,pady=10)
teemail=Entry(sai,font=('time',14,'bold')).grid(row=3,column=1)

b=Button(sai,text='Submit',bg='green',fg='white',padx=20,pady=5,width=5,font=('time',15,'bold')).grid(row=4,column=1,sticky=W)
c=Button(sai,text='Clear',bg='red',fg='white',padx=20,pady=5,width=5,font=('time',15,'bold')).grid(row=4,column=1,sticky=E)


sai.mainloop()



# frame



from tkinter import *
sai=Tk()
sai.title('frame')
sai.geometry('800x400')


frame1=Frame(sai,highlightbackground="black",highlightthickness=2,padx=50,pady=50)
frame1.grid()

l1=Label(frame1,text='Registration...',font=('times',25,'bold'),fg='green')
l1.grid(columnspan=2)

l2=Label(frame1,text='Name',font=('times',15,"bold"))
l2.grid(row=2,column=0,pady=10)
txtname=Entry(frame1,font=('times',15,"bold"))
txtname.grid(row=2,column=1)

l3=Label(frame1,text='Password',font=('times',15,"bold"))
l3.grid(row=3,column=0,pady=10)
txtpassword=Entry(frame1,font=('times',15,"bold"))
txtpassword.grid(row=3,column=1)

l4=Label(frame1,text="Com_Password",font=('times',15,"bold"))
l4.grid(row=4,column=0,pady=10)
txtC_password=Entry(frame1,font=('times',15,"bold"),show='-')
txtC_password.grid(row=4,column=1)

sub=Button(frame1,text='Submit',padx=20,pady=10,bg='green',fg='white')
sub.grid(row=5,column=1,sticky=W,pady=10)
cle=Button(frame1,text='Clear',padx=20,pady=10,bg='red',fg='white')
cle.grid(row=5,column=1,sticky=E)



frame2=Frame(sai,highlightbackground="black",highlightthickness=2,padx=20,pady=20)
frame2.grid(row=0,column=1,padx=50,pady=50)
l1=Label(frame2,text='login',font=('times',25,'bold'),fg='green')
l1.grid(columnspan=2,pady=10)

l2=Label(frame2,text='Name',font=('times',15,"bold"))
l2.grid(row=2,column=0,pady=10)
txtname=Entry(frame2,font=('times',15,"bold"))
txtname.grid(row=2,column=1)

l3=Label(frame2,text='Password',font=('times',15,"bold"))
l3.grid(row=3,column=0,pady=10)
txtpassword=Entry(frame2,font=('times',15,"bold"),show='*')
txtpassword.grid(row=3,column=1)


sub=Button(frame2,text='Submit',padx=20,pady=10,bg='green',fg='white')
sub.grid(row=5,column=1,sticky=W,pady=10)
cle=Button(frame2,text='Clear',padx=20,pady=10,bg='red',fg='white')
cle.grid(row=5,column=1,sticky=E)


sai.mainloop()



# messagebox

'''
1.show info
2.show error
3.show Warning
4.Ask question
5.Ask okcancel
6.Ask retrycancel
7.Ask yes no
8.Ask yesnocancel
'''

from tkinter import *
from tkinter import messagebox

sai=Tk()
sai.geometry('500x600')


def info():
    messagebox.showinfo('shoe info','information')

def error():
    messagebox.showerror('show errer','information')

def warning():
    messagebox.showwarning('showwarning','warning')

def question():
    messagebox.askquestion('question','yes or no')

def okcancel():
    messagebox.askokcancel('show ok','as you wish')

def retrycancel():
    messagebox.askretrycancel('retry','as yor wish')

def yesno():
    messagebox.askyesno('ok','as you wish')
def yesnocancel():
    messagebox.askyesnocancel('ask yes no cancel','say')







info=Button(sai,text='Show info',command=info)
info.grid(row=0,column=0,pady=5)

Error=Button(sai,text='Show error',command=error)
Error.grid(row=1,column=0,pady=5)

Warning=Button(sai,text='Show warning',command=warning)
Warning.grid(row=2,column=0,pady=5)

Question=Button(sai,text='show Question',command=question)
Question.grid(row=3,column=0,pady=5)

OKcancel=Button(sai,text='show okcancel',command=okcancel)
OKcancel.grid(row=4,column=0,pady=5)

RetryCancel=Button(sai,text='retrycancel',command=retrycancel)
RetryCancel.grid(row=5,column=0,pady=5)

Yesno=Button(sai,text='show yesno',command=yesno)
Yesno.grid(row=6,column=0,pady=5)


Yesnocancel=Button(sai,text='yesnocansel',command=yesnocancel)
Yesnocancel.grid(row=7,column=0)



sai.mainloop()
