import tkinter as tk
import mysql.connector
from tkinter import ttk
from tkinter import *
from tkinter import messagebox as mb

r = tk.Tk()
r.title("SQL GATE")
r.geometry("900x500") 

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="123456789",
  database="boutique"
)

conn = mydb.cursor()

conn.execute("SELECT * FROM produit")
tree=ttk.Treeview(r)
tree['show'] = 'headings'

s = ttk.Style(r)
s.theme_use("clam")
s.configure(".", font =('Helvetica',11,"bold"))
tree["columns"]=("id","nom","description","prix","quantite","id_category")
tree.column("id",width=150,minwidth=150,anchor=tk.CENTER)
tree.column("nom",width=150,minwidth=150,anchor=tk.CENTER)
tree.column("description",width=150,minwidth=150,anchor=tk.CENTER)
tree.column("prix",width=150,minwidth=150,anchor=tk.CENTER)
tree.column("quantite",width=150,minwidth=150,anchor=tk.CENTER)
tree.column("id_category",width=150,minwidth=150,anchor=tk.CENTER)

tree.heading("id",text="id",anchor=tk.CENTER)
tree.heading("nom",text="nom",anchor=tk.CENTER)
tree.heading("description",text="description",anchor=tk.CENTER)
tree.heading("prix",text="prix",anchor=tk.CENTER)
tree.heading("quantite",text="quantite",anchor=tk.CENTER)
tree.heading("id_category",text="id_category",anchor=tk.CENTER)

i = 0
for ro in conn:
    tree.insert('',i,text="",values=(ro[0],ro[1],ro[2],ro[3],ro[4],ro[5]))
    i=i+1

hsb=ttk.Scrollbar(r,orient="horizontal")
hsb.configure(command=tree.xview)
tree.config(xscrollcommand=hsb.set)
hsb.pack(fill=X,side= BOTTOM)

vsb=ttk.Scrollbar(r,orient="vertical")
vsb.configure(command=tree.yview)
tree.configure(yscrollcommand=vsb.set)
vsb.pack(fill=Y,side=RIGHT)

tree.pack()
nom=tk.StringVar()
description=tk.StringVar()
prix=tk.DoubleVar()
quantite=tk.IntVar()
id_category=tk.IntVar()

def add_data(tree):
    f=Frame(r,width=400,height=250,background="grey")
    f.place(x=100,y=200)
    
    l1=Label(f,text=" nom ",width=8,font=('Times',11,'bold'))
    e1=Entry(f,textvariable=nom,width=25)
    l1.place(x=50,y=30)
    e1.place(x=170,y=30)
    
    l2=Label(f,text=" description ",width=8,font=('Times',11,'bold'))
    e2=Entry(f,textvariable=description,width=25)
    l2.place(x=50,y=70)
    e2.place(x=170,y=70)

    l3=Label(f,text=" prix ",width=8,font=('Times',11,'bold'))
    e3=Entry(f,textvariable=prix,width=25)
    l3.place(x=50,y=110)
    e3.place(x=170,y=110)
    e3.delete(0,END)

    l4=Label(f,text=" quantite ",width=8,font=('Times',11,'bold'))
    e4=Entry(f,textvariable=quantite,width=25)
    l4.place(x=50,y=150)
    e4.place(x=170,y=150)
    e4.delete(0,END)

    l5=Label(f,text=" id_category ",width=8,font=('Times',11,'bold'))
    e5=Entry(f,textvariable=id_category,width=25)
    l5.place(x=50,y=190)
    e5.place(x=170,y=190)
    e5.delete(0,END)
    
    def insert_data():
        nonlocal e1,e2,e3,e4,e5
        n=nom.get()
        d=description.get()
        p=prix.get()
        q=quantite.get()
        id_c=id_category.get()
        conn.execute('INSERT INTO produit(nom,description,prix,quantite,id_category)\
        VALUES (%s,%s,%s,%s,%s)',(n,d,p,q,id_c))
        
        print(conn.lastrowid)
        mydb.commit()
        tree.insert('','end',text="",values=(conn.lastrowid,n,d,p,q,id_c))
        mb.showinfo("Success","Data ajouté")
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
        e5.delete(0,END)
        f.destroy()

    ajouterbutton=tk.Button(f,text="Ajouter",command=insert_data)
    ajouterbutton.configure(font=('Times',12,'bold'),bg='green',fg='white')
    ajouterbutton.place(x=150,y=220)

    cancelbutton=tk.Button(f,text="Cancel",command=f.destroy)
    cancelbutton.configure(font=('calibri',12,'bold'),bg='red',fg='white')
    cancelbutton.place(x=240,y=220)

