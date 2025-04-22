from tkinter import *
from PIL import Image,ImageTk
import ttkbootstrap as tb
import mysql.connector
from tkinter import ttk
from tkinter import messagebox
root=tb.Window(themename="superhero")
root.title("MY CAR SHOWROOM")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="DB1")
cur=mydb.cursor()


def city():
    global button1,button2,button3,button4,button5

    f1=Frame(root,width=f"{screen_width}",height=f"{screen_height}")
    f1.place(x=0,y=0)
    f1.pack_propagate(0)
    l1=tb.Label(root,text="EXPLORE VARIOUS SHOWROOMS IN DIFFERENT CITIES",bootstyle="light",font=("Helvetica",25))
    l1.place(x=250,y=50)
    img_path=r"C:\Users\chand\Downloads\RTP\Kolkata.jpg"
    image1=Image.open(img_path)
    image1=ImageTk.PhotoImage(image1)
    button1=tb.Button(f1,text="KOLKATA",compound="top",image=image1,bootstyle="info outline",command=Kolkata)
    button1.image=image1
    button1.place(x=150,y=150)


    img_path=r"C:\Users\chand\Downloads\RTP\Hyderabad.jpg"
    image2=Image.open(img_path)
    image2=ImageTk.PhotoImage(image2)
    button2=tb.Button(f1,text="HYDERABAD",compound="top",image=image2,bootstyle="info outline",command=Hyderabad)
    button2.image=image2
    button2.place(x=550,y=150)

    img_path=r"C:\Users\chand\Downloads\RTP\Delhi.jpg"
    image3=Image.open(img_path)
    image3=ImageTk.PhotoImage(image3)
    button3=tb.Button(f1,text="DELHI",compound="top",image=image3,bootstyle="info outline",command=Delhi)
    button3.image=image3
    button3.place(x=900,y=150)


    img_path=r"C:\Users\chand\Downloads\RTP\Chennai.jpg"
    image4=Image.open(img_path)
    image4=ImageTk.PhotoImage(image4)
    button4=tb.Button(f1,text="CHENNAI",compound="top",image=image4,bootstyle="info outline",command=Chennai)
    button4.image=image4
    button4.place(x=290,y=420)


    img_path=r"C:\Users\chand\Downloads\RTP\Mumbai.jpg"
    image5=Image.open(img_path)
    image5=ImageTk.PhotoImage(image5)
    button5=tb.Button(f1,text="MUMBAI",compound="top",image=image5,bootstyle="info outline",command=Mumbai)
    button5.image=image5
    button5.place(x=750,y=420,anchor=NW)
    







#1#  
def LOGIN():
    global entry1,entry2
    f2=Frame(root,width=f"{screen_width}",height=f"{screen_height}")
    f2.place(x=0,y=0)
    f2.pack_propagate(0)
    b2=tb.Button(root,text="HOME",bootstyle="primary outline",command=city, width="30")
    b2.place(x= 100,y=100 , anchor=NW)
    b3=tb.Button(root,text="CONTACT US",bootstyle="primary outline",command=CONTACT, width="30")
    b3.place(x= 900,y=100 , anchor=NW)
    c=Canvas(f2,bg='white',height='950',width='750')
    c.place(x=320,y=0)
    rec1=c.create_rectangle((0,180,700,400))
    label1 = tb.Label(f2, text=" SHOWROOM ID")
    label1.place(x=350,y=200,anchor=NW)
    l1 = tb.Label(f2, text="SHOWROOM LOGIN")
    l1.place(x=500,y=150,anchor=NW)
    entry1 = tb.Entry(f2, width="50")
    entry1.place(x=500,y=200,anchor=NW)
    label2 = tb.Label(f2, text="PASSWORD")
    label2.place(x=350,y=260,anchor=NW)
    entry2 = tb.Entry(f2,width="50")
    entry2.place(x=500,y=255,anchor=NW)
    b3=tb.Button(f2,text="LOGIN",bootstyle="sucess outline",command=LOGIN_VERIFY, width="30")
    b3.place(x= 500,y=330 , anchor=NW)

#1#+
def LOGIN_VERIFY():
    Id=entry1.get()
    Password=entry2.get()
    mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="DB1")
    cur=mydb.cursor()
    sqlqry="SELECT ID,PASSWORD FROM DE WHERE ID=%s AND PASSWORD=%s"
    cur.execute(sqlqry,(Id,Password))
    result=cur.fetchall()
    if(Id=='' or Password==''):
        messagebox.showinfo("warning","please enter all the fields")
    if result:
        if(result[0][0]==Id and result[0][1]== Password):
                messagebox.showinfo("Information","Login sucessful")
                SHOWROOM_LOGIN()
       
    else:
            messagebox.showinfo("Warning", "Incorrect Credentials")
            LOGIN()



#1#1#   
def SHOWROOM_LOGIN():
    Id=entry1.get()
    Password=entry2.get()
    mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="DB1")
    cur=mydb.cursor()
    sqlqry="SELECT SHOWROOM FROM DE WHERE ID=%s AND PASSWORD=%s"
    cur.execute(sqlqry,(Id,Password))
    result=cur.fetchone()
    str1="CARS"
    str2="FINANCIALINFO"
    str3="USERINFO"
    TABLE1 = [str(item) + str1 for item in result]
    TABLE2 = [str(item) + str2 for item in result]
    TABLE3 = [str(item) + str3 for item in result]
    for table_name1 in TABLE1:
        sqlqry1=f"CREATE TABLE IF NOT EXISTS {table_name1}(MODEL CHAR(10),CAR VARCHAR(20),MILEAGE INT,SEATER VARCHAR(8),FUELTYPE CHAR(7),MINPRICE INT,MAXPRICE INT,QUANTITY INT,COLOR CHAR(10),IMAGE VARCHAR(100))"
        cur.execute(sqlqry1)
    for table_name2 in TABLE2:
        sqlqry2=f"CREATE TABLE IF NOT EXISTS {table_name2}(MODEL CHAR(10),CAR VARCHAR(20),AMOUNT INT,COLOR CHAR(10))"
        cur.execute(sqlqry2)
    for table_name3 in TABLE3:
        sqlqry3=f"CREATE TABLE IF NOT EXISTS {table_name3}(MODEL CHAR(10),CAR VARCHAR(20),COLOR CHAR(10),NAME CHAR(20),PHONENO INT,ADDRESS VARCHAR(40),GMAIL VARCHAR(20))"
        cur.execute(sqlqry3)
    
    f2=Frame(root,width=f"{screen_width}",height=f"{screen_height}")
    f2.place(x=0,y=0)
    f2.pack_propagate(0)
    b3=tb.Button(root,text="CARS INFO",bootstyle="primary outline",command=CARS, width="30")
    b3.place(x= 200,y=100 , anchor=NW)
    b4=tb.Button(root,text="FINANCIAL INFORMATION",bootstyle="primary outline",command=MONEY, width="50")
    b4.place(x= 400,y=100 , anchor=NW)
    b5=tb.Button(root,text="CUSTOMER INFO",bootstyle="primary outline",command=USER, width="30")
    b5.place(x= 600,y=100 , anchor=NW)
    b6=tb.Button(root,text="NEW CAR",bootstyle="primary outline",command=ADD_CAR, width="30")
    b6.place(x= 800,y=100 , anchor=NW)
    b7=tb.Button(root,text="LOGOUT",bootstyle="primary outline",command=LOGIN, width="30")
    b7.place(x= 1000,y=100 , anchor=NW)
    ADD_CAR()
    mydb.commit()


