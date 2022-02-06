from tkinter import *
from tkinter.messagebox import *
aken=Tk()

aken.title("Tunniplaan")
aken.geometry("680x600")

t0=Label(aken,text="0", heigh=3, width=5,font="Arial 20", bg="white",relief="groove").grid(row=0,column=1,sticky=N+S+W+E)

l2=Label(aken,text=" ", heigh=3, width=5,font="Arial 20", bg="white",relief="groove").grid(row=3,column=1,rowspan=2,sticky=N+S+W+E)
l3=Label(aken,text=" ", heigh=3, width=5,font="Arial 20", bg="white",relief="groove").grid(row=5,column=1,rowspan=2,sticky=N+S+W+E)
l4=Label(aken,text=" ", heigh=3, width=5,font="Arial 20", bg="white",relief="groove").grid(row=7,column=1,rowspan=2,sticky=N+S+W+E)
l5=Label(aken,text=" ", heigh=3, width=5,font="Arial 20", bg="white",relief="groove").grid(row=9,column=1,rowspan=2,sticky=N+S+W+E)

#Date
t1=Label(aken,text="1", heigh=2, width=5,font="Arial 20", bg="white",relief="groove").grid(row=0,column=2,sticky=N+S+W+E)
t2=Label(aken,text="2", heigh=2, width=5,font="Arial 20", bg="white",relief="groove").grid(row=0,column=3,sticky=N+S+W+E)
t3=Label(aken,text="3", heigh=2, width=5,font="Arial 20", bg="white",relief="groove").grid(row=0,column=4,sticky=N+S+W+E)
t4=Label(aken,text="4", heigh=2, width=5,font="Arial 20", bg="white",relief="groove").grid(row=0,column=5,sticky=N+S+W+E)
t5=Label(aken,text="5", heigh=2, width=5,font="Arial 20", bg="white",relief="groove").grid(row=0,column=6,sticky=N+S+W+E)
t6=Label(aken,text="6", heigh=2, width=5,font="Arial 20", bg="white",relief="groove").grid(row=0,column=7,sticky=N+S+W+E)
t7=Label(aken,text="7", heigh=2, width=5,font="Arial 20", bg="white",relief="groove").grid(row=0,column=8,sticky=N+S+W+E)
t8=Label(aken,text="8", heigh=2, width=5,font="Arial 20", bg="white",relief="groove").grid(row=0,column=9,sticky=N+S+W+E)
t9=Label(aken,text="9", heigh=2, width=5,font="Arial 20", bg="white",relief="groove").grid(row=0,column=10,sticky=N+S+W+E)
t10=Label(aken,text="10", heigh=2, width=5,font="Arial 20", bg="white",relief="groove").grid(row=0,column=11,sticky=N+S+W+E)

