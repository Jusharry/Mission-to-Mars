#!/usr/bin/env python
# coding: utf-8

# In[2503]:


# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
# from iPython.display import HTML

executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# ## Nasa Mars News Site


html = browser.html
news_soup = soup(html, 'html.parser')
#.select_one tells Splinter to select the first/most recent item
slide_elem = news_soup.select_one('div.list_text')
slide_elem.find('div', class_= 'content_title')
news_title = slide_elem.find('div', class_= 'content_title').get_text()
news_title
news_p = slide_elem.find('div', class_= 'article_teaser_body').get_text()
news_p


# ### *Featured Images* 

# In[2510]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[2511]:


#Find and click the full image button which is actually the 2nd button [1]
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


html = browser.html
img_soup = soup(html, 'html.parser')

#Use the parser to find the correct class and then use the .get() to pull what is in the src 
img_url_rel = img_soup.find('img', class_ = 'fancybox-image').get('src')
img_url_rel



# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns= ['description','Mars', 'Earth']
df.set_index('description',inplace=True)
df
df.to_html()




# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'

browser.visit(url)
browser.is_element_present_by_css('div.full-content', wait_time=1)


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.
#results= browser.find_by_css('div#product-section.result-list')
results = browser.find_by_css('a.product-item img')

for result in range(len(results)):
   
    #title= browser.find_by_css('a.itemLink.product-item h3').text.strip()
    # link = browser.find_by_css('div.description a').click()
    title= browser.find_by_css('a.product-item h3')[result].text.strip()
    link =  browser.find_by_css('a.product-item img')[result].click()
    rel_img_url = browser.find_by_css('div.downloads a')['href']
    hemispheres = {
        'title': title,
        'img_url':rel_img_url
    }
    
    browser.back()
    hemisphere_image_urls.append(hemispheres)



#4. Print the list that holds the dictionary of each image url and title.
#hemisphere_image_urls = [hemispheres]
hemisphere_image_urls


browser.quit()

