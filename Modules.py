# Modules
from tkinter import *
from tkinter import ttk
import random
from datetime import datetime
import time

def signin(k,frm):
    frm.destroy()
    root = Tk()
    root.geometry("1000x1000")
    root.title("Restaurant Management System")
    frame1= Frame(root,padx=10,pady=20,)
    frame1.grid(row=0,column=0)
    l1=Label(frame1,text="Welcome "+str(k)+"!",font=(" Times New Roman",20))
    l1.grid(padx=20,pady=12,row=0,column=0)

    user = Label(frame1, text="Name",font="Algerian 16",anchor=W)
    people = Label(frame1, text="No. of people",font="Algerian 16",anchor=W)

    user.grid(row=1,padx=12,pady=20)
    people.grid(row=2,padx=12,pady=16)

    uservalue = StringVar()
    peoplevalue = StringVar()

    userentry = Entry(frame1, textvariable = uservalue)
    peopleentry = Entry(frame1, textvariable = peoplevalue)
    userentry.grid(row=1,column=1)
    peopleentry.grid(row=2,column=1)
    Button(frame1,text="Submit",command = lambda: welcome(frame1,root),padx=20,pady=10,font="20",bg="grey",fg="white").grid(row=4,column=1)

    label = Label(frame1,font=("Courier", 20, 'bold'), bg="gray", fg="white", bd =12,padx=10,pady=6)
    label.grid(row =0, column=2)

    def digitalclock():
        text_input = time.strftime("%H:%M:%S")
        label.config(text=text_input)
        label.after(200, digitalclock)
    digitalclock()



def welcome(f,r):
    a=random.randrange(1,6)
    #print("Please proceed to table no.",a,"\n","We hope you have a nice experience!!!!")
    l1=Label(f,text="Please proceed to table no."+str(a),font="20")
    l1.grid(padx=20,pady=12,row=1,column=2)
    l2 = Label(f,text="Click on proceed button below to view menu card",font="20")
    l2.grid(padx=20,pady=12,row=2,column=2)
    l3 = Label(f,text="We hope you have a great experience!!!!",font="20")
    l3.grid(padx=20,pady=12,row=3,column=2)
    Button(f,text="Proceed",command = lambda:mnu(f,r),padx=20,pady=10,font="20",bg="grey",fg="white").grid(row=4,column=2)


bev = (        'Regular Tea',
                'Masala Tea',
            	'Coffee',
                'Cold Drink',
                'Bread Butter',
                'Bread Jam',
                'Veg. Sandwich',
                'Veg. Toast Sandwich'
                'Cheese Toast Sandwich',
                'Grilled Sandwich')

suop = (	    'Tomato Soup',
                'Hot & Sour',
                'Veg. Noodle Soup',
                'Sweet Corn',
                'Veg. Munchow')

m_course = (    'Shahi Paneer',
                'Kadai Paneer',
                'Handi Paneer',
                'Palak Paneer',
                'Chilli Paneer',
                'Matar Mushroom',
                'Mix Veg',
                'Jeera Aloo',
                'Malai Kofta',
                'Aloo Matar',
				'Dal Fry',
				'Dal Makhani',
				'Dal Tadka')

chapti = (		'Plain Roti',  
                'Butter Roti',  
                'Tandoori Roti', 
                'Butter Naan')
 
rice = (        'Plain Rice',
               	'Jeera Rice',
                'Veg Pulao',
                'Peas Pulao')

souin = (        'Plain Dosa',
          		'Onion Dosa',
                'Masala Dosa',
                'Paneer Dosa',
                'Rice Idli',
                'Sambhar Vada')

icrm = (        'Vanilla',
                'Strawberry',
                'Pineapple',
                'Butter Scotch')

