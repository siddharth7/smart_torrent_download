python script that automatically download new releases according to your predefined preferences

Prerequisites:
Python 2
PyNotify
BeautifulSoup

How to use:

Add python script to crontab file to repeat it after desired number of hours/days.

Edit the rating.txt file according to your preference, this file contains the the minimum imdb rating that you would like to watch.

Edit the genre.txt file according to your preference, if you have multiple preferences, write each of them in individual line, this file contains the preferred genre by the user.

Don't edit done.txt file, it has the list of movies downloaded, so that you don't end up downloading the same movie again!
