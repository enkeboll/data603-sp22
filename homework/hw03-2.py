from mrjob.job import MRJob
import re


class MrjobDateavgbyM(MRJob):
    
    @staticmethod
    def formattoDY(datecol):
        date_formatting = re.compile(r"\d{4}-\d{2}") # Formatting the date in required format
        new_date = date_formatting.findall(datecol)
        return new_date

    def mapper(self, _, line):
        columns=line.split(',')
        datecol=columns[1]
        if datecol.startswith('date'):
            pass
        else:
            dateval = self.formattoDY(str(datecol))
            
            yield dateval, 1

    def reducer(self, key, values):
        yield key, sum(values)

if __name__ == '__main__':
    MrjobDateavgbyM.run()