from tkinter import *
import tkinter.font

# 모든 객체 파괴도 왜 안되냐
def clear():
    components = root.grid_slaves()
    for component in components:
        component.destroy()

def loginPage():
    def login():
        id = idInput.get()
        pw = pwInput.get()
        print(id)
        print(pw)
        print('login')
        return
    
    # placeHolder 왜 안되냐
    def idInputFocusIn():
        if idInput.get() == '아이디 또는 이메일':
            idInput.delete(0,'end')
    
    def idInputFocusOut():
        if not idInput.get():
            idInput.insert(0,'아이디 또는 이메일')
    
    clear() # 모든 객체 파괴

    # 사용 객체
    title = Label(root,text='TodoT', font=titleFont, bg=purple1, fg=purple3)
    idInput = Entry(root, width= wholeX, bg=purple1, fg=purple3)
    idInput.insert(0,'아이디 또는 이메일')
    idInput.bind("<FocusIn>",idInputFocusIn)
    idInput.bind("<FocusOut>",idInputFocusOut)
    pwInput = Entry(root, width= wholeX, bg=purple1, fg=purple3)
    pwInput.insert(0,'비밀번호')
    pwInput.bind("<Return>",login)
    loginBtn = Button(root, text='로그인', font=btnFont, width= wholeX, bg=purple3, fg=purple1, command=login)
    joinBtn = Button(root, text='회원가입', font=btnFont, width= wholeX, bg=purple3, fg=purple1, command=joinPage)

    # 위치 선정
    title.grid(row=0,column=0,padx=10,pady=25)
    
    idInput.grid(row=1,column=0,padx=10,pady=5)
    pwInput.grid(row=2,column=0,padx=10,pady=5)
    loginBtn.grid(row=3,column=0,padx=10,pady=5)
    joinBtn.grid(row=4,column=0,padx=10,pady=5)
    return

def joinPage():
    def join():
        return
    
    clear() # 모든 객체 파괴

    # 사용 객체
    title = Label(root,text='TodoT', font=titleFont, bg=purple1, fg=purple3)
    idInput = Entry(root, width= wholeX, bg=purple1, fg=purple3)
    emailInput = Entry(root, width= wholeX, bg=purple1, fg=purple3)
    pwInput = Entry(root, width= wholeX, bg=purple1, fg=purple3)
    cfInput = Entry(root, width= wholeX, bg=purple1, fg=purple3)
    joinBtn = Button(root, text='회원가입', font=btnFont, width= wholeX, bg=purple3, fg=purple1, command=join)
    
    # 위치 선정
    title.place(x=110,y=20)
    idInput.place(x=10,y=70)
    emailInput.place(x=10,y=100)
    pwInput.place(x=10,y=130)
    cfInput.place(x=10,y=160)
    joinBtn.place(x=10,y=190)
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

# 기본창 설정
root.title("TodoT") # 타이틀
root.geometry("300x300") # 창 크기
root.configure(bg=purple1) # 배경색
root.resizable(False,False) # 리사이징 허용(True),불가(False)

loginPage()

root.mainloop()