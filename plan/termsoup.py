from bs4 import BeautifulSoup
import urllib.request


def department_recommendations():
	opener = urllib.request.FancyURLopener({})
	url = "https://www.gov.za/about-sa/school-calendar"
	try:
		html_file = opener.open(url)
		html_subtract = html_file.read()
		soup = BeautifulSoup(html_subtract, 'html.parser')
		better_soup = soup.find_all('td')
		html_local = open("local_copy.txt", 'w')
		for i in better_soup:
			try:
				better = i.p.string
			except AttributeError:
				pass
			html_local.write(better + '\n')
		html_local.close()
	except OSError:
		print("Check internet connection")
		print("Reading from local file")
	html_local = open("local_copy.txt", 'r')
	lines = html_local.readlines()

	term1 = {"Term": lines[7][:-1],
    	     "Weeks": lines[8][:-1],
        	 "Days": lines[11][:-1]}
	term2 = {"Term": lines[13][:-1],
    	     "Weeks": lines[14][:-1],
        	 "Days": lines[17][:-1]}
	term3 = {"Term": lines[19][:-1],
    	     "Weeks": lines[20][:-1],
        	 "Days": lines[23][:-1]}
	term4 = {"Term": lines[25][:-1],
    	     "Weeks": lines[26][:-1],
        	 "Days": lines[29][:-1]}
	termdicionary = [term1["Term"], term2["Term"], term3["Term"], term4["Term"]]
	return termdicionary