from requests_html import HTMLSession

session = HTMLSession()
resp = session.get('https://habr.com/ru/company/yandex/blog/508180/')

title = str(resp.html.xpath('//title/text()'))
h1 = str(resp.html.xpath('//span[@class="post__title-text"]/text()'))
keywords = str(resp.html.xpath('//meta[@name="keywords"]/@content'))
description = str(resp.html.xpath('//meta[@name="description"]/@content')).replace('\\r\\n','')
post = str(resp.html.xpath('//div[@id = "post-content-body"]/text()'))
post = str(post).replace(r"'\n',","")
post = str(post).replace(r"'\r\n","")
post = str(post).replace(r"',","")
post = str(post).replace(r"'.","")
post = str(post).replace(r"'","")
post = str(post).replace(r"  ","")

print('длинна title: '+str(len(title))+' символов')
print('длинна заголовка H1: '+str(len(h1))+' символов')
print('ключевые слова: '+keywords)
print('длинна описания description: '+str(len(description))+' символов')
print('количество слов в статье: '+str(len(post.split())))
