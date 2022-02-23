from mrjob.job import MRJob

class AverageCoolRating(MRJob):
    """Returns average rating of any review marked cool"""
    def mapper(self, _, line):
        fields = line.split(',')
        if fields[7] != 0 and fields[3] != "stars":
            yield 'cool-rating', float(fields[3])

    def reducer(self, key, values):
        total, count = 0, 0
        for value in values:
            total += value
            count += 1
        yield "average-cool-rating", total / count

if __name__ == '__main__':
    AverageCoolRating.run()