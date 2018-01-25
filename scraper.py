# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

import scraperwiki
import lxml.html

baseurl = "http://www.imdb.com/"
# # Read in a page
html = scraperwiki.scrape("http://www.imdb.com/chart/toptv/?ref_=nv_tvv_250_3")

#
# # Find something on the page using css selectors
root = lxml.html.fromstring(html)
##main > div > span > div > div > div.lister > table > tbody > tr:nth-child(1) > td.titleColumn > a
links = root.cssselect("td.titleColumn a")
linkslist = []
for link in links:
  print link
  print link.text
  print link.text_content()
  cleanurl = link.attrib['href'].split("?")[0]
  print cleanurl
  fullurl = baseurl+cleanurl
  linkslist.append(fullurl)

for url in linkslist:
  print url
  
# # Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".
