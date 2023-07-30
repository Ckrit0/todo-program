from tkinter import *
import tkinter.font
import json
import requests

def clear():
    components = root.grid_slaves()
    for component in components:
        component.destroy()

# 로그인 페이지
def loginPage():
    def login(): # 로그인 버튼 누름
        id = idInput.get()
        pw = pwInput.get()
        url = host + 'login'
        print(url)
        reqBody = '{mbId:' + id + ', mbEmail:' + id + ',mbPw:' + pw + '}'
        resp = requests.post(url=url, headers=reqHeader, data=reqBody).json()
        global member
        member = resp
    
    def focusPwInput(event): # 아이디창에서 엔터누름
        pwInput.focus_set()

    def login2(event): # 비밀번호창에서 엔터 누름
        login()
    
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
    def join():
        pass
    
    clear() # 모든 객체 파괴

    title = Label(root, text='TodoT', font=titleFont, bg=purple1, fg=purple3)
    title.grid(row=0,column=0,padx=10,pady=1)
    idLabel = Label(root, text='아이디', fg=purple3)
    idLabel.grid(row=1,column=0,padx=10,pady=1)
    idInput = Entry(root, width= wholeX, bg=purple1, fg=purple3)
    idInput.grid(row=2,column=0,padx=10,pady=1)
    emailLabel = Label(root, text='이메일주소', fg=purple3)
    emailLabel.grid(row=3,column=0,padx=10,pady=1)
    emailInput = Entry(root, width= wholeX, bg=purple1, fg=purple3)
    emailInput.grid(row=4,column=0,padx=10,pady=1)
    pwLabel = Label(root, text='비밀번호', fg=purple3)
    pwLabel.grid(row=5,column=0,padx=10,pady=1)
    pwInput = Entry(root, width= wholeX, bg=purple1, fg=purple3)
    pwInput.grid(row=6,column=0,padx=10,pady=1)
    cfLabel = Label(root, text='비밀번호 확인', fg=purple3)
    cfLabel.grid(row=7,column=0,padx=10,pady=1)
    cfInput = Entry(root, width= wholeX, bg=purple1, fg=purple3)
    cfInput.grid(row=8,column=0,padx=10,pady=1)
    joinBtn = Button(root, text='회원가입하기', font=btnFont, width= wholeX, bg=purple3, fg=purple1, command=join)
    joinBtn.grid(row=9,column=0,padx=10,pady=2)
    backBtn = Button(root, text='로그인화면', font=btnFont, width= wholeX, bg=purple3, fg=purple1, command=loginPage)
    backBtn.grid(row=10,column=0,padx=10,pady=2)
    
    return


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
member = {}

# 기본창 설정
root.title("TodoT") # 타이틀
root.geometry("300x300") # 창 크기
root.configure(bg=purple1) # 배경색
root.resizable(False,False) # 리사이징 허용(True),불가(False)

loginPage()

root.mainloop()