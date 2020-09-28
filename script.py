import requests
from bs4 import BeautifulSoup

#Download the file mp4 from the url with the name('episode-name.mp4') and url indicates
def download_file(name, url, episodeNumber):
    r = requests.get(url)
    f = open(name, 'wb')
    print ("Downloading episode "+str(episodeNumber)+"...")
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
    if (a != None):
        downloadLink = a['href']
    else:
        downloadLink = None

    return downloadLink

#Extract the url of mediafire in jkanime
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

#Check is the link to mediafire is no broken
#Example of a broken link: 'https://www.mediafire.com/file/null/oretresf-01.mp4/file'
def is_valid(mediafireURL):
    isValid = True
    linkParts = mediafireURL.split("/")
    if (linkParts[4] == "null"):
        isValid = False

    return isValid

#Download all the episodes between the firstEpisode and the lastEpisode, them included.
def download_episodes(firstEpisode, lastEpisode, url):
    episodeNumber = firstEpisode

    while (episodeNumber <= lastEpisode) :
        actualEpisodeURL = url+str(episodeNumber)+"/"
        mediafireURL = get_mediafire_url(actualEpisodeURL)
        if ( is_valid(mediafireURL) ):
            mp4URL = extract_mp4_mediafire_url(mediafireURL)
            if(mp4URL != None):
                mp4Name = get_episode_name_from_string(mp4URL)
                download_file(mp4Name, mp4URL, episodeNumber)
            else:
                print("The link to mediafire of the episode "+str(episodeNumber)+" is broken.")
        else:
            print("The link to mediafire of the episode "+str(episodeNumber)+" is broken.")
        episodeNumber += 1

if __name__ == "__main__":
    animeURL = input("Insert URL: ")#https://jkanime.net/yahari-ore-no-seishun-love-comedy-wa-machigatteiru-kan/
    chapters = get_number_chapters(animeURL)
    numChapters = extract_number_from_string(chapters)
    print ("This anime has "+str(numChapters)+" episodes available.")
    optionSelectec = input ("Which option do you prefer?\n[1]: Download one episode.\n[2]: Select the range of episodes to download.\n[3]: Download all the episodes.\nOption selected: ")
    optionSelectec = int(optionSelectec)
    
    print("Remember that the episodes availables are: "+str(1)+" - "+str(numChapters))
    if (optionSelectec == 1):
        episodeA = input("Which episode do you want to download: ")
        episodeA = int(episodeA)
        episodeB = episodeA
        print("One episode will be downloaded")

    if (optionSelectec == 2):
        print("Select the first and the last episode that do you want to download")
        episodeA = input("Select the first episode: ")
        episodeA = int(episodeA)
        episodeB = input("Select the last episode: ")
        episodeB = int(episodeB)
        print("The episodes from the "+str(episodeA)+" to the "+str(episodeB)+" will be downloaded")

    if (optionSelectec == 3):
        episodeA = 1
        episodeB = numChapters
        print("All the episodes from the serie will be downloaded")
    
    if (optionSelectec != 1 | optionSelectec != 2 |optionSelectec != 3):
        print("Invalid option, please try again.")

    download_episodes(episodeA, episodeB, animeURL)
