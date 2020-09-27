import requests
from bs4 import BeautifulSoup
import re

#Download the file mp4 from the url with the name('episode-name.mp4') and url indicates
def download_file(name, url):
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
def extract_number_from_string(chapString):
    numbers = []
    for word in chapString.split():
        if (word.isdigit()):
            numbers.append(int(word))
    return numbers[-1]

#Extract the url used to download the episode from the page mediafire
def extract_mp4_mediafire_url(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    a = soup.find('a', class_="input popsok")
    downloadLink = a['href']
    return downloadLink

def get_mediafire_url(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    div = soup.find(id="basic-modal-content")
    a = div.findAll('a')
    for name in a:
        href = name['href'].split("/")
        endString = href[-1]
        if (endString == "file"):
            mediafireURL = str(name['href'])
    return mediafireURL

#Get the name of the mp4 file for future use
def get_episode_name_from_string(urlString):
    names = urlString.split("/")
    name = names[-1]
    return name

def one_episode():
    return "option 1"

def range_of_episodes():
    return "option 2"

def all_episodes():
    return "option 3"

animeURL = input("Insert URL: ")
chapters = get_number_chapters("animeURL")
numChapters = extract_number_from_string(chapters)
print ("This anime has "+str(numChapters)+" episodes available.")
optionSelectec = input ("Which option do you prefer?\n[1]: Download one episode.\n[2]: Select the range of episodes to download.\n[3]: Download all the episodes.")
optionSelectec = int(optionSelectec)


episodeURL = "https://jkanime.net/yahari-ore-no-seishun-love-comedy-wa-machigatteiru-kan/2/"
mediafireURL = get_mediafire_url(episodeURL)
mp4URL = extract_mp4_mediafire_url(mediafireURL)
mp4Name = get_episode_name_from_string(mp4URL)
download_file(mp4Name, mp4URL)