#1#1#1#    
def CARS():
    #f2=Frame(root,width=f"{screen_width}",height=f"{screen_height}")
    #f2.place(x=0,y=0)
    #f2.pack_propagate(0)
    b3=tb.Button(root,text="CARS INFO",bootstyle="primary outline",command=CARS, width="30")
    b3.place(x= 200,y=100 , anchor=NW)
    b4=tb.Button(root,text="FINANCIAL INFORMATION",bootstyle="primary outline",command=MONEY, width="50")
    b4.place(x= 400,y=100 , anchor=NW)
    b6=tb.Button(root,text="NEW CAR",bootstyle="primary outline",command=ADD_CAR, width="30")
    b6.place(x= 600,y=100 , anchor=NW)
    b5=tb.Button(root,text="CUSTOMER INFO",bootstyle="primary outline",command=USER, width="30")
    b5.place(x= 800,y=100 , anchor=NW)
    b7=tb.Button(root,text="LOGOUT",bootstyle="primary outline",command=LOGIN, width="30")
    b7.place(x= 1000,y=100 , anchor=NW)
    mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="DB1")
    cur=mydb.cursor()
    def retrieve1_data():
        Id = entry1.get()
        Password = entry2.get()
        sqlqry = "SELECT SHOWROOM FROM DE WHERE ID=%s AND PASSWORD=%s"
        cur.execute(sqlqry, (Id, Password))
        result = cur.fetchone()
        str1 = "CARS"
        TABLE11 = [str(item) + str1 for item in result]
        for table_cars1 in TABLE11:
            cur.execute(f"SELECT * FROM {table_cars1}")
            rows = cur.fetchall()
            return screen_height

    def populate_table1(table1, data):
        for i, row in enumerate(data):
            table1.insert('', 'end', values=row)
        for col in table1["columns"]:
            table1.column(col, anchor="center")


    # Create a frame to hold the Treeview and scrollbars
    f2 = Frame(root, width=screen_width, height=screen_height)
    f2.place(x=0, y=0)
    f2.pack_propagate(0)

    # Create the Treeview widget
    columns = ("Column 0", "Column 1", "Column 2", "Column 3", "Column 4", "Column 5", "Column 6", "Column 7", "Column 8", "Column 9")
    table1 = ttk.Treeview(f2, columns=columns)
    table1.place(x=10, y=10, width=screen_width-30, height=screen_height-50)

    # Define columns
    for col in columns:
        table1.column(col, width=100, minwidth=100)
    table1.column("Column 9", width=200, minwidth=200)

    # Define column headings
    table1.heading("#0", text="CARS_INFO")
    table1.heading("Column 0", text="MODEL")
    table1.heading("Column 1", text="CAR_NAME")
    table1.heading("Column 2", text="MILEAGE")
    table1.heading("Column 3", text="SEATER")
    table1.heading("Column 4", text="FUELTYPE")
    table1.heading("Column 5", text="MINPRICE")
    table1.heading("Column 6", text="MAXPRICE")
    table1.heading("Column 7", text="AVAILABLE_CARS")
    table1.heading("Column 8", text="COLOR")
    table1.heading("Column 9", text="IMAGE")

    data = retrieve1_data()
    populate_table1(table1, data)

    vsb = ttk.Scrollbar(f2, orient="vertical", command=table1.yview)
    vsb.place(x=screen_width-20, y=10, height=screen_height-50)

    
    hsb = ttk.Scrollbar(f2, orient="horizontal", command=table1.xview)
    hsb.place(x=10, y=screen_height-40, width=screen_width-30)

    
    table1.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

   
    b3 = tb.Button(root, text="CARS INFO", bootstyle="primary outline", command=CARS, width=30)
    b3.place(x=200, y=100, anchor='nw')
    b4 = tb.Button(root, text="FINANCIAL INFORMATION", bootstyle="primary outline", command=MONEY, width=50)
    b4.place(x=400, y=100, anchor='nw')
    b6 = tb.Button(root, text="NEW CAR", bootstyle="primary outline", command=ADD_CAR, width=30)
    b6.place(x=600, y=100, anchor='nw')
    b5 = tb.Button(root, text="CUSTOMER INFO", bootstyle="primary outline", command=USER, width=30)
    b5.place(x=800, y=100, anchor='nw')
    b7 = tb.Button(root, text="LOGOUT", bootstyle="primary outline", command=LOGIN, width=30)
    b7.place(x=1000, y=100, anchor='nw')
    b4 = tb.Button(f2, text="Back", bootstyle="primary outline", command=SHOWROOM_LOGIN, width=30)
    b4.place(x=1100, y=900, anchor='nw')

        



