import requests
from bs4 import BeautifulSoup
u = [
    "http://www.manit.ac.in/content/biological-science-engineering",
"http://www.manit.ac.in/civil-engineering-department",
"http://www.manit.ac.in/content/chemical-engineering-0",
"http://www.manit.ac.in/computer-science-engineering-department-0",
"http://www.manit.ac.in/content/electrical-engineering",
"http://www.manit.ac.in/content/electronics-communication-engineering",
"http://www.manit.ac.in/content/materials-metallurgical-engineering",
"http://www.manit.ac.in/content/mechanical-engineering",
"http://www.manit.ac.in/content/chemistry-department",
"http://www.manit.ac.in/content/mathematics-0",
"http://www.manit.ac.in/content/bioinformatics",
"http://www.manit.ac.in/content/computer-applications-department",
"http://www.manit.ac.in/content/physics-department",
"http://www.manit.ac.in/content/humanities-department",   
# //doubt
"http://www.manit.ac.in/content/department-management-studies-dms",
]

dept_name = [
    "biological-science-engineering",
"civil-engineering-department",
"chemical-engineering",
"computer-science-engineering-department",
"electrical-engineering",
"electronics-communication-engineering",
"materials-metallurgical-engineering",
"mechanical-engineering",
"chemistry-department",
"mathematics",
"bioinformatics",
"computer-applications-department",
"physics-department",
"humanities-department",
"department-management-studies-dms"
]

i = 0

file_bhopal = open("file2.txt",'a')
file_bhopal.write("NIT Bhopal\n\n\n")

for url in u:
    r = requests.get(url)
    html = r.content
    soup = BeautifulSoup(html,'html.parser')
    num = soup.find_all(class_ = "row")

    file_bhopal.write(dept_name[i]+"\n\n\n")
    for e in num:
        

       j = 0
       detail = e.find(class_ = "col-xs-12 col-sm-9 col-md-9 pdleft")
       k=0
       if detail:     
        for elem in detail.stripped_strings:
                
                if elem == "More Information" or elem == "more information":
                    continue

                file_bhopal.write(elem)
                
                j = j+1  
        file_bhopal.write("\n")  
       

    i = i+1

