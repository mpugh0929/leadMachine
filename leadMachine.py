from tkinter import *
import tkinter.messagebox
from tkinter.font import Font
from tkinter import ttk
def sendText():
    try:
        from twilio.rest import Client
        account_sid = 'AC7b66cb11605b92ce428bc790874f01da'
        auth_token = '09c7b1b91613c41b2154389dce03658b'
        client = Client(account_sid, auth_token)
        global e
        number = e.get()
        message = client.messages \
        .create(
        body="Hi I am Matt's robot!",
        from_='+13215783097',
        to=number)
        tkinter.messagebox.showinfo(title="Success", message="Text Sent!")
    except:
        tkinter.messagebox.showinfo(title="Error!", message="Something went wrong.")

root = Tk()
C = Canvas(root, bg="blue", height=250, width=300)
filename = PhotoImage(file = 'giphy2.gif')
background_label = Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
root.title('Lead Machine')
root.iconbitmap(r'roboticon.ico')
root.geometry("300x300")
myFont = Font(family="Times New Roman", size=12)
w = Message(root, text="ENTER A PHONE NUMBER", font=myFont, width=300)
w.pack()
e = Entry(root)
e.pack()
e.focus_set()
b = Button(root,text='Send',command=sendText)
b.pack(side='bottom')
root.mainloop()
