from tkinter import *
from tkinter import messagebox
import time
pname=oname=""
def thankNote():
    tk.destroy()
    msg="Hope you liked the project..."
    time.sleep(1)
    for i in range(0,len(msg)):
        print(msg[i],end='')
        time.sleep(0.05)
    time.sleep(.4)
    print("THANK YOU",end='')
    time.sleep(0.5)
    print(" !")
def clearScreen(window):
    global c
    for widget in window.winfo_children():
        widget.destroy()
    c=Canvas(tk,height=conv(650),width=conv(1200),border=conv(10),relief='raised',bg='pink')
    c.place(x=conv(75),y=conv(50))
def conv(a):
    return a*1.14
def dimension():
    global tk,screen_width,screen_height
    tk=Tk()
    screen_width = tk.winfo_screenwidth()
    screen_height = tk.winfo_screenheight()
def displayMarksheet():
    tk.configure(bg='orange')
    makeButton(tk,'Back to Home','times',0,'purple',3,0,0,'white',homeScreen).place(x=conv(1110),y=conv(700))
    w1=Canvas(tk,height=conv(225),width=conv(1200),bg='pink').place(x=conv(75),y=conv(50))
    w2=Canvas(tk,height=conv(100),width=conv(100),bg='pink').place(x=conv(75),y=conv(275))
    w3=Canvas(tk,height=conv(100),width=conv(450),bg='pink').place(x=conv(175),y=conv(275))
    w4=Canvas(tk,height=conv(50),width=conv(550),bg='pink').place(x=conv(625),y=conv(275))
    w5=Canvas(tk,height=conv(100),width=conv(100),bg='pink').place(x=conv(1175),y=conv(275))
    w6=Canvas(tk,height=conv(50),width=conv(100),bg='pink').place(x=conv(625),y=conv(325))
    w7=Canvas(tk,height=conv(50),width=conv(100),bg='pink').place(x=conv(725),y=conv(325))
    w8=Canvas(tk,height=conv(50),width=conv(100),bg='pink').place(x=conv(825),y=conv(325))
    w9=Canvas(tk,height=conv(50),width=conv(250),bg='pink').place(x=conv(925),y=conv(325))
    w10=Canvas(tk,height=conv(180),width=conv(100),bg='pink').place(x=conv(75),y=conv(375))
    w11=Canvas(tk,height=conv(180),width=conv(450),bg='pink').place(x=conv(175),y=conv(375))
    w12=Canvas(tk,height=conv(180),width=conv(100),bg='pink').place(x=conv(625),y=conv(375))
    w13=Canvas(tk,height=conv(180),width=conv(100),bg='pink').place(x=conv(725),y=conv(375))
    w14=Canvas(tk,height=conv(180),width=conv(100),bg='pink').place(x=conv(825),y=conv(375))
    w15=Canvas(tk,height=conv(180),width=conv(250),bg='pink').place(x=conv(925),y=conv(375))
    w16=Canvas(tk,height=conv(180),width=conv(100),bg='pink').place(x=conv(1175),y=conv(375))
    w17=Canvas(tk,height=conv(100),width=conv(1200),bg='pink').place(x=conv(75),y=conv(555))
    Label(tk,text="CENTRAL BOARD OF SECONDARY EDUCATION",fg='red',bg='pink',font=('arial’,conv(19),’bold')).place(x=conv(330),y=conv(53))
    Label(tk,text="MARKS STATEMENT",bg='pink',fg='red',font=('arial’,conv(16),’bold')).place(x=conv(475),y=conv(85))
    Label(tk,text="Name of Student",fg='red',bg='pink',font=('arial’,conv(12),’bold')).place(x=conv(100),y=conv(120))
    Label(tk,text="Roll No.",bg='pink',fg='red',font=('arial’,conv(12),’bold')).place(x=conv(100),y=conv(140))
    Label(tk,text="Mother's Name ",fg='red',bg='pink',font=('arial’,conv(12),’bold')).place(x=conv(100),y=conv(160))
    Label(tk,text="Father's Name",bg='pink',fg='red',font=('arial’,conv(12),’bold')).place(x=conv(100),y=conv(180))
    Label(tk,text="Date of Birth ",fg='red',bg='pink',font=('arial’,conv(12),’bold')).place(x=conv(100),y=conv(200))
    Label(tk,text="School",bg='pink',fg='red',font=('arial’,conv(12),’bold')).place(x=conv(100),y=conv(220))
    Label(tk,text=e11,fg='black',bg='pink',font=('arial’,conv(12),’bold')).place(x=conv(275),y=conv(120))
    Label(tk,text=e14,bg='pink',fg='black',font=('arial’,conv(12),’bold')).place(x=conv(195),y=conv(140))
    Label(tk,text=e13,fg='black',bg='pink',font=('arial’,conv(12),’bold')).place(x=conv(265),y=conv(160))
    Label(tk,text=e12,bg='pink',fg='black',font=('arial’,conv(12),’bold')).place(x=conv(265),y=conv(180))
    Label(tk,text=e15,fg='black',bg='pink',font=('arial’,conv(12),’bold')).place(x=conv(240),y=conv(200))
    Label(tk,text=e16,bg='pink',fg='black',font=('arial’,conv(12),’bold')).place(x=conv(185),y=conv(220))
    Label(tk,text="Scholastic Achievements",bg='pink',fg='red',font=('arial’,conv(12),’bold')).place(x=conv(100),y=conv(240))
    Label(tk,text="CODE",bg='pink',fg='black',font=('arial’,conv(14),’bold')).place(x=conv(105),y=conv(335))
    Label(tk,text="SUBJECT",bg='pink',fg='black',font=('arial’,conv(14),’bold')).place(x=conv(375),y=conv(335))
    Label(tk,text="MARKS OBTAINED",bg='pink',fg='black',font=('arial’,conv(14),’bold')).place(x=conv(850),y=conv(295))
    Label(tk,text="GRADE",bg='pink',fg='black',font=('arial’,conv(14),’bold')).place(x=conv(1185),y=conv(345))
    Label(tk,text="THEORY",bg='pink',fg='black',font=('arial’,conv(14),’bold')).place(x=conv(635),y=conv(345))
    Label(tk,text="PR.",bg='pink',fg='black',font=('arial’,conv(14),’bold')).place(x=conv(775),y=conv(345))
    Label(tk,text="TOTAL",bg='pink',fg='black',font=('arial’,conv(14),’bold')).place(x=conv(850),y=conv(345))
    Label(tk,text="TOTAL(IN WORDS)",bg='pink',fg='black',font=('arial’,conv(14),’bold')).place(x=conv(950),y=conv(345))
    Label(tk,text="301",bg='pink',fg='black',font=('arial’,conv(14),’bold')).place(x=conv(125),y=conv(385))
    Label(tk,text="305",bg='pink',fg='black',font=('arial’,conv(14),’bold')).place(x=conv(125),y=conv(410))
    Label(tk,text="343",bg='pink',fg='black',font=('arial’,conv(14),’bold')).place(x=conv(125),y=conv(435))
    Label(tk,text="044",bg='pink',fg='black',font=('arial’,conv(14),’bold')).place(x=conv(125),y=conv(460))
    Label(tk,text="051",bg='pink',fg='black',font=('arial’,conv(14),’bold')).place(x=conv(125),y=conv(485))
    Label(tk,text=aname,bg='pink',fg='black',font=('arial’,conv(14),’bold')).place(x=conv(200),y=conv(385))
    Label(tk,text=bname,bg='pink',fg='black',font=('arial’,conv(14),’bold')).place(x=conv(200),y=conv(410))
    Label(tk,text=cname,bg='pink',fg='black',font=('arial’,conv(14),’bold')).place(x=conv(200),y=conv(435))
    Label(tk,text=pname,bg='pink',fg='black',font=('arial’,conv(14),’bold')).place(x=conv(200),y=conv(460))
    Label(tk,text=oname,bg='pink',fg='black',font=('arial’,conv(14),’bold')).place(x=conv(200),y=conv(485))
    Label(tk,text=markToWords(int(xa)),bg='pink',fg='black',font=('arial’,conv(14),’bold')).place(x=conv(985),y=conv(385))
    Label(tk,text=markToWords(int(xb)),bg='pink',fg='black',font=('arial’,conv(14),’bold')).place(x=conv(985),y=conv(410))
    Label(tk,text=markToWords(int(xc)),bg='pink',fg='black',font=('arial’,conv(14),’bold')).place(x=conv(985),y=conv(435))
    Label(tk,text=markToWords(int(xp)),bg='pink',fg='black',font=('arial’,conv(14),’bold')).place(x=conv(985),y=conv(460))
    Label(tk,text=markToWords(int(xo)),bg='pink',fg='black',font=('arial’,conv(14),’bold')).place(x=conv(985),y=conv(485))
    Label(tk,text=ta,bg='pink',fg='black',font=('arial’,conv(14),’bold')).place(x=conv(675),y=conv(385))
    Label(tk,text=tb,bg='pink',fg='black',font=('arial’,conv(14),’bold')).place(x=conv(675),y=conv(410))
    Label(tk,text=tc,bg='pink',fg='black',font=('arial’,conv(14),’bold')).place(x=conv(675),y=conv(435))
    Label(tk,text=tp,bg='pink',fg='black',font=('arial’,conv(14),’bold')).place(x=conv(675),y=conv(460))
    Label(tk,text=to,bg='pink',fg='black',font=('arial’,conv(14),’bold')).place(x=conv(675),y=conv(485))
    Label(tk,text=xa,bg='pink',fg='black',font=('arial’,conv(14),’bold')).place(x=conv(875),y=conv(385))
    Label(tk,text=xb,bg='pink',fg='black',font=('arial’,conv(14),’bold')).place(x=conv(875),y=conv(410))
    Label(tk,text=xc,bg='pink',fg='black',font=('arial’,conv(14),’bold')).place(x=conv(875),y=conv(435))
    Label(tk,text=xp,bg='pink',fg='black',font=('arial’,conv(14),’bold')).place(x=conv(875),y=conv(460))
    Label(tk,text=xo,bg='pink',fg='black',font=('arial’,conv(14),’bold')).place(x=conv(875),y=conv(485))
    Label(tk,text=pa,bg='pink',fg='black',font=('arial’,conv(14),’bold')).place(x=conv(775),y=conv(385))
    Label(tk,text=pb,bg='pink',fg='black',font=('arial’,conv(14),’bold')).place(x=conv(775),y=conv(410))
    Label(tk,text=pc,bg='pink',fg='black',font=('arial’,conv(14),’bold')).place(x=conv(775),y=conv(435))
    Label(tk,text=pp,bg='pink',fg='black',font=('arial’,conv(14),’bold')).place(x=conv(775),y=conv(460))
    Label(tk,text=po,bg='pink',fg='black',font=('arial’,conv(14),’bold')).place(x=conv(775),y=conv(485))
    Label(tk,text=grade(xa),bg='pink',fg='black',font=('arial’,conv(14),’bold')).place(x=conv(1225),y=conv(385))
    Label(tk,text=grade(xb),bg='pink',fg='black',font=('arial’,conv(14),’bold')).place(x=conv(1225),y=conv(410))
    Label(tk,text=grade(xc),bg='pink',fg='black',font=('arial’,conv(14),’bold')).place(x=conv(1225),y=conv(435))
    Label(tk,text=grade(xp),bg='pink',fg='black',font=('arial’,conv(14),’bold')).place(x=conv(1225),y=conv(460))
    Label(tk,text=grade(xo),bg='pink',fg='black',font=('arial’,conv(14),’bold')).place(x=conv(1225),y=conv(485))
    Label(tk,text="Abbreviations",bg='pink',fg='red',font=('arial’,conv(12),’bold')).place(x=conv(100),y=conv(560))
    Label(tk,text="AB: Absent",bg='pink',fg='red',font=('arial’,conv(12),’bold')).place(x=conv(100),y=conv(580))
    Label(tk,text="PR: Practical",bg='pink',fg='red',font=('arial’,conv(12),’bold')).place(x=conv(100),y=conv(600))
    Label(tk,text="DELHI : ",bg='pink',fg='red',font=('arial’,conv(12),’bold')).place(x=conv(100),y=conv(625))
    Label(tk,text="18/01/2024",bg='pink',fg='black',font=('arial’,conv(12),’bold')).place(x=conv(185),y=conv(625))
    Label(tk,text="Result:",bg='pink',fg='red',font=('arial’,conv(12),’bold')).place(x=conv(750),y=conv(570))
    Label(tk,text=result(grade(xa),grade(xb),grade(xc),grade(xp),grade(xo)),bg='pink',fg='black',font=('arial’,conv(12),’bold')).place(x=conv(830),y=conv(570))
