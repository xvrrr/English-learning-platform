from tkinter import *
import random
from tkinter import messagebox
import store_ZHANG


def run():
    # Frame design
    root1 = Tk()
    root1.title('Learning English')
    root1['width'] = 200
    root1['height'] = 300
    mainframe = Frame(root1)
    mainframe.pack()
    blank1 = Frame(root1, height=400, width=200)
    blank1.pack()

    # SET VAR
    rest = StringVar()  # rest
    w = StringVar()  # word
    m = StringVar()  # meaning
    i = StringVar()  # sequence of words
    n = StringVar()  # number of words during this time
    p = StringVar()  # review meaning
    e = StringVar()  # enter word
    r = StringVar()  # output result
    c = StringVar()  # once wrong, display correct answer

    Label(mainframe, text='Random Vocabulary Learning Platform', font=('Times New Roman', 30)).grid(column=1, row=0)

    # SECOND
    Label(mainframe, text='    Number of remaining words：', height=2, font=('Times New Roman', 15)).grid(column=0,row=1,columnspan=1,sticky=('W', 'E'))
    Label(mainframe, textvariable=rest, width=10, height=2, font=('Times New Roman', 15)).grid(row=1, column=1)
    f1 = open('dictionary.txt', 'r', encoding='utf-8')
    s1 = f1.read()
    s1 = s1.strip()
    f1.close()
    words = s1.split('\n')
    rest.set(str(len(words)))

    # THIRD
    Label(mainframe, text='Enter the numbers of the words that you want to memorize this time', height=2,font=('Times New Roman', 15)).grid(row=2, column=0, sticky=('W', 'E'))
    entry1 = Entry(mainframe, textvariable=n, width=18).grid(row=2, column=1)

    # FIFTH
    Label(mainframe, text='Sequence  ', height=2, font=('Times New Roman', 15)).grid(column=0, row=3, columnspan=1,sticky=('W', 'E'))
    Label(mainframe, textvariable=i, width=1).grid(row=3, column=1)

    # SIXTH
    Label(mainframe, text='Word   ', height=2, font=('Times New Roman', 15)).grid(row=4, column=0,sticky=('W', 'E'))
    Label(mainframe, text="Word's Meaning ", height=2, font=('Times New Roman', 15)).grid(row=4, column=2,sticky=('W', 'E'))

    # SEVENTH
    Label(mainframe, textvariable=w, width=50, font=('Times New Roman', 15), fg='green').grid(row=5, column=0,sticky=E)
    Label(mainframe, textvariable=m, width=50, font=('Times New Roman', 15), fg='green').grid(row=5, column=2,sticky=W)
    Label(mainframe, text=" ", height=2, font=('Times New Roman', 15)).grid(row=6, column=2, sticky=('W', 'E'))

    def empty():
        f2 = open('selected words.txt', 'w', encoding='utf-8')
        f2.write('')
        f2.close()
        return

    # FOURTH recite word
    def begin():
        empty()
        n1 = int(n.get())
        f1 = open('dictionary.txt', 'r', encoding='utf-8-sig')
        s1 = f1.read()
        s1 = s1.strip()
        f1.close()
        words = s1.split('\n')  # read dict
        rd = random.sample(range(0, len(words)), n1)  # random number for word
        i.set(1)
        word = words[rd[0]].split('/')  # word and meaning
        w.set(word[0])  # display first word
        m.set(word[1])
        f2 = open('selected words.txt', 'w', encoding='utf-8')  # Put n words into a file named "selected words"
        for j in range(0, n1):
            str1 = words[rd[j]] + '\n'
            f2.write(str1)
        f2.close()

    # EIGHTH
    # define next
    def Next():

        f2 = open('selected words.txt', 'r', encoding='utf-8')
        s2 = f2.read()
        s2 = s2.strip()  # The strip() method removes line breaks before and after the text
        f2.close()
        words = s2.split('\n')  # push word into word list
        if len(words) > 0:
            f3 = open('revision.txt', 'a+',
                      encoding='utf-8')  # Pop up the first word in words and put it into the file named "revision"
            str3 = words.pop(0) + '\n'
            f3.write(str3)
            f3.close()
            f2 = open('selected words.txt', 'w', encoding='utf-8')  # delete first word in select file
            str2 = '\n'.join(words)
            f2.write(str2)
            f2.close()
        if int(i.get()) == int(n.get()):
            messagebox.showinfo('prompt', "Click Review")
        else:
            word = words[0].split('/')  # word meaning
            w.set(word[0])
            m.set(word[1])
            k = int(i.get())
            i.set(str(k + 1))

    def begin2():
        empty()
        n1 = int(n.get())
        f1 = open('revision.txt', 'r', encoding='utf-8-sig')
        s1 = f1.read()
        s1 = s1.strip()
        f1.close()
        words = s1.split('\n')  # read dict
        rd = random.sample(range(0, len(words)), n1)  # random number for word
        i.set(1)
        word = words[rd[0]].split('/')  # word and meaning
        w.set(word[0])  # display first word
        m.set(word[0])

    def check(event):
        f3 = open('revision.txt', 'r', encoding='utf-8')
        s3 = f3.read()
        s3 = s3.strip()
        words = s3.split('\n')
        word = words[0].split('/')
        Label(mainframe, text='Answer is：', height=2, font=('Times New Roman', 15)).grid(column=0, row=11,
                                                                                         columnspan=1)
        c.set(word[0])
        answer = e.get()
        answer = answer.strip()
        word[0] = word[0].strip()
        if word[0] == answer:
            name = store_ZHANG.a
            score = str(int(store_ZHANG.num))
            new_score = str(int(score) + 1)
            combine1 = '{},{}'.format(name, score)
            combine2 = '{},{}'.format(name, new_score)
            store_ZHANG.changetext(combine1, combine2)
            store_ZHANG.login(name)
            r.set('Correct！Score +1, now your score is {} '.format(store_ZHANG.num[:-1]))
        else:
            r.set('Incorrect！')

    # Review Next
    def Next1():
        if True:
            r.set('')
            c.set('')  # Remove the relevant information of the previous word to avoid interference with the answer
            f3 = open('revision.txt', 'r', encoding='utf-8')
            s3 = f3.read()
            s3 = s3.strip()
            f3.close()
            words = s3.split('\n')
            rdint = random.randint(1, len(words)) - 1
            rdword = words[rdint]
            rdword1 = rdword.split('/')
            p.set(rdword1[1])  # Open the "review" file, randomly select a word, and display its meaning
            words[0], words[rdint] = words[rdint], words[1]  # Put randomly selected words at the beginning of words for easy search
            f3 = open('revision.txt', 'w', encoding='utf-8')  # Rewrite words into the "review" file
            f3.write('\n'.join(words))
            f3.close()

    def review():
        if int(i.get()) < int(n.get()):
            messagebox.showinfo("Haven't finished")
        else:
            Next1()
            Label(mainframe, text=" ", height=2, font=('Times New Roman', 15)).grid(row=8, column=2,sticky=('W', 'E'))
            Label(mainframe, text='Spell out the word according to the meaning(Then press Enter)：', height=2,font=('Times New Roman', 15)).grid(column=0, row=9, columnspan=1)
            Label(mainframe, textvariable=p, height=2, font=('Times New Roman', 15)).grid(column=0, row=10,columnspan=1)
            entry2 = Entry(mainframe, textvariable=e, width=18).grid(row=10, column=1)
            root1.bind('<Return>', check)  # Call the check() function with the enter key
            Button(mainframe, text='4. Next', command=Next1, width=15, bg='orange', height=2,font=('Times New Roman', 15)).grid(row=13, column=1)
            Label(mainframe, textvariable=r, height=2, font=('Times New Roman', 15)).grid(column=2, row=11,columnspan=3)
            Label(mainframe, textvariable=c, height=2, font=('Times New Roman', 15)).grid(column=1, row=11,columnspan=1)

           


    bt1 = Button(mainframe, text='1. Start', command=begin, bg='mediumslateblue', width=15, height=2,
                 font=('Times New Roman', 15)).grid(row=7, column=0)  # Set start
    bt2 = Button(mainframe, text='2. Next', command=Next, width=15, bg='gold', height=2,
                 font=('Times New Roman', 15)).grid(row=7, column=1)
    bt3 = Button(mainframe, text='3. Review', command=review, width=15, bg='GreenYellow', height=2,
                 font=('Times New Roman', 15)).grid(row=7, column=2)


    root1.mainloop()





