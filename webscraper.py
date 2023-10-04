import requests
from bs4  import BeautifulSoup


URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

#need to save the scraped file to the folder here



#open the scraped file here
with open("your_html_file.html", "r", encoding="utf-8") as html_file:
    soup = BeautifulSoup(page.content, "html.parser")

#save as a file
with open("parsed_data.txt", "w", encoding="utf-8") as output_file:
    title = soup.title.text
output_file.write("Title: " + title + "\n")




print(page.text)
