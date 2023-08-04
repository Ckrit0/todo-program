from tkinter import *
from tkinter.messagebox import Message as msgbox
import tkinter.font
import requests
from functools import partial
import datetime

# 모든 객체 파괴
def clear():
    components = root.grid_slaves()
    for component in components:
        component.destroy()

# 로그인 페이지
def loginPage():
    if(member.get('mbNo') != 0): # 로그인 정보가 있으면 할일목록 페이지로
        todoPage()
        return
    
    def login(): # 로그인 버튼 누름
        id = idInput.get()
        pw = pwInput.get()
        url = host + 'login'
        reqBody = '{mbId:' + id + ', mbEmail:' + id + ',mbPw:' + pw + '}'
        resp = requests.post(url=url, headers=reqHeader, data=reqBody).json()
        if(resp.get('mbNo') == 0):
            msgbox(title='로그인 정보 확인',message='로그인 정보가 틀립니다.').show()
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

    versionLabel = Label(root, text=version, fg=blue1)
    versionLabel.grid(row=7,column=0,padx=10,pady=10,sticky='e')
  
# 회원가입 페이지
def joinPage():
    if(member.get('mbNo') != 0): # 로그인 정보가 있으면 할일목록 페이지로
        todoPage()
        return
    
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
    if(member.get('mbNo') == 0): # 로그인 정보가 없으면 로그인페이지로
        loginPage()
        return
        
    def getTodos(order):
        urlNext = ''
        if order == 0 :
            urlNext = 'progresstdorderdate'
        elif order == 1 :
            urlNext = 'progresstdreversedate'
        elif order == 2 :
            urlNext = 'progresstdordertargetdate'
        elif order == 3 :
            urlNext = 'progresstdreversetargetdate'
        elif order == 4:
            urlNext = 'alltdorderdate'
        elif order == 5:
            urlNext = 'alltdreversedate'
        elif order == 6:
            urlNext = 'alltdordertargetdate'
        elif order == 7:
            urlNext = 'alltdreversetargetdate'

        url = host + urlNext
        reqBody = '{mbNo:' + str(member.get('mbNo')) + '}'
        resp = requests.post(url=url,headers=reqHeader, data=reqBody).json()
        todos = resp
        return todos

    def logout():
        global member
        member = { 'mbNo' : 0 }
        loginPage()
        return

    def newTodo():
        mbNo = str(member.get('mbNo'))
        tdContent = str(newContentInput.get())
        tdTargetdate = str(newDateInput.get())
        url = host + 'tdnew'
        reqBody = '{mbNo: ' + mbNo + ', tdContent: ' + tdContent + ', tdTargetdate: ' + tdTargetdate + '}'
        resp = requests.post(url=url,headers=reqHeader, data=reqBody.encode(encoding='UTF-8')).json()
        print(reqBody)
        print(resp)
        todoPage()
        return
    
    def newTodo2(event):
        newTodo()
    
    def completeTodo(tdNo,isComplete):
        urlNext = ''
        if(isComplete == 0):
            urlNext = 'complete'
        else:
            urlNext = 'cancelcomplete'
        url = host + urlNext
        reqBody = '{tdNo:' + str(tdNo) + '}'
        resp = requests.post(url=url,headers=reqHeader, data=reqBody).json()
        todoPage()
        return
    
    def updateSet(rowNo,event):
        global updateNo
        updateNo = rowNo
        todoPage()
        return
        
    def updateTodoSubmit(tdNo,event):
        tdContent = contentInput.get()
        url = host + 'tdupdate'
        reqBody = '{tdNo:' + str(tdNo) + ', tdContent:' + tdContent + '}'
        resp = requests.post(url=url,headers=reqHeader, data=reqBody.encode(encoding='UTF-8')).json()
        global updateNo
        updateNo = -1
        todoPage()
        return

    def updateTodoCancel(event):
        global updateNo
        updateNo = -1
        todoPage()
        return
    
    def updateDateSet(rowNo,event):
        global updateDateNo
        updateDateNo = rowNo
        todoPage()
        return
        
    def updateTododateSubmit(tdNo,event):
        tdDate = dateInput.get()
        url = host + 'changetargetdate'
        reqBody = '{tdNo:' + str(tdNo) + ', tdTargetdate:' + tdDate + '}'
        resp = requests.post(url=url,headers=reqHeader, data=reqBody).json()
        global updateDateNo
        updateDateNo = -1
        todoPage()
        return

    def updateTododateCancel(event):
        global updateDateNo
        updateDateNo = -1
        todoPage()
        return


    def deleteTodo(tdNo):
        url = host + 'delete'
        reqBody = '{tdNo:' + str(tdNo) + '}'
        resp = requests.post(url=url,headers=reqHeader, data=reqBody).json()
        todoPage()
        return
    
    def checkSeeall():
        global order
        if(seeallVar.get() == 0):
            if(order == 4):
                order = 0
            elif(order == 5):
                order = 1
            elif(order == 6):
                order = 2
            elif(order == 7):
                order = 3
        else:
            if(order == 0):
                order = 4
            elif(order == 1):
                order = 5
            elif(order == 2):
                order = 6
            elif(order == 3):
                order = 7
        todoPage()
        return
    
    def orderDate():
        global order
        if(seeallVar.get() == 0):
            order = 0
        else:
            order = 4
        todoPage()
        return
    
    def reverseDate():
        global order
        if(seeallVar.get() == 0):
            order = 1
        else:
            order = 5
        todoPage()
        return

    def orderTargetDate():
        global order
        if(seeallVar.get() == 0):
            order = 2
        else:
            order = 6
        todoPage()
        return

    def reverseTargetDate():
        global order
        if(seeallVar.get() == 0):
            order = 3
        else:
            order = 7
        todoPage()
        return
    
    def refresh():
        todoPage()
        return

    todos = getTodos(order)
    height = (len(todos)*30) + 200
    root.geometry("455x"+ str(height) +"+500+500") # 창 크기 설정
    clear() # 모든 객체 파괴

    title = Label(root, text='TodoT', font=titleFont, bg=purple1, fg=purple3)
    title.grid(row=0,column=0,padx=10,pady=1,columnspan=10)

    
    greetLabel = Label(root, text=str(member.get('mbId')) + '(' + str(member.get('mbEmail')) + ')님 환영합니다.', font=greetFont, fg=blue1)
    greetLabel.grid(row=1,column=0,padx=5,pady=1,columnspan=6)

    refreshBtn = Button(root, text='나가기', width=5, bg=purple3, fg=purple1, command=logout)
    refreshBtn.grid(row=1, column=7, padx=2, pady=2)

    refreshBtn = Button(root, text='변경', width=5, bg=purple3, fg=purple1, command=changePwPage)
    refreshBtn.grid(row=1, column=8, padx=2, pady=2)

    refreshBtn = Button(root, text='탈퇴', width=5, bg=purple3, fg=purple1, command=leavePage)
    refreshBtn.grid(row=1, column=9, padx=2, pady=2)

    rowNo = 0
    
    for todoItem in todos:
        checkVar = IntVar()
        checkVar.set(todoItem.get('tdIscomplete'))
        todoCheck = Checkbutton(root,fg=purple3, variable=checkVar, command= partial(completeTodo, todoItem.get('tdNo'), todoItem.get('tdIscomplete')))
        todoCheck.grid(row=rowNo+2, column=0, padx=0, pady=2)
        
        if(rowNo == updateNo):
            contentInput = Entry(root, width=35, bg=purple1, fg=purple3)
            contentInput.insert(0,todoItem.get('tdContent'))
            contentInput.focus_set()
            contentInput.grid(row=rowNo+2, column=1, padx=2, pady=2, columnspan=6, sticky='w')
            contentInput.bind('<Return>',partial(updateTodoSubmit,todoItem.get('tdNo')))
            contentInput.bind('<Escape>',updateTodoCancel)
        else:
            contentLabel = Label(root,text=todoItem.get('tdContent'), wraplength=280, fg=purple3, anchor='w', justify='left')
            contentLabel.grid(row=rowNo+2, column=1, padx=2, pady=2, columnspan=6, sticky='w')
            contentLabel.bind("<Button-1>", partial(updateSet, rowNo))

        if(rowNo == updateDateNo):
            dateInput = Entry(root, width=10, bg=purple1, fg=purple3)
            dateInput.insert(0,todoItem.get('tdTargetdate'))
            dateInput.focus_set()
            dateInput.grid(row=rowNo+2, column=7, padx=2, pady=2, columnspan=2)
            dateInput.bind('<Return>',partial(updateTododateSubmit,todoItem.get('tdNo')))
            dateInput.bind('<Escape>',updateTododateCancel)
        else:
            dateLabel = Label(root, text=str(todoItem.get('tdTargetdate')), fg=purple3)
            dateLabel.grid(row=rowNo+2, column=7, padx=2, pady=2, columnspan=2)
            dateLabel.bind("<Button-1>", partial(updateDateSet, rowNo))

        deleteBtn = Button(root, text='삭제',font=btnFont, bg=blue1, fg=purple1, width=5, command= partial(deleteTodo,todoItem.get('tdNo')))
        deleteBtn.grid(row=rowNo+2, column=9, padx=5, pady=2)

        #완료된 아이템 처리
        if(checkVar.get() == 1):
            todoCheck.config(variable=checkVar.get())
            todoCheck.select()
            contentLabel.config(font=complteFont)
            dateLabel.config(font=complteFont)


        rowNo += 1

    rowNo += 2

    newContentInput = Entry(root, width=35, bg=purple1, fg=purple3)
    newContentInput.grid(row=rowNo, column=1, padx=2, pady=2, columnspan=6, sticky='w')
    newContentInput.bind('<Return>',newTodo2)
    newContentInput.focus_set()

    newDateInput = Entry(root, width=10, bg=purple1, fg=purple3)
    newDateInput.grid(row=rowNo, column=7, padx=2, pady=2, columnspan=2)
    newDateInput.insert(0,today)
    newDateInput.bind('<Return>',newTodo2)

    newBtn = Button(root, text='추가',font=btnFont, bg=blue1, fg=purple1, width=5, command= newTodo)
    newBtn.grid(row=rowNo, column=9, padx=5, pady=2)

    rowNo += 1
    seeallVar = IntVar()
    seeallCheck = Checkbutton(root, text='완료된 일정 포함', fg=blue1, variable=seeallVar, command=checkSeeall)
    seeallCheck.grid(row=rowNo,column=1,columnspan=8)
    if(order == 0 or order == 1 or order == 2 or order == 3):
        seeallVar.set(0)
    else:
        seeallVar.set(1)
    
    rowNo += 1
    orderDateBtn = Button(root, text='작성일▲', bg=purple2, fg=purple1, command=orderDate)
    orderDateBtn.grid(row=rowNo, column=1, padx=10, pady=2, columnspan=2)
    reverseDateBtn = Button(root, text='작성일▼', bg=purple2, fg=purple1, command=reverseDate)
    reverseDateBtn.grid(row=rowNo, column=3, padx=10, pady=2, columnspan=2)
    orderTargetDateBtn = Button(root, text='목표일▲', bg=purple2, fg=purple1, command=orderTargetDate)
    orderTargetDateBtn.grid(row=rowNo, column=5, padx=10, pady=2, columnspan=2)
    reverseTargetDateBtn = Button(root, text='목표일▼', bg=purple2, fg=purple1, command=reverseTargetDate)
    reverseTargetDateBtn.grid(row=rowNo, column=7, padx=10, pady=2, columnspan=2)

    rowNo += 1
    refreshBtn = Button(root, text='새로고침', bg=blue1, fg=purple1, command=refresh, width=48)
    refreshBtn.grid(row=rowNo, column=1, padx=10, pady=2, columnspan=8)

