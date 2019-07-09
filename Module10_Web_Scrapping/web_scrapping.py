# Web Scrapping

#Step 1: Find the URL that you want to scrape
#For this example, we are going scrape Amazon website to extract the Price, Name, and Rating of iPhone. 
#The URL for this page is https://www.amazon.in/s?k=iphone&ref=nb_sb_noss

# Step 2: Inspecting the Page
#The data is usually nested in tags. So, we inspect the page to see, under which tag the data we want to scrape is nested. To inspect the page, just right click on the element and click on “Inspect”.

# Step 3: Find the data you want to extract
#Let’s extract the Price, Name, and Rating which is nested in the “div” tag respectively.

# Step 4: Write the code
# First, let’s create a Python file. To do this, open the terminal in Ubuntu and type gedit <your file name> with .py extension.

# First, let us import all the necessary libraries:

from selenium import webdriver
from BeautifulSoup import BeautifulSoup
import pandas as pd

# To configure webdriver to use Chrome browser, we have to set the path to chromedriver

driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")

# Refer the below code to open the URL:

products=[] #List to store name of the product
prices=[] #List to store price of the product
ratings=[] #List to store rating of the product
driver.get("https://www.flipkart.com/search?q=iphone&otracker=AS_Query_HistoryAutoSuggest_1_0&otracker1=AS_Query_HistoryAutoSuggest_1_0&marketplace=FLIPKART&as-show=on&as=off&as-pos=1&as-type=HISTORY")


content = driver.page_source
soup = BeautifulSoup(content)
for a in soup.findAll('a',href=True, attrs={'class':'_3O0U0u'}):
name=a.find('div', attrs={'class':'_3wU53n'})
price=a.find('div', attrs={'class':'_1vC4OE _2rQ-NK'})
rating=a.find('div', attrs={'class':'_2_KrJI'})
products.append(name.text)
prices.append(price.text)
ratings.append(rating.text)

# Step 5: Run the code and extract the data
# To run the code, use the below command:

#python web_scrapping.py


# After extracting the data, you might want to store it in a format. This format varies depending on your requirement. For this example, we will store the extracted data in a CSV (Comma Separated Value) format. To do this, I will add the following lines to my code:

df = pd.DataFrame({'Product Name':products,'Price':prices,'Rating':ratings}) 
df.to_csv('products.csv', index=False, encoding='utf-8')

