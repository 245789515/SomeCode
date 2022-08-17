# -*- coding: cp936 -*-
import urllib
import urllib2
import time

url = 'http://210.77.16.21/eportal/InterFace.do?method=login'
request = urllib2.Request(url)
request.add_header('Host','210.77.16.21')
request.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0')
request.add_header('Accept','*/*')
request.add_header('Accept-Language','zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3')
request.add_header('Accept-Encoding','gzip,deflate')
request.add_header('Content-Type','application/x-www-form-urlencoded; charset=UTF-8')
#request.add_header('Referer','http://210.77.16.21/eportal/index.jsp?wlanuserip=0bc386d9e643d188b011a0d00c9b5c40&wlanacname=5fcbc245a7ffdfa4&ssid=&nasip=2c0716b583c8ac3cbd7567a84cfde5a8&mac=53ba540bde596b811a6d5617a86fa028&t=wireless-v2&url=2c0328164651e2b4f13b933ddf36628bea622dedcc302b30')
#request.add_header('Content-Length','353')
#request.add_header('Cookie','EPORTAL_COOKIE_OPERATORPWD=; EPORTAL_COOKIE_USERNAME=; EPORTAL_COOKIE_PASSWORD=; EPORTAL_COOKIE_SERVER=; EPORTAL_COOKIE_SERVER_NAME=; EPORTAL_AUTO_LAND=; JSESSIONID=0F11A494564B5DA4C8F5E8A6D2ACDD9F')
#request.add_header('Connection','keep-alive')

username = '' #账号
password = '' #密码

data = 'userId='+username+'&password='+password+'&service=&queryString=wlanuserip%253D0bc386d9e643d188b011a0d00c9b5c40%2526wlanacname%253D5fcbc245a7ffdfa4%2526ssid%253D%2526nasip%253D2c0716b583c8ac3cbd7567a84cfde5a8%2526mac%253D53ba540bde596b811a6d5617a86fa028%2526t%253Dwireless-v2%2526url%253D2c0328164651e2b4f13b933ddf36628bea622dedcc302b30&operatorPwd=&validcode='
response = urllib2.urlopen(request,data)
code = response.getcode()
print code
res = response.read()
print res
'''
exec("res="+res)

print 'code:',code
print 'result:',res['result']
print 'message:',res['message']

if 'success' in res['result']:
        #print username
        print 'ok!'
'''


time.sleep(3)
