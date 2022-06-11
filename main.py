#--------------------------------
#Created by Oftox 
#Date: ??.06.2022
#--------------------------------
import sys
import requests
from bs4 import BeautifulSoup

#functions
def content2str(content):
	string = ""
	for i in range(len(content)):
		if ("</" in str(content[i])):
			string += str(content[i].string)
		else:
			string += str(content[i])
	return string


#check if there are more than 1, or less than 1 command line arguments
if (len(sys.argv) > 2):
	print("Error: too many arguments(", len(sys.argv) - 1, ")")
	sys.exit()
elif (len(sys.argv) < 2):
	print("Error: too few arguments")
	sys.exit()


#read contents of languages.txt and check if command line argument is a valid language abbreviation
language = ""

languageFile = open("languages.txt", mode = "r", encoding = "utf-8")
if (languageFile == ""):
	print("Error: could not open languages.txt")
	sys.exit()
	
abbr = languageFile.readlines()
if (sys.argv[1] + "\n" in abbr):
	language = sys.argv[1]
	languageFile.close()
else:
	print("Error: invalid language abbreviation as argument (english, japanese, russian and finnish are supported)")
	sys.exit()


#connect to wikipedia with "requests" to check if wikipedia is functional
requested = requests.get("https://" + language + ".wikipedia.org")
if (requested.status_code >= 400):
	print("Error: could not connect to " + language +".wikipedia.org")
	sys.exit()


#create translation variables from the "translations.txt" file
translationFile = open("translations.txt", mode = "r", encoding = "utf-8")
if (translationFile == ""):
	print("Error: could not open translations.txt")
	sys.exit()
	
lines = translationFile.readlines()
translationFile.close()

abbrLine = False;
for i in range(len(lines)):
	if(lines[i] == language + "\n"):
		abbrLine = i;

if (abbrLine == False):
	print("Error: could not find translation")

welcome = lines[abbrLine + 1].replace("\n", '')
free = lines[abbrLine + 2].replace("\n", '')

#start main loop with "running" as the flag
running = True
while (running):
	#search page with input 
	print("\n")
	print("\t\t" + welcome)
	print("    " + free)
	print("\n")

	try:
		input("    " + ": ")
	except KeyboardInterrupt:
		print("\n")
		running = False
	
	running = False;




