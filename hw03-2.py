from mrjob.job import MRJob

class YearMonthCounter(MRJob):
    """returns the count of reviews by year-month"""

    def mapper(self, _, line):
        fields = line.split(',')
        if fields[1] != 'date':
            yield fields[1][:7], 1

    def reducer(self, key, values):
        yield key, sum(values)

if __name__ == '__main__':
    YearMonthCounter.run()