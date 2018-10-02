'''
Calls methods in PDF class,
keeps track of results and
plots
'''

from GaussianPDF import GaussPDF
import sys
import matplotlib.pylab as pl

class Experiment:

    def __init__(self):
        self.lowerBound = -4.
        self.upperBound = 4.
        self.mean = 0.
        self.stdDev = 1


    def gatherResults(self):
        pdf = GaussPDF(self.mean, self.stdDev, self.lowerBound, self.upperBound)

        self.results = []
        for i in range(5000):
            self.results.append(pdf.nextBox())

    def plotHist(self, data):
        pl.hist(data, bins = 100)
        pl.show()
