import sqlite3
from sqlite3 import Error
from tkinter import *
from tkinter import messagebox
con=sqlite3.connect("Dolphin",isolation_level=None)
cur=con.cursor()
#cur.execute("DROP TABLE STOCKS")
def szero(root,l1,l3,col):
    for i,k in zip(l1,l3):
        cur.execute(f'update stocks set {col}=? where name=?',(0,i.cget('text')))
    STUI(root,4)
def update(root,l1,l2,l3,col):
    for i,j,k in zip(l1,l2,l3):
        cur.execute(f'update stocks set total=?,{col}=? where name=?',(j.cget("text"),k.cget("text"),i.cget('text')))
    STUI(root,5)
def fe(root,col):
    if col!="":
        r=cur.execute(f"select name,total,{col} from STOCKS")
        STUI(root,2,r,col)
    else:
        STUI(root,3)
def stup(e1,root3):
    na=e1.get()
    cur.execute(f'ALTER TABLE STOCKS ADD {na} int default 0 not null')
    STUI(root3,cal=1)

def addST(root4):
    root3 = Tk()
    root3.title('ST Details')
    e1 = Entry(root3, width=25)
    e1.insert(0, "enter ST name")
    e1.place(x=0, y=0)
    '''e2 = Entry(root3, width=25)
    e2.insert(0, "enter  Qty ")
    e2.place(x=0, y=50)'''
    b2 = Button(root3, text="submit", width=10, command=lambda: stup(e1,root3))
    # e3.place(x=100, y=0)
    b2.place(x=0, y=150)
    root4.destroy()
    root3.mainloop()

def STUI(root,cal=0,r="",col=''):
    def inc(j):
        if int(l3[j].cget('text'))<int(l2[j].cget('text')):
            l3[j]['text']=int(l3[j].cget('text'))+1
            l2[j]['text'] = int(l2[j].cget('text')) - 1
    def dec(j):
        if(int(l3[j].cget('text'))>0):
            l3[j]['text']=int(l3[j].cget('text'))-1
            l2[j]['text'] = int(l2[j].cget('text')) + 1
    if(cal==1):
        messagebox.showinfo(message='ST Added Succesfully')
    if (cal == 4):
        messagebox.showinfo(message='ST Stock set to zero ')
    if (cal == 5):
        messagebox.showinfo(message='ST Stock Updated')
    con.row_factory = sqlite3.Row
    curs=con.cursor()
    root3 = Tk()
    root3['bg']='white'
    root3.geometry("500x900")
    tkvar = StringVar(root3)
    c=curs.execute("select * from Stocks")
    re=c.fetchone()
    cols=re.keys()
    cord=70
    if cal==3:
        messagebox.showinfo(message="please select a ST")
    if(cal==2):
        tkvar.set(col)
        l1=[]
        l2=[]
        l3=[]
        b1=[]
        b2=[]
        j=0
        result=r.fetchall()
        l8 = Label(root3, text=col,font=['bold-italic'],fg='white',bg='black')
        l8.place(x=200,y=cord)
        cord+=30
        l4=Label(root3,text="STOCK",font=['bold'],fg='white',bg='black')
        l5 = Label(root3, text="STORE",font=['bold'],fg='white',bg='black')
        l6 = Label(root3, text="ST QTY",font=['bold'],fg='white',bg='black')
        l7 = Label(root3, text="INC/DEC",font=['bold'],fg='white',bg='black')
        l4.place(x=20,y=cord)
        l5.place(x=90,y=cord)
        l6.place(x=170,y=cord)
        l7.place(x=250,y=cord)
        cord+=30
        for i in result:
            l1.append(Label(root3,text=i[0],bg='blue',fg='black',width=10))
            l2.append(Label(root3,text=i[1],bg="Brown",fg='white',width=10))
            l3.append(Label(root3,text=i[2],bg='Yellow',fg='black',width=10))
            b1.append(Button(root3,text="-",bg="red",fg="black",command=lambda c=j:dec(c),width=2))
            b2.append(Button(root3, text="+", bg="green", fg="black", command=lambda c=j: inc(c),width=2))
            l1[j].place(x=0,y=cord)
            l2[j].place(x=80,y=cord)
            l3[j].place(x=160,y=cord)
            b1[j].place(x=240,y=cord)
            b2[j].place(x=270,y=cord)
            j+=1
            cord+=20
        b3=Button(root3,text='update',fg='blue',command=lambda:update(root3,l1,l2,l3,col))
        b3.place(x=0,y=cord)
        b4=Button(root3,text='set to zero',command=lambda:szero(root3,l1,l3,col))
        b4.place(x=100,y=cord)
    a=len(cols)
    print(a)
    ls_tech = []
    if(a>3):
        i=3
        b2 = Button(root3, text="View", command=lambda: fe(root3, tkvar.get()))
        b2.place(x=200, y=0)
        while(i<a):
            ls_tech.append(cols[i])
            i+=1
    elif(a==3):
        ls_tech.append("no technician in record \nadd technician to view records")
    l=Label(root3,text='Select ST',fg='black',bg='white')
    l.place(x=0,y=0)
    Op = OptionMenu(root3, tkvar, *ls_tech)
    Op.config(indicatoron=1,width=10,bg='brown',fg='white')
    Op.place(x=80,y=0)
    b=Button(root3,text="Add ST",command=lambda:addST(root3))
    b.place(x=0,y=30)

    root.destroy()
    root3.mainloop()

