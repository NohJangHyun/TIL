from mrjob.job import MRJob
from mrjob.step import MRStep

class PopMovie(MRJob):
        def steps(self):
                return [
                        MRStep(mapper=self.map_rating_count,
                        combiner=self.combine_rating_count,
                        reducer=self.reduce_rating_count),
                        MRStep(reducer=self.reduce_sort)
                        ]

        def map_rating_count(self,_,line):
                userid, movieid, rating, timestamp = line.split(',')
                if userid != 'userId':
                        yield(movieid, (float(rating), 1))

        def combine_rating_count(self, movie_id, rating):
                value = 0
                count = 0
                for val, cnt in rating:
                    value += val
                    count += cnt
                yield(movie_id, (value, count))

        def reduce_rating_count(self, movie_id, rating):
                value = 0
                count = 0
                for val, cnt in rating:
                    value += val
                    count += cnt
                yield None, (value/count, movie_id)

        def reduce_sort(self, count, movie_ids):
            for avg, movie in sorted(movie_ids, reverse=True):
                yield(movie, avg)

if __name__ == '__main__':
        PopMovie.run()

