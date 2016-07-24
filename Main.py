# import the functions needed for this app to run.
#  requests to get the source code of the page
#  BeautifulSoup to make the source code useable.
import requests
from bs4 import BeautifulSoup

# Funny dance to make the code take all pages into account.
urlp1 = "https://www.penguin.co.uk/search/?ctype=w&p="
urlp2 = 1 #set to 8 for testing. Set to 1 when deploying.
urlp3 = "&ps=100&f=i%3AVintage%2BClassics"
url = str(urlp1)+str(urlp2)+str(urlp3)
print (url)

# Set variable r to sourcecode of link
r = requests.get(url)
# Use r.content to view the retrieved source code.

# Import the content of r into BeautifulSoup to be able to use it.
soup = BeautifulSoup(r.content, "html.parser")
# Use print (soup.prettify()) to view the source code and check whether your request made it through.

# find all values equal to the value in between brackets. E.g. a = <a, img = <img
links = soup.find_all("a")

# This function will put all the retrieved lines in HTML image embedded code
#for link in links:
#    print ("<img src="'%s'">" %(link.get("href")))

#find all values equal to the value in between brackets within a certain class. E.g. a = <a, img = <img
g_data = soup.find_all("div", {"class": "content"})

result = 1
while result == 1:
    while urlp2 < 11:
        # print only the data in the element equal to the number in item.contents[#].
        # .text retrieves only the text in the string.
        for item in g_data:
            try:
                print (item.contents[1].text) #Title(1)
            except:
                pass
            try:
                print (item.contents[3].text) #Author(s)(2)
            except:
                pass
            try:
                print (item.contents[4]) #Description(3)
            except:
                pass
        #go to the next page
        urlp2 = urlp2 + 1
        url = str(urlp1)+str(urlp2)+str(urlp3)
        print(url)
        #check wether there are any results on this page
        #see if you get results back.
        try:
        #look in class "number-of-results" and only return the value between the tags.
            p_data = soup.find('span', {"class": "number-of-results"}).getText()
        except:
        #if no value between te tags(i.e. no results) set p_data to 0
            p_data = 0
        if int(p_data) > 0 :
            result = 1
        else:
            result = 0
# This function will put all the retrieved lines with the value of ".jpg" in HTML image embedded code
#for link in links:
#    if ".jpg" in link:
#        print ("<img src="'%s'">" %(link.get("href")))
