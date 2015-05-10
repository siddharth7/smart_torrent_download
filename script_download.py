from bs4 import BeautifulSoup
import pynotify
import requests
import os
def sendmessage(title, message):
    pynotify.init("Test")
    notice = pynotify.Notification(title, message)
    notice.show()
    return

f=open("rating.txt","r")
f2=open("genre.txt","r")
f3=open("done.txt","r")
user_rating=f.read()
user_genre=[]
already_done=[]
for line in f2:
	for word in line.split():
		user_genre.append(word)
already_done = [line.strip() for line in f3]
f.close()
f2.close()
f3.close()
r  = requests.get("https://yts.to/browse-movies")
data = r.text
soup = BeautifulSoup(data)
f3=open("done.txt","a")
for di in soup.findAll('div',{"class":"browse-movie-wrap col-xs-10 col-sm-4 col-md-5 col-lg-4"}):
	genrelist=[]
	torrentdata={}
	flag=0

	movie_name=di.findAll('a',{"class":"browse-movie-title"})[0]
	movie_year=di.findAll('div',{"class":"browse-movie-year"})[0]
	rating=di.findAll('h4',{"class":"rating"})[0]

	for data in di.a.figure.figcaption:
		for elements in data:
			if len(str(elements))>1:
				genrelist.append(str(elements).lower())
	
	genrelist.pop()
	genrelist.pop(0)

	for dii in di.findAll('div',{"class":"browse-movie-tags"}):
		for r in dii.findAll('a'):
			torrentdata[str(r.text)]=str(r.attrs['href'])
	
	if float(str(rating.text[0:3]))>=float(str(user_rating)):
		for genre_in in user_genre:
			if genre_in in genrelist:
				flag=1
				break		
	if flag==1:		
		try:
			if str(movie_name.text) not in already_done:
				sendmessage("Download Started",str(movie_name.text))
				os.system("aria2c "+ torrentdata["1080p"])
				f3.write(str(movie_name.text))
				f3.write("\n")
				sendmessage("Movie Downloaded",str(movie_name.text))
		except:
			if str(movie_name.text) not in already_done:
				sendmessage("Download Started",str(movie_name.text))
				os.system("aria2c "+ torrentdata["720p"])
				f3.write(str(movie_name.text))
				f3.write("\n")
				sendmessage("Movie Downloaded",str(movie_name.text))
f3.close()
