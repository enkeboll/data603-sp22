from re import I
from mrjob.job import MRJob

class AverageWords(MRJob):
    """Calculates the average number of words per review in the yelp csv file."""

    def mapper(self, _, line):
        fields = line.split(',')
        if fields[4] != 'text':
            yield 'words', len(fields[4].split())

    def reducer(self, key, values):
        total, count = 0, 0
        for value in values:
            total += value
            count += 1
        yield "average-review-len", total / count  

if __name__ == '__main__':
    AverageWords.run()