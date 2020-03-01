1.准备images-optional文件夹，存放test图片
  两种方法🕐：1是把测试图片拷贝到文件夹下；2是修改mAP/main.py中的IMG_PATH路径值；
2.准备ground_truth文件夹
   两种方法：1是测试图片少的话，直接拷贝xml文件到ground_truth文件夹下；
   2.测试图片较多的情况下，运行findxml.py，然后粘贴到ground_truth文件夹下。(findxml.py注意修改路径值)
3. 将xml文件转换为txt文件
    运行mAP/scripts/extra/covert_gt_xml.py 文件。执行后，你的xml文件自动放进了ground_truth/backup中，然后在ground_truth下生成了txt文件。
4. 准备detection-results文件夹
    1.保存test测试图片的结果，运行k-yolov3/yolo_test_result_only.py得到result.txt;
    2.执行scripts/extra/make_dr.py（注意修改文件路径），即可得到detection-results文件夹下的txt文件。
5.得到mAP
    运行mAP/main.py即可得到模型的mAP了。