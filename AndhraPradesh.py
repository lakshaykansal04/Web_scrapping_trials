from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.nitandhra.ac.in/main/departments').text
soup = BeautifulSoup(html_text, 'lxml')
departments = soup.find_all('div', class_='col-md-4')
for department in departments:
    department_link = department.find('a')['href']
    main_text = requests.get(department_link+'faculty').text
    Real_soup = BeautifulSoup(main_text, 'lxml')
    faculties = Real_soup.find_all('div', class_='col-md-4')
    for faculty in faculties:
        faculty_link = faculty.find('a', class_='pull-left')['href']
        faculty_page_text = requests.get(faculty_link).text
        soupx = BeautifulSoup(faculty_page_text, 'lxml')
        faculty_info = soupx.find_all('div', class_='col-sm-6')
        for i in faculty_info:
            print(i.text.replace(' ', '').strip())
        faculty_area_of_interest = soupx.find('div', class_='col-md-12').text
        print(faculty_area_of_interest)
        print("\n==================================\n")
