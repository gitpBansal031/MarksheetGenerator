from tkinter import *
import time
def result():
    result_window=Toplevel(searchmark_window)
    result_window.configure(bg="purple")
    result_window.geometry('1350x750')
    w1=Canvas(result_window,height=225,width=1200,bg='pink')
    w1.place(x=75,y=50)
    w2=Canvas(result_window,height=100,width=100,bg='pink')
    w2.place(x=75,y=275)
    w3=Canvas(result_window,height=100,width=450,bg='pink')
    w3.place(x=175,y=275)
    w4=Canvas(result_window,height=50,width=550,bg='pink')
    w4.place(x=625,y=275)
    w5=Canvas(result_window,height=100,width=100,bg='pink')
    w5.place(x=1175,y=275)
    w6=Canvas(result_window,height=50,width=100,bg='pink')
    w6.place(x=625,y=325)
    w7=Canvas(result_window,height=50,width=100,bg='pink')
    w7.place(x=725,y=325)
    w8=Canvas(result_window,height=50,width=100,bg='pink')
    w8.place(x=825,y=325)
    w9=Canvas(result_window,height=50,width=250,bg='pink')
    w9.place(x=925,y=325)
    w10=Canvas(result_window,height=180,width=100,bg='pink')
    w10.place(x=75,y=375)
    w11=Canvas(result_window,height=180,width=450,bg='pink')
    w11.place(x=175,y=375)
    w12=Canvas(result_window,height=180,width=100,bg='pink')
    w12.place(x=625,y=375)
    w13=Canvas(result_window,height=180,width=100,bg='pink')
    w13.place(x=725,y=375)
    w14=Canvas(result_window,height=180,width=100,bg='pink')
    w14.place(x=825,y=375)
    w15=Canvas(result_window,height=180,width=250,bg='pink')
    w15.place(x=925,y=375)
    w16=Canvas(result_window,height=180,width=100,bg='pink')
    w16.place(x=1175,y=375)
    w17=Canvas(result_window,height=100,width=1200,bg='pink')
    w17.place(x=75,y=555)
    Label(result_window,text="CENTRAL BOARD OF SECONDARY EDUCATION",fg='red',bg='pink',font=('arial',19,'bold')).place(x=330,y=53)
    Label(result_window,text="MARKS STATEMENT",bg='pink',fg='red',font=('arial',16,'bold')).place(x=475,y=85)
    Label(result_window,text="Name of Student",fg='red',bg='pink',font=('arial',12,'bold')).place(x=100,y=120)
    Label(result_window,text="Roll No.",bg='pink',fg='red',font=('arial',12,'bold')).place(x=100,y=140)
    Label(result_window,text="Mother's Name ",fg='red',bg='pink',font=('arial',12,'bold')).place(x=100,y=160)
    Label(result_window,text="Father's Name",bg='pink',fg='red',font=('arial',12,'bold')).place(x=100,y=180)
    Label(result_window,text="Date of Birth ",fg='red',bg='pink',font=('arial',12,'bold')).place(x=100,y=200)
    Label(result_window,text="School",bg='pink',fg='red',font=('arial',12,'bold')).place(x=100,y=220)
    Label(result_window,text=e11,fg='black',bg='pink',font=('arial',12,'bold')).place(x=275,y=120)
    Label(result_window,text=e14,bg='pink',fg='black',font=('arial',12,'bold')).place(x=195,y=140)
    Label(result_window,text=e13,fg='black',bg='pink',font=('arial',12,'bold')).place(x=265,y=160)
    Label(result_window,text=e12,bg='pink',fg='black',font=('arial',12,'bold')).place(x=265,y=180)
    Label(result_window,text=e15,fg='black',bg='pink',font=('arial',12,'bold')).place(x=240,y=200)
    Label(result_window,text=e16,bg='pink',fg='black',font=('arial',12,'bold')).place(x=185,y=220)
    Label(result_window,text="Scholastic Achievements",bg='pink',fg='red',font=('arial',12,'bold')).place(x=100,y=240)
    Label(result_window,text="CODE",bg='pink',fg='black',font=('arial',14,'bold')).place(x=105,y=335)
    Label(result_window,text="SUBJECT",bg='pink',fg='black',font=('arial',14,'bold')).place(x=375,y=335)
    Label(result_window,text="MARKS OBTAINED",bg='pink',fg='black',font=('arial',14,'bold')).place(x=850,y=295)
    Label(result_window,text="GRADE",bg='pink',fg='black',font=('arial',14,'bold')).place(x=1185,y=345)
    Label(result_window,text="THEORY",bg='pink',fg='black',font=('arial',14,'bold')).place(x=635,y=345)
    Label(result_window,text="PR.",bg='pink',fg='black',font=('arial',14,'bold')).place(x=775,y=345)
    Label(result_window,text="TOTAL",bg='pink',fg='black',font=('arial',14,'bold')).place(x=850,y=345)
    Label(result_window,text="TOTAL(IN WORDS)",bg='pink',fg='black',font=('arial',14,'bold')).place(x=950,y=345)
    Label(result_window,text=ca,bg='pink',fg='black',font=('arial',14,'bold')).place(x=125,y=385)
    Label(result_window,text=cb,bg='pink',fg='black',font=('arial',14,'bold')).place(x=125,y=410)
    Label(result_window,text=cc,bg='pink',fg='black',font=('arial',14,'bold')).place(x=125,y=435)
    Label(result_window,text=cp,bg='pink',fg='black',font=('arial',14,'bold')).place(x=125,y=460)
    Label(result_window,text=co,bg='pink',fg='black',font=('arial',14,'bold')).place(x=125,y=485)
    Label(result_window,text=aname,bg='pink',fg='black',font=('arial',14,'bold')).place(x=200,y=385)
    Label(result_window,text=bname,bg='pink',fg='black',font=('arial',14,'bold')).place(x=200,y=410)
    Label(result_window,text=cname,bg='pink',fg='black',font=('arial',14,'bold')).place(x=200,y=435)
    Label(result_window,text=pname,bg='pink',fg='black',font=('arial',14,'bold')).place(x=200,y=460)
    Label(result_window,text=opt,bg='pink',fg='black',font=('arial',14,'bold')).place(x=200,y=485)
    Label(result_window,text=mta,bg='pink',fg='black',font=('arial',14,'bold')).place(x=985,y=385)
    Label(result_window,text=mtb,bg='pink',fg='black',font=('arial',14,'bold')).place(x=985,y=410)
    Label(result_window,text=mtc,bg='pink',fg='black',font=('arial',14,'bold')).place(x=985,y=435)
    Label(result_window,text=mtp,bg='pink',fg='black',font=('arial',14,'bold')).place(x=985,y=460)
    Label(result_window,text=mto,bg='pink',fg='black',font=('arial',14,'bold')).place(x=985,y=485)
    Label(result_window,text=ta,bg='pink',fg='black',font=('arial',14,'bold')).place(x=675,y=385)
    Label(result_window,text=tb,bg='pink',fg='black',font=('arial',14,'bold')).place(x=675,y=410)
    Label(result_window,text=tc,bg='pink',fg='black',font=('arial',14,'bold')).place(x=675,y=435)
    Label(result_window,text=tp,bg='pink',fg='black',font=('arial',14,'bold')).place(x=675,y=460)
    Label(result_window,text=to,bg='pink',fg='black',font=('arial',14,'bold')).place(x=675,y=485)
    Label(result_window,text=xa,bg='pink',fg='black',font=('arial',14,'bold')).place(x=875,y=385)
    Label(result_window,text=xb,bg='pink',fg='black',font=('arial',14,'bold')).place(x=875,y=410)
    Label(result_window,text=xc,bg='pink',fg='black',font=('arial',14,'bold')).place(x=875,y=435)
    Label(result_window,text=xp,bg='pink',fg='black',font=('arial',14,'bold')).place(x=875,y=460)
    Label(result_window,text=xo,bg='pink',fg='black',font=('arial',14,'bold')).place(x=875,y=485)
    Label(result_window,text=pa,bg='pink',fg='black',font=('arial',14,'bold')).place(x=775,y=385)
    Label(result_window,text=pb,bg='pink',fg='black',font=('arial',14,'bold')).place(x=775,y=410)
    Label(result_window,text=pc,bg='pink',fg='black',font=('arial',14,'bold')).place(x=775,y=435)
    Label(result_window,text=pp,bg='pink',fg='black',font=('arial',14,'bold')).place(x=775,y=460)
    Label(result_window,text=po,bg='pink',fg='black',font=('arial',14,'bold')).place(x=775,y=485)
    Label(result_window,text=ga,bg='pink',fg='black',font=('arial',14,'bold')).place(x=1225,y=385)
    Label(result_window,text=gb,bg='pink',fg='black',font=('arial',14,'bold')).place(x=1225,y=410)
    Label(result_window,text=gc,bg='pink',fg='black',font=('arial',14,'bold')).place(x=1225,y=435)
    Label(result_window,text=gp,bg='pink',fg='black',font=('arial',14,'bold')).place(x=1225,y=460)
    Label(result_window,text=go,bg='pink',fg='black',font=('arial',14,'bold')).place(x=1225,y=485)
    Label(result_window,text="Abbreviations",bg='pink',fg='red',font=('arial',12,'bold')).place(x=100,y=560)
    Label(result_window,text="AB: Absent",bg='pink',fg='red',font=('arial',12,'bold')).place(x=100,y=580)
    Label(result_window,text="PR: Practical",bg='pink',fg='red',font=('arial',12,'bold')).place(x=100,y=600)
    Label(result_window,text="DELHI : ",bg='pink',fg='red',font=('arial',12,'bold')).place(x=100,y=625)
    Label(result_window,text="28/08/2019",bg='pink',fg='black',font=('arial',12,'bold')).place(x=185,y=625)
    Label(result_window,text="Result:",bg='pink',fg='red',font=('arial',12,'bold')).place(x=750,y=570)
    Label(result_window,text=pf,bg='pink',fg='black',font=('arial',12,'bold')).place(x=830,y=570)
def result1():
    result_window=Toplevel(science_window)
    result_window.configure(bg="purple")
    result_window.geometry('1350x750')
    w1=Canvas(result_window,height=225,width=1200,bg='pink')
    w1.place(x=75,y=50)
    w2=Canvas(result_window,height=100,width=100,bg='pink')
    w2.place(x=75,y=275)
    w3=Canvas(result_window,height=100,width=450,bg='pink')
    w3.place(x=175,y=275)
    w4=Canvas(result_window,height=50,width=550,bg='pink')
    w4.place(x=625,y=275)
    w5=Canvas(result_window,height=100,width=100,bg='pink')
    w5.place(x=1175,y=275)
    w6=Canvas(result_window,height=50,width=100,bg='pink')
    w6.place(x=625,y=325)
    w7=Canvas(result_window,height=50,width=100,bg='pink')
    w7.place(x=725,y=325)
    w8=Canvas(result_window,height=50,width=100,bg='pink')
    w8.place(x=825,y=325)
    w9=Canvas(result_window,height=50,width=250,bg='pink')
    w9.place(x=925,y=325)
    w10=Canvas(result_window,height=180,width=100,bg='pink')
    w10.place(x=75,y=375)
    w11=Canvas(result_window,height=180,width=450,bg='pink')
    w11.place(x=175,y=375)
    w12=Canvas(result_window,height=180,width=100,bg='pink')
    w12.place(x=625,y=375)
    w13=Canvas(result_window,height=180,width=100,bg='pink')
    w13.place(x=725,y=375)
    w14=Canvas(result_window,height=180,width=100,bg='pink')
    w14.place(x=825,y=375)
    w15=Canvas(result_window,height=180,width=250,bg='pink')
    w15.place(x=925,y=375)
    w16=Canvas(result_window,height=180,width=100,bg='pink')
    w16.place(x=1175,y=375)
    w17=Canvas(result_window,height=100,width=1200,bg='pink')
    w17.place(x=75,y=555)
    Label(result_window,text="CENTRAL BOARD OF SECONDARY EDUCATION",fg='red',bg='pink',font=('arial',19,'bold')).place(x=330,y=53)
    Label(result_window,text="MARKS STATEMENT",bg='pink',fg='red',font=('arial',16,'bold')).place(x=475,y=85)
    Label(result_window,text="Name of Student",fg='red',bg='pink',font=('arial',12,'bold')).place(x=100,y=120)
    Label(result_window,text="Roll No.",bg='pink',fg='red',font=('arial',12,'bold')).place(x=100,y=140)
    Label(result_window,text="Mother's Name ",fg='red',bg='pink',font=('arial',12,'bold')).place(x=100,y=160)
    Label(result_window,text="Father's Name",bg='pink',fg='red',font=('arial',12,'bold')).place(x=100,y=180)
    Label(result_window,text="Date of Birth ",fg='red',bg='pink',font=('arial',12,'bold')).place(x=100,y=200)
    Label(result_window,text="School",bg='pink',fg='red',font=('arial',12,'bold')).place(x=100,y=220)
    Label(result_window,text=e11,fg='black',bg='pink',font=('arial',12,'bold')).place(x=275,y=120)
    Label(result_window,text=e14,bg='pink',fg='black',font=('arial',12,'bold')).place(x=195,y=140)
    Label(result_window,text=e13,fg='black',bg='pink',font=('arial',12,'bold')).place(x=265,y=160)
    Label(result_window,text=e12,bg='pink',fg='black',font=('arial',12,'bold')).place(x=265,y=180)
    Label(result_window,text=e15,fg='black',bg='pink',font=('arial',12,'bold')).place(x=240,y=200)
    Label(result_window,text=e16,bg='pink',fg='black',font=('arial',12,'bold')).place(x=185,y=220)
    Label(result_window,text="Scholastic Achievements",bg='pink',fg='red',font=('arial',12,'bold')).place(x=100,y=240)
    Label(result_window,text="CODE",bg='pink',fg='black',font=('arial',14,'bold')).place(x=105,y=335)
    Label(result_window,text="SUBJECT",bg='pink',fg='black',font=('arial',14,'bold')).place(x=375,y=335)
    Label(result_window,text="MARKS OBTAINED",bg='pink',fg='black',font=('arial',14,'bold')).place(x=850,y=295)
    Label(result_window,text="GRADE",bg='pink',fg='black',font=('arial',14,'bold')).place(x=1185,y=345)
    Label(result_window,text="THEORY",bg='pink',fg='black',font=('arial',14,'bold')).place(x=635,y=345)
    Label(result_window,text="PR.",bg='pink',fg='black',font=('arial',14,'bold')).place(x=775,y=345)
    Label(result_window,text="TOTAL",bg='pink',fg='black',font=('arial',14,'bold')).place(x=850,y=345)
    Label(result_window,text="TOTAL(IN WORDS)",bg='pink',fg='black',font=('arial',14,'bold')).place(x=950,y=345)
    Label(result_window,text=ca,bg='pink',fg='black',font=('arial',14,'bold')).place(x=125,y=385)
    Label(result_window,text=cb,bg='pink',fg='black',font=('arial',14,'bold')).place(x=125,y=410)
    Label(result_window,text=cc,bg='pink',fg='black',font=('arial',14,'bold')).place(x=125,y=435)
    Label(result_window,text=cp,bg='pink',fg='black',font=('arial',14,'bold')).place(x=125,y=460)
    Label(result_window,text=co,bg='pink',fg='black',font=('arial',14,'bold')).place(x=125,y=485)
    Label(result_window,text=aname,bg='pink',fg='black',font=('arial',14,'bold')).place(x=200,y=385)
    Label(result_window,text=bname,bg='pink',fg='black',font=('arial',14,'bold')).place(x=200,y=410)
    Label(result_window,text=cname,bg='pink',fg='black',font=('arial',14,'bold')).place(x=200,y=435)
    Label(result_window,text=pname,bg='pink',fg='black',font=('arial',14,'bold')).place(x=200,y=460)
    Label(result_window,text=opt,bg='pink',fg='black',font=('arial',14,'bold')).place(x=200,y=485)
    Label(result_window,text=mta,bg='pink',fg='black',font=('arial',14,'bold')).place(x=985,y=385)
    Label(result_window,text=mtb,bg='pink',fg='black',font=('arial',14,'bold')).place(x=985,y=410)
    Label(result_window,text=mtc,bg='pink',fg='black',font=('arial',14,'bold')).place(x=985,y=435)
    Label(result_window,text=mtp,bg='pink',fg='black',font=('arial',14,'bold')).place(x=985,y=460)
    Label(result_window,text=mto,bg='pink',fg='black',font=('arial',14,'bold')).place(x=985,y=485)
    Label(result_window,text=ta,bg='pink',fg='black',font=('arial',14,'bold')).place(x=675,y=385)
    Label(result_window,text=tb,bg='pink',fg='black',font=('arial',14,'bold')).place(x=675,y=410)
    Label(result_window,text=tc,bg='pink',fg='black',font=('arial',14,'bold')).place(x=675,y=435)
    Label(result_window,text=tp,bg='pink',fg='black',font=('arial',14,'bold')).place(x=675,y=460)
    Label(result_window,text=to,bg='pink',fg='black',font=('arial',14,'bold')).place(x=675,y=485)
    Label(result_window,text=xa,bg='pink',fg='black',font=('arial',14,'bold')).place(x=875,y=385)
    Label(result_window,text=xb,bg='pink',fg='black',font=('arial',14,'bold')).place(x=875,y=410)
    Label(result_window,text=xc,bg='pink',fg='black',font=('arial',14,'bold')).place(x=875,y=435)
    Label(result_window,text=xp,bg='pink',fg='black',font=('arial',14,'bold')).place(x=875,y=460)
    Label(result_window,text=xo,bg='pink',fg='black',font=('arial',14,'bold')).place(x=875,y=485)
    Label(result_window,text=pa,bg='pink',fg='black',font=('arial',14,'bold')).place(x=775,y=385)
    Label(result_window,text=pb,bg='pink',fg='black',font=('arial',14,'bold')).place(x=775,y=410)
    Label(result_window,text=pc,bg='pink',fg='black',font=('arial',14,'bold')).place(x=775,y=435)
    Label(result_window,text=pp,bg='pink',fg='black',font=('arial',14,'bold')).place(x=775,y=460)
    Label(result_window,text=po,bg='pink',fg='black',font=('arial',14,'bold')).place(x=775,y=485)
    Label(result_window,text=ga,bg='pink',fg='black',font=('arial',14,'bold')).place(x=1225,y=385)
    Label(result_window,text=gb,bg='pink',fg='black',font=('arial',14,'bold')).place(x=1225,y=410)
    Label(result_window,text=gc,bg='pink',fg='black',font=('arial',14,'bold')).place(x=1225,y=435)
    Label(result_window,text=gp,bg='pink',fg='black',font=('arial',14,'bold')).place(x=1225,y=460)
    Label(result_window,text=go,bg='pink',fg='black',font=('arial',14,'bold')).place(x=1225,y=485)
    Label(result_window,text="Abbreviations",bg='pink',fg='red',font=('arial',12,'bold')).place(x=100,y=560)
    Label(result_window,text="AB: Absent",bg='pink',fg='red',font=('arial',12,'bold')).place(x=100,y=580)
    Label(result_window,text="PR: Practical",bg='pink',fg='red',font=('arial',12,'bold')).place(x=100,y=600)
    Label(result_window,text="DELHI : ",bg='pink',fg='red',font=('arial',12,'bold')).place(x=100,y=625)
    Label(result_window,text="28/08/2019",bg='pink',fg='black',font=('arial',12,'bold')).place(x=185,y=625)
    Label(result_window,text="Result:",bg='pink',fg='red',font=('arial',12,'bold')).place(x=750,y=570)
    Label(result_window,text=pf,bg='pink',fg='black',font=('arial',12,'bold')).place(x=830,y=570)
    insert_marks()
