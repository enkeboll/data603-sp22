from mrjob.job import MRJob
import csv

class MRWordFrequencyCount(MRJob):

    def mapper(self, _, line):
        reader = csv.reader([line])
        for line in reader:
            if line[0].startswith('business_id'):
                return
            yield 'avg_words', len(line[4].split())


    def reducer(self, key, values):
        total_words = 0
        total_reviews = 0
        for val in values:
            total_words += val
            total_reviews += 1
        yield "The average number of words", total_words / total_reviews


if __name__ == '__main__':
    MRWordFrequencyCount.run()
