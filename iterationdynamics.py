#import matplotlib as plt
import numpy as np
import config
import accurancy
import diagmatrix
class IterationDynamic(object):
    def __init__ (self, x_new:np, x_old:np):
        self._itmark = 0
        self.x_new: np = x_new
        self.x_old: np = x_old
        self.matrix = diagmatrix.rdiagmatrix(len(x_new))
        self._accuracy = accurancy.maxvectoraccuracy(self.x_new, self.x_old, self.matrix)
        self.xhistory = np.zeros((len(x_new), config.maxiter+1))
        for i in range(x_new.size): self.xhistory[i, 0] = x_new[i]
        self.accuracyhistory = np.zeros(config.maxiter+1)
        self.accuracyhistory[0] = self._accuracy
    def state_version(self, itmark):
        self._itmark = itmark
        self._accuracy = accurancy.maxvectoraccuracy(self.x_new, self.x_old, self.matrix)
        self.accuracyhistory[itmark] = accurancy.maxvectoraccuracy(self.x_new, self.x_old, self.matrix)
        for i in range(len(self.x_new)):
            self.xhistory[i,itmark,] = self.x_new[i]
    def accuracyget(self):
        return(self._accuracy)
    def itmarkget(self):
        return(self._itmark)
    def isNeedToComplete(self):
        eps = config.eps
        return(self._accuracy<=eps)
    # def PlotAccuracyGraphic(self):
    #     marks = np.zeros((len(self.x_new)))
    #     for i in range(1,len(self.x_new)):
    #         marks[i]+= 1
    #     plt.plot(itmarks,self.accurancyhistory)
    #     plt.show()
    # def PlotValsDynamicsTab(self):
    #     val1 = ["{:X}".format(i) for i in range(len(self.accurancyhistory))]
    #     val2 = ["{:02X}".format(len(self.accurancyhistory)) for i in range(len(self.accurancyhistory))]
    #     val3 = [["" for c in range(len(self.accurancyhistory))] for r in range(len(self.accurancyhistory))]
    #     fig,.subplots()
    #     ax.set_axis_off() .table(
    #         ,
    #         ,
    #         ,
    #         rowColors =["palegreen"]*len(self.accurancyhistory)
    #         colColors =["palegreen"]*len(self.accurancyhistory)
    #         ,
    #         )
