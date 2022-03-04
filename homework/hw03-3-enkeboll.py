from mrjob.job import MRJob
import csv

class MRReviewsByMonth(MRJob):

    def mapper(self, _, line):
        reader = csv.reader([line])
        for line in reader:
            if line[0].startswith('business_id'):
                return
            if int(line[7]) > 0:
                yield "stars", line[3]


    def reducer(self, key, values):
        sum_stars, count_stars = 0, 0
        for val in values:
            sum_stars += int(val)
            count_stars += 1
        yield key, sum_stars / count_stars

if __name__ == '__main__':
    MRReviewsByMonth.run()