#1#1#2#
def MONEY():
    f3=Frame(root,width=f"{screen_width}",height=f"{screen_height}")
    f3.place(x=0,y=0)
    f3.pack_propagate(0)
    b3=tb.Button(root,text="CARS INFO",bootstyle="primary outline",command=CARS, width="30")
    b3.place(x= 200,y=100 , anchor=NW)
    b4=tb.Button(root,text="FINANCIAL INFORMATION",bootstyle="primary outline",command=MONEY, width="50")
    b4.place(x= 400,y=100 , anchor=NW)
    b6=tb.Button(root,text="NEW CAR",bootstyle="primary outline",command=ADD_CAR, width="30")
    b6.place(x= 600,y=100 , anchor=NW)
    b5=tb.Button(root,text="CUSTOMER INFO",bootstyle="primary outline",command=USER, width="30")
    b5.place(x= 800,y=100 , anchor=NW)
    b7=tb.Button(root,text="LOGOUT",bootstyle="primary outline",command=LOGIN, width="30")
    b7.place(x= 1000,y=100 , anchor=NW)
    mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="DB1")
    cur=mydb.cursor()
    def retrieve2_data():
        Id=entry1.get()
        Password=entry2.get()
        sqlqry="SELECT SHOWROOM FROM DE WHERE ID=%s AND PASSWORD=%s"
        cur.execute(sqlqry,(Id,Password))
        result=cur.fetchone()
        str2="FINANCIALINFO"
        TABLE12 = [str(item) + str2 for item in result]
        for table_finance1 in TABLE12:
        
            cur.execute(f"SELECT * FROM {table_finance1}")
            rows = cur.fetchall()
            cur.close()
            mydb.close()
            return rows

    def populate_table2(table2, data):
        for i, row in enumerate(data):
            table2.insert('', 'end', values=row)
            for col in table2["columns"]:
                        table2.column(col, anchor="center")
    table2 = ttk.Treeview(root, columns=("Column 0", "Column 1", "Column 2","column 3")) 
    table2.heading("#0", text="FINANCIAL_INFO")
    table2.heading("#1", text="MODEL")
    table2.heading("#2", text="CAR_NAME")
    table2.heading("#3", text="AMOUNT")
    table2.heading("#4", text="COLOR")

    data = retrieve2_data()
    populate_table2(table2, data)
    table2.pack(expand=True, fill='both')
    b4=tb.Button(root,text="Back",bootstyle="primary outline",command=SHOWROOM_LOGIN, width="30")
    b4.place(x= 1100,y=900 , anchor=NW)



#1#1#3#
def USER():
    f3=Frame(root,width=f"{screen_width}",height=f"{screen_height}")
    f3.place(x=0,y=0)
    f3.pack_propagate(0)
    b3=tb.Button(root,text="CARS INFO",bootstyle="primary outline",command=CARS, width="30")
    b3.place(x= 200,y=100 , anchor=NW)
    b4=tb.Button(root,text="FINANCIAL INFORMATION",bootstyle="primary outline",command=MONEY, width="50")
    b4.place(x= 400,y=100 , anchor=NW)
    b5=tb.Button(root,text="CUSTOMER INFO",bootstyle="primary outline",command=USER, width="30")
    b5.place(x= 800,y=100 , anchor=NW)
    b6=tb.Button(root,text="NEW CAR",bootstyle="primary outline",command=ADD_CAR, width="30")
    b6.place(x= 600,y=100 , anchor=NW)
    b7=tb.Button(root,text="LOGOUT",bootstyle="primary outline",command=LOGIN, width="30")
    b7.place(x= 1000,y=100 , anchor=NW)
    mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="DB1")
    cur=mydb.cursor()
    def retrieve3_data():
        Id=entry1.get()
        Password=entry2.get()
        sqlqry="SELECT SHOWROOM FROM DE WHERE ID=%s AND PASSWORD=%s"
        cur.execute(sqlqry,(Id,Password))
        result=cur.fetchone()
        str3="USERINFO"
        TABLE13 = [str(item) + str3 for item in result]
        for table_user1 in TABLE13:
        
            cur.execute(f"SELECT * FROM {table_user1}")
            rows = cur.fetchall()
            cur.close()
            mydb.close()
            return rows

    def populate_table3(table3, data):
        for i, row in enumerate(data):
            table3.insert('', 'end', values=row)
            for col in table3["columns"]:
                        table3.column(col, anchor="center")
    table3 = ttk.Treeview(root, columns=("Column 0", "Column 1", "Column 2","column 3","Column 4", "Column 5","Column 6")) 
    table3.heading("#0", text="FINANCIAL_INFO")
    table3.heading("#1", text="MODEL")
    table3.heading("#2", text="CAR_NAME")
    table3.heading("#3", text="COLOR")
    table3.heading("#4", text="USER_NAME")
    table3.heading("#5", text="PHONE_NUMBER")
    table3.heading("#6", text="ADDRESS")
    table3.heading("#7", text="GMAIL")

    data = retrieve3_data()
    populate_table3(table3, data)
    table3.pack(expand=True, fill='both')
    b4=tb.Button(root,text="Back",bootstyle="primary outline",command=SHOWROOM_LOGIN, width="30")
    b4.place(x= 1100,y=900 , anchor=NW)


