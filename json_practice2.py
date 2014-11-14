import json
import urllib2
import time

#this gets the user to plug in two reddit urls
url_input1 = raw_input("Enter a .json reddit URL: ")
url_input2 = raw_input("Enter a different .json reddit URL: ")
user1 = url_input1
user2 = url_input2

#this takes the urls and opens them using urllib2
json_obj = urllib2.urlopen(user1)
json_obj2 = urllib2.urlopen(user2)

#this sets the json data equal to data and data2
data = json.load(json_obj)
data2 = json.load(json_obj2)

#this digs into the json dicts and lists to pull out the value we're looking for.
score = data['data']['children'][0]['data']['score']

#this delays the second score request so as to not flood reddit
time.sleep(5)

score2 = data2['data']['children'][0]['data']['score']

print "The first user you entered scored %s karma on their most recent post" % score
print "The second user you entered has scored %s karma on their most recent post" % score2

