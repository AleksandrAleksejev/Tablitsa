from tkinter import *
aken=Tk()

aken.title("Tunniplaan")
aken.geometry("600x500")


t0=Label(aken,text="0", heigh=1, width=5,font="Arial 20", bg="white",relief="groove").grid(row=0,column=1,sticky=N+S+W+E)

l2=Label(aken,text=" ", heigh=1, width=5,font="Arial 20", bg="white",relief="groove").grid(row=3,column=1,rowspan=2,sticky=N+S+W+E)
l3=Label(aken,text=" ", heigh=1, width=5,font="Arial 20", bg="white",relief="groove").grid(row=5,column=1,rowspan=2,sticky=N+S+W+E)
l4=Label(aken,text=" ", heigh=1, width=5,font="Arial 20", bg="white",relief="groove").grid(row=7,column=1,rowspan=2,sticky=N+S+W+E)
l5=Label(aken,text=" ", heigh=1, width=5,font="Arial 20", bg="white",relief="groove").grid(row=9,column=1,rowspan=2,sticky=N+S+W+E)

#Date
t1=Label(aken,text="1", heigh=1, width=5,font="Arial 20", bg="white",relief="groove").grid(row=0,column=2,sticky=N+S+W+E)
t2=Label(aken,text="2", heigh=1, width=5,font="Arial 20", bg="white",relief="groove").grid(row=0,column=3,sticky=N+S+W+E)
t3=Label(aken,text="3", heigh=1, width=5,font="Arial 20", bg="white",relief="groove").grid(row=0,column=4,sticky=N+S+W+E)
t4=Label(aken,text="4", heigh=1, width=5,font="Arial 20", bg="white",relief="groove").grid(row=0,column=5,sticky=N+S+W+E)
t5=Label(aken,text="5", heigh=1, width=5,font="Arial 20", bg="white",relief="groove").grid(row=0,column=6,sticky=N+S+W+E)
t6=Label(aken,text="6", heigh=1, width=5,font="Arial 20", bg="white",relief="groove").grid(row=0,column=7,sticky=N+S+W+E)
t7=Label(aken,text="7", heigh=1, width=5,font="Arial 20", bg="white",relief="groove").grid(row=0,column=8,sticky=N+S+W+E)
t8=Label(aken,text="8", heigh=1, width=5,font="Arial 20", bg="white",relief="groove").grid(row=0,column=9,sticky=N+S+W+E)
t9=Label(aken,text="9", heigh=1, width=5,font="Arial 20", bg="white",relief="groove").grid(row=0,column=10,sticky=N+S+W+E)
t10=Label(aken,text="10", heigh=1, width=5,font="Arial 20", bg="white",relief="groove").grid(row=0,column=11,sticky=N+S+W+E)

#Esmaspsev
Ep=Label(aken,text="Esmaspaev",heigh=1, width=9,font="Arial 20", bg="white",relief="groove").grid(row=1,column=0,rowspan=2,sticky=N+S+W+E)
l1=Label(aken,text=" ", heigh=1, width=5,font="Arial 15", bg="white",relief="groove").grid(row=1,column=1,rowspan=2,sticky=N+S+W+E)
Button(text="Multimeedia", heigh=1, width=5,font="Arial 15", bg="#acc1ff",relief="groove").grid(row=1,column=2,columnspan=2,sticky=N+S+W+E)
Button(text="Programmeerimine\naklused", heigh=1, width=5,font="Arial 15", bg="#ace1ff",relief="groove").grid(row=2,column=2,columnspan=3,sticky=N+S+W+E)
Button(text=" ", heigh=1, width=5,font="Arial 15", bg="white",relief="groove").grid(row=1,column=4,sticky=N+S+W+E)
Button(text="Programmeerimine\nalused", heigh=1, width=5,font="Arial 15", bg="#ace1ff",relief="groove").grid(row=1,column=5,columnspan=3,sticky=N+S+W+E)
Button(text="Multimeedia", heigh=1, width=5,font="Arial 15", bg="#acc1ff",relief="groove").grid(row=2,column=5,columnspan=2,sticky=N+S+W+E)
Button(text=" ", heigh=1, width=5,font="Arial 15", bg="white",relief="groove").grid(row=2,column=7,sticky=N+S+W+E)
Button(text="Ruhmaju\nhataja\ntund", heigh=1, width=5,font="Arial 15", bg="#ace1ff",relief="groove").grid(row=1,column=8,rowspan=2,sticky=N+S+W+E)
#Teisipaev
Tp=Label(aken,text="Teisipaev",heigh=1, width=9,font="Arial 20", bg="white",relief="groove").grid(row=3,column=0,rowspan=2,sticky=N+S+W+E)
Button(text="Inglise keel", heigh=1, width=5,font="Arial 15", bg="#fffff0",relief="groove").grid(row=3,column=2,columnspan=2,sticky=N+S+W+E)
Button(text="Inglise keel", heigh=1, width=5,font="Arial 15", bg="#e1acff",relief="groove").grid(row=4,column=2,columnspan=2,sticky=N+S+W+E)
Button(text="Operatsioonisustee\nmide\nalused", heigh=1, width=10,font="Arial 15", bg="#e181ff",relief="groove").grid(row=3,column=4,rowspan=2,columnspan=2,sticky=N+S+W+E)
Button(text=" ", heigh=1, width=5,font="Arial 15", bg="white",relief="groove").grid(row=3,column=6,rowspan=2,sticky=N+S+W+E)
Button(text="Kehaline\nkasvatus", heigh=1, width=10,font="Arial 15", bg="#e181c1",relief="groove").grid(row=3,column=7,rowspan=2,columnspan=2,sticky=N+S+W+E)
Button(text="Eesti\nkeel", heigh=1, width=5,font="Arial 15", bg="#cdb4ff",relief="groove").grid(row=3,column=9,sticky=N+S+W+E)
Button(text="Eesti\nkeel", heigh=1, width=5,font="Arial 15", bg="#cbb5c8",relief="groove").grid(row=4,column=9,sticky=N+S+W+E)
Button(text="Ajalugu", heigh=1, width=5,font="Arial 15", bg="#ffe7b4",relief="groove").grid(row=3,column=10,rowspan=2,sticky=N+S+W+E)
#Kolmapaec

