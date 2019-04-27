"""
    作者：jamke
    功能：计算空气质量指数AQI
    版本：5.0
    日期：2019.3.19
    5.0新增功能：网络爬虫，获取城市的AQI
    网络爬虫：自动抓取互联网信息
            步骤：1.通过网络链接获取网页内容
                 2.对获得的网页内容进行处理
    request模块：处理HTTP请求的工具支持丰富的链接访问功能，
                包括URL获取，HTTP会话，cookie记录
    request网页请求：
            get()，对应HTTP的GET方式，拉取网页数据
            post()，对应HTTP的POST方式，推送用户数据
    request对象属性：
            status_code：HTTP请求的返回状态，200表示连接成功，400表示失败
            text：HTTP相应内容的字符串形式，即url对应的页面内容
    参考：http://docs.python-request.org/
"""
import requests


def get_html_text(url):
    """
        获取url的文本
    """
    r = requests.get(url, timeout=30)
    # print(r.status_code)
    return r.text


def main():
    """
        主函数
    """
    city_pinyin = input('请输入城市名字拼音：')
    url = 'http://pm25.in/' + city_pinyin
    url_text = get_html_text(url)
    # print(url_text)

    # 不灵活的方法
    aqi_div = '''<div class="span12 data">
        <div class="span1">
          <div class="value">
            '''
    index = url_text.find(aqi_div)
    print(index)
    begin_index = index + len(aqi_div)
    end_index = begin_index + 3
    aqi_val = url_text[begin_index:end_index]
    print('空气质量为{}'.format(aqi_val))


if __name__ == '__main__':
    main()
