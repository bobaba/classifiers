from random import randrange
import matplotlib.pyplot as plt

class CPSGenerator():
  """ Generate a mock problem space for testing classifier algorithms 
    | lengthOfSides = size for grid(xyz..) 
    | numPoints = number of points to place on grid 
    | numClasses = # of different classes to put in the problem space 
    | numUnseen = # to plot on grid that are not assigned classes 
    | numDimensions = choose between 2D or 3D 
    | data = supply your own set of data if preferred 

    Example Usage: 
    a = CPSGenerator(10,20,3,3)
    print(a.data)
    print(a.unseen)
    a.showScatterPlot()
    """

  def __init__(self, lengthOfSides, numPoints, numClasses, numUnseen, numDimensions = 2, data = None):

    self.lengthOfSides = lengthOfSides 
    self.numPoints = numPoints 
    self.numClasses = numClasses 
    self.numUnseen = numUnseen
    self.dimensions = numDimensions
    if data == None:
      self.data = self.createData()
    else: 
      self.data = data 
    self.unseen = self.createUnseen()
    
  
  def createData(self):
    """ Given the inputs to generator, create a random data set """
    data = []
    while len(data) < self.numPoints:
      coords = []
      for _ in range(0,self.dimensions):
        coords.append(randrange(self.lengthOfSides))
      cls = [randrange(self.numClasses) + 1]
      if coords not in [r[0:-1] for r in data]:
        data.append(coords + cls)
    return data
  
  def createUnseen(self):
    uData = []
    while len(uData) < self.numUnseen:
      coords = []
      for _ in range(0,self.dimensions):
        coords.append(randrange(self.lengthOfSides))    
      if coords not in [r[0:-1] for r in self.data] and coords not in uData:
        uData.append(coords)
    return uData

  def showScatterPlot(self):

    # Plot random known data points
    xs = [self.data[x][0] for x in range(0,self.numPoints)]
    ys = [self.data[y][1] for y in range(0,self.numPoints)]
    clsss = [self.data[c][-1] for c in range(0,self.numPoints)]
    if self.dimensions == 3:
      zs = [self.data[z][0] for z in range(0,self.numPoints)]
    
    # Plot Unseen Data Points 
    uxs = [self.unseen[x][0] for x in range(0,self.numUnseen)]
    uys = [self.unseen[y][1] for y in range(0,self.numUnseen)]
    ulab = list(range(0,len(uxs)))
    
    if self.dimensions == 2:
      fig, ax = plt.subplots()
      scatter = ax.scatter(xs, ys, c=clsss)   
      ax.scatter(uxs, uys, marker="x", c='red', label="Unseen")
      ax.grid(True)
      fig.tight_layout()
      legend1 = ax.legend(*scatter.legend_elements(alpha=0.5),
                            loc="best", title="Classes")
      for i, txt in enumerate(ulab):
        ax.annotate(txt, (uxs[i], uys[i]))
      ax.add_artist(legend1)
      plt.show()


    