"""
1.查看指定网站的robots.txt 文件,明确资源获取的规则
2.按照request库,用于发送网络请求(发送请求,获取资源,第三方库)
3.编写python代码,访问网站,获取资源

"""
import requests
from lxml import html

#定义URL
target_url = "https://www.tiobe.com/tiobe-index/"
#发送请求,获取数据
response=requests.get(target_url)

#输出信息到控制
document = html.fromstring(response.text)

#解析数据

th_list = document.xpath("//*[@id='top20']/thead/tr/th/text()")
print(th_list)

tr_list = document.xpath("//table[@id='top20']/tbody/tr")
for tr in tr_list:
    td_list = tr.xpath("./td/text()")
    print(td_list)