#Esmaspsev
Ep=Label(aken,text="Esmaspaev",heigh=3, width=9,font="Arial 20", bg="white",relief="groove").grid(row=1,column=0,rowspan=2,sticky=N+S+W+E)
l1=Label(aken,text=" ", heigh=3, width=5,font="Arial 15", bg="white",relief="groove").grid(row=1,column=1,rowspan=2,sticky=N+S+W+E)
Button(text="Multimeedia", heigh=2, width=3,font="Arial 15", bg="#acc1ff",relief="groove",command=lambda:kirjeldus_aknasse("ps.png""Multimeedia")).grid(row=1,column=2,columnspan=2,sticky=N+S+W+E)
Button(text="Programmeerimine\nalused", heigh=2, width=6,font="Arial 15", bg="#ace1ff",relief="groove",command=lambda:kirjeldus_aknasse("pr.png""Programmerimise alused")).grid(row=2,column=2,columnspan=3,sticky=N+S+W+E)
Button(text=" ", heigh=2, width=6,font="Arial 15", bg="white",relief="groove").grid(row=1,column=4,sticky=N+S+W+E)
Button(text="Programmeerimine\nalused", heigh=2, width=6,font="Arial 15", bg="#ace1ff",relief="groove",command=lambda:kirjeldus_aknasse("pr.png""Programmerimise alused")).grid(row=1,column=5,columnspan=3,sticky=N+S+W+E)
Button(text="Multimeedia", heigh=2, width=3,font="Arial 15", bg="#acc1ff",relief="groove",command=lambda:kirjeldus_aknasse("ps.png""Multimeedia")).grid(row=2,column=5,columnspan=2,sticky=N+S+W+E)
Button(text=" ", heigh=2, width=6,font="Arial 15", bg="white",relief="groove").grid(row=2,column=7,sticky=N+S+W+E)
Button(text="Ruhmaju\nhataja\ntund", heigh=2, width=6,font="Arial 15", bg="#ace1ff",relief="groove",command=lambda:kirjeldus_aknasse("Ruhmajuhataja tund")).grid(row=1,column=8,rowspan=2,sticky=N+S+W+E)
#Teisipaev
Tp=Label(aken,text="Teisipaev",heigh=3, width=9,font="Arial 20", bg="white",relief="groove").grid(row=3,column=0,rowspan=2,sticky=N+S+W+E)
Button(text="Inglise keel", heigh=2, width=6,font="Arial 15", bg="#fffff0",relief="groove",command=lambda:kirjeldus_aknasse("Inglise keel1")).grid(row=3,column=2,columnspan=2,sticky=N+S+W+E)
Button(text="Inglise keel", heigh=2, width=6,font="Arial 15", bg="#e1acff",relief="groove",command=lambda:kirjeldus_aknasse("Inglise keel2")).grid(row=4,column=2,columnspan=2,sticky=N+S+W+E)
Button(text="Operatsioonisustee\nmide alused", heigh=2, width=6,font="Arial 15", bg="#e181ff",relief="groove",command=lambda:kirjeldus_aknasse("Operatsioonisusteemide alused")).grid(row=3,column=4,rowspan=2,columnspan=2,sticky=N+S+W+E)
Button(text=" ", heigh=2, width=6,font="Arial 15", bg="white",relief="groove").grid(row=3,column=6,rowspan=2,sticky=N+S+W+E)
Button(text="Kehaline\nkasvatus", heigh=2, width=6,font="Arial 15", bg="#e181c1",relief="groove",command=lambda:kirjeldus_aknasse("Kehaline kasvatus")).grid(row=3,column=7,rowspan=2,columnspan=2,sticky=N+S+W+E)
Button(text="Eesti\nkeel", heigh=2, width=6,font="Arial 15", bg="#cdb4ff",relief="groove",command=lambda:kirjeldus_aknasse("Eesti keel1")).grid(row=3,column=9,sticky=N+S+W+E)
Button(text="Eesti\nkeel", heigh=2, width=6,font="Arial 15", bg="#cbb5c8",relief="groove",command=lambda:kirjeldus_aknasse("Eesti keel2")).grid(row=4,column=9,sticky=N+S+W+E)
Button(text="Ajalugu", heigh=2, width=6,font="Arial 15", bg="#ffe7b4",relief="groove",command=lambda:kirjeldus_aknasse("Ajalugu")).grid(row=3,column=10,rowspan=2,sticky=N+S+W+E)
#Kolmapaev

Kp=Label(aken,text="Kolmapaev",heigh=3, width=9,font="Arial 20", bg="white",relief="groove").grid(row=5,column=0,rowspan=2,sticky=N+S+W+E)
Button(text="Programmeerimine\nalused", heigh=2, width=6,font="Arial 15", bg="#ace1ff",relief="groove",command=lambda:kirjeldus_aknasse("pr.png""Programmerimise alused")).grid(row=5,column=2,columnspan=3,sticky=N+S+W+E)
Button(text="Multimeedia", heigh=2, width=3,font="Arial 15", bg="#acc1ff",relief="groove",command=lambda:kirjeldus_aknasse("ps.png""Multimeedia")).grid(row=6,column=2,columnspan=3,sticky=N+S+W+E)
Button(text=" ", heigh=2, width=6,font="Arial 15", bg="white",relief="groove").grid(row=5,column=5,rowspan=2,sticky=N+S+W+E)
Button(text="Multimeedia", heigh=2, width=3,font="Arial 15", bg="#acc1ff",relief="groove",command=lambda:kirjeldus_aknasse("ps.png""Multimeedia")).grid(row=6,column=6,columnspan=3,sticky=N+S+W+E)
Button(text="Programmeerimine\nalused", heigh=2, width=6,font="Arial 15", bg="#ace1ff",relief="groove",command=lambda:kirjeldus_aknasse("pr.png""Programmerimise alused")).grid(row=5,column=6,columnspan=3,sticky=N+S+W+E)
Button(text="Kunstained", heigh=2, width=6,font="Arial 15", bg="#e181cf",relief="groove",command=lambda:kirjeldus_aknasse("Kunstained")).grid(row=5,column=9,rowspan=2,columnspan=2,sticky=N+S+W+E)