# 비밀번호 변경페이지
def changePwPage():
    if(member.get('mbNo') == 0): # 로그인 정보가 없으면 로그인 페이지로
        loginPage()
        return
    
    def changePw():
        if(member.get('mbPw') != oldPwInput.get()):
            msgbox(title='비밀번호 확인', message='현재 비밀번호가 틀립니다.').show()
            return
        if(pwInput.get() == ''):
            msgbox(title='비밀번호 확인', message='새로운 비밀번호가 없습니다.').show()
            return
        if(pwInput.get() != cfInput.get()):
            msgbox(title='새로운 비밀번호 확인', message='새로운 비밀번호와 새로운 비밀번호 확인이 서로 다릅니다.').show()
            return
        pw = pwInput.get()
        url = host + 'changepw'
        reqBody = '{mbNo:' + str(member.get('mbNo')) + ', mbPw:' + pw + '}'
        resp = requests.post(url=url,headers=reqHeader, data=reqBody).json()
        if(resp == True):
            todoPage()
            return

    def changePw2(enent):
        changePw()

    def focusNewPw(event):
        pwInput.focus_set()

    def focusNewCf(event):
        cfInput.focus_set()

    root.geometry(defaultSize) # 기본 창 크기
    clear() # 모든 객체 파괴

    title = Label(root, text='TodoT', font=titleFont, bg=purple1, fg=purple3)
    title.grid(row=0,column=0,padx=10,pady=1)

    oldPwLabel = Label(root, text='현재 비밀번호', fg=purple3)
    oldPwLabel.grid(row=1,column=0,padx=10,pady=1)

    oldPwInput = Entry(root, width= wholeX, bg=purple1, fg=purple3)
    oldPwInput.grid(row=2,column=0,padx=10,pady=1)
    oldPwInput.config(show='*')
    oldPwInput.focus_set()
    oldPwInput.bind("<Return>",focusNewPw)

    pwLabel = Label(root, text='새로운 비밀번호', fg=purple3)
    pwLabel.grid(row=3,column=0,padx=10,pady=1)

    pwInput = Entry(root, width= wholeX, bg=purple1, fg=purple3)
    pwInput.grid(row=4,column=0,padx=10,pady=1)
    pwInput.config(show='*')
    pwInput.bind("<Return>",focusNewCf)

    cfLabel = Label(root, text='새로운 비밀번호 확인', fg=purple3)
    cfLabel.grid(row=5,column=0,padx=10,pady=1)

    cfInput = Entry(root, width= wholeX, bg=purple1, fg=purple3)
    cfInput.grid(row=6,column=0,padx=10,pady=1)
    cfInput.config(show='*')
    cfInput.bind("<Return>",changePw2)

    joinBtn = Button(root, text='비밀번호 변경하기', font=btnFont, width= wholeX, bg=purple3, fg=purple1, command=changePw)
    joinBtn.grid(row=7,column=0,padx=10,pady=2)

    backBtn = Button(root, text='이전 페이지로', font=btnFont, width= wholeX, bg=purple3, fg=purple1, command=todoPage)
    backBtn.grid(row=8,column=0,padx=10,pady=2)
    
