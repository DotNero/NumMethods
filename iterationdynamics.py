import matplotlib as plt
import numpy as np
import config
import accurancy
class IterationDynamic(object):
    _itmark = 0
    x_old:np = np.zeros((1))
    x_new:np = np.zeros((1))
    accuracy = 0
    accuracyhistory = np.zeros((1))
    def __init__ (self, x_new:np, x_old:np):
        self._itmark
        self._accuracy = accurancy.maxvectoraccuracy(self.x_new, self.x_old)
        self.x_new:np = x_new
        self.x_old:np = x_old
        self.accuracyhistory = np.zeros((len(x_new)))
        self.accuracyhistory[0] = self._accuracy
    def state_version(self, itmark):
        self._itmark = itmark
        self._accuracy = accurancy.maxvectoraccuracy(self.x_new, self.x_old)
        self.accuracyhistory[itmark] = accurancy.maxvectoraccuracy(self.x_new, self.x_old)
    def accuracyget(self):
        return(self._accuracy)
    def itmarkget(self):
        return(self._itmark)
    def isNeedToComplete(self):
        eps = config.eps
        return(self.accuracy<=eps)
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
