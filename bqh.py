# -*- coding: utf-8 -*-
"""
Created on Thu May 20 08:02:48 2021

@author: User
"""

from tkinter import *
import tkinter.messagebox
import mysql.connector

#FE UI class

class Books():
    def __init__ (self,root):
       
        #create object reference of Database class as b
        d = Database()
        b.conn()
        #Database methods to perform database operation
        self.root = root
        self.root.title("FORREST BOOKSTORE MANAGEMENT SYSTEM")
        self.root.geometry("1325x690")
        self.root.config(bg="yellow")

        #declare
        
        BookID = StringVar()
        BookName = StringVar()
        Price = StringVar()
        Author = StringVar()
        Year = StringVar()
        Publisher = StringVar()
        Quantity = StringVar()

        #Close function
        
        def close():
            print("Books : close methods called")
            close = tkinter.messagebox.askyesno("FORREST BOOKSTORE MANAGEMENT SYSTEM","Yo man, are you sure about that?")
            if close > 0:
                root.destroy()
                print("Books : close methods finished\n")
                return
        
        # Clear function 
        
        def clear():
            print("Books : clear methods called")
            self.txtBookID.delete(0,END)
            self.txtBookName.delete(0,END)
            self.txtPrice.delete(0,END)
            self.txtAuthor.delete(0,END)
            self.txtYear.delete(0,END)
            self.txtPublisher.delete(0,END)
            self.txtQuantity.delete(0,END)
        
        # Save function for Books info in database table:
        
        def insert():
            print("Books : insert methods called")
            if (len(BookID.get())!=0):
                b.insert(BookID.get(),BookName.get(),Price.get(),Author.get(),Year.get(),Publisher.get().Quantity.get())
                BookList.delete(0,END)
                BookList.insert(END,BookID.get(),BookName.get(),Price.get(),Author.get(),Year.get(),Publisher.get().Quantity.get())
                #after inserting data to DTB table, showinBookList method called
                showinBookList() 
            
            else:
                tkinter.messagebox.askyesno("FORREST BOOKSTORE MANAGEMENT SYSTEM","Yo man, enter BookID please?")
                
            print("Books : insert methods finished\n")
        
        # Show function for books in table data to BookList
        def showinBookList():
            print("Books : showinBookList method called")
            BookList.delete(0,END)
            for row in b.show():
                BookList.insert(END,row,str(""))
            print("Books : showinBookList method finished\n")
        
        #add to Scrollbar
        
        def BookRecord(event): 
            print("Books : BookRecord method called")
            global bkr
            searchbkr = BookList.curselection() [0]
            bkr  = BookList.get(searchbkr)
            
            self.txtBookID.delete(0,END)
            self.txtBookID.insert(END,bkr[0])
            
            self.txtBookName.delete(0,END)
            self.txtBookName.insert(END,bkr[1])
            
            self.txtPrice.delete(0,END)
            self.txtPrice.insert(END,bkr[2])
            
            self.txtAuthor.delete(0,END)
            self.txtAuthor.insert(END,bkr[3])
            
            self.txtYear.delete(0,END)
            self.txtYear.insert(END,bkr[4])
            
            self.txtPublisher.delete(0,END)
            self.txtPublisher.insert(END,bkr[5])
            
            self.txtQuantity.delete(0,END)
            self.txtQuantity.insert(END,bkr[6])
            
            print("Books : BookRecord method finished\n")
        
        #function TO KILLLLLLLLL data BookRecord
        
        def delete():
            print("Books: KILL method called")
            if (len(BookID.get())!=0):
                b.delete(bkr[0])
                clear()
                showinBookList()
            print("Books: KILL method finished\n")
        
        #search function from database table
        
        def search():
            print("Books : search method called")
            BookList.delete(0,END)
            for row in b.search(BookID.get(),BookName.get(),Price.get(),Author.get(),Year.get(),Publisher.get(),Quantity.get()):
                BookList.insert(END,row,str(""))
            print("Books : search method finished\n")
        
        #Update function for the BookRecord
        def update():
            print("Books : update method called")
            if (len(BookID.get())!=0):
                print ("bkr[0]",bkr[b])
                b.delete(bkr[0])
            if (len(BookID.get())!=0):
                b.insert(BookID.get,BookName.get(),Price.get(),Author.get(),Year.get(),Publisher.get(),Quantity.get())
                BookList.delete(0,END)
            BookList.insert(END,(BookID.get,BookName.get(),Price.get(),Author.get(),Year.get(),Publisher.get(),Quantity.get()))
            print("Books : update method finished\n")
        #Frame
        
        MainFrame = Frame(self.root,bg="brown")
        MainFrame.grid()

        HeadFrame = Frame(MainFrame, bd=1, padx=40,pady=12,bg='white',relief=RIDGE)
        HeadFrame.pack(side=TOP)
        
        self.ITitle = Label(HeadFrame,font=('arial',54),text='Forrest bookstore',bg='green')
        self.ITitle.grid()

        OpeFrame = Frame (MainFrame,bd=2,width=1100,height=50, padx=40,pady=20,bg='white',relief=RIDGE)
        OpeFrame.pack(side=BOTTOM)

        Bodyframe = Frame (MainFrame,bd=2,width=1090,height=400, padx=30,pady=20,bg='white',relief=RIDGE)
        Bodyframe.pack(side=BOTTOM)

        LeftBodyFrame = LabelFrame(BodyFrame,bd=2,width=600,height=350, padx=20,pady=10,bg='green',relief=RIDGE, font=('arial',13),text='Details')
        LeftBodyFrame.pack(side=LEFT)

        RightBodyFrame = LabelFrame(BodyFrame,bd=2,width=300,height=350, padx=20,pady=10,bg='green ',relief=RIDGE, font=('arial',13),text='Books Information')
        RightBodyFrame.pack(side=RIGHT)    
        
        # Adding to left body farme
        #BookID
        self.labelBookID = Label(LeftBodyFrame, font=('arial',13), text ="ID", padx = 2, bg='white', fg= 'red')
        self.labelBookID.grid(row = 0 ,column = 0,sticky=W)

        self.txtBookID = Entry(LeftBodyFrame,font=('arial',18),textvariable=BookID, width=25)
        self.txtBookID.grid(row = 0,column = 1,sticky=W)
        
        #BookName
        
        self.labelBookName = Label(LeftBodyFrame, font=('arial',13), text ="Name/Title", padx = 2, bg='white', fg= 'red')
        self.labelBookName.grid(row = 1,column = 0,sticky=W)

        self.txtBookName = Entry(LeftBodyFrame,font=('arial',15),textvariable=BookName, width = 25)
        self.txtBookName.grid(row = 1,column = 1,sticky=W)
        
        #Price

        self.labelPrice = Label(LeftBodyFrame, font=('arial',13), text ="Price", padx = 2, bg='white', fg= 'red')
        self.labelPrice.grid(row = 2 ,column = 0,sticky=W)

        self.txtPrice = Entry(LeftBodyFrame,font=('arial',15),textvariable=Price, width=25)
        self.txtPrice.grid(row = 2,column = 1,sticky=W)

        #Author

        self.labelAuthor = Label(LeftBodyFrame, font=('arial',13), text ="Author", padx = 2, bg='white', fg= 'red')
        self.labelAuthor.grid(row = 3 ,column = 0,sticky=W)

        self.txtAuthor = Entry(LeftBodyFrame,font=('arial',15),textvariable=Author, width=25)
        self.txtAuthor.grid(row = 3,column = 1,sticky=W)
        
        #Year
        
        self.labelYear = Label(LeftBodyFrame, font=('arial',13), text ="Published year", padx = 2, bg='white', fg= 'red')
        self.labelYear.grid(row = 4 ,column = 0,sticky=W)

        self.txtYear = Entry(LeftBodyFrame,font=('arial',15),textvariable=Year, width=25)
        self.txtYear.grid(row = 4,column = 1,sticky=W)

        #Publisher

        self.labelPublisher = Label(LeftBodyFrame, font=('arial',13), text ="Publisher", padx = 2, bg='white', fg= 'red')
        self.labelPublisher.grid(row = 5 ,column = 0,sticky=W)

        self.txtPublisher = Entry(LeftBodyFrame,font=('arial',15),textvariable=Publisher, width=25)
        self.txtPublisher.grid(row = 5,column = 1,sticky=W)

        #Quantity

        self.labelQuantity = Label(LeftBodyFrame, font=('arial',13), text ="Quantity", padx = 2, bg='white', fg= 'red')
        self.labelQuantity.grid(row = 6 ,column = 0,sticky=W)

        self.txtQuantity = Entry(LeftBodyFrame,font=('arial',18),textvariable=Quantity, width=25)
        self.txtQuantity.grid(row = 6,column = 1,sticky=W)
        #remain spot
        
        self.labelbC1 = Label(LeftBodyFrame, padx = 2, pady = 2)
        self.labelbC1.grid(row = 7 ,column = 0,sticky=W)
        
        self.labelbC1 = Label(LeftBodyFrame, padx = 2, pady = 2)
        self.labelbC1.grid(row = 8 ,column = 0,sticky=W)

        self.labelbC1 = Label(LeftBodyFrame, padx = 2, pady = 2)
        self.labelbC1.grid(row = 9 ,column = 0,sticky=W)

        self.labelbC1 = Label(LeftBodyFrame, padx = 2, pady = 2)
        self.labelbC1.grid(row = 10 ,column = 0,sticky=W)
        
        # Add scroll bar
        
        scroll = Scrollbar(RightBodyFrame)
        scroll.grid(row = 0, column = 1, sticky ='ns')
        
        #add list box
        
        BookList=Listbox(RightBodyFrame, width = 40, height=16, font =('arial',11),yscrollcommand=scroll.set)
        BookList.bind('<<ListBoxSelect>>',BookRecord)  #called BookRecord from init from above
        BookList.grid(row=0, column=0,padx=8)
        scroll.config(command=BookList.yview)
        
        #add button to operation RightBodyFrame
        
        self.buttonSaveData=Button(OpeFrame,text='Save',font=('arial',15,'bold'), height=1, width=8,bd=4, command=insert)
        self.buttonSaveData.grid(row=0,column=0)
        
        self.buttonShowData=Button(OpeFrame,text='Show',font=('arial',15,'bold'), height=1, width=8,bd=4, command=showinBookList)
        self.buttonShowDataData.grid(row=0,column=1)
        
        self.buttonClear=Button(OpeFrame,text='Clear',font=('arial',15,'bold'), height=1, width=8,bd=4, command=clear)
        self.buttonClear.grid(row=0,column=2)
        
        self.buttonDelete=Button(OpeFrame,text='Kill',font=('arial',15,'bold'), height=1, width=8,bd=4)
        self.buttonDelete.grid(row=0,column=3)
        
        self.buttonSearch=Button(OpeFrame,text='Search',font=('arial',15,'bold'), height=1, width=8,bd=4, command=search)
        self.buttonSearch.grid(row=0,column=4)
        
        self.buttonUpdate=Button(OpeFrame,text='Delete',font=('arial',15,'bold'), height=1, width=8,bd=4)
        self.buttonUpdate.grid(row=0,column=5)
        
        self.buttonClose=Button(OpeFrame,text='Close',font=('arial',15,'bold'), height=1, width=8,bd=4, command=close)
        self.buttonClose.grid(row=0,column=6)
        
        
        
