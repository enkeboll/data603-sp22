from mrjob.job import MRJob
import re
import csv


class Mrjobavgrating(MRJob):
      
    
    def mapper(self, _, line):
        
        columns=line.split(',')
        
        starcol = columns[3]
        coolcol = columns[7]
        if starcol.startswith('stars'):
            pass
        else:
            if coolcol.startswith('cool'):
                pass
            else:
                if(coolcol != 0):
                    yield "Avg Rating Stars where cool!=0", int(starcol)
        
    

    def reducer(self,key, values):
      avg,avg1=0,0
      for i in values:
            avg+=1
            avg1+=i
      yield key, round((avg1/avg),2)
        
if __name__ == '_main_':
    Mrjobavgrating.run()