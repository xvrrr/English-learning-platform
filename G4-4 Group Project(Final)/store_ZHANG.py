def regisiter(name):
    file = open('Userfile_ZHANG.txt', 'a')
    file.write('\n' + name + ',' + str(0))
    file.close()


def login(name):
    global num
    global a
    success = False
    file = open('Userfile_ZHANG.txt', 'r')
    for i in file:
        a = i.split(',')[0]
        num = i.split(',')[-1]
        if a == name:
            success = True
            break
    file.close()
    if success:
        print('Login success')
    else:
        regisiter(name)
        print('A new member')

def changetext(a,b):
    with open('Userfile_ZHANG.txt', 'r') as f:
        lines=[]
        for line in f.readlines():
            if line != '\n':
                lines.append(line)
    f.close()
    with open('Userfile_ZHANG.txt', 'w') as f:
        for line in lines:
           if a in line:
               line = b
               f.write('%s\n' %line)
           else:
            f.write('%s' %line)













