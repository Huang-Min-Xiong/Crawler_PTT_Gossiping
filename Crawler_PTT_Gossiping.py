import urllib.request as req
from bs4 import BeautifulSoup


#取得資訊
def GetData(url):
    #設置Request Headers資訊
    request=req.Request(url,headers={
        "cookie":"over18=1",
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
    })

    with req.urlopen(request) as response:
        data=response.read().decode("utf-8") #解碼

    Data=BeautifulSoup(data,"html.parser") #解析原始碼
    titles=Data.find_all("div", class_="title") #尋找所有class="title"的div標籤

    for title in titles:
        #如果標題存在，就顯示資訊
        if title.a !=None:
            title_url='https://www.ptt.cc'+title.a['href'] #標題網址
            print(title.a.string)
            print('網址:'+title_url+'\n')


if __name__ == "__main__":
    url="https://www.ptt.cc/bbs/Gossiping/index.html" #Ptt八卦版網址
    GetData(url)







