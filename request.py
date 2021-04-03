import requests
if __name__ == "__main__":#相当于程序从这开始执行
    #step 1:指定url
    url = 'https://www.sogou.com'
    #step 2:发起请求
    #get方法会返回一个响应对象
    response = requests.get(url=url)
    #step 3:获取响应数据,text返回的是字符串形式的响应数据
    page_text = response.text
    #step 4:持久化数据
    with open('./sogou.html','w',encoding='utf-8') as fp:
        fp.write(page_text)
    print("爬取数据结束！！！")
