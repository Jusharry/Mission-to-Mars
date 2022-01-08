from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'
browser.visit(url)
browser.is_element_present_by_css('div.full-content', wait_time=1)
# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []


# 3. Write code to retrieve the image urls and titles for each hemisphere.
html = browser.html
img_soup = soup(html, 'html.parser')

results = img_soup.find(class_='full-content')

images= results.find_all('item')

for image in images:
    hemispheres={
                'img_url': img_url,
                'title': title
    }
    title= images.find('item',class_= 'product-item').get_text()
    print(title)