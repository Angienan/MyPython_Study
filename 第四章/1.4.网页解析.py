"""
网页解析指:从原始HTML文档当中提取数据的过程,也是网络机器人的关键步骤,解析HTML文档,提取需要的信息

lxml : 一个高性能HTML/XML文档的解析库,支持基于Xpath语法来解析和获取页面数据
安装 : pip install lxml

Xpath : 是一种用于在HTML/XML 文档中定位节点的语言,常用于解析HTML/XML文档
"""
from lxml import html

with open("","r",encoding="utf-8") as f:
    html_text = f.read()

    doc =html.fromstring(html_text)

    th_list = doc.xpath("//table/thead/tr/th/text()")


td_list = doc.xpath("//table/tbody/tr")
for tr in td_list:
    td_list = tr.xpath("./td/text()")
    print(td_list)

