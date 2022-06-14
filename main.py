import sys
import requests
from bs4 import BeautifulSoup

#functions

#convert contents of HTML tags to strings
def content2str(content):
	string = ""
	for i in range(len(content)):
		if ("<b" in str(content[i])):
			for l in range(len(content[i])):
				if ("</" in str(content[i].contents[l]) or "<br>" in str(content[i].contents[l])):
					if (content[i].contents[l].string != None):
						string += str(content[i].contents[l].string)
				else:
					string += str(content[i].contents[l])
					
		elif ("</" in str(content[i]) or "<br>" in str(content[i])):
			if (content[i].string != None):
				string += str(content[i].string)
		else:
			string += str(content[i])
	return string


#check if there are more than 1, or less than 1 command line arguments
if (len(sys.argv) > 2):
	print("Error: too many arguments(", len(sys.argv) - 1, ")")
	sys.exit(1)
elif (len(sys.argv) < 2):
	print("Error: too few arguments")
	sys.exit(1)


#read contents of .languages.txt and check if command line argument is a valid language abbreviation
language = ""

languageFile = open(".languages.txt", mode = "r", encoding = "utf-8")
if (languageFile == ""):
	print("Error: could not open .languages.txt")
	sys.exit(1)
	
abbr = languageFile.readlines()
if (sys.argv[1] + "\n" in abbr):
	language = sys.argv[1]
	languageFile.close()
else:
	print("Error: invalid language abbreviation as argument (supported languages can be found in the README file)")
	sys.exit(1)


#connect to wikipedia with "requests" to check if wikipedia is functional
requested = requests.get("https://" + language + ".wikipedia.org")
if (requested.status_code >= 400):
	print("Error: could not connect to " + language +".wikipedia.org")
	sys.exit(1)
requested = None


#create translation variables from the ".translations.txt" file
translationFile = open(".translations.txt", mode = "r", encoding = "utf-8")
if (translationFile == ""):
	print("Error: could not open .translations.txt")
	sys.exit(1)
	
lines = translationFile.readlines()
translationFile.close()

abbrLine = False;
for i in range(len(lines)):
	if(lines[i] == language + "\n"):
		abbrLine = i;

if (abbrLine == False):
	print("Error: could not find translation")
	sys.exit(1)

welcome = lines[abbrLine + 1].replace("\n", '')
free = lines[abbrLine + 2].replace("\n", '')
empty = lines[abbrLine + 3].replace("\n", '')
noarticle = lines[abbrLine + 4].replace("\n", '')


#start main loop with "running" as the flag
running = True
while (running):
	try:
		print("\n")
		print("\t\t" + welcome)
		print("    " + free)
		print("\n")
		
		
		#get user input and check validity
		searchValid = False
		while (searchValid == False):	
			search = input("    " + ": ")
			if (search == "" or search == " "):
				print("")
				print("\t" + empty)
				print("")
			else:
				searchValid = True
				print("\n")

		print("#" * 60)
		
		
		#connect to wikipedia and print if article not found
		requested = requests.get("https://" + language + ".wikipedia.org/w/index.php?search=" + search)
		if (requested.status_code >= 400):
			print("Error: could not connect to " + language +".wikipedia.org")
			sys.exit(1)
		page = BeautifulSoup(requested.text, 'html.parser')
		pahe = page.prettify()

		searchbar = page.find(class_='oo-ui-fieldLayout-field')
		if(searchbar != None):
			print("\n")
			print("\t\t" + noarticle)
			print("\n")		
		else:
		
		
			#print title and loop through the list of all tags and check if it's a tag we want printed and print it accordingly
			firstheading = page.find(class_='firstHeading')
			print("\n")
			print("\t\t" + content2str(firstheading.contents))
			print("\n")
			
			allcontent = page.find(class_="mw-parser-output").contents
			for i in range(len(allcontent)):
				#paragraph aka. normal text
				if (allcontent[i].name == "p"):
					if (content2str(allcontent[i].contents) != ""):
						print(content2str(allcontent[i].contents))
						
				elif (allcontent[i].name == "dl"):
					for l in range(len(allcontent[i].contents)):
						if (allcontent[i].contents[l].name == "dt"):
							print("")
							print("\t" + content2str(allcontent[i].contents[l].contents))
						elif (allcontent[i].contents[l].name == "dd"):
							print(content2str(allcontent[i].contents[l].contents))	

				#ul contains multiple 'li' tags which contain either only text or text with links
				elif (allcontent[i].name == "ul"):
					for l in range(len(allcontent[i].contents)):
						if (type(allcontent[i].contents[l]).__name__ != 'NavigableString'):
							print("  ∙  " + str(content2str(allcontent[i].contents[l].contents)))
					print("")
						
				elif (allcontent[i].name == "h2"):
					if (allcontent[i + 1].name != "div"):
						print("\n")
						print("\t\t" + content2str(allcontent[i].contents))
						print("-" * 60)
						
				elif (allcontent[i].name == "h3"):
					if (allcontent[i + 1].name != "div"):
						print("\n")
						print("\t\t" + content2str(allcontent[i].contents))
						print("")
						
				elif (allcontent[i].name == "h4"):
					if (allcontent[i + 1].name != "div"):
						print("")
						print("\t" + content2str(allcontent[i].contents))
						print("")
						
				elif (allcontent[i].name == "div"):
					if (allcontent[i].attrs != {'id': 'toc'} and allcontent[i].ul != None and len(allcontent[i].contents) == 1):
						print(content2str(allcontent[i].ul.contents))
											
		print("#" * 60) 
				
	except KeyboardInterrupt:
		print("\n")
		running = False
