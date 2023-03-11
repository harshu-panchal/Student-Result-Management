from tkinter import *
from customtkinter import *
from PIL import Image
import os, shutil
from tkinter import filedialog as fd
import mysql.connector

db_connect = mysql.connector.connect(host="Localhost",user="root",passwd="654321")
db_cursor = db_connect.cursor()
db_cursor.execute("use database_connectivity")

root = CTk()
root.minsize(width=400,height=400)
root.geometry("400x400+475+100")
root.maxsize(width=400,height=400)
root.title("Result Management System")

flag = 0


def login():

    login_ = CTkToplevel()
    login_.title("Login")
    login_.minsize(width=400,height=250)
    login_.geometry("400x250+450+100")
    login_.maxsize(width=400,height=250)

    def create():
        error = CTkLabel(login_, text="invalid username or password", text_color="red",font=('',16))
        login_.deiconify()

        u=''
        p=''
        try:
            u = username_entr.get()
            p = password_entr.get()
        except:
            print("error")

        if (u == "harshvardhan" and p == "4076"):
            error.destroy()
            heading.destroy()
            username_lbl.destroy()
            username_entr.destroy()
            password_entr.destroy()
            login_btn.destroy()
            password_lbl.destroy()

            login_.title("Create Result")
            login_.minsize(width=500,height=530)
            login_.geometry("500x530")
            login_.maxsize(width=500,height=530)

            def submit1():
                def submit2():
                    def final_submit():
                        def dest_marks():
                            for q in range(len(marks_entr)):
                                marks_entr[q].destroy()
                                marks_lbl[q].destroy()
                                head3.destroy()
                                submit.destroy()
                                submit_alrt.destroy()

                        marks = ['','','','','']
                        db_connect = mysql.connector.connect(host="Localhost", user="root", passwd="654321")
                        db_cursor = db_connect.cursor()
                        db_cursor.execute("use database_connectivity")

                        for m in range(len(marks_entr)):
                            marks[m] = marks_entr[m].get()
                        try:
                            sql = "insert into marks values (%s,%s,%s,%s,%s,%s);"
                            try:
                                val = (roll_number1,int(marks[0]), int(marks[1]), int(marks[2]), int(marks[3]), int(marks[4]))
                            except:
                                print("something went wrong: ")
                            db_cursor.execute(sql, val)
                            db_connect.commit()
                            db_cursor.close()
                            db_connect.close()
                            print("submited")
                        except:
                            print("{error occured}")

                        login_.withdraw()

                        submit_alrt = CTkToplevel()
                        submit_alrt.title("SUBMITED")
                        submit_alrt.minsize(width=400,height=200)
                        submit_alrt.geometry("400x200+475+200")
                        submit_alrt.maxsize(width=400,height=200)
                        head4 = CTkLabel(submit_alrt, text="RESULT IS CREATED", font=("Bahnschrift Condensed", 25))
                        head4.pack(padx=0, pady=20)
                        show_result1 = CTkButton(submit_alrt, text="Show Result",command=display)
                        show_result1.place(x=45, y=90)
                        create_another = CTkButton(submit_alrt, text="Create Another Result",command=lambda:[dest_marks(),create()])
                        create_another.place(x=210, y=90)
                        abort = CTkButton(submit_alrt, text="Exit", fg_color="#fc033d", text_color="white",command=submit_alrt.destroy)
                        abort.place(x=130, y=140)
                        submit_alrt.mainloop()

                    subjects = ['', '', '', '', '']
                    for i in range(len(subject_entr)):
                        subjects[i] = subject_entr[i].get()

                    db_connect = mysql.connector.connect(host="Localhost", user="root", passwd="654321")
                    db_cursor = db_connect.cursor()
                    db_cursor.execute("use database_connectivity")

                    try:
                        sql2 = "insert into subjects values (%s,%s,%s,%s,%s,%s);"
                        try:
                            val2 = (roll_number1,subjects[0], subjects[1], subjects[2], subjects[3], subjects[4])
                        except:
                            print("something went wrong subj: ")
                        db_cursor.execute(sql2, val2)
                        db_connect.commit()
                        db_cursor.close()
                        db_connect.close()
                        print("submited")
                    except:
                        print("error occured subj")

                    if (subjects[0] != '' and subjects[1] != '' and subjects[2] != '' and subjects[3] != '' and
                            subjects[4] != ''):
                        for j in range(len(subject_entr)):
                            subject_entr[j].destroy()
                            subjects_lbl[j].destroy()
                            head2.destroy()
                            next_btn2.destroy()
                            invalid2.destroy()
                        head3 = CTkLabel(login_, text="Marks", font=("Gabriola", 35, "bold"))
                        head3.pack(padx=0, pady=20)

                        marks1_lbl = CTkLabel(login_, text=subjects[0], font=("calibri", 20, "bold"))
                        marks1_entr = CTkEntry(login_, font=("calibri", 20, "bold"), width=200)

                        marks2_lbl = CTkLabel(login_, text=subjects[1], font=("calibri", 20, "bold"))
                        marks2_entr = CTkEntry(login_, font=("calibri", 20, "bold"), width=200)

                        marks3_lbl = CTkLabel(login_, text=subjects[2], font=("calibri", 20, "bold"))
                        marks3_entr = CTkEntry(login_, font=("calibri", 20, "bold"), width=200)

                        marks4_lbl = CTkLabel(login_, text=subjects[3], font=("calibri", 20, "bold"))
                        marks4_entr = CTkEntry(login_, font=("calibri", 20, "bold"), width=200)

                        marks5_lbl = CTkLabel(login_, text=subjects[4], font=("calibri", 20, "bold"))
                        marks5_entr = CTkEntry(login_, font=("calibri", 20, "bold"), width=200)

                        marks_lbl = [marks1_lbl, marks2_lbl, marks3_lbl, marks4_lbl, marks5_lbl]
                        marks_entr = [marks1_entr, marks2_entr, marks3_entr, marks4_entr, marks5_entr]
                        Y = 120
                        for k in range(5):
                            marks_lbl[k].place(x=70, y=Y)
                            marks_entr[k].place(x=220, y=Y)
                            Y += 50

                        submit = CTkButton(login_, text="SUBMIT", font=("Berlin Sans FB", 15), text_color="black",
                                               height=40, width=80, fg_color="#42f595", command=final_submit)
                        submit.place(x=215, y=400)
                    else:
                        invalid2.place(x=170, y=80)

                db_connect = mysql.connector.connect(host="Localhost", user="root", passwd="654321")
                db_cursor = db_connect.cursor()
                db_cursor.execute("use database_connectivity")

                details = ['', '', '', '', '', '', '']

                for i in range(len(des_entr_details)):
                    details[i] = des_entr_details[i].get()
                try:
                    flag = 0
                    sql = "insert into details values (%s,%s,%s,%s,%s,%s,%s);"
                    try:
                        val = (details[0], details[1], details[2],int(details[3]),details[4],int(details[5]),details[6])
                    except:
                        print("something went wrong: ")
                    db_cursor.execute(sql, val)
                except mysql.connector.errors.IntegrityError:
                    flag = 1
                    roll_alrt = CTkToplevel()
                    roll_alrt.minsize(width=400,height=200)
                    roll_alrt.geometry("400x200+475+200")
                    roll_alrt.maxsize(width=400,height=200)
                    roll_alrt.title("ERROR")
                    root.eval(f"tk::PlaceWindow {str(roll_alrt)} center")
                    err_head= CTkLabel(roll_alrt, text="ERROR", font=("Bahnschrift Condensed", 25))
                    err_head.pack(padx=0, pady=20)
                    roll_err = CTkLabel(roll_alrt,text="The Roll Number You Entered Already Exist",font=("Bahnschrift Condensed", 18))
                    roll_err.place(x=70,y=80)
                    re_entr_btn = CTkButton(roll_alrt, text="Re-Enter", font=("Berlin Sans FB", 15), text_color="white",height=25, width=60, fg_color="#fc033d", command=roll_alrt.destroy)
                    re_entr_btn.place(x=170, y=130)
                    roll_alrt.mainloop()

                except:
                    flag = 1
                    roll_alrt = CTkToplevel()
                    roll_alrt.minsize(width=400, height=200)
                    roll_alrt.geometry("400x200+475+200")
                    roll_alrt.maxsize(width=400, height=200)
                    roll_alrt.title("ERROR")
                    root.eval(f"tk::PlaceWindow {str(roll_alrt)} center")
                    err_head = CTkLabel(roll_alrt, text="ERROR", font=("Bahnschrift Condensed", 25))
                    err_head.pack(padx=0, pady=20)
                    roll_err = CTkLabel(roll_alrt, text="Something Went Wrong", font=("Bahnschrift Condensed", 18))
                    roll_err.place(x=120, y=80)
                    re_entr_btn = CTkButton(roll_alrt, text="Retry", font=("Berlin Sans FB", 15), text_color="white",height=25, width=60, fg_color="#fc033d", command=roll_alrt.destroy)
                    re_entr_btn.place(x=170, y=130)
                    roll_err.mainloop()
                    print("error occured...")

                roll_number1 = details[5]

                db_connect.commit()
                db_cursor.close()
                db_connect.close()
                if (flag==0 and details[0] != '' and details[1] != '' and details[2] != '' and details[3] != '' and details[4] != '' and details[5] != '' and details[6] != ''):
                    for j in range(len(des_entr_details)):
                        des_entr_details[j].destroy()
                        des_lbl_details[j].destroy()
                        head.destroy()
                        next_btn.destroy()
                        invalid1.place_forget()
                        upload_img.destroy()
                    head2 = CTkLabel(login_, text="Subjects", font=("Gabriola", 35, "bold"))
                    head2.pack(padx=0, pady=20)

                    invalid2 = CTkLabel(login_, text="please fill all the details", text_color="red", font=('', 16))

                    sub1_lbl = CTkLabel(login_, text="First Subject      : ", font=("calibri", 20, "bold"))
                    sub1_entr = CTkEntry(login_, font=("calibri", 20, "bold"), width=200)

                    sub2_lbl = CTkLabel(login_, text="Second Subject  : ", font=("calibri", 20, "bold"))
                    sub2_entr = CTkEntry(login_, font=("calibri", 20, "bold"), width=200)

                    sub3_lbl = CTkLabel(login_, text="Third Subject     : ", font=("calibri", 20, "bold"))
                    sub3_entr = CTkEntry(login_, font=("calibri", 20, "bold"), width=200)

                    sub4_lbl = CTkLabel(login_, text="Fourth Subject   : ", font=("calibri", 20, "bold"))
                    sub4_entr = CTkEntry(login_, font=("calibri", 20, "bold"), width=200)

                    sub5_lbl = CTkLabel(login_, text="Fifth Subject      : ", font=("calibri", 20, "bold"))
                    sub5_entr = CTkEntry(login_, font=("calibri", 20, "bold"), width=200)

                    subjects_lbl = [sub1_lbl, sub2_lbl, sub3_lbl, sub4_lbl, sub5_lbl]
                    subject_entr = [sub1_entr, sub2_entr, sub3_entr, sub4_entr, sub5_entr]

                    Y = 120
                    for k in range(5):
                        subjects_lbl[k].place(x=70, y=Y)
                        subject_entr[k].place(x=220, y=Y)
                        Y += 50

                    next_btn2 = CTkButton(login_, text="NEXT", font=("Berlin Sans FB", 15), text_color="black",
                                          height=40, width=80, fg_color="#42f595", command=submit2)
                    next_btn2.place(x=215, y=400)

                else:
                    invalid1.place(x=170, y=70)

            invalid1 = CTkLabel(login_, text="please fill all the details", text_color="red")

            head = CTkLabel(login_, text="Details", font=("Gabriola", 35, "bold"))
            head.pack(padx=0, pady=5)

            s_name_lbl = CTkLabel(login_, text="Student's Name : ", font=("calibri", 20, "bold"))
            s_name_entr = CTkEntry(login_, font=("calibri", 20, "bold"), width=200)

            f_name_lbl = CTkLabel(login_, text="Father's Name   : ", font=("calibri", 20, "bold"))
            f_name_entr = CTkEntry(login_, font=("calibri", 20, "bold"), width=200)

            m_name_lbl = CTkLabel(login_, text="Mother's Name : ", font=("calibri", 20, "bold"))
            m_name_entr = CTkEntry(login_, font=("calibri", 20, "bold"), width=200)

            class_lbl = CTkLabel(login_, text="Class                   : ", font=("calibri", 20, "bold"))
            class_entr = CTkEntry(login_, font=("calibri", 20, "bold"), width=200)

            sectn_lbl = CTkLabel(login_, text="Section               : ", font=("calibri", 20, "bold"))
            sectn_entr = CTkEntry(login_, font=("calibri", 20, "bold"), width=200)

            roll_lbl = CTkLabel(login_, text="Roll no.              : ", font=("calibri", 20, "bold"))
            roll_entr = CTkEntry(login_, font=("calibri", 20, "bold"), width=200)

            session_lbl = CTkLabel(login_, text="Session               : ", font=("calibri", 20, "bold"))
            session_entr = CTkEntry(login_, font=("calibri", 20, "bold"), width=200)

            des_lbl_details = [s_name_lbl, f_name_lbl, m_name_lbl, class_lbl, sectn_lbl, roll_lbl, session_lbl]
            des_entr_details = [s_name_entr, f_name_entr, m_name_entr, class_entr, sectn_entr, roll_entr, session_entr]
            Y = 100
            for k1 in range(len(des_lbl_details)):
                des_lbl_details[k1].place(x=70, y=Y)
                des_entr_details[k1].place(x=220, y=Y)
                Y += 50

            def image_upload():
                f = fd.askopenfilename(initialdir="/", title="select a file",filetypes=(("jpeg", "*.jpg"), ("png", "*.png")))
                os.chdir('C:\\Users\\MY\\Desktop\\my python projects\\result maker\\photos')
                shutil.copy(f, 'C:\\Users\\MY\\Desktop\\my python projects\\result maker\\photos')
                sl = '\\'
                rec = -1
                for i in range(len(f) - 1, 0, -1):
                    if (f[i] != "/"):
                        rec -= 1
                    else:
                        break
                st = f[-1:(rec):-1] + sl
                fst = st[-1:-(len(st) + 1):-1]
                f1 = "C:\\Users\\MY\\Desktop\\my python projects\\result maker\\photos"
                f = f1 + fst
                print(f)
                roll_number = roll_entr.get()
                sql1 = "insert into images values(%s,%s)"
                val1 = (int(roll_number), f)
                db_cursor.execute(sql1, val1)
                db_connect.commit()
                db_cursor.close()
                db_connect.close()

            upload_img = CTkButton(login_, text="UPLOAD PHOTO", font=("Berlin Sans FB", 15), text_color="black", height=40, width=80, fg_color="#42f595", command=image_upload)
            upload_img.place(x=120, y=460)

            next_btn = CTkButton(login_, text="NEXT", font=("Berlin Sans FB", 15), text_color="black", height=40,width=80, fg_color="#42f595", command=submit1)
            next_btn.place(x=285, y=460)
            # else:
            # error.place(x=115, y=150)

    heading = CTkLabel(login_,text="Admin Login", font=("Gabriola", 45, "bold"))
    heading.pack(padx=0, pady=0)
    username_lbl = CTkLabel(login_, text="Username : ", font=("calibri", 20, "bold"))
    username_lbl.place(x=75, y=80)
    username_entr = CTkEntry(login_, font=("calibri", 20, "bold"), width=150)
    username_entr.place(x=175, y=80)
    password_lbl = CTkLabel(login_, text="Password  : ", font=("calibri", 20, "bold"))
    password_lbl.place(x=75, y=120)
    password_entr = CTkEntry(login_, font=("calibri", 20, "bold"), width=150)
    password_entr.place(x=175, y=120)

    login_btn = CTkButton(login_, text="Login", font=("Berlin Sans FB", 15), text_color="black", height=40,width=80, fg_color="#42f595",command=create)
    login_btn.place(x=160, y=180)

    login_.mainloop()