def markToWords(x):
    arr= ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
        "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen",
        "twenty", "twenty-one", "twenty-two", "twenty-three", "twenty-four", "twenty-five", "twenty-six", "twenty-seven", "twenty-eight", "twenty-nine",
        "thirty", "thirty-one", "thirty-two", "thirty-three", "thirty-four", "thirty-five", "thirty-six", "thirty-seven", "thirty-eight", "thirty-nine",
        "forty", "forty-one", "forty-two", "forty-three", "forty-four", "forty-five", "forty-six", "forty-seven", "forty-eight", "forty-nine",
        "fifty", "fifty-one", "fifty-two", "fifty-three", "fifty-four", "fifty-five", "fifty-six", "fifty-seven", "fifty-eight", "fifty-nine",
        "sixty", "sixty-one", "sixty-two", "sixty-three", "sixty-four", "sixty-five", "sixty-six", "sixty-seven", "sixty-eight", "sixty-nine",
        "seventy", "seventy-one", "seventy-two", "seventy-three", "seventy-four", "seventy-five", "seventy-six", "seventy-seven", "seventy-eight", "seventy-nine",
        "eighty", "eighty-one", "eighty-two", "eighty-three", "eighty-four", "eighty-five", "eighty-six", "eighty-seven", "eighty-eight", "eighty-nine",
        "ninety", "ninety-one", "ninety-two", "ninety-three", "ninety-four", "ninety-five", "ninety-six", "ninety-seven", "ninety-eight", "ninety-nine", "one-hundred"]
    return arr[x]
