from urllib.request import urlopen
import re
# Opening the URL and saving the content in book variable.
book= urlopen( 'https://www.gutenberg.org/files/2600/2600-0.txt' )
all_words=[]
for b in book:
  content = b.decode("utf-8")
  for c in content.lower().split():  # Converting the content to lower case and split
      c=re.sub("[^a-zA-Z]","",c)     # Considering only the words with alphabets and removing the special characters and numbers
      all_words.append(c)
print("Length of words after cleaning (duplicate values included)", len(all_words))
unique_words = set(all_words)                   # Considering only the unique values 
print("Length of words after removing the duplicate values", len(unique_words))
count=0
for each_word in unique_words:                   # Counting only the unique values without using len function
    count += 1
    
print('Count of Unique Words:', count)
