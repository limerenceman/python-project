import requests as r
if __name__ == "__main__":
    #UA伪装：将对应的UA封装到一个字典中
    header = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36 Edg/88.0.705.81'
    }
    url = 'https://www.baidu.com/s'
    #处理url携带的参数，封装到字典中
    kw = input('enter a word:')
    param ={
        'query': kw
    }
    #对指定的url发起请求对应的url是携带参数的，并且请求过程中处理了参数
    response = r.get(url=url,params=param,headers=header)

    page_text = response.text
    fileName = kw+'.html'
    with open(fileName,'w',encoding='utf-8') as fp:
        fp.write(page_text)
    print(fileName,'保存成功！！！')
