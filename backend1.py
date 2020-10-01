import sqlite3

con=sqlite3.connect("Books.db")
cur=con.cursor()
def crt():
    con=sqlite3.connect("book1s.db")
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book1(id integer PRIMARY KEY,title varchar(10),author varchar(10),year int,isbn int)")
    cur.close()
    con.close()
crt()
def add(a,b,c,d):
    con=sqlite3.connect("Books.db")
    cur=con.cursor()
    cur.execute("INSERT INTO book1 values(NULL,?,?,?,?)",(a,b,c,d))  
    con.commit()
    cur.close()
    con.close()
    view()

def delet(a):
    con=sqlite3.connect("Books.db")
    cur=con.cursor()
    cur.execute("delete from book1 where id=?",(a,))
    con.commit()
    cur.close()
    con.close()     

def view():
    con=sqlite3.connect("Books.db")
    cur=con.cursor()
    cur.execute("Select * from book1")
    row=cur.fetchall()
    cur.close()
    con.close()
    return row

def updat(a,b,c,d,e):
    con=sqlite3.connect("Books.db")
    cur=con.cursor()
    cur.execute("Update book1 set title=?,author=?,year=?,isbn=? where id=?",(b,c,d,e,a))
    cur.close()
    con.close()

def serch(title="",author="",year="",isbn=""):
    con=sqlite3.connect("Books.db")
    cur=con.cursor()
    cur.execute("SELECT * from book1 where title=? or author=? or year=? or isbn=?",(title,author,year,isbn))
    row=cur.fetchall()
    cur.close()
    con.close()
    return row