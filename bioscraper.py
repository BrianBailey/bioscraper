import requests   # fetches raw web pages for us
from bs4 import BeautifulSoup  # turns raw web pages into object hierarchy and provides selectors
import re     # regular expression module for matching, parsing
import csv    # simplifies process of writing data to csv 
import nltk   # natural language tool kit module for quick analysis

#  a list of URLs about venture capital, investing,  data stores

pagesToScrape = ["http://www.bizjournals.com/stlouis/blog/biznext/2015/07/10-biggest-funding-rounds-for-startups-so-far-this.html", "http://www.bizjournals.com/stlouis/news/", "http://www.stltoday.com/", "http://news.stlpublicradio.org/#stream/0", "http://www.alivemag.com/", "http://www.stlamerican.com/", "http://techli.com/#.", "http://www.stlregionalchamber.com/who-we-are/chamber-blog", "http://stlouis.cbslocal.com/station/kmox/", "http://www.ktrs.com/", "http://www.ksdk.com/", "http://www.kmov.com/", "http://fox2now.com/", "http://kplr11.com/", "http://www.biospace.com/", "http://medcitynews.com/", "http://www.fiercebiotech.com/", "http://blogs.wsj.com/venturecapital/page/2/", "http://techcrunch.com/", "http://venturebeat.com/", "http://www.bloomberg.com/", "http://www.americanentrepreneurship.com/", "http://siteselection.com/", "http://businessfacilities.com/", "http://www.tradeandindustrydev.com/", "http://www.sec.gov/edgar.shtml", "https://www.sec.gov/about/forms/formd.pdf", "http://www.edgar-online.com/"]


# open a file in append mode to write into same directory where script originates
#csvfile = open("biodata.csv", "wb")

#output = csv.writer(csvfile, delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)


# loop over our list of URL's one at a time
for URL in pagesToScrape:



    webpage = requests.get(URL)     # fetch webpage
    


    content = webpage.content

    soup = BeautifulSoup(content, 'html.parser')  # make an object from the HTML
    #print soup.body.text  # good line , gives good text info
    #print soup.title.text  #  also decent line here for quick line-up of titles
    #print soup.select("td")  # good, produces a lot of information but it is all in html as <td info, need to parse futher
    print soup.body.text
    
    
    
    
    
	
	
