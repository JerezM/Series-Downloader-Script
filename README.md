# Series Downloader Script

This is a script that will help you download episodes from your favorite series. This version only let you download from jkanime, but we are trying to expand this in future versions.

## Getting Started

This script is written in Python 3.8 and using pip 20.2.3 to install the respective dependencies.

### Installing Dependencies
I will show you how is the installation using python 3.8.
#### Installing Requests and Supported Versions

Requests is available on PyPI:

```console
$ python3.8 -m pip install requests
```

Requests officially supports Python 2.7 & 3.5+.
#### Installing bs4 and BeautifulSoup

```console
$ python3.8 -m pip install bs4
```
```console
$ python3.8 -m pip install beautifulsoup4
```

## How to use it
First of all, you must be located in the folder that contains the script, in my case it will be:
```console
... :~/VS-workspace/Series-Downloader-Script$
```
Then you run the script and you will see the next:
```console
Please insert the URL: 
```
After sending the URL you shall see the next display showing you the different options of download: 
![Options DL](https://www.linkpicture.com/q/Options_DL.jpeg)

You can choose which one you like, on this case we will use the second one. After choosing the option 2, you will have to complete 2 sections:
```console
Select the first episode: 
Select the last episode:
```
At the end of this, the downloads will start and all the episodes will be stored at the same folder of the script.
Example:
![DL Process](https://linkpicture.com/q/DL_process.jpeg)