def result2():
    result_window=Toplevel(commerce_window)
    result_window.configure(bg="purple")
    result_window.geometry('1350x750')
    w1=Canvas(result_window,height=225,width=1200,bg='pink')
    w1.place(x=75,y=50)
    w2=Canvas(result_window,height=100,width=100,bg='pink')
    w2.place(x=75,y=275)
    w3=Canvas(result_window,height=100,width=450,bg='pink')
    w3.place(x=175,y=275)
    w4=Canvas(result_window,height=50,width=550,bg='pink')
    w4.place(x=625,y=275)
    w5=Canvas(result_window,height=100,width=100,bg='pink')
    w5.place(x=1175,y=275)
    w6=Canvas(result_window,height=50,width=100,bg='pink')
    w6.place(x=625,y=325)
    w7=Canvas(result_window,height=50,width=100,bg='pink')
    w7.place(x=725,y=325)
    w8=Canvas(result_window,height=50,width=100,bg='pink')
    w8.place(x=825,y=325)
    w9=Canvas(result_window,height=50,width=250,bg='pink')
    w9.place(x=925,y=325)
    w10=Canvas(result_window,height=180,width=100,bg='pink')
    w10.place(x=75,y=375)
    w11=Canvas(result_window,height=180,width=450,bg='pink')
    w11.place(x=175,y=375)
    w12=Canvas(result_window,height=180,width=100,bg='pink')
    w12.place(x=625,y=375)
    w13=Canvas(result_window,height=180,width=100,bg='pink')
    w13.place(x=725,y=375)
    w14=Canvas(result_window,height=180,width=100,bg='pink')
    w14.place(x=825,y=375)
    w15=Canvas(result_window,height=180,width=250,bg='pink')
    w15.place(x=925,y=375)
    w16=Canvas(result_window,height=180,width=100,bg='pink')
    w16.place(x=1175,y=375)
    w17=Canvas(result_window,height=100,width=1200,bg='pink')
    w17.place(x=75,y=555)
    Label(result_window,text="CENTRAL BOARD OF SECONDARY EDUCATION",fg='red',bg='pink',font=('arial',19,'bold')).place(x=330,y=53)
    Label(result_window,text="MARKS STATEMENT",bg='pink',fg='red',font=('arial',16,'bold')).place(x=475,y=85)
    Label(result_window,text="Name of Student",fg='red',bg='pink',font=('arial',12,'bold')).place(x=100,y=120)
    Label(result_window,text="Roll No.",bg='pink',fg='red',font=('arial',12,'bold')).place(x=100,y=140)
    Label(result_window,text="Mother's Name ",fg='red',bg='pink',font=('arial',12,'bold')).place(x=100,y=160)
    Label(result_window,text="Father's Name",bg='pink',fg='red',font=('arial',12,'bold')).place(x=100,y=180)
    Label(result_window,text="Date of Birth ",fg='red',bg='pink',font=('arial',12,'bold')).place(x=100,y=200)
    Label(result_window,text="School",bg='pink',fg='red',font=('arial',12,'bold')).place(x=100,y=220)
    Label(result_window,text=e11,fg='black',bg='pink',font=('arial',12,'bold')).place(x=275,y=120)
    Label(result_window,text=e14,bg='pink',fg='black',font=('arial',12,'bold')).place(x=195,y=140)
    Label(result_window,text=e13,fg='black',bg='pink',font=('arial',12,'bold')).place(x=265,y=160)
    Label(result_window,text=e12,bg='pink',fg='black',font=('arial',12,'bold')).place(x=265,y=180)
    Label(result_window,text=e15,fg='black',bg='pink',font=('arial',12,'bold')).place(x=240,y=200)
    Label(result_window,text=e16,bg='pink',fg='black',font=('arial',12,'bold')).place(x=185,y=220)
    Label(result_window,text="Scholastic Achievements",bg='pink',fg='red',font=('arial',12,'bold')).place(x=100,y=240)
    Label(result_window,text="CODE",bg='pink',fg='black',font=('arial',14,'bold')).place(x=105,y=335)
    Label(result_window,text="SUBJECT",bg='pink',fg='black',font=('arial',14,'bold')).place(x=375,y=335)
    Label(result_window,text="MARKS OBTAINED",bg='pink',fg='black',font=('arial',14,'bold')).place(x=850,y=295)
    Label(result_window,text="GRADE",bg='pink',fg='black',font=('arial',14,'bold')).place(x=1185,y=345)
    Label(result_window,text="THEORY",bg='pink',fg='black',font=('arial',14,'bold')).place(x=635,y=345)
    Label(result_window,text="PR.",bg='pink',fg='black',font=('arial',14,'bold')).place(x=775,y=345)
    Label(result_window,text="TOTAL",bg='pink',fg='black',font=('arial',14,'bold')).place(x=850,y=345)
    Label(result_window,text="TOTAL(IN WORDS)",bg='pink',fg='black',font=('arial',14,'bold')).place(x=950,y=345)
    Label(result_window,text=ca,bg='pink',fg='black',font=('arial',14,'bold')).place(x=125,y=385)
    Label(result_window,text=cb,bg='pink',fg='black',font=('arial',14,'bold')).place(x=125,y=410)
    Label(result_window,text=cc,bg='pink',fg='black',font=('arial',14,'bold')).place(x=125,y=435)
    Label(result_window,text=cp,bg='pink',fg='black',font=('arial',14,'bold')).place(x=125,y=460)
    Label(result_window,text=co,bg='pink',fg='black',font=('arial',14,'bold')).place(x=125,y=485)
    Label(result_window,text=aname,bg='pink',fg='black',font=('arial',14,'bold')).place(x=200,y=385)
    Label(result_window,text=bname,bg='pink',fg='black',font=('arial',14,'bold')).place(x=200,y=410)
    Label(result_window,text=cname,bg='pink',fg='black',font=('arial',14,'bold')).place(x=200,y=435)
    Label(result_window,text=pname,bg='pink',fg='black',font=('arial',14,'bold')).place(x=200,y=460)
    Label(result_window,text=opt,bg='pink',fg='black',font=('arial',14,'bold')).place(x=200,y=485)
    Label(result_window,text=mta,bg='pink',fg='black',font=('arial',14,'bold')).place(x=985,y=385)
    Label(result_window,text=mtb,bg='pink',fg='black',font=('arial',14,'bold')).place(x=985,y=410)
    Label(result_window,text=mtc,bg='pink',fg='black',font=('arial',14,'bold')).place(x=985,y=435)
    Label(result_window,text=mtp,bg='pink',fg='black',font=('arial',14,'bold')).place(x=985,y=460)
    Label(result_window,text=mto,bg='pink',fg='black',font=('arial',14,'bold')).place(x=985,y=485)
    Label(result_window,text=ta,bg='pink',fg='black',font=('arial',14,'bold')).place(x=675,y=385)
    Label(result_window,text=tb,bg='pink',fg='black',font=('arial',14,'bold')).place(x=675,y=410)
    Label(result_window,text=tc,bg='pink',fg='black',font=('arial',14,'bold')).place(x=675,y=435)
    Label(result_window,text=tp,bg='pink',fg='black',font=('arial',14,'bold')).place(x=675,y=460)
    Label(result_window,text=to,bg='pink',fg='black',font=('arial',14,'bold')).place(x=675,y=485)
    Label(result_window,text=xa,bg='pink',fg='black',font=('arial',14,'bold')).place(x=875,y=385)
    Label(result_window,text=xb,bg='pink',fg='black',font=('arial',14,'bold')).place(x=875,y=410)
    Label(result_window,text=xc,bg='pink',fg='black',font=('arial',14,'bold')).place(x=875,y=435)
    Label(result_window,text=xp,bg='pink',fg='black',font=('arial',14,'bold')).place(x=875,y=460)
    Label(result_window,text=xo,bg='pink',fg='black',font=('arial',14,'bold')).place(x=875,y=485)
    Label(result_window,text=pa,bg='pink',fg='black',font=('arial',14,'bold')).place(x=775,y=385)
    Label(result_window,text=pb,bg='pink',fg='black',font=('arial',14,'bold')).place(x=775,y=410)
    Label(result_window,text=pc,bg='pink',fg='black',font=('arial',14,'bold')).place(x=775,y=435)
    Label(result_window,text=pp,bg='pink',fg='black',font=('arial',14,'bold')).place(x=775,y=460)
    Label(result_window,text=po,bg='pink',fg='black',font=('arial',14,'bold')).place(x=775,y=485)
    Label(result_window,text=ga,bg='pink',fg='black',font=('arial',14,'bold')).place(x=1225,y=385)
    Label(result_window,text=gb,bg='pink',fg='black',font=('arial',14,'bold')).place(x=1225,y=410)
    Label(result_window,text=gc,bg='pink',fg='black',font=('arial',14,'bold')).place(x=1225,y=435)
    Label(result_window,text=gp,bg='pink',fg='black',font=('arial',14,'bold')).place(x=1225,y=460)
    Label(result_window,text=go,bg='pink',fg='black',font=('arial',14,'bold')).place(x=1225,y=485)
    Label(result_window,text="Abbreviations",bg='pink',fg='red',font=('arial',12,'bold')).place(x=100,y=560)
    Label(result_window,text="AB: Absent",bg='pink',fg='red',font=('arial',12,'bold')).place(x=100,y=580)
    Label(result_window,text="PR: Practical",bg='pink',fg='red',font=('arial',12,'bold')).place(x=100,y=600)
    Label(result_window,text="DELHI : ",bg='pink',fg='red',font=('arial',12,'bold')).place(x=100,y=625)
    Label(result_window,text="28/08/2019",bg='pink',fg='black',font=('arial',12,'bold')).place(x=185,y=625)
    Label(result_window,text="Result:",bg='pink',fg='red',font=('arial',12,'bold')).place(x=750,y=570)
    Label(result_window,text=pf,bg='pink',fg='black',font=('arial',12,'bold')).place(x=830,y=570)
    insert_marks()
