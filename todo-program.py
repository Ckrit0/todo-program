from tkinter import *
from tkinter.messagebox import Message as msgbox
import tkinter.font
import requests

def clear():
    components = root.grid_slaves()
    for component in components:
        component.destroy()

# 로그인 페이지
def loginPage():
    if(member != {}): # 로그인 정보가 있으면 할일목록 페이지로
        todoPage()
    
    def login(): # 로그인 버튼 누름
        id = idInput.get()
        pw = pwInput.get()
        url = host + 'login'
        reqBody = '{mbId:' + id + ', mbEmail:' + id + ',mbPw:' + pw + '}'
        resp = requests.post(url=url, headers=reqHeader, data=reqBody).json()
        global member
        member = resp
        todoPage()

    def focusPwInput(e): # 아이디창에서 엔터누름
        pwInput.focus_set()

    def login2(e): # 비밀번호창에서 엔터 누름
        login()
    
    root.geometry(defaultSize) # 기본 창 크기
    clear() # 모든 객체 파괴

    title = Label(root,text='TodoT', font=titleFont, fg=purple3)
    title.grid(row=0,column=0,padx=10,pady=20)
    
    idLabel = Label(root,text='아이디 또는 이메일', fg=purple3)
    idLabel.grid(row=1,column=0,padx=10,pady=0)

    idInput = Entry(root, width= wholeX, bg=purple1, fg=purple3)
    idInput.grid(row=2,column=0,padx=10,pady=5)
    idInput.bind("<Return>",focusPwInput)
    idInput.focus_set()
    
    pwLabel = Label(root,text='비밀번호', fg=purple3)
    pwLabel.grid(row=3,column=0,padx=10,pady=0)

    pwInput = Entry(root, width= wholeX, bg=purple1, fg=purple3)
    pwInput.grid(row=4,column=0,padx=10,pady=5)
    pwInput.config(show='*')
    pwInput.bind("<Return>",login2)

    loginBtn = Button(root, text='로그인', font=btnFont, width= wholeX, bg=purple3, fg=purple1, command=login)
    loginBtn.grid(row=5,column=0,padx=10,pady=10)
    joinBtn = Button(root, text='회원가입', font=btnFont, width= wholeX, bg=purple3, fg=purple1, command=joinPage)
    joinBtn.grid(row=6,column=0,padx=10,pady=10)

    
# 회원가입 페이지
def joinPage():
    if(member != {}): # 로그인 정보가 있으면 할일목록 페이지로
        todoPage()
    
    def join(): # 회원가입 버튼 누름
        id = idInput.get()
        email = emailInput.get()
        pw = pwInput.get()
        cf = cfInput.get()
        if(pw != cf):
            msgbox(title='비밀번호 확인', message='비밀번호랑 비밀번호 확인이 서로 다릅니다.').show()
            return
        url = host + 'join'
        reqBody = '{mbId:' + id + ', mbEmail:' + email + ',mbPw:' + pw + '}'
        resp = requests.post(url=url,headers=reqHeader, data=reqBody).json()
        if(bool(resp)):
            url = host + 'login'
            reqBody = '{mbId:' + id + ', mbEmail:' + id + ',mbPw:' + pw + '}'
            resp = requests.post(url=url, headers=reqHeader, data=reqBody).json()
            global member
            member = resp
            todoPage()
        else:
            msgbox(title='아이디, 이메일 확인', message='이미 존재하는 아이디 또는 이메일주소 입니다.').show()
            return
        

    def focusEmail(e): # 아이디창에서 엔터 누름
        emailInput.focus_set()

    def focusPw(e): # 이메일창에서 엔터 누름
        pwInput.focus_set()

    def focusCf(e): # 비밀번호창에서 엔터 누름
        cfInput.focus_set()

    def join2(e): # 비밀번호확인창에서 엔터 누름
        join()
    
    root.geometry(defaultSize) # 기본 창 크기
    clear() # 모든 객체 파괴

    title = Label(root, text='TodoT', font=titleFont, bg=purple1, fg=purple3)
    title.grid(row=0,column=0,padx=10,pady=1)

    idLabel = Label(root, text='아이디', fg=purple3)
    idLabel.grid(row=1,column=0,padx=10,pady=1)

    idInput = Entry(root, width= wholeX, bg=purple1, fg=purple3)
    idInput.grid(row=2,column=0,padx=10,pady=1)
    idInput.bind("<Return>",focusEmail)
    idInput.focus_set()
    
    emailLabel = Label(root, text='이메일주소', fg=purple3)
    emailLabel.grid(row=3,column=0,padx=10,pady=1)

    emailInput = Entry(root, width= wholeX, bg=purple1, fg=purple3)
    emailInput.grid(row=4,column=0,padx=10,pady=1)
    emailInput.bind("<Return>",focusPw)

    pwLabel = Label(root, text='비밀번호', fg=purple3)
    pwLabel.grid(row=5,column=0,padx=10,pady=1)

    pwInput = Entry(root, width= wholeX, bg=purple1, fg=purple3)
    pwInput.grid(row=6,column=0,padx=10,pady=1)
    pwInput.config(show='*')
    pwInput.bind("<Return>",focusCf)

    cfLabel = Label(root, text='비밀번호 확인', fg=purple3)
    cfLabel.grid(row=7,column=0,padx=10,pady=1)

    cfInput = Entry(root, width= wholeX, bg=purple1, fg=purple3)
    cfInput.grid(row=8,column=0,padx=10,pady=1)
    cfInput.config(show='*')
    cfInput.bind("<Return>",join2)

    joinBtn = Button(root, text='회원가입하기', font=btnFont, width= wholeX, bg=purple3, fg=purple1, command=join)
    joinBtn.grid(row=9,column=0,padx=10,pady=2)

    backBtn = Button(root, text='로그인화면', font=btnFont, width= wholeX, bg=purple3, fg=purple1, command=loginPage)
    backBtn.grid(row=10,column=0,padx=10,pady=2)
    
