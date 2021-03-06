"""
    作者：jamke
    功能：获取空气质量指数AQI
    日期：2019.7.20

    学到的点（踩过的坑）：
    1.程序运行的时间：
        程序执行时间=cpu时间 + io时间 + 休眠或者等待时间
        import datetime，datetime.datetime.now()和import time，time.time()测的时间包含了其他程序使用CPU的时间（程序执行时间）
        import time，time.clock()测的是该程序使用CPU的时间（程序运行时间）
        https://blog.csdn.net/wangshuang1631/article/details/54286551

        from timeit import timeit，timtit()经常用来测某个语句多次执行的时间（取平均，去误差）
        from timeit import repeat，repeat()通过重复测，取最小时间作为运行时间
        https://www.cnblogs.com/PrettyTom/p/6657984.html
    2.网页访问过于频繁：
    暂时解决办法：
        1.设置requests的timeout
        2.访问一个网页，休眠0.1秒

"""
import requests
from bs4 import BeautifulSoup
import pandas
import matplotlib.pyplot as plt
import time
# from timeit import repeat
# from timeit import timeit

print('...模块加载完毕')
# 解决中文和负数显示问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


# 根据PM2.5和CO的浓度计算AQI
# 1.实现两种污染物对应的IAQI（IAQI：空气质量分指数）
#     1个输入参数，即cp
# 2.实现线性缩放函数
#     5个输入参数
# def get_html_text(url):
#     """
#         获取url的文本
#     """
#     r = requests.get(url, timeout=30)
#     # print(r.status_code)
#     return r.text
#
#
# def cal_linear(iaqi_lo, iaqi_hi, bp_lo, bp_hi, cp):
#     """
#         范围缩放
#     """
#     iaqi = (iaqi_hi - iaqi_lo) * (cp - bp_lo) / (bp_hi - bp_lo) + iaqi_lo
#     return iaqi
#
#
# def cal_pm_iaqi(pm_val):
#     """
#         计算pm2.5的IAQI
#     """
#     iaqi = 0
#     if 0 <= pm_val < 36:
#         iaqi = cal_linear(0, 50, 0, 35, pm_val)
#     elif 36 <= pm_val < 76:
#         iaqi = cal_linear(50, 100, 35, 75, pm_val)
#     elif 76 <= pm_val < 116:
#         iaqi = cal_linear(100, 150, 75, 115, pm_val)
#     elif 116 <= pm_val < 151:
#         iaqi = cal_linear(150, 200, 115, 150, pm_val)
#     elif 151 <= pm_val < 251:
#         iaqi = cal_linear(200, 300, 150, 250, pm_val)
#     elif 251 <= pm_val < 351:
#         iaqi = cal_linear(300, 400, 250, 350, pm_val)
#     elif 351 <= pm_val < 501:
#         iaqi = cal_linear(400, 500, 350, 500, pm_val)
#     return iaqi
#
#
# def cal_co_iaqi(co_val):
#     """
#         计算CO的IAQI，24小时的CO浓度
#     """
#     iaqi = 0
#     if 0 <= co_val < 3:
#         iaqi = cal_linear(0, 50, 0, 2, co_val)
#     elif 3 <= co_val < 5:
#         iaqi = cal_linear(50, 100, 2, 4, co_val)
#     elif 5 <= co_val < 15:
#         iaqi = cal_linear(100, 150, 4, 14, co_val)
#     elif 15 <= co_val < 25:
#         iaqi = cal_linear(150, 200, 14, 24, co_val)
#     elif 25 <= co_val < 37:
#         iaqi = cal_linear(200, 300, 24, 36, co_val)
#     elif 37 <= co_val < 49:
#         iaqi = cal_linear(300, 400, 36, 48, co_val)
#     elif 49 <= co_val < 61:
#         iaqi = cal_linear(400, 500, 48, 60, co_val)
#     return iaqi
#
#
# def cal_aqi(param_list):
#     """
#         计算AQI
#     """
#     pm_val = param_list[0]
#     co_val = param_list[1]
#
#     pm_iaqi = cal_pm_iaqi(pm_val)
#     co_iaqi = cal_co_iaqi(co_val)
#
#     iaqi_list = [pm_iaqi, co_iaqi]
#
#     aqi = max(iaqi_list)
#
#     return aqi
#
#
# def main():
#     """
#         主函数
#     """
#     print('请输入以下信息，用空格分割')
#     input_str = input('(1)PM2.5 (2)CO:')
#     str_list = input_str.split(' ')
#     pm_val = float(str_list[0])
#     co_val = float(str_list[1])
#
#     param_list = [pm_val, co_val]
#
#     # 调用AQI计算函数
#     aqi = cal_aqi(param_list)
#
#     print('空气质量指数为：{}'.format(aqi))
def get_url(city=''):
    """
        获取所有城市的URL
    """
    url = 'http://www.pm25.com/rank.html'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    ul = soup.find('ul', class_='pj_area_data_details rrank_box')
    ali = ul.find_all('a')
    city_name = []
    for i in ali:
        city_name.append(i.text)
    url_li = []
    for i in city_name:
        url_li.append('http://www.pm25.com/city/' + i + '.html')
    if city == '':
        print('...网页URL获取完毕')
        return url_li
    else:
        if city in city_name:
            print('...网页URL获取完毕')
            return 'http://www.pm25.com/city/' + city + '.html'


def get_info(url='http://www.pm25.com/city/guangzhou.html'):
    """
        获取一个城市的信息：名字、AQI和pm2.5
    """
    r = requests.get(url, timeout=5000)
    soup = BeautifulSoup(r.text, 'lxml')
    city_name = soup.find('span', class_='city_name').text
    aqi = int(soup.find('a', class_='cbol_aqi_num').text)
    pm25 = int(soup.find('span', class_='cbol_nongdu_num_1').text)
    dic = {'城市': city_name, 'aqi': aqi, 'pm2.5(ug/m^3)': pm25}
    return dic


def main():
    """
        主函数
    """

    start = time.clock()
    url_li = get_url()
    inf = []
    for i in url_li:
        inf.append(get_info(i))
        time.sleep(0.1)
    end = time.clock()
    print('...数据采集完毕，所用时间为{}'.format(end-start))
    df = pandas.DataFrame(inf)
    # 数据清洗
    df = df[df['aqi'] > 0]
    print(df.sort_values(by='aqi', ascending=True))
    top50_city = df.sort_values(by='aqi', ascending=True).head(50)
    top50_city.plot(figsize=(20, 10), kind='barh', title='空气质量指数最好的前50个城市', x='城市', y='aqi')
    plt.savefig('top50_city.png')
    plt.show()


if __name__ == '__main__':
    main()
    # 由于电脑永远有其他程序占用资源，所以这个程序基本不可能高效运行，为了尽量排除偶然因素，用repeat更好
    # t = repeat('main()', 'from __main__  import main', number=1, repeat=5)
    # timeit经常用于测试一行语句的运行时间，默认执行1000,000次
    # t = timeit('[0 for _ in range(10)]', number=1)
