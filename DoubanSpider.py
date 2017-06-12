
import urllib
import urllib2
import re
import sys
import time

url1 = "https://www.douban.com/photos/album/48392888/?start=1"
html1 = urllib2.urlopen(url1).read()

pattern1 = re.compile(r'<a href="(.*?)" class="photolst_photo"')
url2 = re.findall(pattern1,html1)

x = 0

for link in url2:
	html2 = urllib2.urlopen(link).read()
	pattern2 = re.compile(r'<a href="(.*?large)" title')
	url3 = re.search(pattern2,html2).group(1)
	html3 = urllib2.urlopen(url3).read()
	pattern3 = re.compile(r'<img src="(.*?\.jpg)" alt')
	origin_img_src = re.search(pattern3,html3).group(1)
	urllib.urlretrieve(origin_img_src,'%s.jpg'%x)
	x+=1
	time.sleep(3)
	