# 회원 탈퇴 페이지
def leavePage():
    if(member.get('mbNo') == 0): # 로그인 정보가 없으면 로그인 페이지로
        loginPage()
        return
    
    def goodBye():
        global member
        if(member.get('mbPw') != oldPwInput.get()):
            msgbox(title='비밀번호 확인', message='현재 비밀번호가 틀립니다.').show()
            return
        url = host + 'leave'
        reqBody = '{mbNo:' + str(member.get('mbNo')) + '}'
        resp = requests.post(url=url,headers=reqHeader, data=reqBody).json()
        if(resp == True):
            member = { 'mbNo' : 0 }
            loginPage()
            return

    def goodBye2(event):
        goodBye()

    root.geometry(defaultSize) # 기본 창 크기
    clear() # 모든 객체 파괴

    warningTextLabel = Label(root, text='탈퇴 후에 복구가 불가능합니다.\n 진짜 나갈거임? 진짜?', bg=purple2, fg=purple1, bd=1, relief='flat', width=35, height=5)
    warningTextLabel.grid(row=0, column=0, padx=10, pady= 30)

    oldPwLabel = Label(root, text='현재 비밀번호', fg=purple3)
    oldPwLabel.grid(row=1,column=0,padx=10,pady=1)

    oldPwInput = Entry(root, width= wholeX, bg=purple1, fg=purple3)
    oldPwInput.grid(row=2,column=0,padx=10,pady=5)
    oldPwInput.config(show='*')
    oldPwInput.focus_set()
    oldPwInput.bind("<Return>",goodBye2)
    
    joinBtn = Button(root, text='회원 탈퇴하기', font=btnFont, width= wholeX, bg=purple3, fg=purple1, command=goodBye)
    joinBtn.grid(row=3,column=0,padx=10,pady=5)

    backBtn = Button(root, text='이전 페이지로', font=btnFont, width= wholeX, bg=purple3, fg=purple1, command=todoPage)
    backBtn.grid(row=4,column=0,padx=10,pady=5)



##################
#                #
#  여기부터 시작  #
#                #
##################

root = Tk() # 기본 창 생성

# 공통 변수
version = 'Version : 1.0.0'
titleFont = tkinter.font.Font(family="맑은고딕", size=20, weight='bold')
btnFont = tkinter.font.Font(family="맑은고딕", size=8, weight='bold')
greetFont = tkinter.font.Font(family='맑은고딕', size=10, weight='bold')
complteFont = tkinter.font.Font(family='맑은고딕', size=9, overstrike=True)
wholeX = 38
purple1 = '#f4eff8'
purple2 = '#8045b4'
purple3 = '#581458'
blue1 = '#2118a3'
host = 'http://58.79.123.11:8080/'
reqHeader = {"Content-Type" : "application/json"}
member = { 'mbNo' : 0 } # 로그인한 멤버
order = 0
updateNo = -1
updateDateNo = -1
today = datetime.date.today()

# 기본창 설정
root.title("TodoT") # 타이틀
defaultSize="300x300+500+500"
root.geometry(defaultSize) # 기본 창 크기
root.configure(bg=purple1) # 배경색
root.resizable(False,True) # 리사이징 세로 허용(True), 가로 불가(False)

loginPage()

root.mainloop()