import numpy as np

class GaussPDF(object):

    def __init__(self, mean, stdDev, lowerBound, upperBound):
        self.mean = float(mean)
        self.stdDev = float(stdDev)
        self.lower = float(lowerBound)
        self.upper = float(upperBound)
        #this is particular to the gaussian
        self.fMax = self.evaluate(self.mean)

    #returns random number with gaussian distribution
    #uses box method
    def nextBox(self):
        #boolean for wether we have found a value to return
        foundVal = False
        while not(foundVal):
            x = np.random.uniform(self.lower, self.upper)
            y = np.random.uniform(0., self.fMax)
            if y <= self.evaluate(x):
                foundVal = True
        return x


    #returns value of gaussian function at x
    def evaluate(self, x):
        val = (1./(self.stdDev*np.sqrt(2.*np.pi))) * np.exp(-(x-self.mean)**2./(2*self.stdDev**2.))
        return val