def result3():
    result_window=Toplevel(art_window)
    result_window.configure(bg="purple")
    result_window.geometry('1350x750')
    w1=Canvas(result_window,height=225,width=1200,bg='pink')
    w1.place(x=75,y=50)
    w2=Canvas(result_window,height=100,width=100,bg='pink')
    w2.place(x=75,y=275)
    w3=Canvas(result_window,height=100,width=450,bg='pink')
    w3.place(x=175,y=275)
    w4=Canvas(result_window,height=50,width=550,bg='pink')
    w4.place(x=625,y=275)
    w5=Canvas(result_window,height=100,width=100,bg='pink')
    w5.place(x=1175,y=275)
    w6=Canvas(result_window,height=50,width=100,bg='pink')
    w6.place(x=625,y=325)
    w7=Canvas(result_window,height=50,width=100,bg='pink')
    w7.place(x=725,y=325)
    w8=Canvas(result_window,height=50,width=100,bg='pink')
    w8.place(x=825,y=325)
    w9=Canvas(result_window,height=50,width=250,bg='pink')
    w9.place(x=925,y=325)
    w10=Canvas(result_window,height=180,width=100,bg='pink')
    w10.place(x=75,y=375)
    w11=Canvas(result_window,height=180,width=450,bg='pink')
    w11.place(x=175,y=375)
    w12=Canvas(result_window,height=180,width=100,bg='pink')
    w12.place(x=625,y=375)
    w13=Canvas(result_window,height=180,width=100,bg='pink')
    w13.place(x=725,y=375)
    w14=Canvas(result_window,height=180,width=100,bg='pink')
    w14.place(x=825,y=375)
    w15=Canvas(result_window,height=180,width=250,bg='pink')
    w15.place(x=925,y=375)
    w16=Canvas(result_window,height=180,width=100,bg='pink')
    w16.place(x=1175,y=375)
    w17=Canvas(result_window,height=100,width=1200,bg='pink')
    w17.place(x=75,y=555)
    Label(result_window,text="CENTRAL BOARD OF SECONDARY EDUCATION",fg='red',bg='pink',font=('arial',19,'bold')).place(x=330,y=53)
    Label(result_window,text="MARKS STATEMENT",bg='pink',fg='red',font=('arial',16,'bold')).place(x=475,y=85)
    Label(result_window,text="Name of Student",fg='red',bg='pink',font=('arial',12,'bold')).place(x=100,y=120)
    Label(result_window,text="Roll No.",bg='pink',fg='red',font=('arial',12,'bold')).place(x=100,y=140)
    Label(result_window,text="Mother's Name ",fg='red',bg='pink',font=('arial',12,'bold')).place(x=100,y=160)
    Label(result_window,text="Father's Name",bg='pink',fg='red',font=('arial',12,'bold')).place(x=100,y=180)
    Label(result_window,text="Date of Birth ",fg='red',bg='pink',font=('arial',12,'bold')).place(x=100,y=200)
    Label(result_window,text="School",bg='pink',fg='red',font=('arial',12,'bold')).place(x=100,y=220)
    Label(result_window,text=e11,fg='black',bg='pink',font=('arial',12,'bold')).place(x=275,y=120)
    Label(result_window,text=e14,bg='pink',fg='black',font=('arial',12,'bold')).place(x=195,y=140)
    Label(result_window,text=e13,fg='black',bg='pink',font=('arial',12,'bold')).place(x=265,y=160)
    Label(result_window,text=e12,bg='pink',fg='black',font=('arial',12,'bold')).place(x=265,y=180)
    Label(result_window,text=e15,fg='black',bg='pink',font=('arial',12,'bold')).place(x=240,y=200)
    Label(result_window,text=e16,bg='pink',fg='black',font=('arial',12,'bold')).place(x=185,y=220)
    Label(result_window,text="Scholastic Achievements",bg='pink',fg='red',font=('arial',12,'bold')).place(x=100,y=240)
    Label(result_window,text="CODE",bg='pink',fg='black',font=('arial',14,'bold')).place(x=105,y=335)
    Label(result_window,text="SUBJECT",bg='pink',fg='black',font=('arial',14,'bold')).place(x=375,y=335)
    Label(result_window,text="MARKS OBTAINED",bg='pink',fg='black',font=('arial',14,'bold')).place(x=850,y=295)
    Label(result_window,text="GRADE",bg='pink',fg='black',font=('arial',14,'bold')).place(x=1185,y=345)
    Label(result_window,text="THEORY",bg='pink',fg='black',font=('arial',14,'bold')).place(x=635,y=345)
    Label(result_window,text="PR.",bg='pink',fg='black',font=('arial',14,'bold')).place(x=775,y=345)
    Label(result_window,text="TOTAL",bg='pink',fg='black',font=('arial',14,'bold')).place(x=850,y=345)
    Label(result_window,text="TOTAL(IN WORDS)",bg='pink',fg='black',font=('arial',14,'bold')).place(x=950,y=345)
    Label(result_window,text=ca,bg='pink',fg='black',font=('arial',14,'bold')).place(x=125,y=385)
    Label(result_window,text=cb,bg='pink',fg='black',font=('arial',14,'bold')).place(x=125,y=410)
    Label(result_window,text=cc,bg='pink',fg='black',font=('arial',14,'bold')).place(x=125,y=435)
    Label(result_window,text=cp,bg='pink',fg='black',font=('arial',14,'bold')).place(x=125,y=460)
    Label(result_window,text=co,bg='pink',fg='black',font=('arial',14,'bold')).place(x=125,y=485)
    Label(result_window,text=aname,bg='pink',fg='black',font=('arial',14,'bold')).place(x=200,y=385)
    Label(result_window,text=bname,bg='pink',fg='black',font=('arial',14,'bold')).place(x=200,y=410)
    Label(result_window,text=cname,bg='pink',fg='black',font=('arial',14,'bold')).place(x=200,y=435)
    Label(result_window,text=pname,bg='pink',fg='black',font=('arial',14,'bold')).place(x=200,y=460)
    Label(result_window,text=opt,bg='pink',fg='black',font=('arial',14,'bold')).place(x=200,y=485)
    Label(result_window,text=mta,bg='pink',fg='black',font=('arial',14,'bold')).place(x=985,y=385)
    Label(result_window,text=mtb,bg='pink',fg='black',font=('arial',14,'bold')).place(x=985,y=410)
    Label(result_window,text=mtc,bg='pink',fg='black',font=('arial',14,'bold')).place(x=985,y=435)
    Label(result_window,text=mtp,bg='pink',fg='black',font=('arial',14,'bold')).place(x=985,y=460)
    Label(result_window,text=mto,bg='pink',fg='black',font=('arial',14,'bold')).place(x=985,y=485)
    Label(result_window,text=ta,bg='pink',fg='black',font=('arial',14,'bold')).place(x=675,y=385)
    Label(result_window,text=tb,bg='pink',fg='black',font=('arial',14,'bold')).place(x=675,y=410)
    Label(result_window,text=tc,bg='pink',fg='black',font=('arial',14,'bold')).place(x=675,y=435)
    Label(result_window,text=tp,bg='pink',fg='black',font=('arial',14,'bold')).place(x=675,y=460)
    Label(result_window,text=to,bg='pink',fg='black',font=('arial',14,'bold')).place(x=675,y=485)
    Label(result_window,text=xa,bg='pink',fg='black',font=('arial',14,'bold')).place(x=875,y=385)
    Label(result_window,text=xb,bg='pink',fg='black',font=('arial',14,'bold')).place(x=875,y=410)
    Label(result_window,text=xc,bg='pink',fg='black',font=('arial',14,'bold')).place(x=875,y=435)
    Label(result_window,text=xp,bg='pink',fg='black',font=('arial',14,'bold')).place(x=875,y=460)
    Label(result_window,text=xo,bg='pink',fg='black',font=('arial',14,'bold')).place(x=875,y=485)
    Label(result_window,text=pa,bg='pink',fg='black',font=('arial',14,'bold')).place(x=775,y=385)
    Label(result_window,text=pb,bg='pink',fg='black',font=('arial',14,'bold')).place(x=775,y=410)
    Label(result_window,text=pc,bg='pink',fg='black',font=('arial',14,'bold')).place(x=775,y=435)
    Label(result_window,text=pp,bg='pink',fg='black',font=('arial',14,'bold')).place(x=775,y=460)
    Label(result_window,text=po,bg='pink',fg='black',font=('arial',14,'bold')).place(x=775,y=485)
    Label(result_window,text=ga,bg='pink',fg='black',font=('arial',14,'bold')).place(x=1225,y=385)
    Label(result_window,text=gb,bg='pink',fg='black',font=('arial',14,'bold')).place(x=1225,y=410)
    Label(result_window,text=gc,bg='pink',fg='black',font=('arial',14,'bold')).place(x=1225,y=435)
    Label(result_window,text=gp,bg='pink',fg='black',font=('arial',14,'bold')).place(x=1225,y=460)
    Label(result_window,text=go,bg='pink',fg='black',font=('arial',14,'bold')).place(x=1225,y=485)
    Label(result_window,text="Abbreviations",bg='pink',fg='red',font=('arial',12,'bold')).place(x=100,y=560)
    Label(result_window,text="AB: Absent",bg='pink',fg='red',font=('arial',12,'bold')).place(x=100,y=580)
    Label(result_window,text="PR: Practical",bg='pink',fg='red',font=('arial',12,'bold')).place(x=100,y=600)
    Label(result_window,text="DELHI : ",bg='pink',fg='red',font=('arial',12,'bold')).place(x=100,y=625)
    Label(result_window,text="28/08/2019",bg='pink',fg='black',font=('arial',12,'bold')).place(x=185,y=625)
    Label(result_window,text="Result:",bg='pink',fg='red',font=('arial',12,'bold')).place(x=750,y=570)
    Label(result_window,text=pf,bg='pink',fg='black',font=('arial',12,'bold')).place(x=830,y=570)
    insert_marks()
def ways():
    if way=='science':
        result1()
    elif way=='commerce':
        result2()
    elif way=='art':
        result3()
