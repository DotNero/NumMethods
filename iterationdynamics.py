import matplotlib as plt
import numpy as np
import config
import accurancy
class IterationDynamic(object):
    """docstring"""
    def _init_ (self, x_new, x_old):
        self._itmark = 0
        self._accuracy = accurancy.accuracyparametrforvector(self.x_new, self.x_old)
        self.x_new:np = x_new
        self.x_old:np = x_old
        self.accuracyhistory = accurancy.accuracyparametrforvector(self.x_new, self.x_old)

    # def _init_(self):
    #     self._itmark = 0
    #     self._accuracy
    #     self.x_new:np
    #     self.x_old:np
    #     self.accuracyhistory
    def state_version(self, itmark:int):
        self._itmark = itmark
        self._accuracy = accurancy.accuracyparametrforvector(self.x_new, self.x_old)
        self.accuracyhistory[itmark] = accurancy.accuracyparametrforvector(self.x_new, self.x_old)
    def itmarkget(self):
        return(self._itmark)
    def accuracyget(self):
        return(self._accuracy)

    def isNeedToComplete(self):
        eps = config.eps
        return(accurancy.accuracyparametr(self.x_new, self.x_old))
    def PlotAccuracyGraphic(self):
        marks = np.zeros((len(self.x_new)))
        for i in range(1,len(self.x_new)):
            marks[i]+= 1
        plt.plot(marks,self.accurancyhistory)
        plt.show()
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
