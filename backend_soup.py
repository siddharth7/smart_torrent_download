from bs4 import BeautifulSoup
import requests
mainlist=[]
class movie(object):
    def __init__(self,movie_name,rating,year,genre,links):
        self.movie_name=movie_name
        self.rating=rating
        self.year=year
        self.genre=genre
        self.links=links
    def printname(self):
    	print "Name", self.movie_name

#f=open("out.txt","w")

r  = requests.get("https://yts.to/browse-movies")

data = r.text
soup = BeautifulSoup(data)

#f.write(soup.prettify().encode('utf-8'))

alldiv=soup.findAll('div',{"class":"browse-movie-wrap col-xs-10 col-sm-4 col-md-5 col-lg-4"})

for di in soup.findAll('div',{"class":"browse-movie-wrap col-xs-10 col-sm-4 col-md-5 col-lg-4"}):
	finallist=[]
	templist=[]
	linklist=[]

	movie_name=di.findAll('a',{"class":"browse-movie-title"})[0]
	movie_year=di.findAll('div',{"class":"browse-movie-year"})[0]
	rating=di.findAll('h4',{"class":"rating"})[0]

	finallist.append(str(movie_name.text))
	finallist.append(str(rating.text[0:3]))
	finallist.append(str(movie_year.text))
	
	for data in di.a.figure.figcaption:
		for elements in data:
			if len(str(elements))>1:
				#print elements
				templist.append(str(elements))
	
	templist.pop()
	templist.pop(0)
	finallist.append(templist)

	for dii in di.findAll('div',{"class":"browse-movie-tags"}):
		for r in dii.findAll('a'):
			inner_list=[]
			inner_list.append(str(r.attrs['href']))
			inner_list.append(str(r.text))
			linklist.append(inner_list)

	finallist.append(linklist)
	movie1=movie(str(movie_name.text), str(rating.text[0:3]), str(movie_year.text), templist, linklist)
	#movie1.printname()
	print finallist
	
