from bs4 import BeautifulSoup
import requests 
import csv 



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
# print(soup.title.string)
# print(soup.h1)

courses = soup.find_all('h2')

course_list = [] 

for course in courses:
    
    # Create a new variable --> obj to store
    # only courses name getting rid of unwanted tages
    
    obj = course.string
    
    # Append each course into a caurse_list variable 

    course_list.append(obj)
    
print(course_list)

csv_col = [['title'], [course_list]]

# Name a file, and put w as an argument to tell this 
f = open('course_list.csv', 'w')

with f:
    writer = csv.writer(f) 
    
    for row in csv_col:
        writer.writerow(row)

# Display type of this object (Of course, it's "list" )
print(type(course_list))

# Test accessing position 1 of the list 
print(course_list[1])


# To count how many courses in the list 
print(len(course_list))