# 할일목록 페이지
def todoPage():
    if(member == {}): # 로그인 정보가 없으면 로그인페이지로
        loginPage()

    checkVar=BooleanVar()
    def checkCheck():
        print(checkVar.get())

    # 일정 갯수 가져와서 사이즈 맞추기
    root.geometry("500x500+500+500") # 창 크기 설정
    clear() # 모든 객체 파괴

    title = Label(root, text='TodoT', font=titleFont, bg=purple1, fg=purple3)
    title.grid(row=0,column=0,padx=10,pady=1,columnspan=10)

    greetLabel = Label(root, text=member.get('mbId')+'('+member.get('mbEmail')+')님 환영합니다.', fg=purple3)
    greetLabel.grid(row=1,column=0,padx=10,pady=1,columnspan=10)

    todoCheck = Checkbutton(root,text='일정내용',fg=purple3, variable=checkVar, command=checkCheck)
    todoCheck.grid(row=2,column=0,padx=10,pady=2,columnspan=6, sticky='w')

    dateLabel = Label(root, text='2222-22-22', fg=purple3, width=15)
    dateLabel.grid(row=2,column=6,padx=10,pady=2,columnspan=3)

    deleteBtn = Button(root, text='삭제',font=btnFont, bg=blue1, fg=purple1, width=5)
    deleteBtn.grid(row=2,column=9,padx=10,pady=2)

    todoCheck2 = Checkbutton(root,text='일정내용두번째가 겁나게 길어지면 밑으로 내려가게 되는것인가? 진짜 진짜 많이 길어져도 밑으로 가나',fg=purple3, wraplength=280, variable=checkVar, command=checkCheck)
    todoCheck2.grid(row=3,column=0,padx=10,pady=2,columnspan=6, sticky='w')

    dateLabel2 = Label(root, text='2222-22-22', fg=purple3, width=15)
    dateLabel2.grid(row=3,column=6,padx=10,pady=2,columnspan=3)

    deleteBtn2 = Button(root, text='삭제',font=btnFont, bg=blue1, fg=purple1, width=5)
    deleteBtn2.grid(row=3,column=9,padx=10,pady=2)
    


root = Tk() # 기본 창 생성

# 공통 변수
titleFont = tkinter.font.Font(family="맑은고딕", size=20, weight='bold')
btnFont = tkinter.font.Font(family="맑은고딕", size=8, weight='bold')
wholeX = 38
purple1 = '#f4eff8'
purple2 = '#8045b4'
purple3 = '#581458'
blue1 = '#2118a3'
host = 'http://58.79.123.11:8080/'
reqHeader = {"Content-Type" : "application/json"}
member = {} # 로그인한 멤버

# 기본창 설정
root.title("TodoT") # 타이틀
defaultSize="300x300+500+500"
root.geometry(defaultSize) # 기본 창 크기
root.configure(bg=purple1) # 배경색
root.resizable(False,False) # 리사이징 허용(True),불가(False)

loginPage()

root.mainloop()