from requests_html import HTMLSession

session = HTMLSession()
resp = session.get(f'https://habr.com/ru/company/yandex/blog/508180/')

title = str(resp.html.xpath('//title/text()'))
h1 = str(resp.html.xpath('//span[@class="post__title-text"]/text()'))
keywords = str(resp.html.xpath('//meta[@name="keywords"]/@content'))
description = str(resp.html.xpath('//meta[@name="description"]/@content')).replace('\\n','')
post = str(resp.html.xpath('//div[@id = "post-content-body"]/text()')).replace('\\n','')
print(title)
print(h1)
print(keywords)
print(description)
print(post)
