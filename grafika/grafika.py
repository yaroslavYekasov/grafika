from time import *
from tkinter import *
k=0

def klikker(event):
    global k 
    k+=1
    b="youre good"
    btn.configure(text=k)
    if k%10==0:
        lbl.configure(text=b)

def klikkermaha(event):
    global k 
    k-=1
    btn.configure(text=k)

def tekst_to_lbl(event):
    t=ent.get()
    lbl.configure(text=t)
    ent.delete(0,END)

aken=Tk() 
aken.geometry("400x500")
aken.title("Minu esimene aken")

lbl=Label(aken,text="Elemendid", bg="black",fg="#880808", font="Arial 20", heigh=5, width=15)
btn=Button(aken,text="Vajuta siia", font="Arial 24", relief=GROOVE, width=15)

ent=Entry(aken,fg="blue",bg="lightblue",width=15,font="Arial 20", justify=CENTER)

btn.bind("<Button-1>", klikker)
btn.bind("<Button-3>", klikkermaha)
ent.bind("<Return>", tekst_to_lbl)

lbl.pack()
btn.pack()
ent.pack()

aken.mainloop()




