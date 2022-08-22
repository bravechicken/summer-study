import os
def read_all ():
    all_content = ""
    file_list = os.listdir("data")
    print(file_list)
    for file in file_list:
        a = os.path.splitext(file)
        if a[1] == ".txt":
            print(a)
            # 1.打开这个文件
            file = open(os.path.join("./data", file), "r")
            c = file.read()
            file.close()
            # 2. 读取这个文件的所有内容

            # 3.把这个新的内容，追击到all_content里面去
            all_content = all_content+c
    # 最后，打印出所有的内容
    # print(all_content)
    return all_content