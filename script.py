import requests

URL = "http://download2341.mediafire.com/np1fuwdg7vug/jzvatwj4039ixai/yahorr-12.mp4"

def downloadfile(name,url):
    name=name+".mp4"
    r=requests.get(url)
    print ("****Connected****")
    f=open(name,'wb')
    print ("Downloading.....")
    for chunk in r.iter_content(chunk_size=255): 
        if chunk: # filter out keep-alive new chunks
            f.write(chunk)
    print ("Done")
    f.close()

downloadfile("yahorr-12",URL)

