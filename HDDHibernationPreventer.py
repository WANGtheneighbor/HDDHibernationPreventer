import time

def text_create(name, msg):
    desktop_path = "./" 
    full_path = desktop_path + name + '.txt'  
    with open(full_path, 'w') as file:
        file.write(msg)

class HibernationPreventer:
    duration=60
    def __init__(self, duration=60):
        text_create('hdrun', 'Create Successful!\n')
        self.duration=duration
        print('''
这是一个不让硬盘休眠的程序,将本程序放至目标硬盘中,
本程序将在所在目录创建hdrun.txt并定期读写
''')

    def set_duration(self,duration):
        self.duration=duration
        print(f"本程序将每{(int)(duration/60) if duration>=60 else duration/60}分钟读写一次")
        
    def write(self):
        print("开始运行")
        n = 0
        while True:
            n += 1
            with open('hdrun.txt', "w", encoding="utf8") as f:
                f.writelines(f"第{n}次写入")
            with open('hdrun.txt', "r", encoding="utf8") as f:
                data = f.read()
            print(data)
            
            time.sleep(self.duration)
app = HibernationPreventer(60)
duration=input("输入写入的时间间隔（秒），回车以使用默认值1分钟：")
if duration:
    app.set_duration(int(duration))
app.write()