def result(ga,gb,gc,gp,go):
    if ga=="F" or gb=="F" or gc=="F" or gp=="F" or go=="F": return "FAIL"
    else: return "PASS"
def grade(strX):
    x=int(strX)
    if x>90 and x<101: g="A1"
    elif x>80 and x<91: g="A2"
    elif x>70 and x<81: g="B1"
    elif x>60 and x<71: g="B2"
    elif x>50 and x<61: g="C1"
    elif x>40 and x<51: g="C2"
    elif x>32 and x<41: g="D"
    else: g="F"
    return g
def fetchingMarks():
    global ta,tb,tc,tp,to,pa,pb,pc,pp,po,xa,xb,xc,xp,xo,pname,oname
    ta=amarks.get()
    tb=bmarks.get()
    tc=cmarks.get()
    tp=pmarks.get()
    to=omarks.get()
    pa=amarkss.get()
    pb=bmarkss.get()
    pc=cmarkss.get()
    pp=pmarkss.get()
    po=omarkss.get()
    if(pname=="" or oname==""):
        l1=makeLabel(tk,"Choose opt subject",'arial',10,'red',25,0,0,'pink')
        c2.create_window(conv(150),conv(560),window=l1)
    elif len(ta)==0 or len(tb)==0 or len(tc)==0 or len(tp)==0 or len(to)==0 or len(pa)==0 or len(pb)==0 or len(pc)==0 or len(pp)==0 or len(po)==0:
        l1=makeLabel(tk,"Fill all enteries",'arial',10,'red',25,0,0,'pink')
        c2.create_window(conv(150),conv(560),window=l1)
    elif(ta.isnumeric()==False or tb.isnumeric()==False or tc.isnumeric()==False or tp.isnumeric()==False or to.isnumeric()==False or pa.isnumeric()==False or pb.isnumeric()==False or pc.isnumeric()==False or pp.isnumeric()==False or po.isnumeric()==False):
        l1=makeLabel(tk,"Invalid Input",'arial',10,'red',25,0,0,'pink')
        c2.create_window(conv(150),conv(560),window=l1)
    elif int(ta)>80 or int(tb)>80 or int(tc)>80 or int(tp)>80 or int(to)>80 or int(ta)<0 or int(tb)<0 or int(tc)<0 or int(tp)<0 or int(to)<0 or int(pa)>20 or int(pb)>20 or int(pc)>20 or int(pp)>20 or int(po)>20 or int(pa)<0 or int(pb)<0 or int(pc)<0 or int(pp)<0 or int(po)<0:
        l1=makeLabel(tk,"Invalid Input",'arial',10,'red',25,0,0,'pink')
        c2.create_window(conv(150),conv(560),window=l1)
    else:
        xa=int(ta)+int(pa)
        xb=int(tb)+int(pb)
        xc=int(tc)+int(pc)
        xp=int(tp)+int(pp)
        xo=int(to)+int(po)
        displayMarksheet()