dict={'Regular Tea':20,'Masala Tea':25,'Coffee':25,'Cold Drink':25,'Bread Butter':30,'Bread Jam':30,'Veg. Sandwich':50,'Veg. Toast Sandwich':50,'Cheese Toast Sandwich':70,'Grilled Sandwich':70,
'Tomato Soup':100,'Hot & Sour':100,'Veg. Noodle Soup':110,'Sweet Corn':110,'Veg Munchow':110,
'Shahi Paneer':110,'Kadai Paneer':110,'Handi Paneer':120,'Palak Paneer':120,'Chilli Paneer':140,'Matar Mashroom':140,'Mix Veg':140,'Jeera Aloo':140,'Malai Kofta':140,'Aloo Matar':140,'Dal Fry':140,'Dal Makhani':150,'Dal Tadka':150,
'Plain Roti':15,'Butter Roti':15,'Tandoori Roti':20,'Butter Naan':20,'Plain Rice':90,'Jeera Rice':90,'Veg Pulao':110,'Peas Pulao':110,
'Plain Dosa':110,'Onion Dosa':110,'Masala Dosa':110,'Paneer Dosa':130,'Rice Idli':130,'Sambhar Vada':140,
'Vanilla':60,'Strawberry':60,'Pineapple':60,'Butter Scotch':60}
num_lis = ['example'] 
od_lis = [0]
flag = 0
def get_order():
    global od_lis
    global num_lis
    return [num_lis[1:],od_lis[1:]]

def selected_item(lb,fm):
    global od_lis
    global num_lis
    itm = lb.get(lb.curselection())
    for i in range(len(itm)):
        if itm[i]=='*':
           t = i
           r = get_order()[1].index(itm[:t-1])
           if get_order()[0][r]==1:
               p = od_lis.index(itm[:t-1])
               od_lis.remove(itm[:t-1])
               num_lis.pop(p)
           else:
               p = od_lis.index(itm[:t-1])
               num_lis[p] = num_lis[p] -1
    show_item(fm)

def show_item(fm):
    lisbox = Listbox(fm,width = 30,height = 30)

    for i in range(len(get_order()[1])):
        lisbox.insert(i,str(get_order()[1][i])+" *"+str(get_order()[0][i]))

    lisbox.grid(row = 0, column = 0)
    btn =Button(fm,text="REMOVE", command=lambda: selected_item(lisbox,fm))
    btn.grid(row=0,column=1)
    
def ad(k,frme):
    global od_lis
    global num_lis
    if k in od_lis:
        j = od_lis.index(k)
        num_lis[j] = num_lis[j] + 1
    else:
        od_lis = od_lis + [k]
        num_lis = num_lis + [1]
    show_item(frme)

