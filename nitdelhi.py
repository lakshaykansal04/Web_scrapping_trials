import requests
from bs4 import BeautifulSoup
ctr=0
file=open("nitdelhi.txt","a+")
for x in range (11979,11999):
    url = "https://nitdelhi.ac.in/?page_id="+str(x)
    all_reqs=requests.get(url)
    soup=BeautifulSoup(all_reqs.text,'lxml')
    # print(soup.title)
    # names=soup.select('h3')
    details=soup.select('div.computersci')
    for i in details:
        print("Professor "+i.text.strip())
        print("=======THIS ENDS HERE==============\n\n")
        ctr+=1
        
print(ctr)