#Neljapaev
Np=Label(aken,text="Neljapaev",heigh=3, width=9,font="Arial 20", bg="white",relief="groove").grid(row=7,column=0,rowspan=2,sticky=N+S+W+E)
Button(text="Andmebaasisustee\nmide alused", heigh=2, width=6,font="Arial 15", bg="#ff81a2",relief="groove",command=lambda:kirjeldus_aknasse("Andmebaasisusteemide alused")).grid(row=7,column=2,rowspan=2,columnspan=2,sticky=N+S+W+E)
Button(text="Andmebaasisusteemide\nalused", heigh=2, width=6,font="Arial 15", bg="#ff81a2",relief="groove",command=lambda:kirjeldus_aknasse("Andmebaasisusteemide alused")).grid(row=7,column=4,rowspan=2,columnspan=3,sticky=N+S+W+E)
Button(text="Ajalugu", heigh=2, width=6,font="Arial 15", bg="#ffe7b4",relief="groove",command=lambda:kirjeldus_aknasse("Ajalugu")).grid(row=7,column=7,rowspan=2,sticky=N+S+W+E)
Button(text="Eesti\nkeel", heigh=2, width=6,font="Arial 15", bg="#cdb4ff",relief="groove",command=lambda:kirjeldus_aknasse("Eesti keel1")).grid(row=7,column=8,sticky=N+S+W+E)
Button(text="Eesti\nkeel", heigh=2, width=6,font="Arial 15", bg="#cbb5c8",relief="groove",command=lambda:kirjeldus_aknasse("Eesti keel2")).grid(row=8,column=8,sticky=N+S+W+E)

#Reede
Rp=Label(aken,text="Reede",heigh=3, width=9,font="Arial 20", bg="white",relief="groove").grid(row=9,column=0,rowspan=2,sticky=N+S+W+E)
Button(text=" ", heigh=3, width=5,font="Arial 15", bg="white",relief="groove").grid(row=9,column=2,rowspan=2,sticky=N+S+W+E)
Button(text="Keel ja kirjandus", heigh=2, width=6,font="Arial 15", bg="#e1ff81",relief="groove",command=lambda:kirjeldus_aknasse("Keel ja kirjandus")).grid(row=9,column=3,rowspan=2,columnspan=2,sticky=N+S+W+E)
Button(text=" ", heigh=3, width=5,font="Arial 15", bg="white",relief="groove").grid(row=9,column=5,rowspan=2,sticky=N+S+W+E)
Button(text="Matemaatika", heigh=2, width=3,font="Arial 15", bg="#fcbad2",relief="groove",command=lambda:kirjeldus_aknasse("Matemaatika")).grid(row=9,column=6,rowspan=2,columnspan=2,sticky=N+S+W+E)
Button(text="Suhtlemine ja\nklienditeenindus", heigh=2, width=3,font="Arial 15", bg="#c1acff",relief="groove",command=lambda:kirjeldus_aknasse("Suhtlemine ja klienditeenindus")).grid(row=9,column=8,rowspan=2,columnspan=2,sticky=N+S+W+E)
Button(text="Ajalugu", heigh=2, width=6,font="Arial 15", bg="#ffe7b4",relief="groove",command=lambda:kirjeldus_aknasse("Ajalugu")).grid(row=9,column=10,rowspan=2,sticky=N+S+W+E)

#p=["Esmaspaev","Teisipaev","Kolmapaev","Neljapaev","Reede"]
#j=0
#for i in range(1,10,2):
#    Ep=Label(aken,text=p[j],relief="solid".grid(row=i,column=0,rowspan=2,sticky=N+S+W+E))
#kell=["7:40-8:35","8:30-9:15","9:20-10:05","10:10-10:55","11:00-11:45","11:50-12:35","12:40-13:25","13:30-14:15","14:20-15:04","15:10-15:55","16:00-16:45"]
#for i in range(11):
#    tm=Label(aken,text=str(i)+"\n"+Kell[i],relief="solid").grid(row=0,column=i+1,sticky=N+S+W+E)
#tund1=Button(aken,text="Programmerimise alused",command=lambda:kirjeldus_aknasse("Programmerimise alused"))
#tund1.grid(row=1,column=2,columnspan=3)
def failist_sonastikule():
    tund_kirjeldus={}
    file=open(r"TextFile2.txt",'r')
    for line in file:
        tund,kirjeldus=line.strip().split(':')
        tund_kirjeldus[tund.strip()]=kirjeldus.strip()
    file.close()
    print(tund_kirjeldus)
    return tund_kirjeldus

def kirjeldus_aknasse(t:str):
    if (askyesno("kusimus","Kas tahad kirjeldust naha")):
        alam_aken=Toplevel()
        alam_aken.geometry("500x400")
        lbl_kirjeldus=Label(alam_aken, text=tund_kirjeldus[t], font=("Arial 35")).pack()
        c=Canvas(alam_aken,height=500,width=500)
        file=PhotoImage(file="pr.png")
        c.create_image(10,10,image=file,anchor=NW)
        c.pack()
        alam_aken.mainloop()
    else:
        showinfo("Vastus","kui ei taha, siis ei taha")


tund_kirjeldus=failist_sonastikule()

def kirjeldus_Aknasse(t):
    print(tund_kirjeldus[t])
    nfe



aken.mainloop()
