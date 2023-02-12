from pynput.keyboard import Key,Controller
import time
Keyboard=Controller()

a = input("输入你需要循环的内容：")
b = eval(input("输入循环的次数："))
print("信息已接收！将光标移动到会话框")
time.sleep(2)
for i in range (3):
    print(r"距离程序运行还有%d秒"%(3-i))
    time.sleep(1)
for i in range(b):
    Keyboard.type(a)
    Keyboard.press(Key.enter)
    Keyboard.release(Key.enter)
print("完成")
