"""
    作者：jamke
    功能：计算空气质量指数AQI
    版本：3.0
    日期：2019.3.19
    3.0新增功能：读取已经获取的JSON格式的数据，转换成CSV格式
    CSV格式：
            以行为单位，
            每一行是一个对象，
            以英文逗号分割每列数据，
            列名通常放在文件第一行
    csv.writer(file).writerow([])，将列表元素写入文件的一行
"""
import json
import csv


def process_json_file(file_path):
    """
        解码json文件
    """
    f = open(file_path, 'r', encoding='utf-8')
    city_list = json.load(f)
    return city_list


def main():
    """
        主函数
    """
    file_path = input('请输入JSON文件名称：')
    city_list = process_json_file(file_path)
    city_list.sort(key=lambda x: x['iaqi'])

    lines = [list(city_list[0].keys())]
    for city in city_list:
        lines.append(city.values())

    f = open('aqi.csv', 'w', encoding='utf-8', newline='')
    writer = csv.writer(f)
    for line in lines:
        writer.writerow(line)
    f.close()


if __name__ == '__main__':
    main()
