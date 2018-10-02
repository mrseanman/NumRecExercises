'''
For some function defined in the class, uses the bisection method
to find a root near a guess x_0
'''

import numpy as np
from Function import Function

class minBisect(object):

    def __init__(self):
        return null


    def rootBracketFind(accuracy, x1, x2):
        function = Function()

        maxIter = 200
        #calculates num iterations necessary for given accuracy
        numIter = int(np.ceil(np.log2((x1 - x2)/accuracy)))

        for i in range(numIter):
            xMid = (x1 + x2)/2.
            y1 = function.eval(x1)
            y2 = function.eval(x2)
            yMid = function.eval(xMid)

            if changeOfSign(x1, mid):
                x2 = xMid
            elif changeOfSign(x2, mid):
                x1 = xMid

        return x1, x2


    def changeOfSign(x1, x2):
        s1 = np.sign(x1)
        s2 = np.sign(x2)
        signChange = True
        if s1 == s2:
            signChange = False
        return signChange
