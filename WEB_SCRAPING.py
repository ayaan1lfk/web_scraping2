from email import header
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browse = webdriver.Chrome("/path/to/chromedriver")
browser.get(START_URL)
time.sleep(10)

def scrape():
    header= ["Name", "Distance", "Mass", "Radious"]
    planet_data =[]
    for i in range(0,428):
        soup = BeautifulSoup(browser.page_source, "html.parser")
        for ul_tag in soup.find_all("ul", attrs={"class", "exoplanet"}):
            li_tags = ul_tag.find_all("li")
        temp_list = []
        for index, li_tag in enumerate(li_tags):
            if index == 0:
                temp_list.append(li_tag.find_all("a")[0].contents[0])
        else:
            try:
                temp_list.append(li_tag.contents[0])
            except:
                temp_list.append("")

        planet_data.append(temp_list)
    browse.find_element_by_xpath('//*[@id = "primary_colum"]/footer/div/div/nav/span[2]/a').click()

def scrape_more_data(hyperlink):
    page = request.get(hyperlink)
    soup = BeautifulSoup(page.content, "html.paraser")
    for tr_tag in soup.find_all("tr", attrs={"class": "fact_row"}):
        td_tag = tr_tag.find_all("td")
        temp_list = []
        for td_tag in td_tag:
            try:
                temp_list.append(td_tag.find_all("div", attrs={"class": "value"})[0].contents[0])
            except:
                temp_list.append("")
        new_planet_data.append(temp_list)
scrape()
for data in planet_data:
    scrape_more_data(data[5])

final_planet_data = []
for index, data in enumerate(planet_data):
    final_planet_data.append(data + final_planet_data[index])


with open("final.csv","w") as f:
    csvwriter = csv.writer(f)
    csvwriter = csv.writerow(headers)
    csvwriter = csv.writerow(final_planet_data)