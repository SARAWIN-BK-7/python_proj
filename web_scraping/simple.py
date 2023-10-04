from bs4 import BeautifulSoup
import requests 



url = "https://stackpython.co/courses"


res = requests.get(url)
res.encoding = "utf-8"

# print(res
if res.status_code == 200:
    print("Success")
elif res.status_code == 404:
    print("Not Found 404 ")
else:
    print("Not both 200 and 404")
    
soup = BeautifulSoup(res.text, 'html.parser')
# print(soup.prettify())
print(soup.title.string)
print(soup.h1)