def hindi():
    global oname
    oname="Hindi"
    label=makeLabel(tk,"  Hindi  ",'arial',24,'black',0,0,0,'orange')
    c1.create_window(conv(200),conv(500),window=label)
def music():
    global oname
    oname="Music"
    label=makeLabel(tk,"  Music  ",'arial',24,'black',0,0,0,'orange')
    c1.create_window(conv(200),conv(500),window=label)
def phe():
    global oname
    oname="Physical Edu."
    label=makeLabel(tk,"   P.Ed    ",'arial',24,'black',0,0,0,'orange')
    c1.create_window(conv(200),conv(500),window=label)
def maths2():
    global oname
    oname="Maths"
    label=makeLabel(tk,"  Maths   ",'arial',24,'black',0,0,0,'orange')
    c1.create_window(conv(200),conv(500),window=label)
def cs():
    global oname
    oname="C.S."
    label=makeLabel(tk,"   C.S.    ",'arial',24,'black',0,0,0,'orange')
    c1.create_window(conv(200),conv(500),window=label)
def phycho():
    global oname
    oname="Psychology"
    label=makeLabel(tk,"  Phycho   ",'arial',24,'black',0,0,0,'orange')
    c1.create_window(conv(200),conv(500),window=label)
def socialogy():
    global pname
    pname="Socialogy"
    l4=makeLabel(tk," Socialogy ",'arial',24,'black',0,0,0,'orange')
    c1.create_window(conv(200),conv(350),window=l4)
