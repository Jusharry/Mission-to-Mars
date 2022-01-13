#!/usr/bin/env python
# coding: utf-8



# Import dependencies
#from bs4.builder import HTML
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import datetime as dt

def scrape_all():
    #Initiates the headless driver for deployment 
    #browser currently set to visible i.e headless=False
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True)
    news_title, news_p = mars_news(browser)
    hemisphere_image_urls = hemispheres(browser)
    #Run scraping functions and save in a dictionary
    data = {
        "news_title": news_title,
        "news_paragraph": news_p,
        "featured_image":featured_image(browser),
        "facts": mars_facts(),
        "last_modified": dt.datetime.now(),
        "hemispheres":hemisphere_image_urls
    }
    #Stop webdriver and return data
    browser.quit()
    return data

#use the foll. code as a function 
def mars_news(browser):

    #Scrape mars news
    # Visit the mars nasa news site
    url = 'https://redplanetscience.com'
    browser.visit(url)
    # Optional delay for loading the page
    browser.is_element_present_by_css('div.list_text', wait_time=1)

    # ## Nasa Mars News Site

    html = browser.html
    news_soup = soup(html, 'html.parser')
    #.select_one tells Splinter to select the first/most recent item
    try:
        slide_elem = news_soup.select_one('div.list_text')
        slide_elem.find('div', class_= 'content_title')

        # Use the parent element to find the first 'a' tag and save it as 'news_title'
        news_title = slide_elem.find('div', class_= 'content_title').get_text()
        #news_title

        # Use the parent element to find the paragraph text
        news_p = slide_elem.find('div', class_= 'article_teaser_body').get_text()
        #news_p
    except AttributeError:
        return None,None
    return news_title, news_p

#Featured Images 
def featured_image(browser):
    # Visit URL
    url = 'https://spaceimages-mars.com'
    browser.visit(url)

    #Find and click the full image button which is actually the 2nd button [1]
    full_image_elem = browser.find_by_tag('button')[1]
    full_image_elem.click()

    html = browser.html
    img_soup = soup(html, 'html.parser')
    try:
        #Use the parser to find the correct class and then use the .get() to pull what is in the src 
        img_url_rel = img_soup.find('img', class_ = 'fancybox-image').get('src')
        #img_url_rel
    except AttributeError:
        return None
    # Use the base URL to create an absolute URL
    img_url = f'https://spaceimages-mars.com/{img_url_rel}'
    #img_url

    return img_url
def mars_facts():
    try:
    #use read_html to scrape the facts table into a df
        df = pd.read_html('https://galaxyfacts-mars.com')[0]
    except BaseException:
        return None
    #Assign columns and set index of df
    df.columns= ['description','Mars', 'Earth']
    df.set_index('description',inplace=True)

    #Convert df to html format , add bootstrap
    return df.to_html()

def hemispheres(browser):
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
    return hemisphere_image_urls

if __name__ == "__main__":
    #If running as script print scraped data
    print(scrape_all())







