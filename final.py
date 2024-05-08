from tkinter import *
root=Tk()

import pandas as pd
import joblib
def new():
    new=Toplevel(root)
    new.geometry("710x500")
    new.resizable(0,0)
    new.title("A1 CAR BAZAAR")
    new.config(bg="#FFE4C4")
    Label(new,text="A1 CAR BAZAAR",font="italic 20 bold",pady=30,padx=50,bg="#FFE4C4").grid(row=0,column=0)
    

    def show_entry_feilds():
        new2=Toplevel(new)
        new2.geometry("710x500")
        new2.resizable(0,0)
        new2.title("A1 CAR BAZAAR")
        new2.config(bg="#E0EEEE")
        Label(new2,text="A1 CAR BAZAAR",font="italic 20 bold",pady=30,padx=50,bg="#E0EEEE").pack()
        p1=float(e1.get())
        p2=float(e2.get())
        # p3=t3.get()
        # p4=t4.get()
        # p5=t5.get()
        p3=1
        p4=1
        p5=0

        p6=float(myslider.get())
        p7=float(myslider2.get())

        model = joblib.load('Car_Bazaar')
        data_new = pd.DataFrame({
            'Present_Price':p1,
            'Kms_Driven':p2,
            'Fuel_Type':p3,
            'Seller_Type':p4,
            'Transmission':p5,
            'Owner':p6,
            'Age':p7
        },index=[0])

        result = model.predict(data_new)

        Label(new2,text="THE ESTIMATED COST OF YOUR CAR COMES OUT TO BE : ",font="lucida 15 bold",bg="#E0EEEE",padx=20,pady=20).pack()
        Label(new2,text=f"Amount : {result[0]:.2f} Lakhs",font="lucida 12 bold",padx=20,pady=20,bg="#E0EEEE").pack()

    Label(new, text="PRESENT PRICE :",bg="#FFE4C4",pady=5).grid(row=1,column=0)
    Label(new, text="Kms DRIVEN :",bg="#FFE4C4",pady=5).grid(row=2,column=0)
    Label(new, text="FUEL TYPE :",bg="#FFE4C4",pady=5).grid(row=3,column=0)
    Label(new, text="SELLER TYPE :",bg="#FFE4C4",pady=5).grid(row=4,column=0)
    Label(new, text="TRANSMISSION :",bg="#FFE4C4",pady=5).grid(row=5,column=0)
    Label(new, text="No. OF PAST OWNERS :",bg="#FFE4C4",pady=5).grid(row=6,column=0)
    Label(new, text="AGE SINCE REGISTERED :",bg="#FFE4C4",pady=5).grid(row=7,column=0)

    e1 = Entry(new)
    e2 = Entry(new)

    e1.grid(row=1,column=1)
    e2.grid(row=2,column=1)

    Label(new,text="Lakhs",bg="#FFE4C4").grid(row=1,column=2)
    Label(new,text="Km",bg="#FFE4C4").grid(row=2,column=2)

    
    t3 = IntVar
    radio = Radiobutton(new,text="PETROL",padx=20,variable=t3,value=0,bg="#FFE4C4").grid(row=3,column=1)
    radio = Radiobutton(new,text="DIESEL",padx=20,variable=t3,value=1,bg="#FFE4C4").grid(row=3,column=2)
    radio = Radiobutton(new,text="CNG",padx=20,variable=t3,value=2,bg="#FFE4C4").grid(row=3,column=3)

    t4 = IntVar
    radio = Radiobutton(new,text="DEALER",padx=20,variable=t4,value=0,bg="#FFE4C4").grid(row=4,column=1)
    radio = Radiobutton(new,text="INDIVIDUAL",padx=20,variable=t4,value=1,bg="#FFE4C4").grid(row=4,column=2)

    t5 = IntVar
    radio = Radiobutton(new,text="MANUAL",padx=20,variable=t5,value=0,bg="#FFE4C4").grid(row=5,column=1)
    radio = Radiobutton(new,text="AUTOMATIC",padx=20,variable=t5,value=1,bg="#FFE4C4").grid(row=5,column=2)

    myslider = Scale(new,from_=0,to=10,orient=HORIZONTAL,tickinterval=2,bg="#CDB79E")
    myslider.grid(row=6,column=1)
    myslider2 = Scale(new,from_=0,to=10,orient=HORIZONTAL,tickinterval=2,bg="#CDB79E")
    myslider2.grid(row=7,column=1)

    Button(new,text='PREDICT',command=show_entry_feilds,padx=5,pady=5,relief=SUNKEN).grid(column=1)


root.geometry("710x500")
root.title("CAR BAZAAR")
root.config(bg='#00FFFF')
root.resizable(0,0)
Label(root,text="A1 CAR BAZAAR",font="CooperBlack 24 bold ",pady=30,padx=225,fg="blue",bg="skyblue",relief=RIDGE).pack()
Label(root,text="Want To Find Out The BEST Selling Price Of Your Used Car ?",font="BerlinSansFBDemi 15 bold",padx=5,pady=40,bg="#00FFFF").pack()
Button(text="LETS GO!!!",font="ArialBlack 15 bold",padx=10,pady=20,relief=RIDGE,bg="#F0FFFF",fg="red",command=new).pack()



root.mainloop()