def marks_text():
    global mta
    global mtb
    global mtc
    global mtp
    global mto
    sxa=str(xa)
    sxb=str(xb)
    sxc=str(xc)
    sxp=str(xp)
    sxo=str(xo)
    lsxa=len(sxa)
    lsxb=len(sxb)
    lsxc=len(sxc)
    lsxp=len(sxp)
    lsxo=len(sxo)
    if xa==0:
        mta='ZERO'
    elif xa==1:
        mta='ONE'
    elif xa==2:
        mta='TWO'
    elif xa==3:
        mta='THREE'
    elif xa==4:
        mta='FOUR'
    elif xa==5:
        mta='FIVE'
    elif xa==6:
        mta='SIX'
    elif xa==7:
        mta='SEVEN'
    elif xa==8:
        mta='EIGHT'
    elif xa==9:
        mta='NINE'
    elif xa==10:
        mta='TEN'
    elif xa==11:
        mta='ELEVEN'
    elif xa==12:
        mta='TWELVE'
    elif xa==13:
        mta='THIRTEEN'
    elif xa==14:
        mta='FOURTEEN'
    elif xa==15:
        mta='FIFTEEN'
    elif xa==16:
        mta='SIXTEEN'
    elif xa==17:
        mta='SEVENTEEN'
    elif xa==18:
        mta='EIGHTEEN'
    elif xa==19:
        mta='NINETEEN'
    elif xa==20:
        mta='TWENTY'
    elif xa==21:
        mta='TWENTY ONE'
    elif xa==22:
        mta='TWENTY TWO'
    elif xa==23:
        mta='TWENTY THREE'
    elif xa==24:
        mta='TWENTY FOUR'
    elif xa==25:
        mta='TWENTY FIVE'
    elif xa==26:
        mta='TWENTY SIX'
    elif xa==27:
        mta='TWENTY SEVEN'
    elif xa==28:
        mta='TWENTY EIGHT'
    elif xa==29:
        mta='TWENTY NINE'
    elif xa==30:
        mta='THIRTY'
    elif xa==31:
        mta='THIRTY ONE'
    elif xa==32:
        mta='THIRTY TWO'
    elif xa==33:
        mta='THIRTY THREE'
    elif xa==34:
        mta='THIRTY FOUR'
    elif xa==35:
        mta='THIRTY FIVE'
    elif xa==36:
        mta='THIRTY SIX'
    elif xa==37:
        mta='THIRTY SEVEN'
    elif xa==38:
        mta='THIRTY EIGHT'
    elif xa==39:
        mta='THIRTY NINE'
    elif xa==40:
        mta='FORTY'
    elif xa==41:
        mta='FORTY ONE'
    elif xa==42:
        mta='FORTY TWO'
    elif xa==43:
        mta='FORTY THREE'
    elif xa==44:
        mta='FORTY FOUR'
    elif xa==45:
        mta='FORTY FIVE'
    elif xa==46:
        mta='FORTY SIX'
    elif xa==47:
        mta='FORTY SEVEN'
    elif xa==48:
        mta='FORTY EIGHT'
    elif xa==49:
        mta='FORTY NINE'
    elif xa==50:
        mta='FIFTY '
    elif xa==51:
        mta='FIFTY ONE'
    elif xa==52:
        mta='FIFTY TWO'
    elif xa==53:
        mta='FIFTY THREE'
    elif xa==54:
        mta='FIFTY FOUR'
    elif xa==55:
        mta='FIFTY FIVE'
    elif xa==56:
        mta='FIFTY SIX'
    elif xa==57:
        mta='FIFTY SEVEN'
    elif xa==58:
        mta='FIFTY EIGHT'
    elif xa==59:
        mta='FIFTY NINE'
    elif xa==60:
        mta='SIXTY TEN'
    elif xa==61:
        mta='SIXTY ONE'
    elif xa==62:
        mta='SIXTY TWO'
    elif xa==63:
        mta='SIXTY THREE'
    elif xa==64:
        mta='SIXTY FOUR'
    elif xa==65:
        mta='SIXTY FIVE'
    elif xa==66:
        mta='SIXTY SIX'
    elif xa==67:
        mta='SIXTY SEVEN'
    elif xa==68:
        mta='SIXTY EIGHT'
    elif xa==69:
        mta='SIXTY NINE'
    elif xa==70:
        mta='SEVENTY '
    elif xa==71:
        mta='SEVENTY ONE'
    elif xa==72:
        mta='SEVENTY TWO'
    elif xa==73:
        mta='SEVENTY THREE'
    elif xa==74:
        mta='SEVENTY FOUR'
    elif xa==75:
        mta='SEVENTY FIVE'
    elif xa==76:
        mta='SEVENTY SIX'
    elif xa==77:
        mta='SEVENTY SEVEN'
    elif xa==78:
        mta='SEVENTY EIGHT'
    elif xa==79:
        mta='SEVENTY NINE'
    elif xa==80:
        mta='EIGHTY'
    elif xa==81:
        mta='EIGHTY ONE'
    elif xa==82:
        mta='EIGHTY TWO'
    elif xa==83:
        mta='EIGHTY THREE'
    elif xa==84:
        mta='EIGHTY FOUR'
    elif xa==85:
        mta='EIGHTY FIVE'
    elif xa==86:
        mta='EIGHTY SIX'
    elif xa==87:
        mta='EIGHTY SEVEN'
    elif xa==88:
        mta='EIGHTY EIGHT'
    elif xa==89:
        mta='EIGHTY NINE'
    elif xa==90:
        mta='NINTY'
    elif xa==91:
        mta='NINTY ONE'
    elif xa==92:
        mta='NINTY TWO'
    elif xa==93:
        mta='NINTY THREE'
    elif xa==94:
        mta='NINTY FOUR'
    elif xa==95:
        mta='NINTY FIVE'
    elif xa==96:
        mta='NINTY SIX'
    elif xa==97:
        mta='NINTY SEVEN'
    elif xa==98:
        mta='NINTY EIGHT'
    elif xa==99:
        mta='NINTY NINE'
    elif xa==100:
        mta='HUNDRED'
    if xb==0:
        mtb='ZERO'
    elif xb==1:
        mtb='ONE'
    elif xb==2:
        mtb='TWO'
    elif xb==3:
        mtb='THREE'
    elif xb==4:
        mtb='FOUR'
    elif xb==5:
        mtb='FIVE'
    elif xb==6:
        mtb='SIX'
    elif xb==7:
        mtb='SEVEN'
    elif xb==8:
        mtb='EIGHT'
    elif xb==9:
        mtb='NINE'
    elif xb==10:
        mtb='TEN'
    elif xb==11:
        mtb='ELEVEN'
    elif xb==12:
        mtb='TWELVE'
    elif xb==13:
        mtb='THIRTEEN'
    elif xb==14:
        mtb='FOURTEEN'
    elif xb==15:
        mtb='FIFTEEN'
    elif xb==16:
        mtb='SIXTEEN'
    elif xb==17:
        mtb='SEVENTEEN'
    elif xb==18:
        mtb='EIGHTEEN'
    elif xb==19:
        mtb='NINETEEN'
    elif xb==20:
        mtb='TWENTY'
    elif xb==21:
        mtb='TWENTY ONE'
    elif xb==22:
        mtb='TWENTY TWO'
    elif xb==23:
        mtb='TWENTY THREE'
    elif xb==24:
        mtb='TWENTY FOUR'
    elif xb==25:
        mtb='TWENTY FIVE'
    elif xb==26:
        mtb='TWENTY SIX'
    elif xb==27:
        mtb='TWENTY SEVEN'
    elif xb==28:
        mtb='TWENTY EIGHT'
    elif xb==29:
        mtb='TWENTY NINE'
    elif xb==30:
        mtb='THIRTY'
    elif xb==31:
        mtb='THIRTY ONE'
    elif xb==32:
        mtb='THIRTY TWO'
    elif xb==33:
        mtb='THIRTY THREE'
    elif xb==34:
        mtb='THIRTY FOUR'
    elif xb==35:
        mtb='THIRTY FIVE'
    elif xb==36:
        mtb='THIRTY SIX'
    elif xb==37:
        mtb='THIRTY SEVEN'
    elif xb==38:
        mtb='THIRTY EIGHT'
    elif xb==39:
        mtb='THIRTY NINE'
    elif xb==40:
        mtb='FORTY'
    elif xb==41:
        mtb='FORTY ONE'
    elif xb==42:
        mtb='FORTY TWO'
    elif xb==43:
        mtb='FORTY THREE'
    elif xb==44:
        mtb='FORTY FOUR'
    elif xb==45:
        mtb='FORTY FIVE'
    elif xb==46:
        mtb='FORTY SIX'
    elif xb==47:
        mtb='FORTY SEVEN'
    elif xb==48:
        mtb='FORTY EIGHT'
    elif xb==49:
        mtb='FORTY NINE'
    elif xb==50:
        mtb='SIXTY '
    elif xb==51:
        mtb='SIXTY ONE'
    elif xb==52:
        mtb='SIXTY TWO'
    elif xb==53:
        mtb='SIXTY THREE'
    elif xb==54:
        mtb='SIXTY FOUR'
    elif xb==55:
        mtb='SIXTY FIVE'
    elif xb==56:
        mtb='SIXTY SIX'
    elif xb==57:
        mtb='SIXTY SEVEN'
    elif xb==58:
        mtb='SIXTY EIGHT'
    elif xb==59:
        mtb='SIXTY NINE'
    elif xb==60:
        mtb='SIXTY TEN'
    elif xb==61:
        mtb='SIXTY ONE'
    elif xb==62:
        mtb='SIXTY TWO'
    elif xb==63:
        mtb='SIXTY THREE'
    elif xb==64:
        mtb='SIXTY FOUR'
    elif xb==65:
        mtb='SIXTY FIVE'
    elif xb==66:
        mtb='SIXTY SIX'
    elif xb==67:
        mtb='SIXTY SEVEN'
    elif xb==68:
        mtb='SIXTY EIGHT'
    elif xb==69:
        mtb='SIXTY NINE'
    elif xb==70:
        mtb='SEVENTY '
    elif xb==71:
        mtb='SEVENTY ONE'
    elif xb==72:
        mtb='SEVENTY TWO'
    elif xb==73:
        mtb='SEVENTY THREE'
    elif xb==74:
        mtb='SEVENTY FOUR'
    elif xb==75:
        mtb='SEVENTY FIVE'
    elif xb==76:
        mtb='SEVENTY SIX'
    elif xb==77:
        mtb='SEVENTY SEVEN'
    elif xb==78:
        mtb='SEVENTY EIGHT'
    elif xb==79:
        mtb='SEVENTY NINE'
    elif xb==80:
        mtb='EIGHTY'
    elif xb==81:
        mtb='EIGHTY ONE'
    elif xb==82:
        mtb='EIGHTY TWO'
    elif xb==83:
        mtb='EIGHTY THREE'
    elif xb==84:
        mtb='EIGHTY FOUR'
    elif xb==85:
        mtb='EIGHTY FIVE'
    elif xb==86:
        mtb='EIGHTY SIX'
    elif xb==87:
        mtb='EIGHTY SEVEN'
    elif xb==88:
        mtb='EIGHTY EIGHT'
    elif xb==89:
        mtb='EIGHTY NINE'
    elif xb==90:
        mtb='NINTY'
    elif xb==91:
        mtb='NINTY ONE'
    elif xb==92:
        mtb='NINTY TWO'
    elif xb==93:
        mtb='NINTY THREE'
    elif xb==94:
        mtb='NINTY FOUR'
    elif xb==95:
        mtb='NINTY FIVE'
    elif xb==96:
        mtb='NINTY SIX'
    elif xb==97:
        mtb='NINTY SEVEN'
    elif xb==98:
        mtb='NINTY EIGHT'
    elif xb==99:
        mtb='NINTY NINE'
    elif xb==100:
        mtb='HUNDRED'
    if xc==0:
        mtc='ZERO'
    elif xc==1:
        mtc='ONE'
    elif xc==2:
        mtc='TWO'
    elif xc==3:
        mtc='THREE'
    elif xc==4:
        mtc='FOUR'
    elif xc==5:
        mtc='FIVE'
    elif xc==6:
        mtc='SIX'
    elif xc==7:
        mtc='SEVEN'
    elif xc==8:
        mtc='EIGHT'
    elif xc==9:
        mtc='NINE'
    elif xc==10:
        mtc='TEN'
    elif xc==11:
        mtc='ELEVEN'
    elif xc==12:
        mtc='TWELVE'
    elif xc==13:
        mtc='THIRTEEN'
    elif xc==14:
        mtc='FOURTEEN'
    elif xc==15:
        mtc='FIFTEEN'
    elif xc==16:
        mtc='SIXTEEN'
    elif xc==17:
        mtc='SEVENTEEN'
    elif xc==18:
        mtc='EIGHTEEN'
    elif xc==19:
        mtc='NINETEEN'
    elif xc==20:
        mtc='TWENTY'
    elif xc==21:
        mtc='TWENTY ONE'
    elif xc==22:
        mtc='TWENTY TWO'
    elif xc==23:
        mtc='TWENTY THREE'
    elif xc==24:
        mtc='TWENTY FOUR'
    elif xc==25:
        mtc='TWENTY FIVE'
    elif xc==26:
        mtc='TWENTY SIX'
    elif xc==27:
        mtc='TWENTY SEVEN'
    elif xc==28:
        mtc='TWENTY EIGHT'
    elif xc==29:
        mtc='TWENTY NINE'
    elif xc==30:
        mtc='THIRTY'
    elif xc==31:
        mtc='THIRTY ONE'
    elif xc==32:
        mtc='THIRTY TWO'
    elif xc==33:
        mtc='THIRTY THREE'
    elif xc==34:
        mtc='THIRTY FOUR'
    elif xc==35:
        mtc='THIRTY FIVE'
    elif xc==36:
        mtc='THIRTY SIX'
    elif xc==37:
        mtc='THIRTY SEVEN'
    elif xc==38:
        mtc='THIRTY EIGHT'
    elif xc==39:
        mtc='THIRTY NINE'
    elif xc==40:
        mtc='FORTY'
    elif xc==41:
        mtc='FORTY ONE'
    elif xc==42:
        mtc='FORTY TWO'
    elif xc==43:
        mtc='FORTY THREE'
    elif xc==44:
        mtc='FORTY FOUR'
    elif xc==45:
        mtc='FORTY FIVE'
    elif xc==46:
        mtc='FORTY SIX'
    elif xc==47:
        mtc='FORTY SEVEN'
    elif xc==48:
        mtc='FORTY EIGHT'
    elif xc==49:
        mtc='FORTY NINE'
    elif xc==50:
        mtc='FIFTY '
    elif xc==51:
        mtc='FIFTY ONE'
    elif xc==52:
        mtc='FIFTY TWO'
    elif xc==53:
        mtc='FIFTY THREE'
    elif xc==54:
        mtc='SIXTY FOUR'
    elif xc==55:
        mtc='SIXTY FIVE'
    elif xc==56:
        mtc='SIXTY SIX'
    elif xc==57:
        mtc='SIXTY SEVEN'
    elif xc==58:
        mtc='SIXTY EIGHT'
    elif xc==59:
        mtc='SIXTY NINE'
    elif xc==60:
        mtc='SIXTY TEN'
    elif xc==61:
        mtc='SIXTY ONE'
    elif xc==62:
        mtc='SIXTY TWO'
    elif xc==63:
        mtc='SIXTY THREE'
    elif xc==64:
        mtc='SIXTY FOUR'
    elif xc==65:
        mtc='SIXTY FIVE'
    elif xc==66:
        mtc='SIXTY SIX'
    elif xc==67:
        mtc='SIXTY SEVEN'
    elif xc==68:
        mtc='SIXTY EIGHT'
    elif xc==69:
        mtc='SIXTY NINE'
    elif xc==70:
        mtc='SEVENTY '
    elif xc==71:
        mtc='SEVENTY ONE'
    elif xc==72:
        mtc='SEVENTY TWO'
    elif xc==73:
        mtc='SEVENTY THREE'
    elif xc==74:
        mtc='SEVENTY FOUR'
    elif xc==75:
        mtc='SEVENTY FIVE'
    elif xc==76:
        mtc='SEVENTY SIX'
    elif xc==77:
        mtc='SEVENTY SEVEN'
    elif xc==78:
        mtc='SEVENTY EIGHT'
    elif xc==79:
        mtc='SEVENTY NINE'
    elif xc==80:
        mtc='EIGHTY'
    elif xc==81:
        mtc='EIGHTY ONE'
    elif xc==82:
        mtc='EIGHTY TWO'
    elif xc==83:
        mtc='EIGHTY THREE'
    elif xc==84:
        mtc='EIGHTY FOUR'
    elif xc==85:
        mtc='EIGHTY FIVE'
    elif xc==86:
        mtc='EIGHTY SIX'
    elif xc==87:
        mtc='EIGHTY SEVEN'
    elif xc==88:
        mtc='EIGHTY EIGHT'
    elif xc==89:
        mtc='EIGHTY NINE'
    elif xc==90:
        mtc='NINTY'
    elif xc==91:
        mtc='NINTY ONE'
    elif xc==92:
        mtc='NINTY TWO'
    elif xc==93:
        mtc='NINTY THREE'
    elif xc==94:
        mtc='NINTY FOUR'
    elif xc==95:
        mtc='NINTY FIVE'
    elif xc==96:
        mtc='NINTY SIX'
    elif xc==97:
        mtc='NINTY SEVEN'
    elif xc==98:
        mtc='NINTY EIGHT'
    elif xc==99:
        mtc='NINTY NINE'
    elif xc==100:
        mtc='HUNDRED'
    if xp==0:
        mtp='ZERO'
    elif xp==1:
        mtp='ONE'
    elif xp==2:
        mtp='TWO'
    elif xp==3:
        mtp='THREE'
    elif xp==4:
        mtp='FOUR'
    elif xp==5:
        mtp='FIVE'
    elif xp==6:
        mtp='SIX'
    elif xp==7:
        mtp='SEVEN'
    elif xp==8:
        mtp='EIGHT'
    elif xp==9:
        mtp='NINE'
    elif xp==10:
        mtp='TEN'
    elif xp==11:
        mtp='ELEVEN'
    elif xp==12:
        mtp='TWELVE'
    elif xp==13:
        mtp='THIRTEEN'
    elif xp==14:
        mtp='FOURTEEN'
    elif xp==15:
        mtp='FIFTEEN'
    elif xp==16:
        mtp='SIXTEEN'
    elif xp==17:
        mtp='SEVENTEEN'
    elif xp==18:
        mtp='EIGHTEEN'
    elif xp==19:
        mtp='NINETEEN'
    elif xp==20:
        mtp='TWENTY'
    elif xp==21:
        mtp='TWENTY ONE'
    elif xp==22:
        mtp='TWENTY TWO'
    elif xp==23:
        mtp='TWENTY THREE'
    elif xp==24:
        mtp='TWENTY FOUR'
    elif xp==25:
        mtp='TWENTY FIVE'
    elif xp==26:
        mtp='TWENTY SIX'
    elif xp==27:
        mtp='TWENTY SEVEN'
    elif xp==28:
        mtp='TWENTY EIGHT'
    elif xp==29:
        mtp='TWENTY NINE'
    elif xp==30:
        mtp='THIRTY'
    elif xp==31:
        mtp='THIRTY ONE'
    elif xp==32:
        mtp='THIRTY TWO'
    elif xp==33:
        mtp='THIRTY THREE'
    elif xp==34:
        mtp='THIRTY FOUR'
    elif xp==35:
        mtp='THIRTY FIVE'
    elif xp==36:
        mtp='THIRTY SIX'
    elif xp==37:
        mtp='THIRTY SEVEN'
    elif xp==38:
        mtp='THIRTY EIGHT'
    elif xp==39:
        mtp='THIRTY NINE'
    elif xp==40:
        mtp='FORTY'
    elif xp==41:
        mtp='FORTY ONE'
    elif xp==42:
        mtp='FORTY TWO'
    elif xp==43:
        mtp='FORTY THREE'
    elif xp==44:
        mtp='FORTY FOUR'
    elif xp==45:
        mtp='FORTY FIVE'
    elif xp==46:
        mtp='FORTY SIX'
    elif xp==47:
        mtp='FORTY SEVEN'
    elif xp==48:
        mtp='FORTY EIGHT'
    elif xp==49:
        mtp='FORTY NINE'
    elif xp==50:
        mtp='SIXTY '
    elif xp==51:
        mtp='SIXTY ONE'
    elif xp==52:
        mtp='SIXTY TWO'
    elif xp==53:
        mtp='SIXTY THREE'
    elif xp==54:
        mtp='SIXTY FOUR'
    elif xp==55:
        mtp='SIXTY FIVE'
    elif xp==56:
        mtp='SIXTY SIX'
    elif xp==57:
        mtp='SIXTY SEVEN'
    elif xp==58:
        mtp='SIXTY EIGHT'
    elif xp==59:
        mtp='SIXTY NINE'
    elif xp==60:
        mtp='SIXTY TEN'
    elif xp==61:
        mtp='SIXTY ONE'
    elif xp==62:
        mtp='SIXTY TWO'
    elif xp==63:
        mtp='SIXTY THREE'
    elif xp==64:
        mtp='SIXTY FOUR'
    elif xp==65:
        mtp='SIXTY FIVE'
    elif xp==66:
        mtp='SIXTY SIX'
    elif xp==67:
        mtp='SIXTY SEVEN'
    elif xp==68:
        mtp='SIXTY EIGHT'
    elif xp==69:
        mtp='SIXTY NINE'
    elif xp==70:
        mtp='SEVENTY '
    elif xp==71:
        mtp='SEVENTY ONE'
    elif xp==72:
        mtp='SEVENTY TWO'
    elif xp==73:
        mtp='SEVENTY THREE'
    elif xp==74:
        mtp='SEVENTY FOUR'
    elif xp==75:
        mtp='SEVENTY FIVE'
    elif xp==76:
        mtp='SEVENTY SIX'
    elif xp==77:
        mtp='SEVENTY SEVEN'
    elif xp==78:
        mtp='SEVENTY EIGHT'
    elif xp==79:
        mtp='SEVENTY NINE'
    elif xp==80:
        mtp='EIGHTY'
    elif xp==81:
        mtp='EIGHTY ONE'
    elif xp==82:
        mtp='EIGHTY TWO'
    elif xp==83:
        mtp='EIGHTY THREE'
    elif xp==84:
        mtp='EIGHTY FOUR'
    elif xp==85:
        mtp='EIGHTY FIVE'
    elif xp==86:
        mtp='EIGHTY SIX'
    elif xp==87:
        mtp='EIGHTY SEVEN'
    elif xp==88:
        mtp='EIGHTY EIGHT'
    elif xp==89:
        mtp='EIGHTY NINE'
    elif xp==90:
        mtp='NINTY'
    elif xp==91:
        mtp='NINTY ONE'
    elif xp==92:
        mtp='NINTY TWO'
    elif xp==93:
        mtp='NINTY THREE'
    elif xp==94:
        mtp='NINTY FOUR'
    elif xp==95:
        mtp='NINTY FIVE'
    elif xp==96:
        mtp='NINTY SIX'
    elif xp==97:
        mtp='NINTY SEVEN'
    elif xp==98:
        mtp='NINTY EIGHT'
    elif xp==99:
        mtp='NINTY NINE'
    elif xp==100:
        mtp='HUNDRED'
    if xo==0:
        mto='ZERO'
    elif xo==1:
        mto='ONE'
    elif xo==2:
        mto='TWO'
    elif xo==3:
        mto='THREE'
    elif xo==4:
        mto='FOUR'
    elif xo==5:
        mto='FIVE'
    elif xo==6:
        mto='SIX'
    elif xo==7:
        mto='SEVEN'
    elif xo==8:
        mto='EIGHT'
    elif xo==9:
        mto='NINE'
    elif xo==10:
        mto='TEN'
    elif xo==11:
        mto='ELEVEN'
    elif xo==12:
        mto='TWELVE'
    elif xo==13:
        mto='THIRTEEN'
    elif xo==14:
        mto='FOURTEEN'
    elif xo==15:
        mto='FIFTEEN'
    elif xo==16:
        mto='SIXTEEN'
    elif xo==17:
        mto='SEVENTEEN'
    elif xo==18:
        mto='EIGHTEEN'
    elif xo==19:
        mto='NINETEEN'
    elif xo==20:
        mto='TWENTY'
    elif xo==21:
        mto='TWENTY ONE'
    elif xo==22:
        mto='TWENTY TWO'
    elif xo==23:
        mto='TWENTY THREE'
    elif xo==24:
        mto='TWENTY FOUR'
    elif xo==25:
        mto='TWENTY FIVE'
    elif xo==26:
        mto='TWENTY SIX'
    elif xo==27:
        mto='TWENTY SEVEN'
    elif xo==28:
        mto='TWENTY EIGHT'
    elif xo==29:
        mto='TWENTY NINE'
    elif xo==30:
        mto='THIRTY'
    elif xo==31:
        mto='THIRTY ONE'
    elif xo==32:
        mto='THIRTY TWO'
    elif xo==33:
        mto='THIRTY THREE'
    elif xo==34:
        mto='THIRTY FOUR'
    elif xo==35:
        mto='THIRTY FIVE'
    elif xo==36:
        mto='THIRTY SIX'
    elif xo==37:
        mto='THIRTY SEVEN'
    elif xo==38:
        mto='THIRTY EIGHT'
    elif xo==39:
        mto='THIRTY NINE'
    elif xo==40:
        mto='FORTY'
    elif xo==41:
        mto='FORTY ONE'
    elif xo==42:
        mto='FORTY TWO'
    elif xo==43:
        mto='FORTY THREE'
    elif xo==44:
        mto='FORTY FOUR'
    elif xo==45:
        mto='FORTY FIVE'
    elif xo==46:
        mto='FORTY SIX'
    elif xo==47:
        mto='FORTY SEVEN'
    elif xo==48:
        mto='FORTY EIGHT'
    elif xo==49:
        mto='FORTY NINE'
    elif xo==50:
        mto='SIXTY '
    elif xo==51:
        mto='SIXTY ONE'
    elif xo==52:
        mto='SIXTY TWO'
    elif xo==53:
        mto='SIXTY THREE'
    elif xo==54:
        mto='SIXTY FOUR'
    elif xo==55:
        mto='SIXTY FIVE'
    elif xo==56:
        mto='SIXTY SIX'
    elif xo==57:
        mto='SIXTY SEVEN'
    elif xo==58:
        mto='SIXTY EIGHT'
    elif xo==59:
        mto='SIXTY NINE'
    elif xo==60:
        mto='SIXTY TEN'
    elif xo==61:
        mto='SIXTY ONE'
    elif xo==62:
        mto='SIXTY TWO'
    elif xo==63:
        mto='SIXTY THREE'
    elif xo==64:
        mto='SIXTY FOUR'
    elif xo==65:
        mto='SIXTY FIVE'
    elif xo==66:
        mto='SIXTY SIX'
    elif xo==67:
        mto='SIXTY SEVEN'
    elif xo==68:
        mto='SIXTY EIGHT'
    elif xo==69:
        mto='SIXTY NINE'
    elif xo==70:
        mto='SEVENTY '
    elif xo==71:
        mto='SEVENTY ONE'
    elif xo==72:
        mto='SEVENTY TWO'
    elif xo==73:
        mto='SEVENTY THREE'
    elif xo==74:
        mto='SEVENTY FOUR'
    elif xo==75:
        mto='SEVENTY FIVE'
    elif xo==76:
        mto='SEVENTY SIX'
    elif xo==77:
        mto='SEVENTY SEVEN'
    elif xo==78:
        mto='SEVENTY EIGHT'
    elif xo==79:
        mto='SEVENTY NINE'
    elif xo==80:
        mto='EIGHTY'
    elif xo==81:
        mto='EIGHTY ONE'
    elif xo==82:
        mto='EIGHTY TWO'
    elif xo==83:
        mto='EIGHTY THREE'
    elif xo==84:
        mto='EIGHTY FOUR'
    elif xo==85:
        mto='EIGHTY FIVE'
    elif xo==86:
        mto='EIGHTY SIX'
    elif xo==87:
        mto='EIGHTY SEVEN'
    elif xo==88:
        mto='EIGHTY EIGHT'
    elif xo==89:
        mto='EIGHTY NINE'
    elif xo==90:
        mto='NINTY'
    elif xo==91:
        mto='NINTY ONE'
    elif xo==92:
        mto='NINTY TWO'
    elif xo==93:
        mto='NINTY THREE'
    elif xo==94:
        mto='NINTY FOUR'
    elif xo==95:
        mto='NINTY FIVE'
    elif xo==96:
        mto='NINTY SIX'
    elif xo==97:
        mto='NINTY SEVEN'
    elif xo==98:
        mto='NINTY EIGHT'
    elif xo==99:
        mto='NINTY NINE'
    elif xo==100:
        mto='HUNDRED'
    ways()
