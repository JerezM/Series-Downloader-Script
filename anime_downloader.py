import requests
from bs4 import BeautifulSoup

def download_file(name, url, episode_number):
    """Download the file mp4 from the url with the name('episode-name.mp4') and url indicates"""
    r = requests.get(url)
    f = open(name, 'wb')
    print ("Downloading episode "+str(episode_number)+"...")
    for chunk in r.iter_content(chunk_size = 255): 
        if chunk: # filter out keep-alive new chunks
            f.write(chunk)
    print ("Done")
    f.close()


def get_number_episodes(url):
    """Get a string with the numbers of episodes that the anime actually has"""
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    numbers = soup.find_all('a', class_="numbers")
    for a in numbers :
        chaps = a.contents

    return chaps[0]


def extract_number_from_string(episode_string):
    """Parse the string to return the amount of episode in a int type"""
    numbers = []
    for word in episode_string.split():
        if (word.isdigit()):
            numbers.append(int(word))

    return numbers[-1]


def extract_mp4_mediafire_url(url):
    """Extract the url used to download the episode from the page mediafire"""
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    a = soup.find('a', class_="input popsok")
    if (a != None):
        download_link = a['href']
    else:
        download_link = None

    return download_link


def get_mediafire_url(url):
    """Extract the url of mediafire in jkanime"""
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    div = soup.find(id="basic-modal-content")
    a = div.findAll('a')
    for name in a:
        href = name['href'].split("/")
        end_string = href[-1]
        if (end_string == "file"):
            mediafire_url = str(name['href'])

    return mediafire_url


def get_episode_name_from_string(url_string):
    """Get the name of the mp4 file for future use"""
    names = url_string.split("/")
    name = names[-1]

    return name


def is_valid(mediafire_url):
    """
    Check is the link to mediafire is no broken
    Example of a broken link: 'https://www.mediafire.com/file/null/oretresf-01.mp4/file'
    """
    valid = True
    link_parts = mediafire_url.split("/")
    if (link_parts[4] == "null"):
        valid = False

    return valid


def download_episodes(first_episode, last_episode, url):
    """Download all the episodes between the first_episode and the last_episode, them included."""
    episode_number = first_episode

    while (episode_number <= last_episode) :
        actual_episode_url = url+str(episode_number)+"/"
        mediafire_url = get_mediafire_url(actual_episode_url)
        if ( is_valid(mediafire_url) ):
            mp4_url = extract_mp4_mediafire_url(mediafire_url)
            if(mp4_url != None):
                mp4_name = get_episode_name_from_string(mp4_url)
                download_file(mp4_name, mp4_url, episode_number)
            else:
                print("The link to mediafire of the episode "+str(episode_number)+" is broken.")
        else:
            print("The link to mediafire of the episode "+str(episode_number)+" is broken.")
        episode_number += 1


if __name__ == "__main__":
    print("Welcome to the anime downloader, for the moment this version is only available for jkanime.net")
    anime_url = input("Please insert the URL: ")
    episodes = get_number_episodes(anime_url)
    num_episodes = extract_number_from_string(episodes)
    print ("This anime has "+str(num_episodes)+" episodes available.")
    option_selected = input ("Which option do you prefer?\n[1]: Download one episode.\n[2]: Select the range of episodes to download.\n[3]: Download all the episodes.\nOption selected: ")
    option_selected = int(option_selected)
    episode_a = 0
    
    print("Remember that the episodes availables are: "+str(1)+" - "+str(num_episodes))
    if (option_selected == 1):
        episode_a = input("Which episode do you want to download: ")
        episode_a = int(episode_a)
        episode_b = episode_a
        print("One episode will be downloaded")

    if (option_selected == 2):
        print("Select the first and the last episode that do you want to download")
        episode_a = input("Select the first episode: ")
        episode_a = int(episode_a)
        episode_b = input("Select the last episode: ")
        episode_b = int(episode_b)
        print("The episodes from the "+str(episode_a)+" to the "+str(episode_b)+" will be downloaded")

    if (option_selected == 3):
        episode_a = 1
        episode_b = num_episodes
        print("All the episodes from the serie will be downloaded")
    
    if (episode_a == 0):
        print("Invalid option, please try again.")

    download_episodes(episode_a, episode_b, anime_url)