def economics():
    global pname
    pname="Economics"
    l4=makeLabel(tk," Economics ",'arial',24,'black',0,0,0,'orange')
    c1.create_window(conv(200),conv(350),window=l4)
def maths():
    global pname
    pname="Mathematics"
    l4=makeLabel(tk,"Mathematics",'arial',24,'black',0,0,0,'orange')
    c1.create_window(conv(200),conv(350),window=l4)
def bio():
    global pname
    pname="Biology"
    l4=makeLabel(tk,"     Biology      ",'arial',24,'black',0,0,0,'orange')
    c1.create_window(conv(200),conv(350),window=l4)
def science():
    enterMarks("English","Physics","Chemistry","Maths","Biology","Hindi","Music","P.Ed","C.S.")
def commerce():
    enterMarks("English","Economics","Accounts"," "," ","Hindi","Music","P.Ed","Maths")
def arts():
    enterMarks("English","History","Political Sci.","Socialogy","Economics","Music","Hindi","P.Ed","Physco")
def enterMarks(i1,i2,i3,i4,i5,i6,i7,i8,i9):
    global c1,c2,c3,aname,bname,cname,pname,oname,amarks,bmarks,cmarks,pmarks,omarks,amarkss,bmarkss,cmarkss,pmarkss,omarkss
    aname=i1
    bname=i2
    cname=i3
    for widget in tk.winfo_children():
        widget.destroy()
    c1=Canvas(tk,height=conv(600),width=conv(400),border=conv(4),relief='raised',bg='orange')
    c1.place(x=conv(75),y=conv(50))
    c2=Canvas(tk,height=conv(600),width=conv(400),border=conv(4),relief='raised',bg='pink')
    c2.place(x=conv(475),y=conv(50))
    c3=Canvas(tk,height=conv(600),width=conv(400),border=conv(4),relief='raised',bg='cyan')
    c3.place(x=conv(875),y=conv(50))
    lsub=makeLabel(tk,"Subjects",'arial',24,'black',0,0,0,'orange')
    lth=makeLabel(tk,"Theory",'arial',24,'black',0,0,0,'pink')
    lprac=makeLabel(tk,"Practical",'arial',24,'black',0,0,0,'cyan')
    l1=makeLabel(tk,aname,'arial',24,'black',0,0,0,'orange')
    l2=makeLabel(tk,bname,'arial',24,'black',0,0,0,'orange')
    l3=makeLabel(tk,cname,'arial',24,'black',0,0,0,'orange')
    l4=makeLabel(tk,"           ",'arial',24,'black',0,0,0,'orange')
    amarks=makeEntry(tk,'arial',20,'black',2,8)
    bmarks=makeEntry(tk,'arial',20,'black',2,8)
    cmarks=makeEntry(tk,'arial',20,'black',2,8)
    pmarks=makeEntry(tk,'arial',20,'black',2,8)
    omarks=makeEntry(tk,'arial',20,'black',2,8)
    amarkss=makeEntry(tk,'arial',20,'black',2,8)
    bmarkss=makeEntry(tk,'arial',20,'black',2,8)
    cmarkss=makeEntry(tk,'arial',20,'black',2,8)
    pmarkss=makeEntry(tk,'arial',20,'black',2,8)
    omarkss=makeEntry(tk,'arial',20,'black',2,8)
    l11=makeLabel(tk,'/80','arial',20,'black',0,0,0,'orange')
    l12=makeLabel(tk,'/80','arial',20,'black',0,0,0,'orange')
    l13=makeLabel(tk,'/80','arial',20,'black',0,0,0,'orange')
    l14=makeLabel(tk,'/80','arial',20,'black',0,0,0,'orange')
    l15=makeLabel(tk,'/80','arial',20,'black',0,0,0,'orange')
    l21=makeLabel(tk,'/20','arial',20,'black',0,0,0,'orange')
    l22=makeLabel(tk,'/20','arial',20,'black',0,0,0,'orange')
    l23=makeLabel(tk,'/20','arial',20,'black',0,0,0,'orange')
    l24=makeLabel(tk,'/20','arial',20,'black',0,0,0,'orange')
    l25=makeLabel(tk,'/20','arial',20,'black',0,0,0,'orange')
    opt1=makeButton(tk,i6,'arial',12,'black',4,1,10,'cyan',hindi)
    opt2=makeButton(tk,i7,'arial',12,'black',4,1,10,'cyan',music)
    opt3=makeButton(tk,i8,'arial',12,'black',4,1,10,'cyan',phe)
    c1.create_window(conv(200),conv(50),window=lsub)
    c2.create_window(conv(200),conv(50),window=lth)
    c3.create_window(conv(200),conv(50),window=lprac)
    c1.create_window(conv(200),conv(150),window=l1)
    c1.create_window(conv(200),conv(200),window=l2)
    c1.create_window(conv(200),conv(250),window=l3)
    c1.create_window(conv(200),conv(350),window=l4)
    c2.create_window(conv(200),conv(150),window=amarks)
    c3.create_window(conv(200),conv(150),window=amarkss)
    c2.create_window(conv(200),conv(200),window=bmarks)
    c3.create_window(conv(200),conv(200),window=bmarkss)
    c2.create_window(conv(200),conv(250),window=cmarks)
    c3.create_window(conv(200),conv(250),window=cmarkss)
    c2.create_window(conv(200),conv(350),window=pmarks)
    c3.create_window(conv(200),conv(350),window=pmarkss)
    c2.create_window(conv(200),conv(500),window=omarks)
    c3.create_window(conv(200),conv(500),window=omarkss)
    c2.create_window(conv(285),conv(150),window=l11)
    c2.create_window(conv(285),conv(200),window=l12)
    c2.create_window(conv(285),conv(250),window=l13)
    c2.create_window(conv(285),conv(350),window=l14)
    c2.create_window(conv(285),conv(500),window=l15)
    c3.create_window(conv(285),conv(150),window=l21)
    c3.create_window(conv(285),conv(200),window=l22)
    c3.create_window(conv(285),conv(250),window=l23)
    c3.create_window(conv(285),conv(350),window=l24)
    c3.create_window(conv(285),conv(500),window=l25)
    c1.create_window(conv(150),conv(400),window=opt1)
    c1.create_window(conv(280),conv(400),window=opt2)
    c1.create_window(conv(150),conv(450),window=opt3)
    if(i4==" "):
        pname="Business Studies"
        l4=makeLabel(tk,pname,'arial',24,'black',0,0,0,'orange')
        opt4=makeButton(tk,i9,'arial',12,'black',4,1,10,'cyan',phe)
        c1.create_window(conv(200),conv(300),window=l4)
        c1.create_window(conv(280),conv(450),window=opt4)
    elif(i4=="Maths"):
        b1=makeButton(tk,i4,'arial',12,'black',4,1,10,'cyan',maths)
        b2=makeButton(tk,i5,'arial',12,'black',4,1,10,'cyan',bio)
        opt4=makeButton(tk,i9,'arial',12,'black',4,1,10,'cyan',cs)
        c1.create_window(conv(150),conv(300),window=b1)
        c1.create_window(conv(280),conv(300),window=b2)
        c1.create_window(conv(280),conv(450),window=opt4)
    else:
        b1=makeButton(tk,i4,'arial',12,'black',4,1,10,'cyan',socialogy)
        b2=makeButton(tk,i5,'arial',12,'black',4,1,10,'cyan',economics)
        opt4=makeButton(tk,i9,'arial',12,'black',4,1,10,'cyan',phycho)
        c1.create_window(conv(150),conv(300),window=b1)
        c1.create_window(conv(280),conv(300),window=b2)
        c1.create_window(conv(280),conv(450),window=opt4)
    backButton=makeButton(tk,'Back','arial',10,'black',4,1,5,'gold3',chooseStream)
    nextButton=makeButton(tk,'Next','arial',10,'black',4,1,5,'green',fetchingMarks)
    c3.create_window(conv(275),conv(575),window=backButton)
    c3.create_window(conv(350),conv(575),window=nextButton)
