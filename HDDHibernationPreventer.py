import time
import os
cwd=os.path.dirname(__file__)+'\\'

def text_create(name, msg):
    full_path = cwd + name + '.txt'
    print(full_path)
    with open(full_path, 'w') as file:
        file.write(msg)


class HibernationPreventer:
    duration = 60
    txt_name = "nohibernation"

    def __init__(self):
        text_create(self.txt_name, 'Create Successful!\n')

    def set_duration(self, duration):
        self.duration = duration
        print(f"本程序将每{(int)(duration/60) if duration>=60 else duration/60}分钟读写一次硬盘")

    def write(self):
        print("开始运行")
        n = 0
        path=cwd+self.txt_name+'.txt'
        while True:
            n += 1
            with open(path, "w", encoding="utf8") as f:
                f.writelines(f"第{n}次写入")
            with open(path, "r", encoding="utf8") as f:
                data = f.read()
            print(data)

            time.sleep(self.duration)


app = HibernationPreventer()
duration = input("输入写入的时间间隔（秒），回车以使用默认值1分钟：")
if duration:
    app.set_duration(int(duration))
app.write()
