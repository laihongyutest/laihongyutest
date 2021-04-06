import requests
import json


class TestLottery:

    def __init__(self):
        self.url_del = 'http://192.168.15.250/common/delTestUserData'
        self.url_lottery = 'http://120.205.22.79:37785/common/userCommonLottery'
        self.params_del = {'code': 'koznak_double_twelve', 'uid': 'oc_88138307933318485321606844678'}
        self.params = {'code': 'koznak_double_twelve', 'platform': 'koznak', 'user_type': '3',
                       'uid': 'oc_88138307933318485321606844678', 'token': '1b19b4719e69216087fbea947ac8376c',
                       'version': '7.3.0.iOS_Koznak_release'}
        self.url_lottery_times = 'http://120.205.22.79:37785/common/completeActivityTask'
        self.param_lottery_times = {'code': 'koznak_double_twelve', 'platform': 'koznak',
                                    'uid': 'oc_88138307933318485321606844678', 'task_id': '4'}

    # 判断用户token是否过期,如果过期重新获取token
    def get_token(self):
        pass

    # 调用get请求
    def get_method(self, url, param=None):
        request = requests.get(url=url, params=param)
        res = json.loads(request.text)
        return res

    # 清除用户已经抽过奖接口
    def clear_lottery(self):
        response = self.get_method(url=self.url_del, param=self.params_del)
        if response['code'] == 1001 and response['message'] == "清除成功":
            return '清除成功'
        else:
            return '清除失败'

    # 刷新用户抽奖次数
    def update_lottery(self):
        response = self.get_method(url=self.url_lottery_times, param=self.param_lottery_times)
        if response['message'] == '操作成功':
            return response
        else:
            print('获取失败')

    # 抽奖
    def lottery(self):
        res = self.get_method(url=self.url_lottery, param=self.params)
        return res

    # 计算抽奖数和概率
    def cal_lot_per(self, x):
        """"
        vip_numb为vip中奖数量，vip为中奖概率
        goal_numb积分中奖数量，goal为积分概率
        money_numb为中现金数量，money为现金概率
        no_list为未中奖数量
        """
        vip_numb = 0
        goals_numb = 0
        money_numb = 0
        miss_numb = 0
        i = 1
        try:
            while i <= x:
                # 先清除用户已经抽过奖
                self.clear_lottery()
                # 获取该用户抽奖次数
                self.update_lottery()
                # 抽奖，并且拿取抽奖结果
                response = self.lottery()
                # print(response)
                # 判断抽奖结果
                if response["data"] != '' and response['data'] != 0:
                    if response['data']['gift_name'] == '1日会员':
                        vip_numb = vip_numb + 1
                    elif response['data']['gift_name'][-2:] == '积分':
                        goals_numb = goals_numb + 1
                    elif response['data']['gift_name'][-1] == '元':
                        money_numb = money_numb + 1
                elif response["data"] != '' and response['data'] == 0:
                    print("token已过期")
                    break
                else:
                    if response['message'] == '谢谢参与':
                        miss_numb = miss_numb + 1
                        print("抽红包超限")
                        break
                    elif response['message'] == '无剩余抽奖次数':
                        print("没有抽奖次数，没有清理干净")
                i += 1

            count_numb = x
            vip = "%.2f%%" % (vip_numb / count_numb * 100)
            goal = "%.2f%%" % (goals_numb / count_numb * 100)
            money = "%.2f%%" % (money_numb / count_numb * 100)

            print("用户第一次抽奖--抽中vip次数:%d，抽中vip概率：%s" % (vip_numb, vip))
            print("用户第一次抽奖--抽中积分次数:%d，抽中分数概率：%s" % (goals_numb, goal))
            print("用户第一次抽奖--抽中现金次数:%d，抽中现金概率：%s" % (money_numb, money))
            print("一共抽奖：%s次" % x)

        except Exception as e:
            print('抽奖报错:{}'.format(e))


if __name__ == "__main__":
    test = TestLottery()
    lot = test.cal_lot_per(100)
