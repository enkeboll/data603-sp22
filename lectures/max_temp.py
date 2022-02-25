from mrjob.job import MRJob

class MRMaxTemperature(MRJob):
    
    @staticmethod
    def to_fahrenheit(cels):
        celsius = float(cels) / 10.0
        fahrenheit = celsius * 1.8 + 32.0
        return fahrenheit

    def mapper(self, _, line):
        (location, date, measure_type, data, x, y, z, w) = line.split(',')
        if (measure_type == 'PRCP'):
#             temperature = self.to_fahrenheit(data)
            yield location, data

    def reducer(self, location, temps):
        yield location, max(temps)


if __name__ == '__main__':
    MRMaxTemperature.run()
    