def delete_data(tree):
    selected_item=tree.selection()[0]
    print(tree.item(selected_item)['values'])
    uid=tree.item(selected_item)['values'][0]
    del_query="DELETE FROM produit WHERE id=%s"
    sel_data=(uid,)
    conn.execute(del_query,sel_data)
    mydb.commit()
    tree.delete(selected_item)
    mb.showinfo("Success","Data supprimé")

def selected_data(tree):
    curItem=tree.focus()
    values=tree.item(curItem,"values")
    print(values)

    f=Frame(r,width=400,height=250,background="grey")
    f.place(x=100,y=200)
    
    l1=Label(f,text=" nom ",width=8,font=('Times',11,'bold'))
    e1=Entry(f,textvariable=nom,width=25)
    l1.place(x=50,y=30)
    e1.place(x=170,y=30)
    
    l2=Label(f,text=" description ",width=8,font=('Times',11,'bold'))
    e2=Entry(f,textvariable=description,width=25)
    l2.place(x=50,y=70)
    e2.place(x=170,y=70)

    l3=Label(f,text=" prix ",width=8,font=('Times',11,'bold'))
    e3=Entry(f,textvariable=prix,width=25)
    l3.place(x=50,y=110)
    e3.place(x=170,y=110)
    e3.delete(0,END)

    l4=Label(f,text=" quantite ",width=8,font=('Times',11,'bold'))
    e4=Entry(f,textvariable=quantite,width=25)
    l4.place(x=50,y=150)
    e4.place(x=170,y=150)
    e4.delete(0,END)

    l5=Label(f,text=" id_category ",width=8,font=('Times',11,'bold'))
    e5=Entry(f,textvariable=id_category,width=25)
    l5.place(x=50,y=190)
    e5.place(x=170,y=190)
    e5.delete(0,END)

    e1.insert(0,values[1])
    e2.insert(0,values[2])
    e3.insert(0,values[3])
    e4.insert(0,values[4])
    e5.insert(0,values[5])
    
    def update_data():
      nonlocal e1,e2,e3,e4,e5,curItem,values
      n=nom.get()
      d=description.get()
      p=prix.get()
      q=quantite.get()
      id_c=id_category.get()
      tree.item(curItem,values=(values[0],n,d,p,q,id_c))
      conn.execute(
          "UPDATE produit SET nom=%s,description=%s,prix=%s,quantite=%s,id_category=%s \
          WHERE id=%s",(n,d,float(p),int(q),int(id_c),values[0]))
      mydb.commit()
      mb.showinfo("Success","Data modifié")
      e1.delete(0,END)
      e2.delete(0,END)
      e3.delete(0,END)
      e4.delete(0,END)
      e5.delete(0,END)
      f.destroy()
          

    savebutton=tk.Button(f,text="Update",command=update_data)
    savebutton.place(x=150,y=220)
    cancelbutton=tk.Button(f,text="Cancel",command=f.destroy)
    cancelbutton.place(x=240,y=220)



insertbutton=tk.Button(r,text="Insert",command=lambda:add_data(tree))
insertbutton.configure(font=('calibri',12,'bold'),bg='green',fg='white')
insertbutton.place(x=350,y=260)

deletebutton=tk.Button(r,text="Delete",command=lambda:delete_data(tree))
deletebutton.configure(font=('calibri',12,'bold'),bg='red',fg='white')
deletebutton.place(x=500,y=260)

modifybutton=tk.Button(r,text="modify",command=lambda:selected_data(tree))
modifybutton.configure(font=('calibri',12,'bold'),bg='light blue',fg='white')
modifybutton.place(x=650,y=260)
r.mainloop()

 