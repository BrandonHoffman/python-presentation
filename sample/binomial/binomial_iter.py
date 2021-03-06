class BinomilValueIterator(object):
    def __init__(self, binomial, start, stop):
        self.binomial = binomial
        self.start = start
        self.stop = stop
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.stop:
            raise StopIteration("End of elements")
        else:
            cur = self.current
            self.current += 1
            return (cur, self.binomial(cur))


class Binomial(object):
    def __init__(self, slop=1, y_intercept=0):
        self.slop = slop
        self.y_intercept = y_intercept

    def iter_range(self, start, stop):
        return BinomilValueIterator(self, start, stop)

    def __str__(self):
        return "{slop}X + {y_intercept}".format(slop=self.slop,
                                                y_intercept=self.y_intercept)

    def __add__(self, binomial2):
        slop = self.slop + binomial2.slop
        y_intercept = self.y_intercept + binomial2.y_intercept
        return Binomial(slop=slop, y_intercept=y_intercept)

    def __call__(self, x):
        return self.slop * x + self.y_intercept

if __name__ == "__main__":
    b1 = Binomial(slop=2, y_intercept=2)
    print(b1)
    for results in b1.iter_range(1, 10):
        print(results)