#1#1#4#
def ADD_CAR():
    global selected_option,selected_option1,selected_option2,selected_option3,e111,e113,e114,e115,e117,e118
    f2=Frame(root,width=f"{screen_width}",height=f"{screen_height}")
    f2.place(x=0,y=0)
    f2.pack_propagate(0)
    b3=tb.Button(root,text="CARS INFO",bootstyle="primary outline",command=CARS, width="30")
    b3.place(x= 200,y=100 , anchor=NW)
    b4=tb.Button(root,text="FINANCIAL INFORMATION",bootstyle="primary outline",command=MONEY, width="50")
    b4.place(x= 400,y=100 , anchor=NW)
    b5=tb.Button(root,text="CUSTOMER INFO",bootstyle="primary outline",command=USER, width="30")
    b5.place(x= 800,y=100 , anchor=NW)
    b6=tb.Button(root,text="NEW CAR",bootstyle="primary outline",command=ADD_CAR, width="30")
    b6.place(x= 600,y=100 , anchor=NW)
    b7=tb.Button(root,text="LOGOUT",bootstyle="primary outline",command=LOGIN, width="30")
    b7.place(x= 1000,y=100 , anchor=NW)
    c=Canvas(f2,bg='white',height='950',width='900')
    c.place(x=300,y=0)
    rec1=c.create_rectangle((10,180,800,650))
    l6 = tb.Label(f2, text="NEW ENTRY")
    l6.place(x=600,y=150,anchor=NW)
    label1 = tb.Label(f2, text=" MODEL")
    label1.place(x=350,y=200,anchor=NW)
    options = ["BRAND","HYUNDAI", "HONDA", "KIA","MARUTHISUZUKI","AUDI","MG","TATA","MAHINDRA"]
    selected_option = tb.StringVar()
    combobox = tb.Combobox(f2,textvariable=selected_option, values=options,bootstyle="info")
    combobox.place(x=435,y=190)
    combobox.current(0)
    selected_text = tb.StringVar()
    selected_label = tb.Label(f2, textvariable=selected_text)
    l1 = tb.Label(f2, text="CAR NAME")
    l1.place(x=350,y=260,anchor=NW)
    e111=tb.Entry(f2,width="60")
    e111.place(x=435,y=250,anchor=NW)
    label2 = tb.Label(f2, text="SEATER")
    label2.place(x=350,y=500,anchor=NW)
    options3 = ["SEATER","4 SEATER", "5 SEATER", "6 SEATER","7 SEATER","8 SEATER"]
    selected_option3 = tb.StringVar()
    combobox3 = tb.Combobox(f2,textvariable=selected_option3, values=options3,bootstyle="info")
    combobox3.place(x=435,y=500 )
    combobox3.current(0)
    selected_text = tb.StringVar()
    selected_label = tb.Label(f2, textvariable=selected_text)
    l2 = tb.Label(f2, text=" FUEL TYPE")
    l2.place(x=350,y=320,anchor=NW)
    options1 = ["FUEL","PETROL", "DIESEL", "CNG"]
    selected_option1 = tb.StringVar()
    combobox1 = tb.Combobox(f2,textvariable=selected_option1, values=options1,bootstyle="info")
    combobox1.place(x=435,y=310)
    combobox1.current(0)
    selected_text = tb.StringVar()
    selected_label = tb.Label(f2, textvariable=selected_text)
    l6 = tb.Label(f2, text="COLOR")
    l6.place(x=700,y=320,anchor=NW)
    options2 = ["COLOR","WHITE", "GREY", "RED","SILVER","BLUE","BLACK","GREEN","VIOLET","YELLOW"]
    selected_option2 = tb.StringVar()
    combobox2 = tb.Combobox(f2,textvariable=selected_option2, values=options2,bootstyle="info")
    combobox2.place(x=785,y=310)
    combobox2.current(0)
    selected_text = tb.StringVar()
    selected_label = tb.Label(f2, textvariable=selected_text)
    l3 = tb.Label(f2, text="MILEAGE")
    l3.place(x=350,y=380,anchor=NW)
    e113=tb.Entry(f2,width="30")
    e113.place(x=435,y=370,anchor=NW)
    l7 = tb.Label(f2, text="QUANTITY")
    l7.place(x=700,y=380,anchor=NW)
    e117=tb.Entry(f2,width="30")
    e117.place(x=785,y=370,anchor=NW)
    l4 = tb.Label(f2, text="MIN PRICE")
    l4.place(x=350,y=440,anchor=NW)
    e114=tb.Entry(f2,width="30")
    e114.place(x=435,y=430,anchor=NW)
    l5 = tb.Label(f2, text="MAX PRICE")
    l5.place(x=700,y=440,anchor=NW)
    e115=tb.Entry(f2,width="30")
    e115.place(x=785,y=430,anchor=NW)
    l8=tb.Label(f2,text="IMAGE")
    l8.place(x=350,y=560,anchor=NW)
    e118=tb.Entry(f2,width="80")
    e118.place(x=435,y=550,anchor=NW)
    b8=tb.Button(f2,text="SUBMIT",bootstyle="sucess outline",command=NEW_DATA, width="30")
    b8.place(x=580 ,y=610 , anchor=NW)
    
    

#1#1#4#+
def NEW_DATA():
    Id=entry1.get()
    Password=entry2.get()
    model = selected_option.get()
    car_name = e111.get()
    seater = selected_option3.get()
    fuel_type = selected_option1.get()
    color = selected_option2.get()
    mileage = e113.get()
    quantity = e117.get()
    min_price = e114.get()
    max_price = e115.get()
    image=e118.get()
    mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="DB1")
    cur=mydb.cursor()
    sqlqry="SELECT SHOWROOM FROM DE WHERE ID=%s AND PASSWORD=%s"
    cur.execute(sqlqry,(Id,Password))
    result=cur.fetchone()
    str1="CARS"
    TABLE1 = [str(item) + str1 for item in result]
    for table_car1 in TABLE1:
        sqlqry1=f"INSERT INTO {table_car1}(MODEL ,CAR,MILEAGE,SEATER ,FUELTYPE,MINPRICE,MAXPRICE,QUANTITY,COLOR,IMAGE) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        value=(model,car_name,mileage,seater,fuel_type,min_price,max_price,quantity,color,image)
        cur.execute(sqlqry1,value)
        mydb.commit()
        e111.delete(0,END)
        e117.delete(0,END)
        e113.delete(0,END)
        e114.delete(0,END)
        e115.delete(0,END)
        e118.delete(0,END)
        selected_option.set('')
        selected_option1.set('')
        selected_option2.set('')
        selected_option3.set('')
    l5 = tb.Label(root, text="DATA ENTRED SUCCESFULLY")
    l5.place(x=600,y=680,anchor=NW)















#2#
def DEVELOPER():
    f2=Frame(root,width=f"{screen_width}",height=f"{screen_height}")
    f2.place(x=0,y=0)
    f2.pack_propagate(0)
    b2=tb.Button(root,text="HOME",bootstyle="primary outline",command=city, width="30")
    b2.place(x= 100,y=100 , anchor=NW)
    b3=tb.Button(root,text="SHOWROOM",bootstyle="primary outline",command=LOGIN, width="30")
    b3.place(x= 300,y=100 , anchor=NW)
    c=Canvas(f2,bg='white',height='950',width='750')
    c.place(x=320,y=0)
    rec1=c.create_rectangle((0,180,550,400))
    label1 = tb.Label(f2, text=" ID")
    label1.place(x=350,y=200,anchor=NW)
    l1 = tb.Label(f2, text="DEVELOPER LOGIN")
    l1.place(x=500,y=150,anchor=NW)
    entry1 = tb.Entry(f2, width="50")
    entry1.place(x=450,y=200,anchor=NW)
    label2 = tb.Label(f2, text="PASSWORD")
    label2.place(x=350,y=260,anchor=NW)
    entry2 = tb.Entry(f2,width="50")
    entry2.place(x=450,y=255,anchor=NW)
    b3=tb.Button(f2,text="LOGIN",bootstyle="sucess outline",command=DEVELOPERS_LOGIN, width="30")
    b3.place(x= 450,y=330 , anchor=NW)



#2#1#
def DEVELOPERS_LOGIN():
    f2=Frame(root,width=f"{screen_width}",height=f"{screen_height}")
    f2.place(x=0,y=0)
    f2.pack_propagate(0)
    b4=tb.Button(root,text="NEW SHOWROOM",bootstyle="primary outline",command=ADD_SHOWROOM, width="30")
    b4.place(x= 200,y=100 , anchor=NW)
    b5=tb.Button(root,text="FEEDBACKS",bootstyle="primary outline",command=USER_FEEDBACK, width="30")
    b5.place(x= 400,y=100 , anchor=NW)
    b6=tb.Button(root,text="SHOWROOM-ACCESS INFO",bootstyle="primary outline",command=ID_PASSWORD, width="30")
    b6.place(x= 600,y=100 , anchor=NW)
    b7=tb.Button(root,text="LOGOUT",bootstyle="primary outline",command=DEVELOPER, width="30")
    b7.place(x= 1000,y=100 , anchor=NW)



