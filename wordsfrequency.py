import requests
from bs4 import BeautifulSoup
import json

 
def start(url):
    #wordlist = []
    source_code = requests.get(url).text
 
    soup = BeautifulSoup(source_code, 'html.parser')
    content= soup.text
 
    words = content.lower().split()
    create_dictionary(words)
 
def create_dictionary(clean_list):
    word_count = {}

    for word in clean_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    jsonFormat=json.dumps(word_count)
    print(jsonFormat)
 
if __name__ == '__main__':
    url = "https://sunny-creponne-3498ac.netlify.app/"
    
    start(url)