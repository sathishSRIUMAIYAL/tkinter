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
