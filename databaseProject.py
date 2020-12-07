from tkinter import *
import tkinter.messagebox
import sqlite3

#class for front End UI
pd = None
class Product:
    def __init__(self,root): #default constructor

        d = Database()
        d.conn()

        self.root= root
        self.root.title("WARE HOUSE INVENTORY SALES PURCHASE MANAGEMENT SYSTEM")
        self.root.geometry("1325x690")
        self.root.config(bg="yellow")

        #to get entry values
        pId= StringVar()
        pName = StringVar()
        pPrice = StringVar()
        pQty = StringVar()
        pCompany = StringVar()
        pContact = StringVar()

##calling database methods

        def close():
            print("Product : Close method called ")
            close = tkinter.messagebox.askyesno("WARE HOUSE INVENTORY SALES PURCHASE MANAGEMENT SYSTEM","Really...Do you want to close the system")
            if close>0:
                root.destroy()
                print("Product : method close")
                return 

        def clear():
            print("Product : clear method called ")
            self.txtpId.delete(0,END)
            self.txtpName.delete(0,END)
            self.txtpPrice.delete(0,END)
            self.txtpQty.delete(0,END)
            self.txtpCompany.delete(0,END)
            self.txtpContact.delete(0,END)
            print("Product : clear method finished ")

            #save
        def insert():
            print("Product : insert method called ")
            if (len(pId.get())!=0):
                print("Product : clear method finished 11")

                d.insert(pId.get(),pName.get(),pPrice.get(),pQty.get(),pCompany.get(),pContact.get())
                print("Product : clear method finished 1")
                productList.delete(0,END)
                print("Product : clear method finished 2")

                productList.insert(END,pId.get(),pName.get(),pPrice.get(),pQty.get(),pCompany.get(),pContact.get())
                print("Product : clear method finished 3")

                # showInProductlist()
            else:
                tkinter.messagebox.askyesno("WARE HOUSE INVENTORY SALES PURCHASE MANAGEMENT SYSTEM","You have to insert one option... press yes to quit  ")
            print("Product : insert method finished ")


            #show data
        def showInProductlist():
            print("Product : show method called ")
            productList.delete(0,END)
            print("Product : insert method finished 1 ")

            for row in d.show():
                 productList.insert(END,row,str(""))
            print("Product : show method finished ")
            
            #Add to scroll bar
        def productRec(event): #function to be called from scroll bar of product list 
            
            print("Product : productRec method called ")
            global pd
           
            searchPd = productList.curselection()[0]
            pd = productList.get(searchPd)

            self.txtpId.delete (0,END)
            self.txtpId.insert (END,pd[0])

            self.txtpName.delete (0,END)
            self.txtpId.insert (END,pd[1])

            self.txtpPrice.delete (0,END)
            self.txtpPrice.insert (END,pd[2])

            self.txtpQty.delete (0,END)
            self.txtpQty.insert (END,pd[3])

            self.txtpCompany.delete (0,END)
            self.txtpCompany.insert (END,pd[4])

            self.txtpContact.delete (0,END)
            self.txtpContact.insert (END,pd[5])

            print('Product : productRec method finished')


            #searching operation from database
        def search():
            print("Product : search method called ")
            # productList.delete(0,END)
            print("print 1")
            for row in d.search(pId.get(),pName.get(),pPrice.get(),pQty.get(),pCompany.get(),pContact.get()):
             print("print 2")
             productList.insert(END,row,str(""))

            print("Product : search method finished ")


        #function to delete data from table
        def delete():
            print('Product : delete method called')

            if (len(pId.get())!=0):
                d.delete(pd[0])
                clear()
                showInProductlist()
                print("Product : delete method finished 11")

        #function update
        def update():
                print('Product : update method called')
                if (len(pId.get())!=0):
                    print("pd[0]",pd[0])
                    d.delete(pd[0])
                if (len(pId.get())!=0):
                    d.insert(pId.get(),pName.get(),pPrice.get(),pQty.get(),pCompany.get(),pContact.get())
                    productList.delete(0,END)
                d.insert(END,pId.get(),pName.get(),pPrice.get(),pQty.get(),pCompany.get(),pContact.get())
                print('Product : update method finished')


         #create the frame
        MainFrame = Frame (self.root,bg ="red")
        MainFrame.grid()    #grid allocates element in rows and columns

        ##Title 
        HeadFrame = Frame(MainFrame, bd=1,padx=50,pady=10,bg='white',relief=RIDGE)
        HeadFrame.pack(side=TOP)

        self.ITitle=Label(HeadFrame,font=('arial',43,'bold'),fg='red',text=' Warehouse Inventory Sales Purchase ',bg='white')
        self.ITitle.grid()

        ##Operational Frame. We will add buttons in this frame 
        OperationFrame = Frame(MainFrame,bd=2,width=1250,height=60,padx=60,pady=20,bg='white',relief=RIDGE)
        OperationFrame.pack(side=BOTTOM)

        #Body Frame. We will add all the entries and sliders
        BodyFrame = Frame(MainFrame,bd=2,width=1290,height=400,padx=30,pady=20,bg='white',relief=RIDGE)
        BodyFrame.pack(side=BOTTOM)

        #Labels divided in two parts left and right, Label frame will come under BodyFrame 
        LeftBodyFrame = LabelFrame(BodyFrame,bd=2,width=580,height=380,padx=20,pady=10,
        bg='yellow',relief=RIDGE,font=('arial',15,'bold'),text='Product Item Details :')
        LeftBodyFrame.pack(side=LEFT)

        RightBodyFrame = LabelFrame(BodyFrame,bd=2,width=300,height=380,padx=20,pady=10,bg='yellow',relief=RIDGE,font=('arial',15,'bold'),text='Product Item Information :')
        RightBodyFrame.pack(side=RIGHT)

    # Adding widgets to leftBodyFrame

        #ID
        self.labelpId = Label(LeftBodyFrame,font=('arial',15,'bold'),text='Product Id :',padx=2,pady=2,bg='white',fg='blue')
        self.labelpId.grid(row=0,column=0, sticky=W)

        self.txtpId= Entry(LeftBodyFrame,font=('arial',20,'bold'),textvariable=pId,width=35)
        self.txtpId.grid(row=0,column=1, sticky=W)
        
        #Name
        self.labelpName = Label(LeftBodyFrame,font=('arial',15,'bold'),text='Product Name :',padx=2,pady=2,bg='white',fg='blue')
        self.labelpName.grid(row=1,column=0, sticky=W)

        self.txtpName= Entry(LeftBodyFrame,font=('arial',20,'bold'),textvariable=pName,width=35)
        self.txtpName.grid(row=1,column=1, sticky=W)

        #Price
        self.labelpPrice = Label(LeftBodyFrame,font=('arial',15,'bold'),text='Product Price :',padx=2,pady=2,bg='white',fg='blue')
        self.labelpPrice.grid(row=2,column=0, sticky=W)

        self.txtpPrice= Entry(LeftBodyFrame,font=('arial',20,'bold'),textvariable=pPrice,width=35)
        self.txtpPrice.grid(row=2,column=1, sticky=W)

        #QTY
        self.labelpQty = Label(LeftBodyFrame,font=('arial',15,'bold'),text='Product Quantity :',padx=2,pady=2,bg='white',fg='blue')
        self.labelpQty.grid(row=3,column=0, sticky=W)

        self.txtpQty= Entry(LeftBodyFrame,font=('arial',20,'bold'),textvariable=pQty,width=35)
        self.txtpQty.grid(row=3,column=1, sticky=W)

        #CompanyName
        self.labelpCompany = Label(LeftBodyFrame,font=('arial',15,'bold'),text='Mfg.Company :',padx=2,pady=2,bg='white',fg='blue')
        self.labelpCompany.grid(row=4,column=0, sticky=W)

        self.txtpCompany= Entry(LeftBodyFrame,font=('arial',20,'bold'),textvariable=pCompany,width=35)
        self.txtpCompany.grid(row=4,column=1, sticky=W)

        #Contact
        self.labelpContact = Label(LeftBodyFrame,font=('arial',15,'bold'),text='Company Contact :',padx=2,pady=2,bg='white',fg='blue')
        self.labelpContact.grid(row=5,column=0, sticky=W)

        self.txtpContact= Entry(LeftBodyFrame,font=('arial',20,'bold'),textvariable=pContact,width=35)
        self.txtpContact.grid(row=5,column=1, sticky=W)

        #to fill empty spaces
        self.labelpC1 = Label(LeftBodyFrame,padx=2,pady=2)
        self.labelpC1.grid(row=6,column=0, sticky=W)
        self.labelpC1 = Label(LeftBodyFrame,padx=2,pady=2)
        self.labelpC1.grid(row=7,column=0, sticky=W)
        self.labelpC1 = Label(LeftBodyFrame,padx=2,pady=2)
        self.labelpC1.grid(row=8,column=0, sticky=W)
        self.labelpC1 = Label(LeftBodyFrame,padx=2,pady=2)
        self.labelpC1.grid(row=9,column=0, sticky=W)
        
    # Adding Widget to Right Body Pannel

        #Adding scroll Bar
        scroll = Scrollbar(RightBodyFrame)
        scroll.grid(row=0,column=1,sticky = 'ns')
        
        # List Box
        productList= Listbox(RightBodyFrame,width=40,height=16,font=('arial',20,'bold'),yscrollcommand=scroll.set)
        #called above created productrec function of init 
        productList.bind('<<ListboxSelect>>',productRec)
        productList.grid(row=0,column=0,padx=8)
        scroll.config(command=productList.yview)
        
    #Adding buttons to operational frame
        #save
        self.buttonSave = Button(OperationFrame,text='SAVE',font=('arial',18,'bold'),height=1,width=10,bd=4,command=insert)
        self.buttonSave.grid(row=0,column=0) 

        #Show
        self.buttonShow = Button(OperationFrame,text='SHOW DATA',font=('arial',18,'bold'),height=1,width=10,bd=4,command=showInProductlist)
        self.buttonShow.grid(row=0,column=1) 

        #Clear
        self.buttonClear = Button(OperationFrame,text='CLEAR',font=('arial',18,'bold'),height=1,width=10,bd=4,command=clear)
        self.buttonClear.grid(row=0,column=2) 

        #Delete
        self.buttonDelete = Button(OperationFrame,text='DELETE',font=('arial',18,'bold'),height=1,width=10,bd=4,command=delete)
        self.buttonDelete.grid(row=0,column=3) 

        #Search
        self.buttonSearch = Button(OperationFrame,text='SEARCH',font=('arial',18,'bold'),height=1,width=10,bd=4,command=search)
        self.buttonSearch.grid(row=0,column=4) 

        #Update
        self.buttonUpdate = Button(OperationFrame,text='UPDATE',font=('arial',18,'bold'),height=1,width=10,bd=4,command=update)
        self.buttonUpdate.grid(row=0,column=5)

        #Close
        self.buttonClose = Button(OperationFrame,text='CLOSE',font=('arial',18,'bold'),height=1,width=10,bd=4,command=close)
        self.buttonClose.grid(row=0,column=6)


