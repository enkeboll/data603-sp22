
from mrjob.job import MRJob
import re

class ReviewCount(MRJob):

    def mapper(self, _, line):
        col = line.split(',')
        date = col[1]
        year_month = str(re.findall(r"\d{4}-\d{2}", date))
        yield year_month , 1
        

    def reducer(self,key,values):
           yield key, sum (values)

if __name__ == '__main__':
    ReviewCount.run()
