import os
import shutil
import time

src = "C:/Users/dutta/Downloads"
dest = "D:/downloads"

extList = ['.txt', '.doc', '.docx', '.pdf']

fileList = os.listdir(src)

for i in fileList:
    a = os.path.splitext(i)
    if  a[1] in extList:
        print("checking item")
        for i in extList:
            if a[1] in extList :
                    file_name = a[0]
                    print('downloaded '+ file_name)
                    path1 = src + '/' + file_name
                    path2 = dest + '/' + "doc_files"
                    path3 = dest +'/' + "doc_files" + '/' + file_name

                    if os.path.exists(path2):
                        print("dir exists")
                        print ("moving file "+ file_name)
                        shutil.move(path1,path3)
                        time.sleep(1)
                    else:
                        print("making dir")
                        os.makedirs(path2)
                        print ("moving file "+ file_name)
                        shutil.move(path1,path3)
                        time.sleep(1)
   
