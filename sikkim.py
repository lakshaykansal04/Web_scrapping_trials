import requests
from bs4 import BeautifulSoup


def scrape(url):
    soup = BeautifulSoup(requests.get(url).text, "html.parser")
    rows = soup.find_all(attrs={"class": "container-fluid"})[0].div

    prof_arr = rows.find_all(attrs={"class": "col-md-4"})

    for proffesors in prof_arr:
        for data in proffesors.div.div.strings:
            if (data != "More"):
                print(data)
        print("\n----------------------------------------\n")


def parse_name(url):
    names = {"cse": "Computer Engineering Department", "ece": "Electronics and Communication Department",
             "eee": "EEE Department Details", "ce": "Civil Engineering Department Details"}

    start_index = 8
    end_index = url.find(".")
    dept = url[start_index: end_index]
    return names[dept]


urls = ["https://cse.nitsikkim.ac.in/people.php", "https://ece.nitsikkim.ac.in/people.php",
        "https://eee.nitsikkim.ac.in/people.php", "https://ce.nitsikkim.ac.in/people.php"]

for url in urls:
    print("********************************\n")
    print("Printing details for", parse_name(url),"->->->->\n")
    
    scrape(url)
