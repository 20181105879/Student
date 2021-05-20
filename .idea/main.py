
# Press the green button in the gutter to run the script.
import os
filename='studen.txt'
def showmenu():
    # print(15)
    print('======================学生信息系统=================')
    print('\t\t\t\t\t1.添加学生')
    print('\t\t\t\t\t2.删除学生')
    print('\t\t\t\t\t3.修改学生')
    print('\t\t\t\t\t4.排序')
    print('\t\t\t\t\t5.统计学生人数')
    print('\t\t\t\t\t6.显示所以学生信息')
    print('\t\t\t\t\t7.查找学生信息')
    print('\t\t\t\t\t0.退出系统')
def insert():
    stulist=[]
    while True:
        id=input("请输入学生的ID:")
        if not id:
            break
        name=input("请输入学生的姓名:")
        if not name:
            break
        try:
            scorce = int(input("请输入学生的python分数："))
        except:
            print('输入的成绩无效，请重新输入')
            continue
        student={'id':id,'name':name,'scorce':scorce}
        stulist.append(student)
        result=input("你是否继续录入学生信息y/n:")
        if (result == 'n' or result == 'N'):
            save(stulist)
            print('学生成绩录入成功')
            break
        else:
            continue
def save(list):
    try:
        fp=open(filename,'a',encoding='utf-8')
    except:
        fp=open(filename,'w',encoding='utf-8')
    for item in list:
        fp.write(str(item)+'\n')
    fp.close()
def delete():
    while True:
        id=input('请输入你要删除学生的ID：')
        if id!='':
            try:
                if os.path.exists(filename):
                    with open(filename,'r',encoding='utf-8') as rfile:
                        listold=rfile.readlines()
                else:
                    listold=[]
                isdelete=False
                if listold:
                    with open(filename, 'w', encoding='utf-8') as wfile:
                        for item in listold:
                            stuent = dict(eval(item))
                            if stuent['id']==id:
                                isdelete=True
                            else:
                                wfile.write(str(stuent))
                        if isdelete:
                            print('删除成功ID位{0}的学生'.format(id))
                        else:
                            print('没有找到ID位{0}的学生'.format(id))
                        result = input('是否继续删除学生y/n:')
                        if result == 'y' or result == 'Y':
                            continue
                        else:
                            break

                else:
                    print('没有任何学生的信息')

            except:
                print('chuchu')
        else:
            print('请输入有效的学生ID')
def update():
    while True:
        if os.path.exists(filename):
            with open(filename,'r',encoding='utf=8') as rfile:
                stulist=rfile.readlines()
            if(stulist):
                id=input("请输入要修改学生的ID：")
                if id!='':
                    isfind=False
                    with open(filename, 'w', encoding='utf=8') as wfile:
                        for item in stulist:
                         student=dict(eval(item))
                         if student['id']==id:
                             isfind=True
                             try:
                                 student['name']=input('请输入要修改的名字')
                                 student['scorce'] = input('请输入要修改的分数')
                                 wfile.write(str(student + '\n'))
                             except:
                                 print("您输入的信息有误")
                         else:
                            wfile.write(str(student+'\n'))
                            wfile.write(str(item) + '\n')
                    if isfind==False:
                        print('没有找到ID为{}的学生'.format(id))
                    else:
                        print('修改成功')
                    result = input('是否继续删除学生y/n:')
                    if result == 'y' or result == 'Y':
                        continue
                    else:
                        break
                else:
                    print('请输入有效的ID')
            else:
                print("文件夹为空")
                break
        else:
            print("文件不存在")
            break
def stusort():
    pass
def stucount():
    pass
def showmessage(list):
    if len(list):
        stutitle = '{:^6}\t{:^6}\t{:^6}\t'
        title = stutitle.format('ID', '姓名', '分数')
        print(title)
        for item in list:
            stu=dict(eval(item))
            studate = '{:^6}\t{:^6}\t{:^6}\t'
            print(studate.format(stu.get('id'),stu.get('name'),stu.get('scorce')))
    else:
        print('未查询到学生的信息')
    return
def showstu():
    pass

def find():
    while True:
        id=''
        name=''
        if os.path.exists(filename):
            choice=int(input("姓名查找请输入1，ID查找请选择2："))
            if choice==1:
                name=input('请输入要查询的姓名:')
            elif choice==2:
                id=input('请输入要查询的ID:')
            else:
                print('请输入正确的选择')
                continue
            with open(filename,'r',encoding='utf-8') as rfile:
                findlist=[]
                stulist=rfile.readlines()
                if name:
                    for item in stulist:
                        stu=dict(eval(item))
                        if stu['name']==name:
                            findlist.append(item)
                elif id:
                    for item in stulist:
                        stu = dict(eval(item))
                        if stu['id'] == id:
                            findlist.append(item)
                # print(findlist)
                showmessage(findlist)
        else:
            print('还未创建学生表格')

if __name__ == '__main__':
    while True:
        showmenu()
        choice=int(input("请输入您的选择："))
        if(choice==0):
            result=input("是否确认退出系统y/n")
            if(result=='y' or result=='Y'):
                print('退出系成功')
                break
            else:
                continue
        elif(choice==1):
            insert()
        elif(choice==2):
            delete()
        elif(choice==3):
            update()
        elif(choice==4):
            stusort()
        elif(choice==5):
            stucount()
        elif(choice==6):
            showstu()
        elif (choice == 7):
            find()
        else:
            print("请输入正确的操作")