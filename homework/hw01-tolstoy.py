import requests
import re

def remove_punctuation(my_string):
    """
    Removes punctuation from a string using regex.
    """
    return re.sub('[^a-zA-Z0-9\s]', '', my_string)

# use requests to get the text from the url
def main(url):
    """
    Main function that takes a url and returns the lenth of the unique word set.
    """
    response = requests.get(url)
    # It comes back in the wrong encoding ISO-8859-1 when it should be UTF-8-SIG. Easy fix. 
    response.encoding = response.apparent_encoding

    # Text of the actual book starts in the text file after the following string
    raw_text = response.text.split('*** START OF THE PROJECT GUTENBERG EBOOK WAR AND PEACE ***')[1]
    
    # Remove punctuation and split the text into a list of words
    text_no_punctuation = remove_punctuation(raw_text)
    text_unique_words = set(text_no_punctuation.split())

    # Return the len of the set of unique words
    return len(text_unique_words)

if __name__ == '__main__':
    url = 'https://www.gutenberg.org/files/2600/2600-0.txt'
    print('The number of unique words in the book is:', main(url))    

