"""
    作者：jamke
    功能：计算空气质量指数AQI
    版本：4.0
    日期：2019.3.19
    4.0新增功能：根据文件扩展名判断文件类型，再读取文件

    CSV文件读取：
            csv.reader()，将每行记录作为列表返回

    使用with语句操作文件对象，不管在处理文件过程中是否发生异常，
    都能保证with语句执行完毕之后自动关闭文件。不需要close()语句。
        with open('file_name') as somefile:
            for line in somefile:
                print(line)

    os模块：
            提供与系统、目录操作相关的功能，不受平台的限制
            os.remove()
            os.makedirs()
            os.rmdir()
            os.rename()
            os.path.isfile()
            os.path.isdir()
            os.path.join()
            os.path.splitext(),如：将tmp.txt切分为tmp和.txt
"""
import json
import csv
import os


def process_csv_file(file_path):
    """
        处理csv文件
    """
    with open(file_path, 'r', encoding='utf-8', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            print('+'.join(row))


def process_json_file(file_path):
    """
        处理json文件
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        city_list = json.load(f)
    print(city_list)


def main():
    """
        主函数
    """
    file_path = input('请输入文件名称：')
    file_name, file_ext = os.path.splitext(file_path)

    if file_ext == '.json':
        # json文件
        process_json_file(file_path)
    elif file_ext == '.csc':
        # csv文件
        process_csv_file(file_path)
    else:
        print('该版本目前暂不支持该文件扩展名！')


if __name__ == '__main__':
    main()