def mnu(fr,rt):
    fr.destroy()
    frame3= Frame(rt,padx=10,pady=20)
    frame3.grid(row=0,column=0)
    frame4= Frame(rt,padx=10,pady=20)
    frame4.grid(row=0,column=3)
    '''To select Bevrages'''
    l1 = Label(frame3, text = "Select the bevrages :",font = ("Times New Roman", 10))
    l1.grid(column = 0,row = 0, padx = 10, pady = 25)

    n1 = StringVar()
    choosen1 = ttk.Combobox(frame3, width = 27,textvariable = n1)
    # Adding combobox drop down list
    choosen1['values'] = bev
    b1 =Button(frame3,text="ADD", command=lambda: ad(n1.get(),frame4))
    b1.grid(row=1,column=1)
    choosen1.grid(column = 1, row = 0)
    choosen1.current()

    '''To select Soups'''
    l2 = Label(frame3, text = "Select the soups :",font = ("Times New Roman", 10))
    l2.grid(column = 0, row = 3, padx = 10, pady = 25)

    n2 = StringVar()
    choosen2 = ttk.Combobox(frame3, width = 27,textvariable = n2)
    # Adding combobox drop down list
    choosen2['values'] = suop
    b2 = Button(frame3,text="ADD", command=lambda: ad(n2.get(),frame4))
    b2.grid(row=4,column=1)
    choosen2.grid(column = 1, row = 3)
    choosen2.current()

    '''To select Main Course'''
    l3 = Label(frame3, text = "Select the Main Course :",font = ("Times New Roman", 10))
    l3.grid(column = 0,row =6 , padx = 10, pady = 25)

    n3 = StringVar()
    choosen3 = ttk.Combobox(frame3, width = 27,textvariable = n3)
    # Adding combobox drop down list
    choosen3['values'] = m_course
    b3 = Button(frame3,text="ADD", command=lambda: ad(n3.get(),frame4))
    b3.grid(row=7,column=1)
    choosen3.grid(column = 1, row = 6)
    choosen3.current()

    '''To select Chappatis'''
    l4 = Label(frame3, text = "Select the Chapaatis :",font = ("Times New Roman", 10))
    l4.grid(column = 0,row = 9, padx = 10, pady = 25)

    n4 = StringVar()
    choosen4 = ttk.Combobox(frame3, width = 27,textvariable = n4)
    # Adding combobox drop down list
    choosen4['values'] = chapti
    b4 = Button(frame3,text="ADD", command=lambda: ad(n4.get(),frame4))
    b4.grid(row=10,column=1)
    choosen4.grid(column = 1, row = 9)
    choosen4.current()

    '''To select Rice'''
    l5 = Label(frame3, text = "Select Rice :",font = ("Times New Roman", 10))
    l5.grid(column = 0,row = 12, padx = 10, pady = 25)

    n5 = StringVar()
    choosen5 = ttk.Combobox(frame3, width = 27,textvariable = n5)
    # Adding combobox drop down list
    choosen5['values'] = rice
    b5 = Button(frame3,text="ADD", command=lambda: ad(n5.get(),frame4))
    b5.grid(row=13,column=1)
    choosen5.grid(column = 1, row = 12)
    choosen5.current()

    '''To select South Indian'''
    l6 = Label(frame3, text = "Select the South Indian :",font = ("Times New Roman", 10))
    l6.grid(column = 0,row = 15, padx = 10, pady = 25)

    n6 = StringVar()
    choosen6 = ttk.Combobox(frame3, width = 27,textvariable = n6)
    # Adding combobox drop down list
    choosen6['values'] = souin
    b6 = Button(frame3,text="ADD", command=lambda: ad(n6.get(),frame4))
    b6.grid(row=16,column=1)
    choosen6.grid(column = 1, row = 15)
    choosen6.current()

    '''To select ice cream'''
    l7 = Label(frame3, text = "Select the ice cream :",font = ("Times New Roman", 10))
    l7.grid(column = 0,row = 18, padx = 10, pady = 25)

    n7 = StringVar()
    choosen7 = ttk.Combobox(frame3, width = 27,textvariable = n7)
    # Adding combobox drop down list
    choosen7['values'] = icrm
    b7 = Button(frame3,text="ADD", command=lambda: ad(n7.get(),frame4))
    b7.grid(row=19,column=1)
    choosen7.grid(column = 1, row = 18)
    choosen7.current()
    
    b8 =Button(frame4,text="Done",command = bil,padx=20,pady=10,font="20",bg="grey",fg="white")
    b8.grid(row=10,column=3)

def bil():
    rot = Tk()
    rot.geometry("500x500")
    Label(rot,text="Taj Hotel",font="Helvetica 16 bold").grid(column=2,row=0)
    Label(rot,text="Manewada,Nagpur",font="Helvetica 16 bold").grid(column=2,row=1)
    Label(rot,text=(datetime.now())).grid(column=2,row=2)
    cnt=1
    rw=5
    n_lis = get_order()[0]
    o_lis = get_order()[1]
    Label(rot,text='Sr.No',font="Helvetica 16 bold").grid(column=0,row=4)
    Label(rot,text='Quantity',font="Helvetica 16 bold").grid(column=1,row=4)
    Label(rot,text='Item',font="Helvetica 16 bold").grid(column=2,row=4)
    Label(rot,text='Price',font="Helvetica 16 bold").grid(column=3,row=4)
    for i in o_lis:
        Label(rot,text=(cnt),font="Helvetica 16 bold").grid(column=0,row=rw)
        Label(rot,text=n_lis[o_lis.index(i)],font="Helvetica 16 bold").grid(column=1,row=rw)
        Label(rot,text=(i),font="Helvetica 16 bold").grid(column=2,row=rw)
        Label(rot,text=(n_lis[o_lis.index(i)]*dict[i]),font="Helvetica 16 bold").grid(column=3,row=rw)
        rw=rw+2
        cnt=cnt+1
    bill=0
    for i in o_lis:
        bill=bill+n_lis[o_lis.index(i)]*dict[i]
    Label(rot,text=('Total Bill:'),font="Helvetica 16 bold").grid(column=2,row=rw+2)
    Label(rot,text=bill,font="Helvetica 16 bold").grid(column=3,row=rw+2)
    Label(rot,text='*********THANK YOU**********',font="Helvetica 16 bold").grid(column=2,row=rw+5)
    rot.mainloop()