def pof():
    print("you")
    global pf
    if ga=="E1" or ga=="E2" or gb=="E1" or gb=="E2" or gc=="E1" or gc=="E2" or gp=="E1" or gp=="E2" or go=="E1" or go=="E2":
        pf="FAIL"
    else:
        pf="PASS"
    marks_text()
def grade():
    print("thank")
    global ga
    global gb
    global gc
    global gp
    global go
    if xa>90 and xa<101:
        ga="A1"
    elif xa>80 and xa<91:
        ga="A2"
    elif xa>70 and xa<81:
        ga="B1"
    elif xa>60 and xa<71:
        ga="B2"
    elif xa>50 and xa<61:
        ga="C1"
    elif xa>40 and xa<51:
        ga="C2"
    elif xa>32 and xa<41:
        ga="D"
    elif xa>20 and xa<33:
        ga="E1"
    elif xa>=0 and xa<21:
        ga="E2"
    else:
        q=0
    if xb>90 and xb<101:
        gb="A1"
    elif xb>80 and xb<91:
        gb="A2"
    elif xb>70 and xb<81:
        gb="B1"
    elif xb>60 and xb<71:
        gb="B2"
    elif xb>50 and xb<61:
        gb="C1"
    elif xb>40 and xb<51:
        gb="C2"
    elif xb>32 and xb<41:
        gb="D"
    elif xb>20 and xb<33:
        gb="E1"
    elif xb>=0 and xb<21:
        gb="E2"
    else:
        q=0
    if xc>90 and xc<101:
        gc="A1"
    elif xc>80 and xc<91:
        gc="A2"
    elif xc>70 and xc<81:
        gc="B1"
    elif xc>60 and xc<71:
        gc="B2"
    elif xc>50 and xc<61:
        gc="C1"
    elif xc>40 and xc<51:
        gc="C2"
    elif xc>32 and xc<41:
        gc="D"
    elif xc>20 and xc<33:
        gc="E1"
    elif xc>=0 and xc<21:
        gc="E2"
    else:
        q=0
    if xp>90 and xp<101:
        gp="A1"
    elif xp>80 and xp<91:
        gp="A2"
    elif xp>70 and xp<81:
        gp="B1"
    elif xp>60 and xp<71:
        gp="B2"
    elif xp>50 and xp<61:
        gp="C1"
    elif xp>40 and xp<51:
        gp="C2"
    elif xp>32 and xp<41:
        gp="D"
    elif xp>20 and xp<33:
        gp="E1"
    elif xp>=0 and xp<21:
        gp="E2"
    else:
        q=0
    if xo>90 and xo<101:
        go="A1"
    elif xo>80 and xo<91:
        go="A2"
    elif xo>70 and xo<81:
        go="B1"
    elif xo>60 and xo<71:
        go="B2"
    elif xo>50 and xo<61:
        go="C1"
    elif xo>40 and xo<51:
        go="C2"
    elif xo>32 and xo<41:
        go="D"
    elif xo>20 and xo<33:
        go="E1"
    elif xo>=0 and xo<21:
        go="E2"
    else:
        q=0
    pof()
def entry_check1():
    global way
    global ta
    global tb
    global tc
    global tp
    global to
    global pa
    global pb
    global pc
    global pp
    global po
    global xa
    global xb
    global xc
    global xp
    global xo
    way='science'
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
    xa=int(ta)+int(pa)
    xb=int(tb)+int(pb)
    xc=int(tc)+int(pc)
    xp=int(tp)+int(pp)
    xo=int(to)+int(po)
    if len(ta)==0 or len(tb)==0 or len(tc)==0 or len(tp)==0 or len(to)==0 or len(pa)==0 or len(pb)==0 or len(pc)==0 or len(pp)==0 or len(po)==0:
        l1=Label(science_window,text="                                   ",font=('arial',10,'bold'))
        l2=Label(science_window,text="            Fill all boxes         ",fg='red',bg='pink',font=('arial',10,'bold'))
        c2.create_window(150,560,window=l1)
        c2.create_window(150,560,window=l2)
    elif int(tb)>70 or int(tc)>70 or int(to)>70 or int(ta)<0 or int(tb)<0 or int(tc)<0 or int(tp)<0 or int(to)<0 or int(ta)>80 or int(tp)>80 or int(pa)>20 or int(pp)>20 or int(pb)>30 or int(pc)>30 or int(po)>30 or int(pa)<0 or int(pb)<0 or int(pc)<0 or int(pp)<0 or int(po)<0:
        l1=Label(science_window,text="                                    ",font=('arial',10,'bold'))
        l2=Label(science_window,text="              Wrong input           ",fg='red',bg='pink',font=('arial',10,'bold'))
        c2.create_window(150,560,window=l1)
        c2.create_window(150,560,window=l2)
    else:
        grade()
def entry_check2():
    global way
    global ta
    global tb
    global tc
    global tp
    global to
    global pa
    global pb
    global pc
    global pp
    global po
    global xa
    global xb
    global xc
    global xp
    global xo
    print('entry')
    way='commerce'
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
    xa=int(ta)+int(pa)
    xb=int(tb)+int(pb)
    xc=int(tc)+int(pc)
    xp=int(tp)+int(pp)
    xo=int(to)+int(po)
    if ta=='' or tb=='' or tc=='' or tp=='' or to=='' or pa=='' or pb=='' or pc=='' or pp=='' or po=='':
        l1=Label(commerce_window,text="                                   ",font=('arial',10,'bold'))
        l2=Label(commerce_window,text="            Fill all boxes         ",fg='red',bg='pink',font=('arial',10,'bold'))
        c2.create_window(150,560,window=l1)
        c2.create_window(150,560,window=l2)
    elif int(tb)>70 or int(tc)>70 or int(to)>70 or int(ta)<=0 or int(tb)<=0 or int(tc)<=0 or int(tp)<=0 or int(to)<=0 or int(ta)>80 or int(tp)>80 or int(pa)>20 or int(pp)>20 or int(pb)>30 or int(pc)>30 or int(po)>30 or int(pa)<=0 or int(pb)<=0 or int(pc)<=0 or int(pp)<=0 or int(po)<=0:
        l1=Label(commerce_window,text="                                    ",font=('arial',10,'bold'))
        l2=Label(commerce_window,text="              Wrong input           ",fg='red',bg='pink',font=('arial',10,'bold'))
        c2.create_window(150,560,window=l1)
        c2.create_window(150,560,window=l2)
    else:
        grade()
def entry_check3():
    global way
    global ta
    global tb
    global tc
    global tp
    global to
    global pa
    global pb
    global pc
    global pp
    global po
    global xa
    global xb
    global xc
    global xp
    global xo
    way='art'
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
    xa=int(ta)+int(pa)
    xb=int(tb)+int(pb)
    xc=int(tc)+int(pc)
    xp=int(tp)+int(pp)
    xo=int(to)+int(po)
    if ta=='' or tb=='' or tc=='' or tp=='' or to=='' or pa=='' or pb=='' or pc=='' or pp=='' or po=='':
        l1=Label(art_window,text="                                   ",font=('arial',10,'bold'))
        l2=Label(art_window,text="            Fill all boxes         ",fg='red',bg='pink',font=('arial',10,'bold'))
        c2.create_window(150,560,window=l1)
        c2.create_window(150,560,window=l2)
    elif int(tb)>70 or int(tc)>70 or int(to)>70 or int(ta)<=0 or int(tb)<=0 or int(tc)<=0 or int(tp)<=0 or int(to)<=0 or int(ta)>80 or int(tp)>80 or int(pa)>20 or int(pp)>20 or int(pb)>30 or int(pc)>30 or int(po)>30 or int(pa)<=0 or int(pb)<=0 or int(pc)<=0 or int(pp)<=0 or int(po)<=0:
        l1=Label(art_window,text="                                    ",font=('arial',10,'bold'))
        l2=Label(art_window,text="              Wrong input           ",fg='red',bg='pink',font=('arial',10,'bold'))
        c2.create_window(150,560,window=l1)
        c2.create_window(150,560,window=l2) 
    else:
        grade()
