import os
import urllib2

url = "https://api1.mimikko.cn/client/love/ExchangeReward?code=momona&AppID=wjB7LOP2sYkaMGLC&Authorization="+os.environ["mimikko_data"]

req = urllib2.Request(url)
print req

res_data = urllib2.urlopen(req)
res = res_data.read()
print res