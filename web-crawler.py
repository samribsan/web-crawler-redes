import urllib
import urlparse
import BeautifulSoup

url = "http://www.ufpel.edu.br"
nivelmax = 1

urls = [url]
visited = [url] 	

while (nivelmax > 0):
	try:
		htmltext = urllib.urlopen(urls[0])
	except:
		print urls[0]
	
	soup = BeautifulSoup.BeautifulSoup(htmltext)

	urls.pop(0)
	print len(urls)

	for tag in soup.findAll('a',href=True):
		tag['href'] = urlparse.urljoin(url,tag['href'])
		if url in tag['href'] and tag['href'] not in visited:
			urls.append(tag['href'])
			visited.append(str(tag['href']))

	nivelmax = nivelmax - 1

print visited
for i in range (len(visited)):
	urllib.urlretrieve(visited[i],visited[i].split('/')[-1])