def scics():
    global omarks
    global omarkss
    global opt
    global co
    co="083"
    opt="COMPUTER SCIENCE"
    l1=Label(science_window,text="    C.S.    ",font=('arial',24,'bold'),bg='orange')
    omarks=Entry(science_window,width=8,font=('arial',20,'bold'),fg='black',border=3)
    omarkss=Entry(science_window,width=8,font=('arial',20,'bold'),fg='black',border=3)
    l11=Label(science_window,text='/70',font=('arial',20,'bold'),bg='orange')
    l21=Label(science_window,text='/30',font=('arial',20,'bold'),bg='orange')
    c2.create_window(285,500,window=l11)
    c3.create_window(285,500,window=l21)
    c1.create_window(200,500,window=l1)
    c2.create_window(200,500,window=omarks)
    c3.create_window(200,500,window=omarkss)
def commcs():
    global omarks
    global omarkss
    global opt
    global co
    co="083"
    opt="COMPUTER SCIENCE"
    l1=Label(commerce_window,text="      C.S.       ",font=('arial',24,'bold'),bg='orange')
    omarks=Entry(commerce_window,width=8,font=('arial',20,'bold'),fg='black',border=3)
    omarkss=Entry(commerce_window,width=8,font=('arial',20,'bold'),fg='black',border=3)
    l11=Label(commerce_window,text='/70',font=('arial',20,'bold'),bg='orange')
    l21=Label(commerce_window,text='/30',font=('arial',20,'bold'),bg='orange')
    c2.create_window(285,500,window=l11)
    c3.create_window(285,500,window=l21)
    c1.create_window(200,500,window=l1)
    c2.create_window(200,500,window=omarks)
    c3.create_window(200,500,window=omarkss)
def artcs():
    global omarks
    global omarkss
    global opt
    opt="COMPUTER SCIENCE"
    global co
    co="083"
    l1=Label(art_window,text="               C.S.           ",font=('arial',24,'bold'),bg='orange')
    omarks=Entry(art_window,width=8,font=('arial',20,'bold'),fg='black',border=3)
    omarkss=Entry(art_window,width=8,font=('arial',20,'bold'),fg='black',border=3)
    l11=Label(art_window,text='/70',font=('arial',20,'bold'),bg='orange')
    l21=Label(art_window,text='/30',font=('arial',20,'bold'),bg='orange')
    c2.create_window(285,500,window=l11)
    c3.create_window(285,500,window=l21)
    c1.create_window(200,500,window=l1)
    c2.create_window(200,500,window=omarks)
    c3.create_window(200,500,window=omarkss)
def sciped():
    global omarks
    global omarkss
    global opt
    opt="PHYSICAL EDUCATION"
    global co
    co="048"
    l1=Label(science_window,text="   P.Ed      ",font=('arial',24,'bold'),bg='orange')
    omarks=Entry(science_window,width=8,font=('arial',20,'bold'),fg='black',border=3)
    omarkss=Entry(science_window,width=8,font=('arial',20,'bold'),fg='black',border=3)
    l11=Label(science_window,text='/70',font=('arial',20,'bold'),bg='orange')
    l21=Label(science_window,text='/30',font=('arial',20,'bold'),bg='orange')
    c2.create_window(285,500,window=l11)
    c3.create_window(285,500,window=l21)
    c1.create_window(200,500,window=l1)
    c2.create_window(200,500,window=omarks)
    c3.create_window(200,500,window=omarkss)
def artpsycho():
    global omarks
    global omarkss
    global opt
    opt="PSYCHOLOGY"
    global co
    co="037"
    l1=Label(art_window,text=" Psychology  ",font=('arial',24,'bold'),bg='orange')
    omarks=Entry(art_window,width=8,font=('arial',20,'bold'),fg='black',border=3)
    omarkss=Entry(art_window,width=8,font=('arial',20,'bold'),fg='black',border=3)
    l11=Label(art_window,text='/70',font=('arial',20,'bold'),bg='orange')
    l21=Label(art_window,text='/30',font=('arial',20,'bold'),bg='orange')
    c2.create_window(285,500,window=l11)
    c3.create_window(285,500,window=l21)
    c1.create_window(200,500,window=l1)
    c2.create_window(200,500,window=omarks)
    c3.create_window(200,500,window=omarkss)
def commpsycho():
    global omarks
    global omarkss
    global opt
    opt="PSYCHOLOGY"
    global co
    co="037"
    l1=Label(commerce_window,text=" Psychology  ",font=('arial',24,'bold'),bg='orange')
    omarks=Entry(commerce_window,width=8,font=('arial',20,'bold'),fg='black',border=3)
    omarkss=Entry(commerce_window,width=8,font=('arial',20,'bold'),fg='black',border=3)
    l11=Label(commerce_window,text='/70',font=('arial',20,'bold'),bg='orange')
    l21=Label(commerce_window,text='/30',font=('arial',20,'bold'),bg='orange')
    c2.create_window(285,500,window=l11)
    c3.create_window(285,500,window=l21)
    c1.create_window(200,500,window=l1)
    c2.create_window(200,500,window=omarks)
    c3.create_window(200,500,window=omarkss)
def commped():
    global omarks
    global omarkss
    global opt
    opt="PHYSICAL EDUCATION"
    global co
    co="048"
    l1=Label(commerce_window,text="      P.Ed      ",font=('arial',24,'bold'),bg='orange')
    omarks=Entry(commerce_window,width=8,font=('arial',20,'bold'),fg='black',border=3)
    omarkss=Entry(commerce_window,width=8,font=('arial',20,'bold'),fg='black',border=3)
    l11=Label(commerce_window,text='/70',font=('arial',20,'bold'),bg='orange')
    l21=Label(commerce_window,text='/30',font=('arial',20,'bold'),bg='orange')
    c2.create_window(285,500,window=l11)
    c3.create_window(285,500,window=l21)
    c1.create_window(200,500,window=l1)
    c2.create_window(200,500,window=omarks)
    c3.create_window(200,500,window=omarkss)
def scimusic():
    global omarks
    global omarkss
    global opt
    opt="MUSIC"
    global co
    co="034"
    l1=Label(science_window,text="Music    ",font=('arial',24,'bold'),bg='orange')
    omarks=Entry(science_window,width=8,font=('arial',20,'bold'),fg='black',border=3)
    omarkss=Entry(science_window,width=8,font=('arial',20,'bold'),fg='black',border=3)
    l11=Label(science_window,text='/70',font=('arial',20,'bold'),bg='orange')
    l21=Label(science_window,text='/30',font=('arial',20,'bold'),bg='orange')
    c2.create_window(285,500,window=l11)
    c3.create_window(285,500,window=l21)
    c1.create_window(200,500,window=l1)
    c2.create_window(200,500,window=omarks)
    c3.create_window(200,500,window=omarkss)
def commmusic():
    global omarks
    global omarkss
    global opt
    opt="MUSIC"
    global co
    co="034"
    l1=Label(commerce_window,text="      Music      ",font=('arial',24,'bold'),bg='orange')
    omarks=Entry(commerce_window,width=8,font=('arial',20,'bold'),fg='black',border=3)
    omarkss=Entry(commerce_window,width=8,font=('arial',20,'bold'),fg='black',border=3)
    l11=Label(commerce_window,text='/70',font=('arial',20,'bold'),bg='orange')
    l21=Label(commerce_window,text='/30',font=('arial',20,'bold'),bg='orange')
    c2.create_window(285,500,window=l11)
    c3.create_window(285,500,window=l21)
    c1.create_window(200,500,window=l1)
    c2.create_window(200,500,window=omarks)
    c3.create_window(200,500,window=omarkss)
def artmusic():
    global omarks
    global omarkss
    global opt
    opt="MUSIC"
    global co
    co="034"
    l1=Label(art_window,text="     Music     ",font=('arial',24,'bold'),bg='orange')
    omarks=Entry(art_window,width=8,font=('arial',20,'bold'),fg='black',border=3)
    omarkss=Entry(art_window,width=8,font=('arial',20,'bold'),fg='black',border=3)
    l11=Label(art_window,text='/70',font=('arial',20,'bold'),bg='orange')
    l21=Label(art_window,text='/30',font=('arial',20,'bold'),bg='orange')
    c2.create_window(285,500,window=l11)
    c3.create_window(285,500,window=l21)
    c1.create_window(200,500,window=l1)
    c2.create_window(200,500,window=omarks)
    c3.create_window(200,500,window=omarkss)
def scihindi():
    global omarks
    global omarkss
    global opt
    opt="HINDI COURSE A"
    global co
    co="302"
    l1=Label(science_window,text="Hindi     ",font=('arial',24,'bold'),bg='orange')
    omarks=Entry(science_window,width=8,font=('arial',20,'bold'),fg='black',border=3)
    omarkss=Entry(science_window,width=8,font=('arial',20,'bold'),fg='black',border=3)
    l11=Label(science_window,text='/70',font=('arial',20,'bold'),bg='orange')
    l21=Label(science_window,text='/30',font=('arial',20,'bold'),bg='orange')
    c2.create_window(285,500,window=l11)
    c3.create_window(285,500,window=l21)
    c1.create_window(200,500,window=l1)
    c2.create_window(200,500,window=omarks)
    c3.create_window(200,500,window=omarkss)
def commhindi():
    global omarks
    global omarkss
    global opt
    opt="HINDI COURSE A"
    global co
    co="302"
    l1=Label(commerce_window,text="      Hindi      ",font=('arial',24,'bold'),bg='orange')
    omarks=Entry(commerce_window,width=8,font=('arial',20,'bold'),fg='black',border=3)
    omarkss=Entry(commerce_window,width=8,font=('arial',20,'bold'),fg='black',border=3)
    l11=Label(commerce_window,text='/70',font=('arial',20,'bold'),bg='orange')
    l21=Label(commerce_window,text='/30',font=('arial',20,'bold'),bg='orange')
    c2.create_window(285,500,window=l11)
    c3.create_window(285,500,window=l21)
    c1.create_window(200,500,window=l1)
    c2.create_window(200,500,window=omarks)
    c3.create_window(200,500,window=omarkss)
def arthindi():
    global omarks
    global omarkss
    global opt
    opt="HINDI COURSE A"
    global co
    co="302"
    l1=Label(art_window,text="          Hindi       ",font=('arial',24,'bold'),bg='orange')
    omarks=Entry(art_window,width=8,font=('arial',20,'bold'),fg='black',border=3)
    omarkss=Entry(art_window,width=8,font=('arial',20,'bold'),fg='black',border=3)
    l11=Label(art_window,text='/70',font=('arial',20,'bold'),bg='orange')
    l21=Label(art_window,text='/30',font=('arial',20,'bold'),bg='orange')
    c2.create_window(285,500,window=l11)
    c3.create_window(285,500,window=l21)
    c1.create_window(200,500,window=l1)
    c2.create_window(200,500,window=omarks)
    c3.create_window(200,500,window=omarkss)
def scimaths():
    global pmarks
    global pmarkss
    global pname
    pname="MATHEMATICS"
    global cp
    cp="041"
    l1=Label(science_window,text="Maths    ",font=('arial',24,'bold'),bg='orange')
    pmarks=Entry(science_window,width=8,font=('arial',20,'bold'),fg='black',border=3)
    pmarkss=Entry(science_window,width=8,font=('arial',20,'bold'),fg='black',border=3)
    l11=Label(science_window,text='/80',font=('arial',20,'bold'),bg='orange')
    l21=Label(science_window,text='/20',font=('arial',20,'bold'),bg='orange')
    c2.create_window(285,350,window=l11)
    c3.create_window(285,350,window=l21)
    c1.create_window(200,350,window=l1)
    c2.create_window(200,350,window=pmarks)
    c3.create_window(200,350,window=pmarkss)
def arteco():
    global pmarks
    global pmarkss
    global pname
    pname="ECONOMICS"
    global cp
    cp="030"
    l1=Label(art_window,text="Economics  ",font=('arial',24,'bold'),bg='orange')
    pmarks=Entry(art_window,width=8,font=('arial',20,'bold'),fg='black',border=3)
    pmarkss=Entry(art_window,width=8,font=('arial',20,'bold'),fg='black',border=3)
    l11=Label(art_window,text='/80',font=('arial',20,'bold'),bg='orange')
    l21=Label(art_window,text='/20',font=('arial',20,'bold'),bg='orange')
    c2.create_window(285,350,window=l11)
    c3.create_window(285,350,window=l21)
    c1.create_window(200,350,window=l1)
    c2.create_window(200,350,window=pmarks)
    c3.create_window(200,350,window=pmarkss)
def artsocial():
    global pmarks
    global pmarkss
    global pname
    pname="SOCIALOGY"
    global cp
    cp="039"
    l1=Label(art_window,text="Socialogy   ",font=('arial',24,'bold'),bg='orange')
    pmarks=Entry(art_window,width=8,font=('arial',20,'bold'),fg='black',border=3)
    pmarkss=Entry(art_window,width=8,font=('arial',20,'bold'),fg='black',border=3)
    l11=Label(art_window,text='/80',font=('arial',20,'bold'),bg='orange')
    l21=Label(art_window,text='/20',font=('arial',20,'bold'),bg='orange')
    c2.create_window(285,350,window=l11)
    c3.create_window(285,350,window=l21)
    c1.create_window(200,350,window=l1)
    c2.create_window(200,350,window=pmarks)
    c3.create_window(200,350,window=pmarkss)
def commmaths():
    global omarks
    global omarkss
    global opt
    opt="MATHEMATICS"
    global co
    co="041"
    l1=Label(commerce_window,text="      Maths      ",font=('arial',24,'bold'),bg='orange')
    omarks=Entry(commerce_window,width=8,font=('arial',20,'bold'),fg='black',border=3)
    omarkss=Entry(commerce_window,width=8,font=('arial',20,'bold'),fg='black',border=3)
    l11=Label(commerce_window,text='/80',font=('arial',20,'bold'),bg='orange')
    l21=Label(commerce_window,text='/20',font=('arial',20,'bold'),bg='orange')
    c2.create_window(285,500,window=l11)
    c3.create_window(285,500,window=l21)
    c1.create_window(200,500,window=l1)
    c2.create_window(200,500,window=omarks)
    c3.create_window(200,500,window=omarkss)
def scibio():
    global pmarks
    global pmarkss
    global pname
    pname="BIOLOGY"
    global cp
    cp="044"
    l1=Label(science_window,text="Biology ",font=('arial',24,'bold'),bg='orange')
    pmarks=Entry(science_window,width=8,font=('arial',20,'bold'),fg='black',border=3)
    pmarkss=Entry(science_window,width=8,font=('arial',20,'bold'),fg='black',border=3)
    l11=Label(science_window,text='/80',font=('arial',20,'bold'),bg='orange')
    l21=Label(science_window,text='/20',font=('arial',20,'bold'),bg='orange')
    c2.create_window(285,350,window=l11)
    c3.create_window(285,350,window=l21)
    c1.create_window(200,350,window=l1)
    c2.create_window(200,350,window=pmarks)
    c3.create_window(200,350,window=pmarkss)
