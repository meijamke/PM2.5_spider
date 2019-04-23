"""
    作者：jamke
    功能：计算空气质量指数AQI
    版本：1.0
    日期：2019.3.18
    1.实现每种污染物对应的IAQI
        1个输入参数，即Cp
    2.实现线性缩放函数
        5个输入参数
"""


def cal_linear(iaqi_lo, iaqi_hi, bp_lo, bp_hi, cp):
    """
        范围缩放
    """
    iaqi = (iaqi_hi - iaqi_lo) * (cp - bp_lo) / (bp_hi - bp_lo) + iaqi_lo
    return iaqi


def cal_pm_iaqi(pm_val):
    """
        计算pm2.5的IAQI
    """
    if 0 <= pm_val < 36:
        iaqi = cal_linear(0, 50, 0, 35, pm_val)
    elif 36 <= pm_val < 76:
        iaqi = cal_linear(50, 100, 35, 75, pm_val)
    elif 76 <= pm_val < 116:
        iaqi = cal_linear(100, 150, 75, 115, pm_val)
    elif 116 <= pm_val < 151:
        iaqi = cal_linear(150, 200, 115, 150, pm_val)
    elif 151 <= pm_val < 251:
        iaqi = cal_linear(200, 300, 150, 250, pm_val)
    elif 251 <= pm_val < 351:
        iaqi = cal_linear(300, 400, 250, 350, pm_val)
    elif 351 <= pm_val < 501:
        iaqi = cal_linear(400, 500, 350, 500, pm_val)
    return iaqi


def cal_co_iaqi(co_val):
    """
        计算CO的IAQI，24小时的CO浓度
    """
    if 0 <= co_val < 3:
        iaqi = cal_linear(0, 50, 0, 2, co_val)
    elif 3 <= co_val < 5:
        iaqi = cal_linear(50, 100, 2, 4, co_val)
    elif 5 <= co_val < 15:
        iaqi = cal_linear(100, 150, 4, 14, co_val)
    elif 15 <= co_val < 25:
        iaqi = cal_linear(150, 200, 14, 24, co_val)
    elif 25 <= co_val < 37:
        iaqi = cal_linear(200, 300, 24, 36, co_val)
    elif 37 <= co_val < 49:
        iaqi = cal_linear(300, 400, 36, 48, co_val)
    elif 49 <= co_val < 61:
        iaqi = cal_linear(400, 500, 48, 60, co_val)
    return iaqi


def cal_aqi(param_list):
    """
        计算AQI
    """
    pm_val = param_list[0]
    co_val = param_list[1]

    pm_iaqi = cal_pm_iaqi(pm_val)
    co_iaqi = cal_co_iaqi(co_val)

    iaqi_list = [pm_iaqi, co_iaqi]

    aqi = max(iaqi_list)

    return aqi


def main():
    """
        主函数
    """
    print('请输入以下信息，用空格分割')
    input_str = input('(1)PM2.5 (2)CO:')
    str_list = input_str.split(' ')
    pm_val = float(str_list[0])
    co_val = float(str_list[1])

    param_list = [pm_val, co_val]

    # 调用AQI计算函数
    aqi = cal_aqi(param_list)

    print('空气质量指数为：{}'.format(aqi))


if __name__ == '__main__':
    main()
