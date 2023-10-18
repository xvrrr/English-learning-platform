from tkinter import *
import group_project3
import platform_final2


def main():
    root=Tk()
    root.title('MAIN PROGRAM')
    root['width']=400
    root['height']=200
    mainframe=Frame(root)
    mainframe.pack()
    blank=Frame(root,height=300,width=200)
    blank.pack()
    Label(mainframe,text=' ',font=('Times New Roman',30)).grid(column=0,row=0)
    Label(mainframe,text='  Hi！Glad to see you！',font=('Times New Roman',30)).grid(column=0,row=1)
    Label(mainframe,text=' ',font=('Times New Roman',30)).grid(column=0,row=2)
    Label(mainframe,text=' Please choose the module you want to use',font=('Times New Roman',15)).grid(column=0,row=3)
    Label(mainframe,text=' ',font=('Times New Roman',30)).grid(column=0,row=4)

    def runmod1():
        while True:
            root.destroy()
            platform_final2.run()

    def runmod2():
        exec(open('menu_ZHANG.py', encoding='utf-8').read())

    def runmod3():
        group_project3.play()

    def runmod4():
        exec(open('spellingame3.py', encoding='utf-8').read())




    btmod1=Button(mainframe,text='1. Random Vocabulary',command=runmod1,bg='lightgreen',width=25,height=3,font=('Times New Roman',8)).grid(row=6,column=0)

    btmod2=Button(mainframe,text='2. RPG',command=runmod2,bg='plum',width=25,height=3,font=('Times New Roman',8)).grid(row=7,column=0)

    btmod3=Button(mainframe,text='3. Sort Game',command=runmod3,bg='orange',width=25,height=3,font=('Times New Roman',8)).grid(row=8,column=0)

    btmod4=Button(mainframe,text='3. Spelling Game',command=runmod4,bg='grey',width=25,height=3,font=('Times New Roman',8)).grid(row=9,column=0)

    root.mainloop()