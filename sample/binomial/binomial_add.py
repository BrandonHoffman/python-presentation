class Binomial(object):
    def __init__(self, slop=1, y_intercept=0):
        self.slop = slop
        self.y_intercept = y_intercept

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
    b2 = Binomial(slop=1, y_intercept=5)
    print("f=" + str(b1))
    print("g=" + str(b2))
    for x in range(10):
        print("(f+g)({x})={res}".format(x=x, res=(b1 + b2)(x)))