#2#1#1#    
def ADD_SHOWROOM():
    global e11,e12,e13,e14,e15
    f2=Frame(root,width=f"{screen_width}",height=f"{screen_height}")
    f2.place(x=0,y=0)
    f2.pack_propagate(0)
    b4=tb.Button(root,text="NEW SHOWROOM",bootstyle="primary outline",command=ADD_SHOWROOM, width="30")
    b4.place(x= 200,y=100 , anchor=NW)
    b5=tb.Button(root,text="FEEDBACKS",bootstyle="primary outline",command=USER_FEEDBACK, width="30")
    b5.place(x= 400,y=100 , anchor=NW)
    b6=tb.Button(root,text="SHOWROOM-ACCESS INFO",bootstyle="primary outline",command=ID_PASSWORD, width="30")
    b6.place(x= 600,y=100 , anchor=NW)
    b7=tb.Button(root,text="LOGOUT",bootstyle="primary outline",command=DEVELOPER, width="30")
    b7.place(x= 1000,y=100 , anchor=NW)
    c=Canvas(f2,bg='white',height='950',width='900')
    c.place(x=320,y=0)
    rec1=c.create_rectangle((10,180,850,630)) 
    l1=tb.Label(f2,text="SHOWROOM NAME")
    l1.place(x=350,y=230,anchor=NW)
    e11=tb.Entry(f2,width="60")
    e11.place(x=500,y=225,anchor=NW)
    l2=tb.Label(f2,text="CITY")
    l2.place(x=350,y=290,anchor=NW)
    e12=tb.Entry(f2,width="30")
    e12.place(x=500,y=285,anchor=NW)
    l3=tb.Label(f2,text="NEW ID")
    l3.place(x=350,y=350,anchor=NW)
    e13=tb.Entry(f2,width="30")
    e13.place(x=500,y=345,anchor=NW)
    l4=tb.Label(f2,text="NEW PASSWORD")
    l4.place(x=350,y=410,anchor=NW)
    e14=tb.Entry(f2,width="30")
    e14.place(x=500,y=405,anchor=NW)
    b7=tb.Button(root,text="NEW SHOWROOM",bootstyle="success outline",command=NEW_SHOWROOM_DATA, width="30")
    b7.place(x= 550,y=530 , anchor=NW)
    l5=tb.Label(f2,text="ADDRESS")
    l5.place(x=350,y=470,anchor=NW)
    e15=tb.Entry(f2,width="80")
    e15.place(x=500,y=465,anchor=NW)
        #ID PASSWORD TABLE
    cur.execute("CREATE TABLE IF NOT EXISTS DE(ID VARCHAR(20),PASSWORD VARCHAR(20),SHOWROOM VARCHAR(30),CITY CHAR(10),ADDRESS VARCHAR(40))")


#2#1#1#+
def NEW_SHOWROOM_DATA():
    a=e13.get()
    b=e14.get()
    c=e11.get()
    d=e12.get()
    e=e15.get()
    sqlqry=("INSERT INTO DE (ID,PASSWORD,SHOWROOM,CITY,ADDRESS) VALUES(%s,%s,%s,%s,%s)")
    value=(a,b,c,d,e)
    cur.execute(sqlqry,value)
    mydb.commit()
    e11.delete(0,END)
    e12.delete(0,END)
    e13.delete(0,END)
    e14.delete(0,END)
    e15.delete(0,END)
    l4=tb.Label(root,text="SHOWROOM DATABASE CREATED")
    l4.place(x=550,y=650,anchor=NW)
    
    
    

#2#1#2#    
def USER_FEEDBACK():
    f2=Frame(root,width=f"{screen_width}",height=f"{screen_height}")
    f2.place(x=0,y=0)
    f2.pack_propagate(0)
    b4=tb.Button(root,text="NEW SHOWROOM",bootstyle="primary outline",command=ADD_SHOWROOM, width="30")
    b4.place(x= 200,y=100 , anchor=NW)
    b5=tb.Button(root,text="FEEDBACKS",bootstyle="primary outline",command=USER_FEEDBACK, width="30")
    b5.place(x= 400,y=100 , anchor=NW)
    b6=tb.Button(root,text="SHOWROOM-ACCESS INFO",bootstyle="primary outline",command=ID_PASSWORD, width="30")
    b6.place(x= 600,y=100 , anchor=NW)
    b7=tb.Button(root,text="LOGOUT",bootstyle="primary outline",command=DEVELOPER, width="30")
    b7.place(x= 1000,y=100 , anchor=NW)
    


#2#1#3#
def ID_PASSWORD():
    mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="DB1")
    cur=mydb.cursor()
    f2=Frame(root,width=f"{screen_width}",height=f"{screen_height}")
    f2.place(x=0,y=0)
    f2.pack_propagate(0)
    b4=tb.Button(root,text="NEW SHOWROOM",bootstyle="primary outline",command=ADD_SHOWROOM, width="30")
    b4.place(x= 200,y=100 , anchor=NW)
    b5=tb.Button(root,text="FEEDBACKS",bootstyle="primary outline",command=USER_FEEDBACK, width="30")
    b5.place(x= 400,y=100 , anchor=NW)
    b6=tb.Button(root,text="SHOWROOM-ACCESS INFO",bootstyle="primary outline",command=ID_PASSWORD, width="30")
    b6.place(x= 600,y=100 , anchor=NW)
    b7=tb.Button(root,text="LOGOUT",bootstyle="primary outline",command=DEVELOPER, width="30")
    b7.place(x= 1000,y=100 , anchor=NW)
    def retrieve_data():
        cur.execute("SELECT * FROM DE")
        rows = cur.fetchall()
        cur.close()
        mydb.close()
        return rows

    def populate_table(table, data):
        for i, row in enumerate(data):
            table.insert('', 'end', values=row)
            for col in table["columns"]:
                        table.column(col, anchor="center")

    tb.Label(root,text=" ").pack()
    tb.Label(root,text=" ").pack()
    tb.Label(root,text=" ").pack()
    tb.Label(root,text=" ").pack()
    table = ttk.Treeview(root, columns=("Column 0", "Column 1", "Column 2","column 3","column 4")) 
    table.heading("#0", text="ID_PASSWORD")
    table.heading("#1", text="ID")
    table.heading("#2", text="PASSWORD")
    table.heading("#3", text="SHOWROOM")
    table.heading("#4", text="CITY")
    table.heading("#5", text="ADDRESS")
    data = retrieve_data()
    populate_table(table, data)
    table.pack(expand=True, fill='both')
    b4=tb.Button(root,text="Back",bootstyle="primary outline",command=DEVELOPERS_LOGIN, width="30")
    b4.place(x= 20,y=10 , anchor=NW)












