f = open('/home/bu807/Downloads/keras-yolo3-master2/keras-yolo3-master2/result/result.txt',encoding='utf8')
s = f.readlines()
result_path ='/home/bu807/Downloads/keras-yolo3-master2/keras-yolo3-master2/mAP-master/input/detection-results/'

for i in range(len(s)):  # 中按行存放的检测内容，为列表的形式
    r = s[i].split('.jpg ')
    file = open(result_path + r[0] + '.txt', 'w')
    if len(r[1]) > 5:
        t = r[1].split(';')
        # print('len(t):',len(t))
        if len(t) == 3:
            file.write(t[0] + '\n' + t[1] + '\n')  # 有两个对象被检测出
        elif len(t) == 4:
            file.write(t[0] + '\n' + t[1] + '\n' + t[2] + '\n')  # 有三个对象被检测出
        elif len(t) == 5:
            file.write(t[0] + '\n' + t[1] + '\n' + t[2] + '\n' + t[3] + '\n')  # 有四个对象被检测出
        elif len(t) == 6:
            file.write(t[0] + '\n' + t[1] + '\n' + t[2] + '\n' + t[3] + '\n' + t[4] + '\n')  # 有五个对象被检测出
        elif len(t) == 7:
            file.write(t[0] + '\n' + t[1] + '\n' + t[2] + '\n' + t[3] + '\n' + t[4] + '\n' + t[5] + '\n')  # 有六个对象被检测出

        else:
            file.write(t[0] + '\n')  # 有一个对象
    else:
        file.write('')  # 没有检测出来对象，创建一个空白的对象