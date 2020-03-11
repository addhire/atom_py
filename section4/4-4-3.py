import simplejson as json
import urllib.request as req
import os.path, random

#url
url="https://api.github.com/repositories"

#경로 & 파일명
savename = 'D:/atom_py/section4/repo.json'

if not os.path.exists(url):
    req.urlretrieve(url,savename) #url이 경로에 저장된다.

items = json.loads(open(savename, "r", encoding="utf-8").read())

for item in items:
    print(item["full_name"]+" - "+item["owner"]["url"])

#
