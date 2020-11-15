import os
import urllib2

url1 = "https://api1.mimikko.cn/client/love/ExchangeReward?code="++os.environ["servant"]
url2 = "&AppID=wjB7LOP2sYkaMGLC&Authorization="+os.environ["mimikko_data"]

req = urllib2.Request(url1+url2)
print req

res_data = urllib2.urlopen(req)
res = res_data.read()
print res