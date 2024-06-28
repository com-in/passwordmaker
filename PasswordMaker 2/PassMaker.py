import random
import time
print("程序正在导入密码字符")
time.sleep(random.randint(1,6))
Word = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&*()_+-=[]\;./{}|:<>?1234567890"
print("程序正在初始化")
time.sleep(random.randint(1,4))
PWDLong = ""
PWDNeedNum = ""
Password = ""
Passlist = []
print("本程序生成所有密码均为英文状态！")
print("===============================")
print("     ")
print("         PasswordMaker 2       ")
print("     ")
print("===============================")
print("     ")
time.sleep(random.randint(1,3))
while True:
        PWDLong = int(input(" 步骤1/4：密码长度是(整数):"))
        PWDNeedNum = int(input(" 步骤2/4：需要数量(整数):"))
        time.sleep(random.randint(1,5))
        print(" 步骤3/4：生成密码")
        print(" 密码生成中...")
        time.sleep(random.randint(1,5))
        for i in range(PWDNeedNum):
                Password = ""
                for j in range(PWDLong):
                        Password += random.choice(Word)
                print("密码:",Password)
        print(" 步骤4/4：生成完毕")

        ask = int(input("接下来？1.继续生成 2.退出程序(输入序号)"))
        if ask == 1:
                print("")
        elif ask == 2:
                print("退出...")
                break
        else:
                print("您输入了不能被识别的内容，请重新输入！")
                while ask != 1 or ask != 2:
                        ask = int(input("接下来？1.继续生成 2.退出程序(输入序号)"))
                if ask == 1:
                        print("")
                elif ask == 2:
                        print("退出...")
                        break
