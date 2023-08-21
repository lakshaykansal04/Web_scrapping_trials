from bs4 import BeautifulSoup

import requests

html_text=requests.get('https://www.nitmz.ac.in/EMPBiodata.aspx').text


soup=BeautifulSoup(html_text,'lxml')

faculty_cards=soup.find_all('table', class_='matter')

with open(f'nit_mizoram.txt','w') as f:
    for faculty_card in faculty_cards :

        info=faculty_card.find('table', style='line-height: 25px')

        print(info.text.replace(' ',''))

        f.write(info.get_text().replace('  ',''))
        f.write('''
-----------------------------------------------------
-----------------------------------------------------        
        ''')

       



        #     #print(i.text.replace(' ',''))
        #     #f.write(i.text.replace(' ',''))

