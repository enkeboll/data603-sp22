from mrjob.job import MRJob
import csv

class MRWordFrequencyCount(MRJob):

    def mapper(self, _, line):
        reader = csv.reader([line])
        for line in reader:
            if line.startswith('business_id'):
                return
            yield 'num_words', len(line[4].split())


    def reducer(self, key, values):
        total_words = 0
        total_reviews = 0
        for val in values:
            total_words += val
            total_reviews += 1
        yield key, sum(total_words) / total_reviews


if __name__ == '__main__':
    MRWordFrequencyCount.run()