Kp=Label(aken,text="Kolmapaev",heigh=1, width=9,font="Arial 20", bg="white",relief="groove").grid(row=5,column=0,rowspan=2,sticky=N+S+W+E)
Button(text="Programmeerimine\nalused", heigh=1, width=5,font="Arial 15", bg="#ace1ff",relief="groove").grid(row=5,column=2,columnspan=3,sticky=N+S+W+E)
Button(text="Multimeedia", heigh=1, width=5,font="Arial 15", bg="#acc1ff",relief="groove").grid(row=6,column=2,columnspan=3,sticky=N+S+W+E)
Button(text=" ", heigh=1, width=5,font="Arial 15", bg="white",relief="groove").grid(row=5,column=5,rowspan=2,sticky=N+S+W+E)
Button(text="Multimeedia", heigh=1, width=5,font="Arial 15", bg="#acc1ff",relief="groove").grid(row=6,column=6,columnspan=3,sticky=N+S+W+E)
Button(text="Programmeerimine\nalused", heigh=1, width=5,font="Arial 15", bg="#ace1ff",relief="groove").grid(row=5,column=6,columnspan=3,sticky=N+S+W+E)
Button(text="Kunstained", heigh=1, width=5,font="Arial 15", bg="#e181cf",relief="groove").grid(row=5,column=9,rowspan=2,columnspan=2,sticky=N+S+W+E)

#Neljapaev
Np=Label(aken,text="Neljapaev",heigh=1, width=9,font="Arial 20", bg="white",relief="groove").grid(row=7,column=0,rowspan=2,sticky=N+S+W+E)
Button(text="Andmebaasisustee\nmide alused", heigh=1, width=10,font="Arial 15", bg="#ff81a2",relief="groove").grid(row=7,column=2,rowspan=2,columnspan=2,sticky=N+S+W+E)
Button(text="Andmebaasisusteemide\nalused", heigh=1, width=10,font="Arial 15", bg="#ff81a2",relief="groove").grid(row=7,column=4,rowspan=2,columnspan=3,sticky=N+S+W+E)
Button(text="Ajalugu", heigh=1, width=5,font="Arial 15", bg="#ffe7b4",relief="groove").grid(row=7,column=7,rowspan=2,sticky=N+S+W+E)
Button(text="Eesti\nkeel", heigh=1, width=5,font="Arial 15", bg="#cdb4ff",relief="groove").grid(row=7,column=8,sticky=N+S+W+E)
Button(text="Eesti\nkeel", heigh=1, width=5,font="Arial 15", bg="#cbb5c8",relief="groove").grid(row=8,column=8,sticky=N+S+W+E)

#Reede
Rp=Label(aken,text="Reede",heigh=1, width=9,font="Arial 20", bg="white",relief="groove").grid(row=9,column=0,rowspan=2,sticky=N+S+W+E)
Button(text=" ", heigh=1, width=5,font="Arial 15", bg="white",relief="groove").grid(row=9,column=2,rowspan=2,sticky=N+S+W+E)
Button(text="Keel ja kirjandus", heigh=1, width=5,font="Arial 15", bg="#e1ff81",relief="groove").grid(row=9,column=3,rowspan=2,columnspan=2,sticky=N+S+W+E)
Button(text=" ", heigh=1, width=5,font="Arial 15", bg="white",relief="groove").grid(row=9,column=5,rowspan=2,sticky=N+S+W+E)
Button(text="Matemaatika", heigh=1, width=5,font="Arial 15", bg="#fcbad2",relief="groove").grid(row=9,column=6,rowspan=2,columnspan=2,sticky=N+S+W+E)
Button(text="Suhtlemine ja\nklienditeenindus", heigh=1, width=10,font="Arial 15", bg="#c1acff",relief="groove").grid(row=9,column=8,rowspan=2,columnspan=2,sticky=N+S+W+E)
Button(text="Ajalugu", heigh=1, width=5,font="Arial 15", bg="#ffe7b4",relief="groove").grid(row=9,column=10,rowspan=2,sticky=N+S+W+E)


aken.mainloop()