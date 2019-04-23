from splinter import Browser
from bs4 import BeautifulSoup


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "C:/Users/ayildirim/Desktop/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


def scrape():
    browser = init_browser()
    mars_data = {}
# Mars news
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    news_title = soup.find("div", class_='content_title').find("a").text
    news_p = soup.find("div", class_='article_teaser_body').text

    mars_data["news_title"] = news_title
    mars_data["news_p"] = news_p
    
# JPL Mars Space Images - Featured Image
    url_img = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url_img)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    
    img_url = soup.find("article", class_="carousel_item")["style"]
    img_url_add=img_url.split("'")[1]

    featured_image_url = "https://jpl.nasa.gov"+img_url_add
    mars_data["featured_image_url"] = featured_image_url

#   Mars Weather Tweet
    url_tweet = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url_tweet)  
    
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    latest_tweet=soup.find("p", class_="TweetTextSize").text
    latests = latest_tweet.split("\n" or "hPa")
    mars_weather=""
    for latest in latests:
        mars_weather=mars_weather+latest+" "
        
    mars_data["mars_weather"] = mars_weather

# Mars Facts
    url_facts = 'https://space-facts.com/mars/'
    browser.visit(url_facts)
    
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    mars_facts = soup.find("table", class_="tablepress").text

    mars_data["mars_facts"] = mars_facts

# Mars Hemispheres

    url_hemi = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url_hemi)
    url_hemis="https://astrogeology.usgs.gov"

    html_hemispheres = browser.html
    soup = BeautifulSoup(html_hemispheres, 'html.parser')
    items = soup.find_all('div', class_='item')
    hemisphere_image_urls = []

    for i in items: 
        title = i.find('h3').text
        partial_img_url = i.find('a', class_='itemLink product-item')['href']
        browser.visit(url_hemis + partial_img_url)
        partial_img_html = browser.html
        soup = BeautifulSoup( partial_img_html, 'html.parser')
        img_url = url_hemis + soup.find('img', class_='wide-image')['src']
        hemisphere_image_urls.append({"title" : title, "img_url" : img_url})
    
    mars_data["hemisphere_image_urls"] = hemisphere_image_urls

    return mars_data