def science():
    global c1
    global c2
    global c3
    global science_window
    global amarks
    global bmarks
    global cmarks
    global amarkss
    global bmarkss
    global cmarkss
    global aname
    global bname
    global cname
    global ca
    global cb
    global cc
    ca="301"
    cb="042"
    cc="043"
    aname="ENGLISH COMM."
    bname="PHYSICS"
    cname="CHEMISTRY"
    science_window=Toplevel(stream)
    science_window.configure(bg="purple")
    science_window.geometry('1350x750')
    c1=Canvas(science_window,height=600,width=400,border=4,relief='raised',bg='orange')
    c1.place(x=75,y=50)
    c2=Canvas(science_window,height=600,width=400,border=4,relief='raised',bg='pink')
    c2.place(x=475,y=50)
    c3=Canvas(science_window,height=600,width=400,border=4,relief='raised',bg='cyan')
    c3.place(x=875,y=50)
    lsub=Label(science_window,text='Subjects',font=('arial',24,'bold'),bg='orange')
    lth=Label(science_window,text='Theory',font=('arial',24,'bold'),bg='pink')
    lprac=Label(science_window,text='Practical',font=('arial',24,'bold'),bg='cyan')
    l1=Label(science_window,text='Physics',font=('arial',24,'bold'),bg='orange')
    bmarks=Entry(science_window,width=8,font=('arial',20,'bold'),fg='black',border=3)
    bmarkss=Entry(science_window,width=8,font=('arial',20,'bold'),fg='black',border=3)
    l2=Label(science_window,text='Chemistry',font=('arial',24,'bold'),bg='orange')
    cmarks=Entry(science_window,width=8,font=('arial',20,'bold'),fg='black',border=3)
    cmarkss=Entry(science_window,width=8,font=('arial',20,'bold'),fg='black',border=3)
    l3=Label(science_window,text='English',font=('arial',24,'bold'),bg='orange')
    amarks=Entry(science_window,width=8,font=('arial',20,'bold'),fg='black',border=3)
    amarkss=Entry(science_window,width=8,font=('arial',20,'bold'),fg='black',border=3)
    l11=Label(science_window,text='/70',font=('arial',20,'bold'),bg='orange')
    l12=Label(science_window,text='/70',font=('arial',20,'bold'),bg='orange')
    l13=Label(science_window,text='/80',font=('arial',20,'bold'),bg='orange')
    l21=Label(science_window,text='/30',font=('arial',20,'bold'),bg='orange')
    l22=Label(science_window,text='/30',font=('arial',20,'bold'),bg='orange')
    l23=Label(science_window,text='/20',font=('arial',20,'bold'),bg='orange')
    b11=Button(science_window,text='Maths',height=1,width=10,bg='cyan',border=4,font=('arial',12,'bold'),command=scimaths)
    b12=Button(science_window,text='Biology',height=1,width=10,bg='cyan',border=4,font=('arial',12,'bold'),command=scibio)
    b13=Button(science_window,text='C.S.',height=1,width=10,bg='cyan',border=4,font=('arial',12,'bold'),command=scics)
    b14=Button(science_window,text='P.Ed',height=1,width=10,bg='cyan',border=4,font=('arial',12,'bold'),command=sciped)
    b15=Button(science_window,text='Music',height=1,width=10,bg='cyan',border=4,font=('arial',12,'bold'),command=scimusic)
    b16=Button(science_window,text='Hindi',height=1,width=10,bg='cyan',border=4,font=('arial',12,'bold'),command=scihindi)
    b=Button(science_window,text='Next',height=1,width=5,bg='green',border=4,font=('arial',10,'bold'),command=entry_check1)
    c1.create_window(200,50,window=lsub)
    c2.create_window(200,50,window=lth)
    c3.create_window(200,50,window=lprac)
    c1.create_window(150,150,window=l3)
    c2.create_window(200,150,window=amarks)
    c3.create_window(200,150,window=amarkss)
    c1.create_window(150,200,window=l1)
    c2.create_window(200,200,window=bmarks)
    c3.create_window(200,200,window=bmarkss)
    c1.create_window(200,250,window=l2)
    c2.create_window(285,200,window=l11)
    c2.create_window(285,250,window=l12)
    c2.create_window(285,150,window=l13)
    c3.create_window(285,200,window=l21)
    c3.create_window(285,250,window=l22)
    c3.create_window(285,150,window=l23)
    c2.create_window(200,250,window=cmarks)
    c3.create_window(200,250,window=cmarkss)
    c1.create_window(150,300,window=b11)
    c1.create_window(280,300,window=b12)
    c1.create_window(150,450,window=b13)
    c1.create_window(150,400,window=b14)
    c1.create_window(280,450,window=b15)
    c1.create_window(280,400,window=b16)
    c3.create_window(350,560,window=b)
def commerce():
    global c1
    global c2
    global c3
    global commerce_window
    global amarks
    global bmarks
    global cmarks
    global pmarks
    global amarkss
    global bmarkss
    global cmarkss
    global pmarkss
    global aname
    global bname
    global cname
    global pname
    global ca
    global cb
    global cc
    global cp
    ca="301"
    cb="055"
    cc="054"
    cp="030"
    aname="ENGLISH COMM.."
    bname="ACCOUNTANCY"
    cname="BUSINESS STUDIES"
    pname="ECONOMICS"
    commerce_window=Toplevel(stream)
    commerce_window.configure(bg="purple")
    commerce_window.geometry('1350x750')
    c1=Canvas(commerce_window,height=600,width=400,border=4,relief='raised',bg='orange')
    c1.place(x=75,y=50)
    c2=Canvas(commerce_window,height=600,width=400,border=4,relief='raised',bg='pink')
    c2.place(x=475,y=50)
    c3=Canvas(commerce_window,height=600,width=400,border=4,relief='raised',bg='cyan')
    c3.place(x=875,y=50)
    lsub=Label(commerce_window,text='Subjects',font=('arial',24,'bold'),bg='orange')
    lth=Label(commerce_window,text='Theory',font=('arial',24,'bold'),bg='pink')
    lprac=Label(commerce_window,text='Practical',font=('arial',24,'bold'),bg='cyan')
    l1=Label(commerce_window,text='Economics ',font=('arial',24,'bold'),bg='orange')
    pmarks=Entry(commerce_window,width=8,font=('arial',20,'bold'),fg='black',border=3)
    pmarkss=Entry(commerce_window,width=8,font=('arial',20,'bold'),fg='black',border=3)
    l2=Label(commerce_window,text='Accountancy ',font=('arial',24,'bold'),bg='orange')
    bmarks=Entry(commerce_window,width=8,font=('arial',20,'bold'),fg='black',border=3)
    bmarkss=Entry(commerce_window,width=8,font=('arial',20,'bold'),fg='black',border=3)
    l4=Label(commerce_window,text='Business Studies ',font=('arial',24,'bold'),bg='orange')
    cmarks=Entry(commerce_window,width=8,font=('arial',20,'bold'),fg='black',border=3)
    cmarkss=Entry(commerce_window,width=8,font=('arial',20,'bold'),fg='black',border=3)
    l3=Label(commerce_window,text='English ',font=('arial',24,'bold'),bg='orange')
    amarks=Entry(commerce_window,width=8,font=('arial',20,'bold'),fg='black',border=3)
    amarkss=Entry(commerce_window,width=8,font=('arial',20,'bold'),fg='black',border=3)
    l11=Label(commerce_window,text='/80',font=('arial',20,'bold'),bg='orange')
    l12=Label(commerce_window,text='/70',font=('arial',20,'bold'),bg='orange')
    l13=Label(commerce_window,text='/80',font=('arial',20,'bold'),bg='orange')
    l21=Label(commerce_window,text='/20',font=('arial',20,'bold'),bg='orange')
    l22=Label(commerce_window,text='/30',font=('arial',20,'bold'),bg='orange')
    l23=Label(commerce_window,text='/20',font=('arial',20,'bold'),bg='orange')
    l14=Label(commerce_window,text='/70',font=('arial',20,'bold'),bg='orange')
    l24=Label(commerce_window,text='/30',font=('arial',20,'bold'),bg='orange')
    b11=Button(commerce_window,text='Maths',height=1,width=10,bg='cyan',border=4,font=('arial',12,'bold'),command=commmaths)
    b12=Button(commerce_window,text='Psychology',height=1,width=10,bg='cyan',border=4,font=('arial',12,'bold'),command=commpsycho)
    b13=Button(commerce_window,text='C.S.',height=1,width=10,bg='cyan',border=4,font=('arial',12,'bold'),command=commcs)
    b14=Button(commerce_window,text='P.Ed',height=1,width=10,bg='cyan',border=4,font=('arial',12,'bold'),command=commped)
    b15=Button(commerce_window,text='Music',height=1,width=10,bg='cyan',border=4,font=('arial',12,'bold'),command=commmusic)
    b16=Button(commerce_window,text='Hindi',height=1,width=10,bg='cyan',border=4,font=('arial',12,'bold'),command=commhindi)
    b=Button(commerce_window,text='Next',height=1,width=5,bg='green',border=4,font=('arial',10,'bold'),command=entry_check2)
    c1.create_window(200,50,window=lsub)
    c2.create_window(200,50,window=lth)
    c3.create_window(200,50,window=lprac)
    c1.create_window(200,150,window=l3)
    c2.create_window(200,150,window=amarks)
    c3.create_window(200,150,window=amarkss)
    c1.create_window(200,200,window=l1)
    c2.create_window(200,200,window=pmarks)
    c3.create_window(200,200,window=pmarkss)
    c1.create_window(200,250,window=l2)
    c2.create_window(200,250,window=bmarks)
    c3.create_window(200,250,window=bmarkss)
    c1.create_window(200,300,window=l4)
    c2.create_window(285,200,window=l11)
    c2.create_window(285,250,window=l12)
    c2.create_window(285,150,window=l13)
    c3.create_window(285,200,window=l21)
    c3.create_window(285,250,window=l22)
    c3.create_window(285,150,window=l23)
    c2.create_window(285,300,window=l14)
    c3.create_window(285,300,window=l24)
    c2.create_window(200,300,window=cmarks)
    c3.create_window(200,300,window=cmarkss)
    c1.create_window(150,350,window=b11)
    c1.create_window(280,350,window=b12)
    c1.create_window(150,400,window=b13)
    c1.create_window(280,400,window=b14)
    c1.create_window(150,450,window=b15)
    c1.create_window(280,450,window=b16)
    c3.create_window(350,560,window=b)
def art():
    global c1
    global c2
    global c3
    global art_window
    global bmarks
    global cmarks
    global amarks
    global bmarkss
    global cmarkss
    global amarkss
    global aname
    global bname
    global cname
    global ca
    global cb
    global cc
    ca="301"
    cb="027"
    cc="028"
    aname="ENGLISH COMM."
    bname="HISTORY"
    cname="POLITICAL SCI."
    art_window=Toplevel(stream)
    art_window.configure(bg="purple")
    art_window.geometry('1350x750')
    c1=Canvas(art_window,height=600,width=400,border=4,relief='raised',bg='orange')
    c1.place(x=75,y=50)
    c2=Canvas(art_window,height=600,width=400,border=4,relief='raised',bg='pink')
    c2.place(x=475,y=50)
    c3=Canvas(art_window,height=600,width=400,border=4,relief='raised',bg='cyan')
    c3.place(x=875,y=50)
    lsub=Label(art_window,text='Subjects',font=('arial',24,'bold'),bg='orange')
    lth=Label(art_window,text='Theory',font=('arial',24,'bold'),bg='pink')
    lprac=Label(art_window,text='Practical',font=('arial',24,'bold'),bg='cyan')
    l1=Label(art_window,text='History',font=('arial',24,'bold'),bg='orange')
    bmarks=Entry(art_window,width=8,font=('arial',20,'bold'),fg='black',border=3)
    bmarkss=Entry(art_window,width=8,font=('arial',20,'bold'),fg='black',border=3)
    l2=Label(art_window,text='Political Sci.',font=('arial',24,'bold'),bg='orange')
    cmarks=Entry(art_window,width=8,font=('arial',20,'bold'),fg='black',border=3)
    cmarkss=Entry(art_window,width=8,font=('arial',20,'bold'),fg='black',border=3)
    l3=Label(art_window,text='English',font=('arial',24,'bold'),bg='orange')
    amarks=Entry(art_window,width=8,font=('arial',20,'bold'),fg='black',border=3)
    amarkss=Entry(art_window,width=8,font=('arial',20,'bold'),fg='black',border=3)
    l11=Label(art_window,text='/70',font=('arial',20,'bold'),bg='orange')
    l12=Label(art_window,text='/70',font=('arial',20,'bold'),bg='orange')
    l13=Label(art_window,text='/80',font=('arial',20,'bold'),bg='orange')
    l21=Label(art_window,text='/30',font=('arial',20,'bold'),bg='orange')
    l22=Label(art_window,text='/30',font=('arial',20,'bold'),bg='orange')
    l23=Label(art_window,text='/20',font=('arial',20,'bold'),bg='orange')
    b11=Button(art_window,text='Socialogy',height=1,width=10,bg='cyan',border=4,font=('arial',12,'bold'),command=artsocial)
    b12=Button(art_window,text='Economics',height=1,width=10,bg='cyan',border=4,font=('arial',12,'bold'),command=arteco)
    b13=Button(art_window,text='C.S.',height=1,width=10,bg='cyan',border=4,font=('arial',12,'bold'),command=artcs)
    b14=Button(art_window,text='Psycho',height=1,width=10,bg='cyan',border=4,font=('arial',12,'bold'),command=artpsycho)
    b15=Button(art_window,text='Music',height=1,width=10,bg='cyan',border=4,font=('arial',12,'bold'),command=artmusic)
    b16=Button(art_window,text='Hindi',height=1,width=10,bg='cyan',border=4,font=('arial',12,'bold'),command=arthindi)
    b=Button(art_window,text='Next',height=1,width=5,bg='green',border=4,font=('arial',10,'bold'),command=entry_check3)
    c1.create_window(200,50,window=lsub)
    c2.create_window(200,50,window=lth)
    c3.create_window(200,50,window=lprac)
    c1.create_window(200,150,window=l3)
    c2.create_window(200,150,window=amarks)
    c3.create_window(200,150,window=amarkss)
    c1.create_window(200,200,window=l1)
    c2.create_window(200,200,window=bmarks)
    c3.create_window(200,200,window=bmarkss)
    c1.create_window(200,250,window=l2)
    c2.create_window(285,200,window=l11)
    c2.create_window(285,250,window=l12)
    c2.create_window(285,150,window=l13)
    c3.create_window(285,200,window=l21)
    c3.create_window(285,250,window=l22)
    c3.create_window(285,150,window=l23)
    c2.create_window(200,250,window=cmarks)
    c3.create_window(200,250,window=cmarkss)
    c1.create_window(150,300,window=b11)
    c1.create_window(280,300,window=b12)
    c1.create_window(150,450,window=b13)
    c1.create_window(150,400,window=b14)
    c1.create_window(280,450,window=b15)
    c1.create_window(280,400,window=b16)
    c3.create_window(350,560,window=b)
def display():
    global stream
    stream=Toplevel(createmark_window)
    stream.configure(bg="purple")
    stream.geometry('1350x750')
    c=Canvas(stream,height=600,width=1200,border=10,relief='raised',bg='pink')
    c.place(x=75,y=50)
    l1=Label(stream,text='Choose your stream',height=1,width=20,bg='pink',font=('arial',32,'bold'),fg='purple')
    b1=Button(stream,text='Science',height=2,width=20,border=4,bg='green',font=('arial',20,'bold'),command=science)
    b2=Button(stream,text='Commerce',height=2,width=20,border=4,bg='orange',font=('arial',20,'bold'),command=commerce)
    b3=Button(stream,text='Humanities',height=2,width=20,border=4,bg='brown',font=('arial',20,'bold'),command=art)
    c.create_window(600,100,window=l1)
    c.create_window(600,240,window=b1)
    c.create_window(600,340,window=b2)
    c.create_window(600,440,window=b3)
