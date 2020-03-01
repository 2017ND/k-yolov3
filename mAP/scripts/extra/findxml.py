import os
import shutil

testfilepath='/home/bu807/Downloads/keras-yolo3-master2/keras-yolo3-master2/test'
xmlfilepath = '/home/bu807/Downloads/keras-yolo3-master2/keras-yolo3-master2/VOCdevkit/VOC2007/Annotations/'
xmlsavepath = '/home/bu807/Downloads/keras-yolo3-master2/keras-yolo3-master2/mAP-master/input/ground-truth/'
test_jpg = os.listdir(testfilepath)

num = len(test_jpg)
list = range(num)
L=[]

for i in list:
    name = test_jpg[i][:-4] + '.xml'
    L.append(name)

for filename in L:
    shutil.copy(os.path.join(xmlfilepath,filename),xmlsavepath)