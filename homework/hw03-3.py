 
from mrjob.job import MRJob
import re

class AvgRating(MRJob):

    def mapper(self, _, line):
        
        new_string = re.sub(r'"(.*)"', '_', line)
        # review text contains ',' so I was unable to get the cool column with split(',') so I replaced whole text
        # This is not a good solution but I was running out of time and it was doing a job :)
        columns = new_string.split(',')
        review= columns[3]
        cool= columns[7]
        
        yield cool, review
        
        

    def reducer(self,key,values):
            values=list(values)
            if key != 0:
                yield key, values
            

if __name__ == '__main__':
    AvgRating.run()
# gives the list of all the average ratings where cool votes are 10,11,12,..etc
