import requests
from bs4 import BeautifulSoup

#Download the file mp4 from the url with the name and url indicates
def download_file(name, url):
    name = name+".mp4"
    r = requests.get(url)
    print ("****Connected****")
    f = open(name, 'wb')
    print ("Downloading.....")
    for chunk in r.iter_content(chunk_size = 255): 
        if chunk: # filter out keep-alive new chunks
            f.write(chunk)
    print ("Done")
    f.close()

#Get a string with the numbers of episodes that the anime actually has
def get_number_chapters(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    numbers = soup.find_all('a', class_="numbers")
    for a in numbers :
        chaps = a.contents
    return chaps[0]

#Parse the string to return the amount of episode in a int type
def extract_number(chapString):
    numbers = []
    for word in chapString.split():
        if (word.isdigit()):
            numbers.append(int(word))
    return numbers[-1]

#Extract the url used to download the episode from the page mediafire
def extract_mp4_mediafire(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')


#URL = input("Insert URL: ")
#chapters = get_number_chapters("https://jkanime.net/yahari-ore-no-seishun-love-comedy-wa-machigatteiru-kan/")
#numChapters = extract_number(chapters)
#print ("This anime has "+str(numChapters)+" episodes available.")
#optionSelectec = input ("Which option do you prefer?\n[1]: Download one episode.\n[2]: Select the range of episodes to download.\n[3]: Download all the episodes.")
#optionSelectec = int(optionSelectec)





