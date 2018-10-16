from ChiSquare import ChiSquare
import numpy as np

class MCMC(object):

    def walkerFunction(self, paramsStdDev):
        jump = np.random.normal(0.0, paramsStdDev)
        return jump

    def decideJump(self, chiEval, oldParams, newParams):
        a =