#3#   
def CONTACT():
    f2=Frame(root,width=f"{screen_width}",height=f"{screen_height}")
    f2.place(x=0,y=0)
    f2.pack_propagate(0)
    b2=tb.Button(root,text="HOME",bootstyle="primary outline",command=city, width="30")
    b2.place(x= 100,y=70 , anchor=NW)
    b3=tb.Button(root,text="SHOWROOM",bootstyle="primary outline",command=LOGIN, width="30")
    b3.place(x= 300,y=70 , anchor=NW)
    c=Canvas(f2,bg='white',height='950',width='750')
    c.pack()
    rec1=c.create_rectangle((10,180,520,400))
    label1 = tb.Label(f2, text="PROBLEM")
    label1.place(x=350,y=200,anchor=NW)
    l1 = tb.Label(f2, text="CONTACT US")
    l1.place(x=500,y=150,anchor=NW)
    entry1 = tb.Entry(f2, width="50")
    entry1.place(x=430,y=200,anchor=NW)
    label2 = tb.Label(f2, text="EMAIL")
    label2.place(x=350,y=260,anchor=NW)
    entry2 = tb.Entry(f2, width="50")
    entry2.place(x=430,y=255,anchor=NW)
    label3 = tb.Label(f2, text="PHONE NO")
    label3.place(x=350,y=320,anchor=NW)
    entry3 = tb.Entry(f2, width="50")
    entry3.place(x=430,y=315,anchor=NW)
    b4=tb.Button(f2,text="SUBMIT",bootstyle="sucess outline",command=FEEDBACK, width="30")
    b4.place(x= 480,y=365 , anchor=NW)


#3#1#
def FEEDBACK():    
    l1 = tb.Label(root, text="FEEDBACK SENT")
    l1.place(x=520,y=415,anchor=NW)












#
def Hyderabad():
    f2=Frame(root,width=f"{screen_width}",height=f"{screen_height}")
    f2.place(x=0,y=0)
    f2.pack_propagate(0)
    image_path = r"C:\Users\chand\Downloads\RTP\BackGround1.jpg"
    image = Image.open(image_path)
    image = image.resize((860, 600))
    photo = ImageTk.PhotoImage(image)
    image_label = tb.Label(f2, image=photo)
    image_label.image = photo
    image_label.place(x=100,y=135)
    b1=tb.Button(root,text="EXPLORE CARS",bootstyle="success outline",command=SEARCH_CARS, width="30")
    b1.place(x= 400,y=650 , anchor=NW)
    b2=tb.Button(root,text="HOME",bootstyle="primary outline",command=city, width="30")
    b2.place(x= 100,y=100 , anchor=NW)
    b3=tb.Button(root,text="SHOWROOM",bootstyle="primary outline",command=LOGIN, width="30")
    b3.place(x= 300,y=100 , anchor=NW)
    b4=tb.Button(root,text="DEVELOPER LOGIN",bootstyle="primary outline",command=DEVELOPER, width="30")
    b4.place(x= 500,y=100 , anchor=NW)
    b5=tb.Button(root,text="CONTACT US",bootstyle="primary outline",command=CONTACT, width="30")
    b5.place(x= 700,y=100 , anchor=NW)
    
    
#    
def Chennai():
    variable=Chennai
    f2=Frame(root,width=f"{screen_width}",height=f"{screen_height}")
    f2.place(x=0,y=0)
    f2.pack_propagate(0)
    image_path = r"C:\Users\chand\Downloads\RTP\BackGround1.jpg"
    image = Image.open(image_path)
    image = image.resize((860, 600))
    photo = ImageTk.PhotoImage(image)
    image_label = tb.Label(f2, image=photo)
    image_label.image = photo
    image_label.place(x=100,y=135)
    b1=tb.Button(root,text="EXPLORE CARS",bootstyle="success outline",command=SEARCH_CARS, width="30")
    b1.place(x= 400,y=650 , anchor=NW)
    b2=tb.Button(root,text="HOME",bootstyle="primary outline",command=city, width="30")
    b2.place(x= 100,y=100 , anchor=NW)
    b3=tb.Button(root,text="SHOWROOM",bootstyle="primary outline",command=LOGIN, width="30")
    b3.place(x= 300,y=100 , anchor=NW)
    b4=tb.Button(root,text="DEVELOPER LOGIN",bootstyle="primary outline",command=DEVELOPER, width="30")
    b4.place(x= 500,y=100 , anchor=NW)
    b5=tb.Button(root,text="CONTACT US",bootstyle="primary outline",command=CONTACT, width="30")
    b5.place(x= 700,y=100 , anchor=NW)
#
def Delhi():
    image_path = r"C:\Users\chand\Downloads\RTP\BackGround1.jpg"
    image = Image.open(image_path)
    image = image.resize((860, 600))
    photo = ImageTk.PhotoImage(image)
    image_label = tb.Label(f2, image=photo)
    image_label.image = photo
    image_label.place(x=100,y=135)
    b1=tb.Button(root,text="EXPLORE CARS",bootstyle="success outline",command=SEARCH_CARS, width="30")
    b1.place(x= 400,y=650 , anchor=NW)
    b2=tb.Button(root,text="HOME",bootstyle="primary outline",command=city, width="30")
    b2.place(x= 100,y=100 , anchor=NW)
    b3=tb.Button(root,text="SHOWROOM",bootstyle="primary outline",command=LOGIN, width="30")
    b3.place(x= 300,y=100 , anchor=NW)
    b4=tb.Button(root,text="DEVELOPER LOGIN",bootstyle="primary outline",command=DEVELOPER, width="30")
    b4.place(x= 500,y=100 , anchor=NW)
    b5=tb.Button(root,text="CONTACT US",bootstyle="primary outline",command=CONTACT, width="30")
    b5.place(x= 700,y=100 , anchor=NW)