def chooseStream():
    clearScreen(tk)
    l1=makeLabel(tk,'Choose your Stream','arial',32,'purple',0,1,20,'pink')
    b1=makeButton(tk,'Science','arial',20,'black',4,2,20,'green',science)
    b2=makeButton(tk,'Commerce','arial',20,'black',4,2,20,'orange',commerce)
    b3=makeButton(tk,'Arts','arial',20,'black',4,2,20,'brown',arts)
    c.create_window(conv(600),conv(100),window=l1)
    c.create_window(conv(600),conv(240),window=b1)
    c.create_window(conv(600),conv(340),window=b2)
    c.create_window(conv(600),conv(440),window=b3)
def infoNullCheck():
    global e11,e12,e13,e14,e15,e16,e17,e18,lene14,lene17,lene18,alist
    e11=e1.get()
    e12=e2.get()
    e13=e3.get()
    e14=e4.get()
    e15=e5.get()
    e16=e6.get()
    e17=e7.get()
    e18=e8.get()
    alist=[e11,e12,e13,e14,e15,e16,e17,e18]
    lene14=len(e14)
    lene17=len(e17)
    lene18=len(e18)
    xAxis=conv(950)
    yAxis=conv(140)
    status=0
    for i in range(0,8):
        factor=conv(50)*i
        if(len(alist[i])==0 or alist[i].isspace()):
            status=1
            Label(tk,text="Required*",width=20,bg='pink',fg='red').place(x=xAxis,y=yAxis+factor)
        elif((i==3 or i==6 or i==7) and (not alist[i].isnumeric())):
            status=1
            Label(tk,text="Invalid Input",width=20,bg='pink',fg='red').place(x=xAxis,y=yAxis+factor)             
        elif((i==0 or i==1 or i==2 or i==5) and (len(alist[i])>50)):
            status=1
            Label(tk,text="  Max length can be 50",width=20,bg='pink',fg='red').place(x=xAxis,y=yAxis+factor)             
        else:
            Label(tk,text="",width=20,bg='pink',fg='red').place(x=xAxis,y=yAxis+factor)
    if(status==0): chooseStream()
