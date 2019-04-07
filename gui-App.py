from tkinter import *

def saveInfo():
    #-----RETRIEVING INFO FROM REG-FORM -----#
    firstNameInfo = firstName.get()
    emailInfo = Email.get()
    if var.get() :
        radioInfo = 'Male'
    else:
        radioInfo = 'Female'
    dropListInfo = c.get()
    langList = []
    if var3.get() :
        langList.append('Java')
    if var4.get():
        langList.append('Python')
    myDetailsFile = open('myRegFile.txt', 'w')
    myDetailsFile.write(' Name = {} \n Email = {} \n Gender = {} \n Country = {}  \nLanguage = {}'.format(firstNameInfo, emailInfo, radioInfo, dropListInfo, langList))
    myDetailsFile.close()

    #--------NOW ADDING TO FILE-----------#

    myNewWindow = Tk()


    myNewWindow.geometry('500x500')
    myNewWindow.title("ENTERED DETAILS")
    myDetailsFile = open('myRegFile.txt','r')

    label_1 = Label(myNewWindow, text=myDetailsFile.read(),justify=LEFT,bg='cyan', width=50,height=20, font=("bold", 10))
    label_1.place(x=60, y=60)
    myDetailsFile.close()

    myNewWindow.mainloop()
    root.quit()

root = Tk()
root.geometry('500x500')
root.title("Registration Form")
firstName = StringVar()
Email = StringVar()



label_0 = Label(root, text="Registration form",width=20,font=("bold", 20))
label_0.place(x=90,y=53)


label_1 = Label(root, text="FullName",width=20,font=("bold", 10))
label_1.place(x=80,y=130)

entry_1 = Entry(root,textvariable=firstName)
entry_1.place(x=240,y=130)

label_2 = Label(root, text="Email",width=20,font=("bold", 10))
label_2.place(x=68,y=180)

entry_2 = Entry(root,textvariable=Email)
entry_2.place(x=240,y=180)

label_3 = Label(root, text="Gender",width=20,font=("bold", 10))
label_3.place(x=70,y=230)
var = IntVar()
radio1 = Radiobutton(root, text="M",padx = 5, variable=var, value=1)
radio1.place(x=235,y=230)
radio2 = Radiobutton(root, text="F",padx = 20, variable=var, value=2)
radio2.place(x=290,y=230)
label_4 = Label(root, text="country",width=20,font=("bold", 10))
label_4.place(x=70,y=280)

list1 = ['Canada','India','UK','Nepal','Iceland','South Africa'];
c=StringVar()
newtext = StringVar()
droplist=OptionMenu(root,c, *list1)
droplist.config(width=15)
droplist.place(x=240,y=280)

label_4 = Label(root, text="Programming",width=20,font=("bold", 10))
label_4.place(x=85,y=330)
var3 = IntVar()
check1 = Checkbutton(root,onvalue=1,offvalue=0, text="java", variable=var3)
check1.place(x=235,y=330)
var4 = IntVar()
check2 = Checkbutton(root,onvalue=1,offvalue=0, text="python", variable=var4)
check2.place(x=290,y=330)
submitButton = Button(root, text='Submit',width=20,bg='brown',fg='white',command=saveInfo)
submitButton.place(x=180,y=380)

root.mainloop()