def display():
    def show():
        try:
            data = roll_entr.get()
            display_.destroy()
            db_cursor.execute(f"select * from details where roll={data};")
            details = db_cursor.fetchall()
            db_cursor.execute(f"select session from details where roll={data};")
            session = db_cursor.fetchall()
            db_cursor.execute(f"select photo from images where roll={data};")
            photos = db_cursor.fetchall()

            if (details!=[]):
                db_cursor.execute(f"select * from subjects where roll={data};")
                subjects = db_cursor.fetchall()
                db_cursor.execute(f"select * from marks where roll={data};")
                marks = db_cursor.fetchall()

                result = CTkToplevel()
                result.configure(fg_color ="white")
                result.title("RESULT")
                result.minsize(width=750, height=700)
                result.maxsize(width=750, height=700)
                
                heading_ = CTkLabel(result, text="APNA SCHOOL", font=("Times New Roman", 25, "bold"), text_color="red")
                heading_.pack()
                indore = CTkLabel(result, text="---INDORE---", font=("Times New Roman", 18, "bold"), text_color="red")
                indore.pack()
                g_sheet = CTkLabel(result, text="GRADE SHEET", font=("arial", 17), text_color = "black")
                g_sheet.pack(padx=100, pady=30)
                session = CTkLabel(result, text=f"Academic Year : 2020-2021", font=("arial", 17, "bold"), text_color = "black")  # something is missing
                session.place(x=270, y=115)
                name = CTkLabel(result, text="Student's Name: ", font=("arial", 16, "bold"), text_color = "black")
                name.place(x=20, y=150)
                fname = CTkLabel(result, text="Father's Name   : ", font=("arial", 16, "bold"), text_color = "black")
                fname.place(x=20, y=175)
                mname = CTkLabel(result, text="Mother's Name  : ", font=("arial", 16, "bold"), text_color = "black")
                mname.place(x=20, y=200)
                class_ = CTkLabel(result, text="Class                    : ", font=("arial", 16, "bold"), text_color = "black")
                class_.place(x=20, y=225)
                section = CTkLabel(result, text="Section                : ", font=("arial", 16, "bold"), text_color = "black")
                section.place(x=20, y=250)

                class_ = CTkLabel(result, text="Roll Number     : ", font=("arial", 16, "bold"), text_color = "black")
                class_.place(x=400, y=200)
                class_ = CTkLabel(result, text="Session             : ", font=("arial", 16, "bold"), text_color = "black")
                class_.place(x=400, y=225)
                class_ = CTkLabel(result, text="Status                : ", font=("arial", 16, "bold"), text_color = "black")
                class_.place(x=400, y=250)

                try:
                    img = CTkImage(Image.open(photos[0][0]), size=(80, 110))
                    btn = CTkButton(result, text='', height=100, width=100, image=img, bg_color="white", border_color="black",fg_color="white",hover_color="white",border_width=2)
                    btn.place(x=585, y=70)

                except:
                    btn = CTkButton(result, text='Image is not\n available', text_color="black", height=100, width=100, bg_color="white",
                                    border_color="black", fg_color="white", hover_color="white", border_width=2)
                    btn.place(x=585, y=70)

                state = CTkLabel(result, text="Statement of Grades", font=("arial", 16, "bold"), text_color = "black")
                state.place(x=287, y=295)

                c = CTkCanvas(result, height='204', width='630',background="white")
                c.place(x=60, y=325)
                line = 54
                c.create_line(4, 4, 630, 4)
                for i in range(6):
                    c.create_line(4, line, 630, line)
                    line += 30
                c.create_line(4, 4, 4, 204)
                c.create_line(55, 4, 55, 204)
                c.create_line(280, 4, 280, 204)
                c.create_line(400, 4, 400, 204)
                c.create_line(535, 4, 535, 204)
                c.create_line(630, 4, 630, 204)

                state = CTkLabel(result, text="Total :", font=("arial", 16, "bold"), text_color = "black")
                state.place(x=380, y=530)

                state = CTkLabel(result, text="Percentage :", font=("arial", 16, "bold"), text_color = "black")
                state.place(x=20, y=560)

                state = CTkLabel(result, text="CGPA           :", font=("arial", 16, "bold"), text_color = "black")
                state.place(x=20, y=590)

                state = CTkLabel(result, text="Check & verified by", font=("arial", 16, "bold"), text_color = "black")
                state.place(x=20, y=670)

                state = CTkLabel(result, text="Seal & Sign of", font=("arial", 16, "bold"), text_color = "black")
                state.place(x=580, y=645)

                state = CTkLabel(result, text="Controller of Examination", font=("arial", 16, "bold"), text_color = "black")
                state.place(x=535, y=670)


                nm = 150
                for i in range(0,5):
                    l = CTkLabel(result, text=details[0][i], font=("arial", 16, "bold"), text_color = "black")
                    l.place(x=150, y=nm)
                    nm += 25

                nm = 200
                for i in range(5, 7):
                    l = CTkLabel(result, text=details[0][i], font=("arial", 16, "bold"), text_color = "black")
                    l.place(x=530, y=nm)
                    nm += 25

                l = CTkLabel(result, text="Regular", font=("arial", 16, "bold"), text_color = "black")
                l.place(x=530, y=250)

                nm = 380
                for i in range(6):
                    if (i == 0):
                        l = CTkLabel(result, text='S No.', font=("arial", 16, "bold"), text_color = "black")
                        l.place(x=65, y=350)
                    else:
                        l = CTkLabel(result, text=str(i), font=("arial", 16, "bold"), text_color = "black")
                        l.place(x=80, y=nm)
                        nm += 30

                nm = 380
                for i in range(6):
                    if (i == 0):
                        l = CTkLabel(result, text='Subjects', font=("arial", 16, "bold"), text_color = "black")
                        l.place(x=150, y=350)
                    else:
                        l = CTkLabel(result, text=subjects[0][i], font=("arial", 16, "bold"), text_color = "black")
                        l.place(x=150, y=nm)
                        nm += 30
                nm = 380
                for i in range(6):
                    if (i == 0):
                        l = CTkLabel(result, text='Total Marks', font=("arial", 16, "bold"), text_color = "black")
                        l.place(x=350, y=350)
                    else:
                        l = CTkLabel(result, text='100', font=("arial", 16), text_color = "black")
                        l.place(x=385, y=nm)
                        nm += 30

                nm = 380
                for i in range(6):
                    if (i == 0):
                        l = CTkLabel(result, text='Marks Obtained', font=("arial", 16, "bold"), text_color = "black")
                        l.place(x=467, y=350)
                    else:
                        l = CTkLabel(result, text=marks[0][i], font=("arial", 16), text_color = "black")
                        l.place(x=515, y=nm)
                        nm += 30

                grade = ['', '', '', '', '']
                for i in range(1, 6):
                    avg = int(marks[0][i])
                    if avg >= 91 and avg <= 100:
                        grade[i - 1] = "A1"
                    elif avg >= 81 and avg < 91:
                        grade[i - 1] = "A2"
                    elif avg >= 71 and avg < 81:
                        grade[i - 1] = "B1"
                    elif avg >= 61 and avg < 71:
                        grade[i - 1] = "B2"
                    elif avg >= 51 and avg < 61:
                        grade[i - 1] = "C1"
                    elif avg >= 41 and avg < 51:
                        grade[i - 1] = "C2"
                    elif avg >= 33 and avg < 41:
                        grade[i - 1] = "D"
                    elif avg >= 21 and avg < 33:
                        grade[i - 1] = "E1"
                    elif avg >= 0 and avg < 21:
                        grade[i - 1] = "E2"

                nm = 380
                for i in range(-1, 5):
                    if (i == 0):
                        l = CTkLabel(result, text='Grade', font=("arial", 16, "bold"), text_color = "black")
                        l.place(x=617, y=350)
                    else:
                        l = CTkLabel(result, text=grade[i], font=("arial", 16), text_color = "black")
                        l.place(x=625, y=nm)
                        nm += 30

                total = 0
                for i in range(1, 6):
                    total += int(marks[0][i])
                l = CTkLabel(result, text=str(total), font=("arial", 16, "bold"), text_color = "black")
                l.place(x=510, y=530)

                min = 0
                for i in range(1, 6):
                    if (int(marks[0][i]) < 33):
                        min += 1
                if (min > 0):
                    l = CTkLabel(result, text="Fail", font=("arial", 16, "bold"), text_color = "black")
                    l.place(x=620, y=530)
                else:
                    l = CTkLabel(result, text="Pass", font=("arial", 16, "bold"), text_color = "black")
                    l.place(x=620, y=530)

                percentage = ((total) * 100) / (500)

                l = CTkLabel(result, text=f"{percentage}%", font=("arial", 16, "bold"), text_color = "black")
                l.place(x=120, y=560)

                l = CTkLabel(result, text=str(percentage / 10), font=("arial", 16, "bold"), text_color = "black")
                l.place(x=120, y=590)

                result.mainloop()
            else:
                not_found = CTkToplevel()
                not_found.minsize(width=400, height=200)
                not_found.geometry("400x200+475+100")
                not_found.maxsize(width=400, height=200)
                not_found.title("ERROR")
                err_head = CTkLabel(not_found, text="ERROR", font=("Bahnschrift Condensed", 25))
                err_head.pack(padx=0, pady=20)
                roll_err = CTkLabel(not_found, text="RESULT NOT FOUND",
                                    font=("Bahnschrift Condensed", 18))
                roll_err.place(x=150, y=80)
                re_entr_btn = CTkButton(not_found, text="Re-Enter", font=("Berlin Sans FB", 15), text_color="white",
                                        height=25, width=60, fg_color="#fc033d", command=not_found.destroy)
                re_entr_btn.place(x=170, y=130)
                not_found.mainloop()
        except:
            err = CTkToplevel()
            err.minsize(width=400, height=200)
            err.geometry("400x200+475+200")
            err.maxsize(width=400, height=200)
            err.title("ERROR")

            err_head = CTkLabel(err, text="ERROR", font=("Bahnschrift Condensed", 25))
            err_head.pack(padx=0, pady=20)
            err_msg = CTkLabel(err, text="Something Went Wrong!",
                                font=("Bahnschrift Condensed", 18))
            err_msg.place(x=130, y=80)
            re_try_btn = CTkButton(err, text="Re-Try", font=("Berlin Sans FB", 15), text_color="white",
                                    height=25, width=60, fg_color="#fc033d", command=err.destroy)
            re_try_btn.place(x=170, y=130)
            err.mainloop()


    display_ = CTkToplevel()
    display_.title("display record")
    display_.geometry("400x400+450+100")
    heading = CTkLabel(display_,text="Enter Credentials", font=("Gabriola", 35, "bold"))
    heading.pack(padx=0, pady=20)
    name_lbl = CTkLabel(display_, text="Name : ", font=("calibri", 20, "bold"))
    name_lbl.place(x=60,y=100)
    name_entr = CTkEntry(display_,font=("calibri",20,"bold"),width=200)
    name_entr.place(x=135,y=100)
    roll_lbl = CTkLabel(display_, text="Roll no.: ", font=("calibri", 20, "bold"))
    roll_lbl.place(x=60, y=150)
    roll_entr = CTkEntry(display_, font=("calibri", 20, "bold"), width=200)
    roll_entr.place(x=135, y=150)
    class_lbl = CTkLabel(display_, text="Class : ", font=("calibri", 20, "bold"))
    class_lbl.place(x=60, y=200)
    class_entr = CTkEntry(display_, font=("calibri", 20, "bold"), width=200)
    class_entr.place(x=135, y=200)
    sectn_lbl = CTkLabel(display_, text="Section : ", font=("calibri", 20, "bold"))
    sectn_lbl.place(x=60, y=250)
    sectn_entr = CTkEntry(display_, font=("calibri", 20, "bold"), width=200)
    sectn_entr.place(x=135, y=250)

    show_btn = CTkButton(display_, text="SHOW", font=("Berlin Sans FB", 15), text_color="black", height=40, width=80, fg_color="#42f595",command=show)
    show_btn.place(x=160,y=300)
    back_btn = CTkButton(display_, text="Back", font=("Berlin Sans FB", 15), text_color="white", height=25,width=60, fg_color="#fc033d",command=display_.destroy)
    back_btn.place(x=170, y=350)
    display_.mainloop()


'''_________________front page heading_________________'''
l = CTkLabel(root, text="Result Management System", font=("Gabriola", 35, "bold"))
l.pack(padx=0, pady=20)


'''____________________front page logo______________________'''
icon = PhotoImage(file="images/result_logo.png")
root.iconphoto(True,icon)
photo = PhotoImage(file="images/front_pg_logo.png")
small_img = photo.subsample(12,12)
label1 = CTkLabel(root,text="",font=('Arial',40),padx=30,pady=70,image=small_img,compound='bottom',height=100,width=100)
label1.place(x=145,y=90)


'''__________________________front page buttons________________________'''
create_btn = CTkButton(root,text="Create New Result",font=("Berlin Sans FB",15),text_color="black",height=40,width=80,fg_color="#42f595",command=login)
create_btn.pack(padx=0,pady=100)

display_btn = CTkButton(root,text="Display Result",font=("Berlin Sans FB",15),text_color="black",height=40,width=80,fg_color="#42f595",command=display)
display_btn.place(x=151,y=260)

b = CTkButton(root,text="exit",font=("Exit",15),text_color="white",height=40,width=80,fg_color="#fc033d",command=exit)
b.place(x=158,y=320)

root.mainloop()
