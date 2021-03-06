import re
import urllib
import urllib.request 
def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read().decode("utf8")
    return html

def getArticleUrl(html):
    reg = r'(https://www.cnblogs.com/'+blog_name+'/p/[0-9]+.html)'
    articleUrl = re.findall(reg,html)
    return articleUrl

blog_name = input("请输入博主昵称：");
article = []
htmlStr = getHtml("http://www.cnblogs.com/"+blog_name+"/default.html")
for i in range(1,10):
    html = getHtml("http://www.cnblogs.com/"+blog_name+"/default.html?page="+str(i))
    articleUrl = getArticleUrl(html)
    if len(articleUrl)==0:
        break;
    article = article.__add__(articleUrl)

article = list(set(article))
print(article)
