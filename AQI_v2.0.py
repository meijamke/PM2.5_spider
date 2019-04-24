"""
    作者：jamke
    功能：计算空气质量指数AQI
    版本：2.0
    日期：2019.3.18
    2.0新增功能：读取已经获取的JSON格式的数据，并获取前5的数据
    JSON格式：[{"键":值}, {"键":值}, ......]
    JSON格式是采用对象、数组方式组织起来的键值对可以表示任何结构的数据
    JSON库：dumps()：python数据格式——>JSON
            loads()：JSON——>python数据格式
            dump()：输出到文件
            load()：读取文件
    list.sort(fun)，fun简单的时候可以用lamda函数
"""
import json


def process_json_file(file_path):
    """
        解码json文件
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        city_list = json.load(f)
        return city_list


def main():
    """
        主函数
    """
    file_path = input('请输入JSON文件名称：')
    city_list = process_json_file(file_path)
    city_list.sort(key=lambda city: city['iaqi'])
    top5_list = city_list[:5]

    # 输出到文件
    f = open('top5_aqi.json', 'w', encoding='utf-8')
    json.dump(top5_list, f, ensure_ascii=False)
    f.close()


if __name__ == '__main__':
    main()
