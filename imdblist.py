import sys
import urllib2
import re
import json

#Ask for movie title
title = str(input("Please enter a movie title: "))

#Ask for which year
year = str(input("which year? "))

#Search for spaces in the title string
string = re.compile(r' ')

#Replace spaces with a plus sign
searchstring = string.sub('+', title)

#Prints the search string
print (searchstring)

#The actual query
url = "http://www.imdbapi.com/?t=" + searchstring + "&y="+year

request = urllib2.Request(url)

response = json.load(urllib2.urlopen(request))

print (json.dumps(response,indent=2))