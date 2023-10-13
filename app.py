import pygsheets
import os
os.environ['HTTP_PROXY'] = 'http://127.0.0.1:7890'
os.environ['HTTPS_PROXY'] = 'http://127.0.0.1:7890'
client = pygsheets.authorize(service_file = "./testpygsheets.json")

# 打开谷歌表格testPygSheets
sh = client.open('testPygSheets')

#获取表格中的而第一张工作表
wks = sh.sheet1

# 写入A1数据
wks.update_value('A1', "我是A1的内容")
wks.update_value('A2', "我是A2的内容")
wks.update_value('A3', "我是A3的内容")

#读取C3数据
get=wks.get_value('C3')
print(get)