#
def Kolkata():
    f2=Frame(root,width=f"{screen_width}",height=f"{screen_height}")
    f2.place(x=0,y=0)
    f2.pack_propagate(0)
    image_path = r"C:\Users\chand\Downloads\RTP\BackGround1.jpg"
    image = Image.open(image_path)
    image = image.resize((860, 600))
    photo = ImageTk.PhotoImage(image)
    image_label = tb.Label(f2, image=photo)
    image_label.image = photo
    image_label.place(x=100,y=135)
    b1=tb.Button(root,text="EXPLORE CARS",bootstyle="success outline",command=SEARCH_CARS, width="30")
    b1.place(x= 400,y=650 , anchor=NW)
    b2=tb.Button(root,text="HOME",bootstyle="primary outline",command=city, width="30")
    b2.place(x= 100,y=100 , anchor=NW)
    b3=tb.Button(root,text="SHOWROOM",bootstyle="primary outline",command=LOGIN, width="30")
    b3.place(x= 300,y=100 , anchor=NW)
    b4=tb.Button(root,text="DEVELOPER LOGIN",bootstyle="primary outline",command=DEVELOPER, width="30")
    b4.place(x= 500,y=100 , anchor=NW)
    b5=tb.Button(root,text="CONTACT US",bootstyle="primary outline",command=CONTACT, width="30")
    b5.place(x= 700,y=100 , anchor=NW)
#
def Mumbai():
    f2=Frame(root,width=f"{screen_width}",height=f"{screen_height}")
    f2.place(x=0,y=0)
    f2.pack_propagate(0)
    image_path = r"C:\Users\chand\Downloads\RTP\BackGround1.jpg"
    image = Image.open(image_path)
    image = image.resize((860, 600))
    photo = ImageTk.PhotoImage(image)
    image_label = tb.Label(f2, image=photo)
    image_label.image = photo
    image_label.place(x=100,y=135)
    b1=tb.Button(root,text="EXPLORE CARS",bootstyle="success outline",command=SEARCH_CARS, width="30")
    b1.place(x= 400,y=650 , anchor=NW)
    b2=tb.Button(root,text="HOME",bootstyle="primary outline",command=city, width="30")
    b2.place(x= 100,y=100 , anchor=NW)
    b3=tb.Button(root,text="SHOWROOM",bootstyle="primary outline",command=LOGIN, width="30")
    b3.place(x= 300,y=100 , anchor=NW)
    b4=tb.Button(root,text="DEVELOPER LOGIN",bootstyle="primary outline",command=DEVELOPER, width="30")
    b4.place(x= 500,y=100 , anchor=NW)
    b5=tb.Button(root,text="CONTACT US",bootstyle="primary outline",command=CONTACT, width="30")
    b5.place(x= 700,y=100 , anchor=NW)
    

   


def SEARCH_CARS():
    global e21,e22,selected_option11,selected_option22,selected_option33,selected_option44,selected_option55,selected_option66
    f2=Frame(root,width=f"{screen_width}",height=f"{screen_height}")
    f2.place(x=0,y=0)
    f2.pack_propagate(0)
    c=Canvas(f2,bg='white',height='950',width='750')
    c.place(x=300,y=0)
    rec1=c.create_rectangle((10,180,700,600))
    l6 = tb.Label(f2, text="NEW ENTRY")
    l6.place(x=600,y=150,anchor=NW)
    label1 = tb.Label(f2, text=" MODEL")
    label1.place(x=350,y=200,anchor=NW)
    options11 = ["BRAND","HYUNDAI", "HONDA", "KIA","MARUTHISUZUKI","AUDI","MG","TATA","MAHINDRA"]
    selected_option11 = tb.StringVar()
    combobox11 = tb.Combobox(f2,textvariable=selected_option11, values=options11,bootstyle="info")
    combobox11.place(x=435,y=190)
    combobox11.current(0)
    selected_text = tb.StringVar()
    selected_label = tb.Label(f2, textvariable=selected_text)
    l1 = tb.Label(f2, text="SEATER")
    l1.place(x=350,y=260,anchor=NW)
    options22 = ["SEATER","4 SEATER", "5 SEATER", "6 SEATER","7 SEATER","8 SEATER"]
    selected_option22 = tb.StringVar()
    combobox22 = tb.Combobox(f2,textvariable=selected_option22, values=options22,bootstyle="info")
    combobox22.place(x=435,y=250)
    combobox22.current(0)
    selected_text = tb.StringVar()
    selected_label = tb.Label(f2, textvariable=selected_text)
    l2 = tb.Label(f2, text=" FUEL TYPE")
    l2.place(x=350,y=320,anchor=NW)
    options33 = ["FUEL","PETROL", "DIESEL", "CNG"]
    selected_option33 = tb.StringVar()
    combobox33 = tb.Combobox(f2,textvariable=selected_option33, values=options33,bootstyle="info")
    combobox33.place(x=435,y=310)
    combobox33.current(0)
    selected_text = tb.StringVar()
    selected_label = tb.Label(f2, textvariable=selected_text)
    l6 = tb.Label(f2, text="COLOR")
    l6.place(x=700,y=320,anchor=NW)
    options44 = ["COLOR","WHITE", "GREY", "RED","SILVER","BLUE","BLACK","GREEN","VIOLET","YELLOW"]
    selected_option44 = tb.StringVar()
    combobox44 = tb.Combobox(f2,textvariable=selected_option44, values=options44,bootstyle="info")
    combobox44.place(x=785,y=310)
    combobox44.current(0)
    selected_text = tb.StringVar()
    selected_label = tb.Label(f2, textvariable=selected_text)
    l7 = tb.Label(f2, text="CITY")
    l7.place(x=700,y=380,anchor=NW)
    options66 = ["CITY","Hyderabad", "Kolkata", "Delhi","Mumbai","Chennai"]
    selected_option66 = tb.StringVar()
    combobox66 = tb.Combobox(f2,textvariable=selected_option66, values=options66,bootstyle="info")
    combobox66.place(x=785,y=370)
    combobox66.current(0)
    selected_text = tb.StringVar()
    selected_label = tb.Label(f2, textvariable=selected_text)
    l3 = tb.Label(f2, text="MILEAGE")
    l3.place(x=350,y=380,anchor=NW)
    e21=tb.Entry(f2,width="30")
    e21.place(x=435,y=370,anchor=NW)
    l4 = tb.Label(f2, text="AMOUNT")
    l4.place(x=350,y=440,anchor=NW)
    e22=tb.Entry(f2,width="30")
    e22.place(x=435,y=430,anchor=NW)
    b8=tb.Button(f2,text="SEARCH",bootstyle="sucess outline",command=NEW_SEARCH, width="30")
    b8.place(x=580 ,y=550 , anchor=NW)
    b2=tb.Button(root,text="HOME",bootstyle="primary outline",command=city, width="30")
    b2.place(x= 100,y=100 , anchor=NW)
    
