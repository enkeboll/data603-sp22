
from mrjob.job import MRJob
import re

class wordcount(MRJob):

    def mapper(self, _, line):
        #Extracting the text part using regex
        review = str(re.findall(r'"(.*)"',line))   
        yield 'word_count', len(review.split())
        

    def reducer(self,key,values):
        lines,words=0,0
        for val in values:
            lines += 1
            words += val     
        yield "Average words :", words/float(lines)

if __name__ == '__main__':
    wordcount.run()