##*******BACK END DATABASE OPERATIONS***********

class Database:
    def conn(self):
        print("Datebase : connection method called ")
        con = sqlite3.connect("Inventory.db")
        cur = con.cursor()
        queery = "Create table if not exists product(pid integer primary key,pname text, price text,qty text,company text,contact text)"
        cur.execute(queery)
        con.commit()
        con.close()
        print("Datebase : connection method finished \n ")

    def insert(self,pid,name,price,qty,company,contact):
        print("Datebase : insert method called ")
        con = sqlite3.connect("Inventory.db")
        cur = con.cursor()
        query="insert into product values(?,?,?,?,?,?)"
        cur.execute(query,(pid,name,price,qty,company,contact))
        con.commit()
        con.close()
        print("Datebase : insert method finished \n ")

    def show(self):
        print("Datebase : show method called ")
        con = sqlite3.connect("Inventory.db")
        cur = con.cursor()
        query="select * from product"
        cur.execute(query)
        rows=cur.fetchall()
        con.close()
        print("Datebase : show method finished \n ")
        return rows

    def delete(self,pid):
        print("Datebase : delete method called ")
        con = sqlite3.connect("Inventory.db")
        cur = con.cursor()
        cur.execute("delete from product where pid=?",(pid,))
        con.commit()
        con.close()
        print(pid,"Datebase : delete method finished \n")

    def search(self,pid="",name="",price="",qty="",company="",contact=""):
        print("Datebase : Search method called ")
        con = sqlite3.connect("Inventory.db")
        cur = con.cursor()
        cur.execute("select * from product where pid=? or pname=? or price=? or qty=? or company=? or contact=?",(pid,name,price,qty,company,contact))
        row = cur.fetchall()
        con.close()
        print(pid,"Datebase : finidhed method finished \n")
        return row

    def update(self,pid="",name="",price="",qty="",company="",contact=""):
        print("Datebase : update method called ")
        con = sqlite3.connect("Inventory.db")
        cur = con.cursor()
        cur.execute("update product set pid=? or name=? or price=? or qty=? or company=? or contact=? where pid=?",(pid,name,price,qty,company,contact,pid))
        con.commit()
        con.close()
        print(pid,"Datebase : update method finished \n")

if __name__ == "__main__":
    root = Tk()
    application = Product(root)
    root.mainloop()



