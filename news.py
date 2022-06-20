from bs4 import BeautifulSoup
import requests

def LK():
    req = requests.get("https://sinhala.newswire.lk/category/news/")
    soup = BeautifulSoup(req.content , "lxml")

    x = soup.find("div" , {"class" :"entry-featured-img-wrap"})
    image = x.find("a", {"class" : "entry-featured-img-link"})['href']
    all = soup.find("div", {"class" : "entry-grid-content"})
    title = all.find("h2" , {"class" : "entry-title"}).text
    desc = all.find("div" , {"class" : "entry-summary"}).text
    date = all.find("div", {"class" : "entry-byline-block entry-byline-date"}).text
    xx = all.find("span", {"class" : "more-link"})
    link = xx.find_next()['href']

    News = []

    list ={
        "Title" : title,
        "Description" : desc[:-17], 
        "Date" : date,
        "Link" : link,
        "img_url" : image
    }
        
    News.append(list)
    return News
