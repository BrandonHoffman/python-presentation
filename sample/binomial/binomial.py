class Binomial(object):
    def __init__(self, slop=1, y_intercept=0):
        self.slop = slop
        self.y_intercept = y_intercept

if __name__ == "__main__":
    b1 = Binomial(slop=2, y_intercept=2)
    print(b1)
