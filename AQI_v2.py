"""
    作者：jamke
    功能：获取国内城市的空气质量指数（AQI)排名
    日期：2019.7.22

    学到的点（踩过的坑）：
    1.pd.DataFrame.plot 要求y是数值型变量，所以需要把y所在的数据用astype(如int)进行转换
        https://www.cnblogs.com/lsdb/p/9277850.html
    2.将两个列表组成字典用dict(zip(键list, 值list))
        https://blog.csdn.net/u011089523/article/details/60144772
    3.pd.DataFrame 将字典转换成pd.DataFrame，要使字典的键和值都为列，则可以
        pd.DataFrame({'第一列':list(dic.keys()), '第二列':list(dic.values())})
        https://blog.csdn.net/u013061183/article/details/79497254


"""
import requests
from bs4 import BeautifulSoup
import pandas
import matplotlib.pyplot as plt

# 解决中文和负数显示问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

print('模块加载完毕')


def get_info_now(url='http://www.pm25.com/rank.html'):
    """
        获取国内城市实时的排名信息：排名（最差状况排名）、空气质量状况、城市、省份、AQI和PM2.5浓度
    """
    r = requests.get(url)
    print('...网页抓取完毕')
    soup = BeautifulSoup(r.text, 'lxml')
    ul = soup.find('ul', class_='pj_area_data_details rrank_box')
    li_lis = ul.find_all('li')
    inf = []
    for li in li_lis:
        city_rank = li.find('span', class_='pjadt_ranknum').text
        city_name = li.find('a', class_='pjadt_location').text
        city_prov = li.find('span', class_='pjadt_sheng').text
        aqi = li.find('span', class_='pjadt_aqi').text
        pm25 = li.find('span', class_='pjadt_pm25').text.split(' ')[0]
        dic = {'排名': city_rank, '城市': city_name, '省份': city_prov, 'aqi': aqi, 'pm2.5(ug/m^3)': pm25}
        inf.append(dic)
    print('...数据采集完毕')
    return inf


def get_info_day(url='http://www.pm25.com/rank/1day.html'):
    """
        获取国内城市昨天的排名信息：排名（最差状况排名）、空气质量状况、城市、省份、AQI和PM2.5浓度
    """
    r = requests.get(url)
    print('...网页抓取完毕')
    soup = BeautifulSoup(r.text, 'lxml')
    ul = soup.find('ul', class_='pj_area_data_details rrank_box')
    li_lis = ul.find_all('li')
    inf = []
    for li in li_lis:
        city_rank = li.find('span', class_='pjadt_ranknum').text
        city_name = li.find('a', class_='pjadt_location').text
        city_prov = li.find('span', class_='pjadt_sheng').text
        aqi = li.find('span', class_='pjadt_aqi').text
        pm25 = li.find('span', class_='pjadt_pm25').text.split(' ')[0]
        dic = {'排名': city_rank, '城市': city_name, '省份': city_prov, 'aqi': aqi, 'pm2.5(ug/m^3)': pm25}
        inf.append(dic)
    print('...数据采集完毕')
    return inf


def get_info_week(url='http://www.pm25.com/rank/7day.html'):
    """
        获取国内城市一周的排名信息：排名（最差状况排名）、空气质量状况、城市、省份、AQI和PM2.5浓度
    """
    r = requests.get(url)
    print('...网页抓取完毕')
    soup = BeautifulSoup(r.text, 'lxml')
    ul = soup.find('ul', class_='pj_area_data_details rrank_box')
    li_lis = ul.find_all('li')
    inf = []
    for li in li_lis:
        city_rank = li.find('span', class_='pjadt_ranknum').text
        city_name = li.find('a', class_='pjadt_location').text
        city_prov = li.find('span', class_='pjadt_sheng').text
        aqi = li.find('span', class_='pjadt_aqi').text
        pm25 = li.find('span', class_='pjadt_pm25').text.split(' ')[0]
        dic = {'排名': city_rank, '城市': city_name, '省份': city_prov, 'aqi': aqi, 'pm2.5(ug/m^3)': pm25}
        inf.append(dic)
    print('...数据采集完毕')
    return inf


def get_info_month(url='http://www.pm25.com/rank/30day.html'):
    """
        获取国内城市一个月的排名信息：排名（最差状况排名）、空气质量状况、城市、省份、AQI和PM2.5浓度
    """
    r = requests.get(url)
    print('...网页抓取完毕')
    soup = BeautifulSoup(r.text, 'lxml')
    ul = soup.find('ul', class_='pj_area_data_details rrank_box')
    li_lis = ul.find_all('li')
    inf = []
    for li in li_lis:
        city_rank = li.find('span', class_='pjadt_ranknum').text
        city_name = li.find('a', class_='pjadt_location').text
        city_prov = li.find('span', class_='pjadt_sheng').text
        aqi = li.find('span', class_='pjadt_aqi').text
        pm25 = li.find('span', class_='pjadt_pm25').text.split(' ')[0]
        dic = {'排名': city_rank, '城市': city_name, '省份': city_prov, 'aqi': aqi, 'pm2.5(ug/m^3)': pm25}
        inf.append(dic)
    print('...数据采集完毕')
    return inf


def main():
    """
        主函数
    """
    inf = get_info_now()
    df = pandas.DataFrame(inf)

    df['aqi'] = df['aqi'].astype(int)
    df['pm2.5(ug/m^3)'] = df['pm2.5(ug/m^3)'].astype(int)

    # 空气质量状况前50城市
    top50_city = df.tail(50)
    top50_city.plot(kind='barh', figsize=(20, 10), x='城市', y='aqi', title='空气质量状况前50的城市')
    plt.savefig('top50_city.png')
    plt.show()

    # 空气质量状况前50城市的省份分布
    top50_sheng_ = set(top50_city['省份'])
    dic = dict(zip(list(top50_sheng_), [0 for _ in range(len(top50_sheng_))]))
    # print(top50_sheng_)
    for city in top50_city['省份']:
        for sheng in dic.keys():
            if city == sheng:
                dic[sheng] += 1
    # print(dic)
    top50_sheng = pandas.DataFrame({'省份': list(dic.keys()), '城市个数': list(dic.values())})
    # print(top50_sheng)
    top50_sheng.plot(kind='barh', figsize=(20, 10), x='省份', y='城市个数', title='空气质量状况前50城市的省份分布')
    plt.savefig('top50_sheng.png')
    plt.show()


if __name__ == '__main__':
    main()