def createMarksheet():
    global e1,e2,e3,e4,e5,e6,e7,e8
    clearScreen(tk)
    l1=makeLabel(tk,'Name','arial',14,'purple',0,1,15,'pink')
    l2=makeLabel(tk,"Father's Name",'arial',14,'purple',0,1,15,'pink')
    l3=makeLabel(tk,"Mother's Name",'arial',14,'purple',0,1,15,'pink')
    l4=makeLabel(tk,'Roll No.','arial',14,'purple',0,1,15,'pink')
    l5=makeLabel(tk,'D.O.B.','arial',14,'purple',0,1,15,'pink')
    l6=makeLabel(tk,'School Name','arial',14,'purple',0,1,15,'pink')
    l7=makeLabel(tk,'Center No.','arial',14,'purple',0,1,15,'pink')
    l8=makeLabel(tk,'School Code','arial',14,'purple',0,1,15,'pink')
    b1=Button(tk,text='Back',height=2,width=10,border=4,bg='orange',font=('arial',10,'bold'),command=homeScreen)
    b2=Button(tk,text='Next',height=2,width=10,border=4,bg='green',font=('arial',10,'bold'),command=infoNullCheck)
    e1=Entry(tk,width=35,fg='purple',border=4,font=('arial',12,'bold'))
    e2=Entry(tk,width=35,fg='purple',border=4,font=('arial',12,'bold'))
    e3=Entry(tk,width=35,fg='purple',border=4,font=('arial',12,'bold'))
    e4=Entry(tk,width=35,fg='purple',border=4,font=('arial',12,'bold'))
    e5=Entry(tk,width=35,fg='purple',border=4,font=('arial',12,'bold'))
    e6=Entry(tk,width=35,fg='purple',border=4,font=('arial',12,'bold'))
    e7=Entry(tk,width=35,fg='purple',border=4,font=('arial',12,'bold'))
    e8=Entry(tk,width=35,fg='purple',border=4,font=('arial',12,'bold'))
    c.create_window(conv(300),conv(100),window=l1)
    c.create_window(conv(330),conv(150),window=l2)
    c.create_window(conv(330),conv(200),window=l3)
    c.create_window(conv(307),conv(250),window=l4)
    c.create_window(conv(300),conv(300),window=l5)
    c.create_window(conv(322),conv(350),window=l6)
    c.create_window(conv(312),conv(400),window=l7)
    c.create_window(conv(320),conv(450),window=l8)
    c.create_window(conv(890),conv(580),window=b1)
    c.create_window(conv(1040),conv(580),window=b2)
    c.create_window(conv(700),conv(100),window=e1)
    c.create_window(conv(700),conv(150),window=e2)
    c.create_window(conv(700),conv(200),window=e3)
    c.create_window(conv(700),conv(250),window=e4)
    c.create_window(conv(700),conv(300),window=e5)
    c.create_window(conv(700),conv(350),window=e6)
    c.create_window(conv(700),conv(400),window=e7)
    c.create_window(conv(700),conv(450),window=e8)
