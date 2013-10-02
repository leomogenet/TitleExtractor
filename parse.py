import pprint
from BeautifulSoup import BeautifulSoup
html = open("z.html")
soup = BeautifulSoup(html)
metaList = soup.findAll('meta')
pp = pprint.PrettyPrinter(indent=4)
for meta in metaList:
    if meta.has_key('name'):
        if meta['name'] == 'title':
            title = meta['content']
            print(title)





#import urllib2 
#page = urllib2.urlopen("http://www.icc-ccs.org/prc/piracyreport.php")

