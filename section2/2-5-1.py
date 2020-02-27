from urllib.parse import urljoin

baseURL="http://test.com/html/a.html"
print(urljoin(baseURL, "b.html"))
print(urljoin(baseURL, "sub/c.html"))
print(urljoin(baseURL,"../index.html")) #1계단 올라감.
print(urljoin(baseURL,"../../img/hong.png"))    #2계단 올라감.
print(urljoin(baseURL,"../../css/hong.png"))