#BE database operation

class Database:
    
    def conn(self):
        print ("Database : connection calling method")
        con = mysql.connect("inventory.db")
        cur = con.cursor()
        query = "Creata a table for unexist book(BookID integer Primary key,\BookName text, Price text, Author text,Year text,Publisher text,Quantity text)"
        cur.execute(query)
        con.commit()
        con.close()
        print("Database: connection method finished\n")
    
    def insert(self, BookID, BookName, Price, Author, Year, Publisher, Quantity):
        print("Database : insert method called")
        con =mysql.connect("inventory.db")
        cur = con.cursor()
        query = "Insert into value(?,?,?,?,?,?,?)"
        cur.execute(query,(BookID, BookName, Price, Author, Year, Publisher, Quantity))
        con.commit()
        con.close()
        print("Database: insert method finished\n")
    
    def show(self):
        print("Database : show method called")
        con =mysql.connect("inventory.db")
        cur = con.cursor()
        query = "select * from Books"
        cur.execute(query)
        rows=cur.fetchall()
        con.close()
        print("Database: insert method finished\n")
        return rows
    
    def delete(self, BookID):
        print("Database : delete method called")
        con =mysql.connect("inventory.db")
        cur =con.cursor()
        cur.execute("delete from Books where BookID=?",(BookID,))
        con.commit()
        con.close()
        print(BookID,"Database : Delete method finished\n")
    
    def search(self,BookID="",BookName="",Price="", Author="", Year="", Publisher="", Quantity=""):
        print("Database : search method called", BookID)
        con =mysql.connect("inventory.db")
        cur =con.cursor()
        cur.execute("select * from Books where BookID=? or BookName=? or Price =? or Author=? or Year=? or Publisher=? or Quantity=?",(BookID,BookName,Price,Author,Year,Publisher,Quantity))
        rows=cur.fetchall()
        con.close()
        print(BookID,"Database : search method finished\n")
        return row 
        
    def update(self,BookID="",BookName="",Price="", Author="", Year="", Publisher="", Quantity=""):
        print("Database : update method called", BookID)
        con =mysql.connect("inventory.db")
        cur =con.cursor()
        cur.execute("update Books set BookID=? or BookName=? or Price =? or Author=? or Year=? or Publisher=? or Quantity=? where BookID=?",(BookID,BookName,Price,Author,Year,Publisher,Quantity))
        con.commit()
        con.close()
        print(BookID,"Database : update method finished\n")


if __name__=='__main__':
    root = Tk()
    application=Books()
    root.mainloop()
