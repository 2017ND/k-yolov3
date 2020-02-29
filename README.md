# k-yolov3
keras-yolov3训练，加载conv74.74权重，检测图片、视频，保存结果，计算mAP


1.利用labelImg进行样本标注，产生xml文件，存放在voc2007下的Annotations文件夹下；
2.将原始图片数据存放到VOC2007文件夹下的JPEGImages文件夹下；
3.修改model_data文件夹下的voc_classes.txt文件，将类别名称填入；
4.运行VOC2007文件夹下的split.py文件，得到ImageSets/Main下的4个txt文件；
5.修改voc_annotation.py文件中的classes = ["类别1","类别2"......]， 后运行该py文件，得到trainTxt文件夹下的三个txt；
6.修改cfg/yolov3.cfg文件，需要修改共4处地方，1.根据电脑配置设置batch和subdivision的值；2.（共3处）修改送入[yolo]层的fliters值(3*(5+num_classes))和[yolo]层中的calsses值， random：原来是1，显存小改为0;
7.运行my_train.py文件，开展训练，修改py文件中的batchsize和epochs值；
8.在Terminal中运行python yolo_video.py --image，等到出现Input image filename输入即可检测图片；
9.在Terminal中运行python yolo_video.py即可视频，修改yolo.py文件中的detect_video函数参数即可检测不同视频源；设置保存路径，可将检测结果视频为.mp4文件；
10.运行detec_all.py即可完成批量图片检测；
11.运行convert.py 可以将.weights文件转换为.h5文件。
