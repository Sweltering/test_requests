# 1、requests.get，获取网页数据
# import requests

# resp = requests.get('https://www.baidu.com/')
# print(type(resp.text))
# print(resp.text)  # 可能会出现乱码
# print(type(resp.content))
# print(resp.content.decode('utf-8'))
# print(resp.url)
# print(resp.encoding)
# print(resp.status_code)

# params参数查询
# params = {
#     'wd': '中国'
# }
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36'
# }
# resp = requests.get('https://www.baidu.com/s', params=params, headers=headers)
# with open('baidu.html', 'w', encoding='utf-8') as f:
#     f.write(resp.content.decode('utf-8'))
# print(resp.url)


# 2、requests.post，提交data获取网页数据
# import requests
#
# lagou_url = 'https://www.lagou.com/jobs/positionAjax.json?city=%E5%8C%97%E4%BA%AC&needAddtionalResult=false'
# data = {
#     'first': 'true',
#     'pn': 1,
#     'kd': 'python'
# }
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36',
#     'Referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='
# }
# resp = requests.post(lagou_url, data=data, headers=headers)
# print(resp.json())


# 3、使用代理
# 只要在请求的方法中get或者post中传递proxies参数就可以了
# import requests
#
# proxy = {
#     'http': '180.118.73.236:9000'
# }
#
# resp = requests.get('http://httpbin.org/ip', proxies=proxy)
# print(resp.text)


# 4、cookie，通过cookie属性来获取cookie信息
# import requests
#
# resp = requests.get('https://www.baidu.com')
# print(resp.cookies)
# print(resp.cookies.get_dict())


# 5、session，想要在多次请求中共享cookie，应该使用session
# 登录人人网，访问大鹏的主页
import requests

renren_utl = 'http://www.renren.com/PLogin.do'
dapeng_url = 'http://www.renren.com/880151247/profile'
data = {
    'email': '13993601652',
    'password': 'w199548j?*'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36'
}
session = requests.Session()  # 创建一个session对象
session.post(url=renren_utl, data=data, headers=headers )  # 请求登录
resp = session.get(url=dapeng_url)  # 请求大鹏首页数据
with open('renren.html', 'w', encoding='utf-8') as f:
    f.write(resp.text)
