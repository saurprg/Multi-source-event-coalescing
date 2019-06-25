import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
from random import randint as rnd

class barplotter:
    """
        barplotter internally uses the matplotlib.pyplot to plot
        the bar graph
    """

    def __init__(self,obj,performance1,performance2,title,label1,label2):
        """
             ..obj : labels on x axis
             ..perfomance : y axis co-ordinates
             ..title : title for graph
        """
        self.obj=obj
        self.performance1=performance1
        self.performance2=performance2
        self.label1=label1
        self.label2=label2
        self.title=title

    def plot(self):
        """
            ..plots the data stored in barplotter object
        """
        index=np.arange(len(self.obj))
        fig,ax=plt.subplots()
        bar_wid=0.35
        opacity=0.5

        rects1 = plt.bar(index, self.performance1, bar_wid,
        alpha=opacity,
        color='g',
        label=self.label1)

        rects2 = plt.bar(index + bar_wid, self.performance2, bar_wid,
        alpha=opacity,
        color='r',
        label=self.label2)

        plt.xticks(index + bar_wid,self.obj)
        plt.title(self.title)
        plt.legend()
        plt.show()

if __name__=="__main__":
    obj=('Level 1','Level 2','Level 3','Level 4','Level 5')
    performance0=[]
    performance1=[]
    for i in range(5):
        performance0.append(rnd(1,1000))
        performance1.append(rnd(1,1000))
    bar=barplotter(obj,performance0,performance1,'event hits plot','Distinct','Duplicates')
    bar.plot()

