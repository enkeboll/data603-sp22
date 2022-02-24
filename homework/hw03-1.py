from mrjob.job import MRJob
import re

class Mrjobtextwordavg(MRJob):
    @staticmethod
    def avgwords(textcol):
        all_words=[]
        for c in textcol.lower().split():  # Converting the content to lower case and split
            c=re.sub("[^a-zA-Z]","",c)     # Considering only the words with alphabets and removing the special characters and numbers
            all_words.append(c)
            # unique_words = set(all_words)  -- Not considering the unique words as it is not part of the requirement
            avg = len(all_words)
        return avg
    
    def mapper(self, _, line):
        column=line.split(',')
        textcol=column[4]                   # Considering the Text column only to find the average of the number of words
        avg=0
        if column[4].startswith('text'):
            pass
        else:
            avg = self.avgwords(textcol)
        
        yield "Average number of words in each review ", avg
       
    def reducer(self,key, values):
      total=0
      sum=0
      for i in values:
            total+=1
            sum+=i
      yield key, round((sum/total),2)      # Rounding to two decimal values
        
if __name__ == '_main_':
    Mrjobtextwordavg.run()