def up(e1,e2,root2):
    cur.execute('''Create table if  not exists STOCKS(SNo integer primary key autoincrement,Name varchar(50),Total int)''')
    cur.execute("insert into Stocks(Name,Total) values(?,?)",(e1.get(),e2.get()))

    root2.destroy()
    home(1)
def item(root):
    root2 = Tk()
    root2.title('Details')
    e1=Entry(root2,width=25)
    e1.insert(0,"enter Item name")
    e1.place(x=0,y=0)
    e2=Entry(root2,width=25)
    e2.insert(0, "enter total Qty of item in Store")
    '''e3=Entry(root2,width=25)
    e3.insert(0,"enter % req.")'''
    e2.place(x=0, y=50)
    b2=Button(root2,text="submit",width=10,command=lambda:up(e1,e2,root2))
    #e3.place(x=0, y=100)
    b2.place(x=0,y=150)
    root.destroy()
    root2.mainloop()
def change(e1,e2,root):
    for i,j in zip(e1,e2):
        cur.execute('update stocks set total=? where name=?',(j.cget('text'),i.cget('text')))
    root.destroy()
    home(2)
def home(a=0):
    def inc(j):
        val = int(e2[j].cget("text"))
        e2[j]["text"] = val + 1
    def dec(j):
        val = int(e2[j].cget("text"))
        if val>0:
            e2[j]["text"] = val - 1
    root = Tk()
    root.geometry("500x900")
    root.title("DOLPHIN ENTERPRISES")
    root['bg'] = 'black'
    l1 = Label(root, text="DOLPHIN STOCK \n RECORD",font=['bold',10],bg='Black',fg="White")
    l1.place(x=200, y=0)
    if (a == 1):
        messagebox.showinfo(root, message="Stock Added successfully")
    if (a == 2):
        messagebox.showinfo(root, message="Record updated successfully")
    #b = Button(root, text="i", fg="blue", bg='white', font=["Times", 9, 'bold italic'], height=1, command=det)
    #b.place(x=230, y=0)
    a = 40
    b1 = Button(root, width=10, text="Add New Item", command=lambda: item(root))
    cur.execute("select * from sqlite_master where type='table'")
    if(cur.fetchone()):
        # fetch  info from sql
        cur.execute("select name from Stocks")
        myresult2=cur.fetchall()
        cur.execute("select Total from Stocks")
        myresult3 =cur.fetchall()
        print(myresult3)
        e1 = []
        e2 = []
        b3 = []
        b4 = []
        if (len(myresult2) > 0):
            l2 = Label(root, width=10, text="STOCK", bg='black', fg='white')
            l2.place(x=0, y=40)
            l3 = Label(root, width=10, text="IN STORE", bg='black', fg='white')
            l3.place(x=90, y=40)
            l4 = Label(root, width=10, text="INC/DEC", bg='black', fg='white')
            l4.place(x=170, y=40)
            a = (len(myresult2) + 3) * 25
            for i in range(len(myresult2)):
                e1.append(Label(root, width=10, bg='pink', fg='blue', text=myresult2[i]))
                e1[i].place(x=0, y=(i + 3) * 20)
                e2.append(Label(root, width=10, bg='purple', fg='black', text=myresult3[i]))
                e2[i].place(x=90, y=(i + 3) * 20)
                b3.append(
                    Button(root, width=1, text="-", bg='red', fg='blue', font=['arial', 13], command=lambda c=i: dec(c)))
                b3[i].place(x=180, y=(i + 3) * 20)
                b4.append(
                    Button(root, width=1, text="+", bg='green', fg='blue', font=['arial', 13], command=lambda c=i: inc(c)))
                b4[i].place(x=200, y=(i + 3) * 20)
            b2 = Button(root, width=5, text="Update", fg='blue')
            b2['command'] = lambda: change(e1, e2, root)
            b2.place(x=200, y=a)
            b5=Button(root,text="VIEW ST Stock",fg='blue',command=lambda:STUI(root))
            b5.place(x=100,y=a)
    b1.place(x=0, y=a)
    root.mainloop()
home()

