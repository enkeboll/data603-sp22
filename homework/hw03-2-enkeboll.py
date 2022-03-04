import re
from mrjob.job import MRJob

date_update = re.compile(r'\d\d\d\d-\d\d')

class MRDateCount(MRJob):
    
    @staticmethod
    def date_Change(tc_date):
        date = date_update.findall(tc_date)
        return date

    def mapper(self, _, line):
        (a) = line.split(',')
        if a[4].startswith('text'):
            pass
        else:
            date = self.date_Change(str(a[1]))
            yield date, 1

    def reducer(self, date, cur_num):
        yield date, sum(cur_num)

if __name__ == '__main__':
    MRDateCount.run()