def NEW_SEARCH():
    global j
    A=selected_option66.get()
    sqlqry3="SELECT SHOWROOM FROM DE WHERE CITY='"+A+"'"
    cur.execute(sqlqry3)
    res=cur.fetchall()
    for jj in res:
        SEARCH(jj)
    #sqlqry1="SELECT COUNT(*) FROM DE WHERE CITY='"+A+"'"
    #cur.execute(sqlqry1)
    #res1=cur.fetchone()
    #count_result = res1[0]  
    #res2 = count_result + 1
    #for aa in range(0,res2):
     #   SEARCH(res[aa])
    
    

def SEARCH(showroom_name):
    global row, col
    str1="CARS"
    S1 = [str(item) + str1 for item in showroom_name]
    a=(e21.get())
    b=(e22.get())
    c=selected_option11.get()
    d=selected_option22.get()
    e=selected_option33.get()
    f=selected_option44.get()
    g=b
    # Convert the list into a string with elements separated by a comma
    print(S1) 
    separator = ', '
    s1 = separator.join(S1)
    print(s1)
    model ='MODEL'
    seater='SEATER'
    color='COLOR'
    mileage='MILEAGE'
    fuel='FUELTYPE'
    minprice='MINPRICE'
    maxprice='MAXPRICE'
    QUR=("SELECT MODEL, CAR, SEATER, FUELTYPE, MINPRICE, MILEAGE, IMAGE,COUNT(*),QUANTITY FROM  {} where {}=%s and {}=%s and {}=%s and {}=%s and {}<=%s and {}>=%s and {}=%s".format(s1,model,mileage,seater,fuel,minprice,maxprice,color))
    cur.execute(QUR,(c,a,d,e,b,g,f))
    ans= cur.fetchall()
    print(ans)
    A=selected_option66.get()
    sqlqry4="SELECT COUNT(*) FROM DE WHERE CITY='"+A+"'"
    cur.execute(sqlqry4)
    ans1=cur.fetchall()

    max_col = 3
    max_row = 15
    i = 0
    j = 0
    k = 0
    for j in range(0, max_row):
        if j >= len(ans):
            break 
        for k in range(0, ans[j][7]):
            if ans[k][8] > 0:
                t = ans[k][1]
                if i >= max_col:
                    i = 0
                    j += 1
                if j >= max_row:
                    break
                fji = tb.Frame(root, width=f"{screen_width}",height=f"{screen_height}")
                fji.grid(row=j, column=i)
                image_path = rf"C:\Users\chand\Downloads\RTP\CARS1\CARS\{c}\{t}\{f}.jpg"
                print(image_path)
                try:
                    image = Image.open(image_path)
                    image = image.resize((250, 200))
                    photo = ImageTk.PhotoImage(image)
                    image_label = tb.Label(fji, image=photo)
                    image_label.image = photo  
                    image_label.place(x=15, y=15)
                except Exception as e:
                    print(f"Error loading image: {e}")

                lji1 = tb.Label(fji, text="Mileage-")
                lji1.place(x=10, y=250, anchor=tb.NW)
                
                lji2 = tb.Label(fji, text=ans[k][1])
                lji2.place(x=10, y=210, anchor=tb.NW)

                lji3 = tb.Label(fji, text=ans[k][2])
                lji3.place(x=10, y=230, anchor=tb.NW)

                lji4 = tb.Label(fji, text=ans[k][3])
                lji4.place(x=100, y=230, anchor=tb.NW)

                lji5 = tb.Label(fji, text=ans[k][4])
                lji5.place(x=100, y=250, anchor=tb.NW)

                lji6 = tb.Label(fji, text=ans[k][5])
                lji6.place(x=55, y=250, anchor=tb.NW)

                lji7 = tb.Label(fji, text="ShowRoom-")
                lji7.place(x=10, y=270, anchor=tb.NW)

                lji8 = tb.Label(fji, text=showroom_name)
                lji8.place(x=95, y=270, anchor=tb.NW)

                lji9 = tb.Label(fji, text="₹")
                lji9.place(x=90, y=250, anchor=tb.NW)

                bji1 = tb.Button(fji, text="BOOK", bootstyle="success outline", command=lambda: BOOKING(), width=7)
                bji1.place(x=60, y=290, anchor=tb.NW)
                i += 1


            
            
        
        

def BOOKING():
    global h1,h2,h3,h4
    f2=Frame(root,width=f"{screen_width}",height=f"{screen_height}")
    f2.place(x=0,y=0)
    f2.pack_propagate(0)
    b2=tb.Button(root,text="BACK",bootstyle="primary outline",command=SEARCH_CARS, width="30")
    b2.place(x= 100,y=70 , anchor=NW)
    c=Canvas(f2,bg='white',height='950',width='750')
    c.pack()
    rec1=c.create_rectangle((10,180,520,400))
    label1 = tb.Label(f2, text="CAR BOOKING")
    label1.place(x=350,y=200,anchor=NW)
    l1 = tb.Label(f2, text="CUSTOMER NAME")
    l1.place(x=500,y=150,anchor=NW)
    h1 = tb.Entry(f2, width="50")
    h1.place(x=430,y=200,anchor=NW)
    label2 = tb.Label(f2, text="PHONE NUMBER")
    label2.place(x=350,y=260,anchor=NW)
    h2 = tb.Entry(f2, width="50")
    h2.place(x=430,y=255,anchor=NW)
    label3 = tb.Label(f2, text="EMAIL")
    label3.place(x=350,y=320,anchor=NW)
    h3 = tb.Entry(f2, width="50")
    h3.place(x=430,y=315,anchor=NW)
    label4 = tb.Label(f2, text="ADDRESS")
    label4.place(x=350,y=380,anchor=NW)
    h4 = tb.Entry(f2, width="50")
    h4.place(x=430,y=375,anchor=NW)
    b4=tb.Button(f2,text="SUBMIT",bootstyle="sucess outline",command=USER_ENTRY, width="30")
    b4.place(x= 480,y=365 , anchor=NW)



def USER_ENTRY():
    a=h1.get()
    b=h2.get()
    c=h3.get()
    d=h4.get()
    e=m
        
    
    
    
    
    



        
        
        
    
    
    
    
    
    
    
b1=tb.Button(root,text="SELECT CITY",bootstyle="success outline",command=city, width="30")
b1.place(x= 580,y=480 , anchor=NW)
root.mainloop()