def searchMarksheet():
    messagebox.showwarning("Message","Under Construction !")
def credit():
    messagebox.showwarning("Message","Under Construction !")
def exits():
    if(messagebox.askyesno("Close","Are you sure you want to exit?")): thankNote()
def homeScreen():
    global tk
    clearScreen(tk)
    tk.attributes('-fullscreen',True)
    tk.title("PULKIT BANSAL")
    tk.configure(bg='purple')
    l1=makeLabel(tk,'C.B.S.E.','elephant',42,'purple',8,1,0,'pink')
    l2=makeLabel(tk,'MARKSHEET','elephant',42,'purple',8,1,0,'pink')
    b1=makeButton(tk,'Create MarkSheet','times',20,'purple',8,1,25,'white',createMarksheet)
    b2=makeButton(tk,'Search MarkSheet','times',20,'purple',8,1,25,'white',searchMarksheet)
    b3=makeButton(tk,'Credits','times',20,'purple',8,1,25,'white',credit)
    b4=makeButton(tk,'Exit','times',20,'purple',8,1,25,'white',exits)
    c.create_window(conv(325),conv(240),window=l1)
    c.create_window(conv(325),conv(365),window=l2)
    c.create_window(conv(900),conv(200),window=b1)
    c.create_window(conv(900),conv(300),window=b2)
    c.create_window(conv(900),conv(400),window=b3)
    c.create_window(conv(900),conv(500),window=b4)
#<---Widgets---->
def makeLabel(tk,content,fontName,fontSize,fontColour,widgetBorder,widgetHeight,widgetWidth,bgColour):
    return Label(tk,text=content,font=(fontName,int(conv(fontSize)),'bold'),fg=fontColour,bg=bgColour,border=conv(widgetBorder),height=int(conv(widgetHeight)),width=int(conv(widgetWidth)))
def makeButton(tk,content,fontName,fontSize,fontColour,buttonBorder,buttonHeight,buttonWidth,bgColour,onClick):
    return Button(tk,text=content,font=(fontName,int(conv(fontSize)),'bold'),fg=fontColour,bg=bgColour,border=conv(buttonBorder),height=int(conv(buttonHeight)),width=int(conv(buttonWidth)),command=onClick)
def makeEntry(tk,fontName,fontSize,fontColour,widgetBorder,widgetWidth):
    return Entry(tk,font=(fontName,int(conv(fontSize)),'bold'),fg=fontColour,border=conv(widgetBorder),width=int(conv(widgetWidth)))
dimension()
homeScreen()
