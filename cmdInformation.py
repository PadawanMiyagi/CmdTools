# This is the pageviewer for https://www.information.dk
# It will show the topics and summary of the articles of the page
#You can scroll through the topics with numbers 1-4

import bs4 as bs
import urllib.request
import sys 
import bs4 as bs
import urllib.request
import sys 
import os

#sauce = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
sauce = urllib.request.urlopen('https://information.dk').read()
soup = bs.BeautifulSoup(sauce,'lxml')

# Collect the headlines and subtexts from the page
headlines = soup.find_all("h3", { "class" : "node-title" })
fields = soup.find_all("div", { "class" : "field field-name-field-web-underrubrik teaser-text" })

#Alternative print statement for UTF-8
def uprint(*objects, sep=' ', end='\n', file=sys.stdout):
    enc = file.encoding
    if enc == 'UTF-8':
        print(*objects, sep=sep, end=end, file=file)
    else:
        f = lambda obj: str(obj).encode(enc, errors='backslashreplace').decode(enc)
        print(*map(f, objects), sep=sep, end=end, file=file)

def goThrough(ru,rd):
	rangeUp = ru
	rangeDown = rd
	#Clear the screen
	os.system('cls' if os.name == 'nt' else 'clear')
	for x in range(rangeUp-1,rangeDown):
		#Print the headline followed by a empty line followed by the subtopic
		uprint(headlines[x+1].text, ": ")
		print(" ")
		uprint(fields[x].text)
		print('____________________________________________________')
	#Make topics scrollable up to 20 articles	
	choice = input("Gå til side: ")
	if int(choice) == 1:
		goThrough(0,5)
	elif int(choice) == 2:
		goThrough(5,10)
	elif int(choice) == 3:
		goThrough(10,15)
	elif int(choice) == 4:
		goThrough(15,20)
	else:
		print("Sorry, the number is too high")
		goThrough(0,5)
goThrough(0,5)