def check_rollno():
    for i in range(0,lene14):
        zz=e14[i]
        if zz in ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'):
            Label(createmark_window,text="                     ",width=25,bg='pink',fg='red').place(x=100,y=290)
            Label(createmark_window,text="      Invalid        ",width=25,bg='pink',fg='red').place(x=100,y=290)
            pp=0
            break
        elif zz in ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'):
            Label(createmark_window,text="                     ",width=25,bg='pink',fg='red').place(x=100,y=290)
            Label(createmark_window,text="      Invalid        ",width=25,bg='pink',fg='red').place(x=100,y=290)
            pp=0
            break
        elif zz in ("!","@","#","$","%","^","&","*","(",")","_","+","=","-","~",".",",","/","?","<",">",":",";","{","}","[","]","|"):
            Label(createmark_window,text="                     ",width=25,bg='pink',fg='red').place(x=100,y=290)
            Label(createmark_window,text="      Invalid        ",width=25,bg='pink',fg='red').place(x=100,y=290)
            pp=0
            break
        else:
            pp=1
            Label(createmark_window,text="                     ",width=25,bg='pink',fg='red').place(x=100,y=290)
    for i in range(0,lene17):
        zz=e17[i]
        if zz in ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'):
            Label(createmark_window,text="                     ",width=25,bg='pink',fg='red').place(x=100,y=440)
            Label(createmark_window,text="      Invalid        ",width=25,bg='pink',fg='red').place(x=100,y=440)
            qq=0
            break
        elif zz in ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'):
            Label(createmark_window,text="                     ",width=25,bg='pink',fg='red').place(x=100,y=440)
            Label(createmark_window,text="      Invalid        ",width=25,bg='pink',fg='red').place(x=100,y=440)
            qq=0
            break
        elif zz in ("!","@","#","$","%","^","&","*","(",")","_","+","=","-","~",".",",","/","?","<",">",":",";","{","}","[","]","|"):
            Label(createmark_window,text="                     ",width=25,bg='pink',fg='red').place(x=100,y=440)
            Label(createmark_window,text="      Invalid        ",width=25,bg='pink',fg='red').place(x=100,y=440)
            qq=0
            break
        else:
            qq=1
            Label(createmark_window,text="                     ",width=25,bg='pink',fg='red').place(x=100,y=440)
    for i in range(0,lene18):
        zz=e18[i]
        if zz in ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'):
            Label(createmark_window,text="                     ",width=25,bg='pink',fg='red').place(x=100,y=495)
            Label(createmark_window,text="      Invalid        ",width=25,bg='pink',fg='red').place(x=100,y=495)
            rr=0
            break
        elif zz in ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'):
            Label(createmark_window,text="                     ",width=25,bg='pink',fg='red').place(x=100,y=495)
            Label(createmark_window,text="      Invalid        ",width=25,bg='pink',fg='red').place(x=100,y=495)
            rr=0
            break
        elif zz in ("!","@","#","$","%","^","&","*","(",")","_","+","=","-","~",".",",","/","?","<",">",":",";","{","}","[","]","|"):
            Label(createmark_window,text="                     ",width=25,bg='pink',fg='red').place(x=100,y=495)
            Label(createmark_window,text="      Invalid        ",width=25,bg='pink',fg='red').place(x=100,y=495)
            rr=0
            break
        else:
            rr=1
            Label(createmark_window,text="                     ",width=25,bg='pink',fg='red').place(x=100,y=495)
    if pp==1 and qq==1 and rr==1:
        display()
def choose_stream():
    global e11
    global e12
    global e13
    global e14
    global e15
    global e16
    global e17
    global e18
    global lene14
    global lene17
    global lene18
    global alist
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
    if len(e11)>30 or len(e12)>30 or len(e13)>30 or len(e16)>50 or e11=='' or e12=='' or e13=='' or e14=='' or e15=='' or e16=='' or e17=='' or e18=='':
        if len(e11)>30:
            Label(createmark_window,text="                     ",width=25,bg='pink',fg='red').place(x=100,y=130)
            Label(createmark_window,text="Max 30 characters",width=25,bg='pink',fg='red').place(x=100,y=130)
        elif e11=='':
            Label(createmark_window,text="                     ",width=25,bg='pink',fg='red').place(x=100,y=130)
            Label(createmark_window,text="       Enter name    ",width=25,bg='pink',fg='red').place(x=100,y=130)
        else:
            Label(createmark_window,text="                     ",width=25,bg='pink',fg='red').place(x=100,y=130)
        if len(e12)>30:
            Label(createmark_window,text="                     ",width=25,bg='pink',fg='red').place(x=100,y=185)
            Label(createmark_window,text="Max 30 characters",width=25,bg='pink',fg='red').place(x=100,y=185)
        elif e12=='':
            Label(createmark_window,text="                     ",width=25,bg='pink',fg='red').place(x=100,y=185)
            Label(createmark_window,text="       Enter name    ",width=25,bg='pink',fg='red').place(x=100,y=185)
        else:
            Label(createmark_window,text="                     ",width=25,bg='pink',fg='red').place(x=100,y=185)
        if len(e13)>20:
            Label(createmark_window,text="                     ",width=25,bg='pink',fg='red').place(x=100,y=240)
            Label(createmark_window,text="Max 30 characters",width=25,bg='pink',fg='red').place(x=100,y=240)
        elif e13=='':
            Label(createmark_window,text="                     ",width=25,bg='pink',fg='red').place(x=100,y=240)
            Label(createmark_window,text="       Enter name    ",width=25,bg='pink',fg='red').place(x=100,y=240)
        else:
            Label(createmark_window,text="                     ",width=25,bg='pink',fg='red').place(x=100,y=240)
        if len(e16)>50:
            Label(createmark_window,text="                     ",width=25,bg='pink',fg='red').place(x=100,y=390)
            Label(createmark_window,text="Max 50 characters",width=25,bg='pink',fg='red').place(x=100,y=390)
        elif e16=='':
            Label(createmark_window,text="                     ",width=25,bg='pink',fg='red').place(x=100,y=390)
            Label(createmark_window,text="       Enter name    ",width=25,bg='pink',fg='red').place(x=100,y=390)
        else:
            Label(createmark_window,text="                     ",width=25,bg='pink',fg='red').place(x=100,y=390)
        if e14=='':
            Label(createmark_window,text="                     ",width=25,bg='pink',fg='red').place(x=100,y=290)
            Label(createmark_window,text="    Enter Roll no.   ",width=25,bg='pink',fg='red').place(x=100,y=290)
        else:
                Label(createmark_window,text="                     ",width=25,bg='pink',fg='red').place(x=100,y=290)
        if e15=='':
            Label(createmark_window,text="                     ",width=25,bg='pink',fg='red').place(x=100,y=340)
            Label(createmark_window,text="     Enter D.O.B.    ",width=25,bg='pink',fg='red').place(x=100,y=340)
        else:
            Label(createmark_window,text="                     ",width=25,bg='pink',fg='red').place(x=100,y=340)
        if e17=='':
            Label(createmark_window,text="                     ",width=25,bg='pink',fg='red').place(x=100,y=440)
            Label(createmark_window,text="  Enter School code  ",width=25,bg='pink',fg='red').place(x=100,y=440)
        else:
            Label(createmark_window,text="                     ",width=25,bg='pink',fg='red').place(x=100,y=440)
        if e18=='':
            Label(createmark_window,text="                     ",width=25,bg='pink',fg='red').place(x=100,y=495)
            Label(createmark_window,text="   Enter Center no.  ",width=25,bg='pink',fg='red').place(x=100,y=495)
        else:
            Label(createmark_window,text="                     ",width=25,bg='pink',fg='red').place(x=100,y=495)
    else:
        Label(createmark_window,text="                     ",width=25,bg='pink',fg='red').place(x=100,y=130)
        Label(createmark_window,text="                     ",width=25,bg='pink',fg='red').place(x=100,y=185)
        Label(createmark_window,text="                     ",width=25,bg='pink',fg='red').place(x=100,y=240)
        Label(createmark_window,text="                     ",width=25,bg='pink',fg='red').place(x=100,y=390)
        Label(createmark_window,text="                     ",width=25,bg='pink',fg='red').place(x=100,y=290)
        Label(createmark_window,text="                     ",width=25,bg='pink',fg='red').place(x=100,y=340)
        Label(createmark_window,text="                     ",width=25,bg='pink',fg='red').place(x=100,y=440)
        Label(createmark_window,text="                     ",width=25,bg='pink',fg='red').place(x=100,y=495)
        check_rollno()
def create_marksheet():
    global c
    global createmark_window
    global e1
    global e2
    global e3
    global e4
    global e5
    global e6
    global e7
    global e8
    createmark_window=Toplevel(tk)
    createmark_window.configure(bg="purple")
    createmark_window.geometry('1350x750')
    c=Canvas(createmark_window,height=600,width=1200,border=10,relief='raised',bg='pink')
    c.place(x=75,y=50)
    l1=Label(createmark_window,text='Name',height=1,width=15,bg='pink',font=('arial',14,'bold'),fg='purple')
    l2=Label(createmark_window,text="Father's Name",height=1,width=15,bg='pink',font=('arial',14,'bold'),fg='purple')
    l3=Label(createmark_window,text="Mother's Name",height=1,width=15,bg='pink',font=('arial',14,'bold'),fg='purple')
    l4=Label(createmark_window,text='Roll No.',height=1,width=15,bg='pink',font=('arial',14,'bold'),fg='purple')
    l5=Label(createmark_window,text='D.O.B.',height=1,width=15,bg='pink',font=('arial',14,'bold'),fg='purple')
    l6=Label(createmark_window,text='School Name',height=1,width=15,bg='pink',font=('arial',14,'bold'),fg='purple')
    l7=Label(createmark_window,text='Center No.',height=1,width=15,bg='pink',font=('arial',14,'bold'),fg='purple')
    l8=Label(createmark_window,text='School Code',height=1,width=15,bg='pink',font=('arial',14,'bold'),fg='purple')
    b1=Button(createmark_window,text='Back',height=2,width=10,border=4,bg='orange',font=('arial',10,'bold'),command=createmark_window.destroy)
    b2=Button(createmark_window,text='Next',height=2,width=10,border=4,bg='green',font=('arial',10,'bold'),command=display)
    e1=Entry(createmark_window,width=35,fg='purple',border=4,font=('arial',12,'bold'))
    e2=Entry(createmark_window,width=35,fg='purple',border=4,font=('arial',12,'bold'))
    e3=Entry(createmark_window,width=35,fg='purple',border=4,font=('arial',12,'bold'))
    e4=Entry(createmark_window,width=35,fg='purple',border=4,font=('arial',12,'bold'))
    e5=Entry(createmark_window,width=35,fg='purple',border=4,font=('arial',12,'bold'))
    e6=Entry(createmark_window,width=35,fg='purple',border=4,font=('arial',12,'bold'))
    e7=Entry(createmark_window,width=35,fg='purple',border=4,font=('arial',12,'bold'))
    e8=Entry(createmark_window,width=35,fg='purple',border=4,font=('arial',12,'bold'))
    c.create_window(300,100,window=l1)
    c.create_window(330,150,window=l2)
    c.create_window(330,200,window=l3)
    c.create_window(307,250,window=l4)
    c.create_window(300,300,window=l5)
    c.create_window(322,350,window=l6)
    c.create_window(312,400,window=l7)
    c.create_window(320,450,window=l8)
    c.create_window(890,580,window=b1)
    c.create_window(1040,580,window=b2)
    c.create_window(700,100,window=e1)
    c.create_window(700,150,window=e2)
    c.create_window(700,200,window=e3)
    c.create_window(700,250,window=e4)
    c.create_window(700,300,window=e5)
    c.create_window(700,350,window=e6)
    c.create_window(700,400,window=e7)
    c.create_window(700,450,window=e8)
def search_marksheet():
    whattodo=1
def credit():
    credit_window=Toplevel(tk)
    credit_window.configure(bg="purple")
    credit_window.geometry('1350x750')
    c=Canvas(credit_window,height=600,width=1200,border=10,relief='raised',bg='pink')
    c.place(x=75,y=50)
    l1=Label(credit_window,text='Developer',bg='pink',fg='purple',font=('elephant',32,'bold'))
    l2=Label(credit_window,text='  Pulkit Bansal',bg='pink',fg='purple',font=('arial',20,'bold'))
    b1=Button(credit_window,text='Back',height=2,width=10,bg='orange',border=4,font=('arial',12,'bold'),command=credit_window.destroy)
    c.create_window(550,100,window=l1)
    c.create_window(550,200,window=l2)
    c.create_window(1000,550,window=b1)
def exits():
    exit_window=Toplevel(tk)
    exit_window.configure(bg="red")
    exit_window.geometry('1350x750')
    c=Canvas(exit_window,height=600,width=1200,border=10,relief='raised',bg='pink')
    c.place(x=75,y=50)
    l1=Label(exit_window,text='Are you sure you want to exit??',font=('times',50,'bold'),fg='red',border=8,height=1,width=25,bg='pink')
    b1=Button(exit_window,text='Yes',font=('times',20,'bold'),fg='purple',border=8,height=1,width=5,command=tk.destroy)
    b2=Button(exit_window,text='No',font=('times',20,'bold'),fg='purple',border=8,height=1,width=5,command=exit_window.destroy)
    c.create_window(550,200,window=l1)
    c.create_window(450,300,window=b1)
    c.create_window(600,300,window=b2)
def parent_window():
    global tk
    tk=Tk()
    tk.geometry('1350x750')
    tk.title("PULKIT BANSAL")
    tk.configure(bg='purple3')
    c=Canvas(tk,height=600,width=1200,border=10,relief='raised',bg='pink')
    c.place(x=75,y=50)
    l1=Label(tk,text='C.B.S.E.',font=('elephant',42,'bold'),fg='purple',border=8,height=1,bg='pink')
    l2=Label(tk,text='MARKSHEET',font=('elephant',42,'bold'),fg='purple',border=8,height=1,bg='pink')
    l3=Label(tk,text='Menu',font=('times',32,'bold'),fg='purple',border=8,height=1,width=25,bg='pink')
    b1=Button(tk,text='Create Marksheet',font=('times',20,'bold'),fg='purple',border=8,height=1,width=25,command=create_marksheet)
    b2=Button(tk,text='Search Marksheet',font=('times',20,'bold'),fg='purple',border=8,height=1,width=25,command=search_marksheet)
    b3=Button(tk,text='Credits',font=('times',20,'bold'),fg='purple',border=8,height=1,width=25,command=credit)
    b4=Button(tk,text='Exit',font=('times',20,'bold'),fg='purple',border=8,height=1,width=25,command=exits)
    c.create_window(325,225,window=l1)
    c.create_window(325,350,window=l2)
    c.create_window(850,100,window=l3)
    c.create_window(900,200,window=b1)
    c.create_window(900,300,window=b2)
    c.create_window(900,400,window=b3)
    c.create_window(900,500,window=b4)
parent_window()
