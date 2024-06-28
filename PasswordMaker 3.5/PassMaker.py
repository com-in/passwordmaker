import random
import time
import tqdm
import os
Word = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&*()_+-=[]\;./{}|:<>?1234567890"
print("程序正在加载密码字符")
for i in tqdm.tqdm(range(100)):
        time.sleep(random.uniform(0.01,0.1))
print("程序正在加载必要组件")
for i in tqdm.tqdm(range(100)):
        time.sleep(random.uniform(0.01,0.5))
print("程序正在检测更新")
for i in tqdm.tqdm(range(100)):
        time.sleep(random.uniform(0.01,0.5))
print("程序正在初始化")
for i in tqdm.tqdm(range(100)):
        time.sleep(random.uniform(0.01,0.5))
print("准备就绪")
for i in tqdm.tqdm(range(100)):
        time.sleep(random.uniform(0.01,0.5))
os.system("cls")
time.sleep(0.05)
PWDLong = ""
PWDNeedNum = ""
Password = ""
Passlist = []
log = []
time.sleep(random.randint(1,3))
while True:
        print("===============================")
        print("         PasswordMaker 3       ")
        print("     ")
        print("     ")
        print("           [1]生成密码")
        print("           [2]输出日志")
        print("     ")
        print("     ")
        print("           [X]退出")
        print("     ")
        print("===============================")
        print("     ")
        answer = input("输入选项：")
        if answer == "1":
                log.append("执行任务")
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
                        log.append(f"--生成密码{i+1}/{PWDNeedNum}")
                print(" 步骤4/4：生成完毕")
        elif answer == "2":
                for i in log:
                        print(i)
                print("=============")
                input("按回车继续...")
        elif answer == "x" or "X":
                print("退出")
                break
