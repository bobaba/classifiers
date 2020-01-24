from cps_generator import CPSGenerator 
import math
from operator import itemgetter

class KNearestNeighbor():
  """ Find the k closest points on map and determine which class the point belongs to """

  def __init__(self, knownData, newPoints, k=5):
    self.knownData = knownData
    self.newPoints = newPoints 
    self.dimension = len(newPoints[0])
    self.k = k
    self.classes = self.classify()
  
  def pythagoreanDistance(self, point1: list, point2: list, dimensions = 2) -> float:
    """ a^2 + b^2 = c^2 """
    a = abs(point1[0] - point2[0])
    b = abs(point1[1] - point2[1])
    if dimensions == 3:
      c = abs(point1[2] - point2[2])
      return math.sqrt(a*a + b*b + c*c)
    else:
      return math.sqrt(a*a + b*b)

  def likelyClass(self, point) -> list:
    """ for a given point, return the nearest neighbors in a list """
    
    # get distance for all points in grid, store with points
    neighbs = []
    for i in self.knownData:
      d = self.pythagoreanDistance(point, i[0:-1] )
      neighbs.append([d, i])

    # sort by closest in distance, get first 'k'
    kNearest = sorted(neighbs, key=itemgetter(0))[0:self.k]

    # create a list of the classes in closest 'k' and find the most occurring one
    nearestNeighbsClasses = []
    for k in kNearest:
      nearestNeighbsClasses.append(k[1][-1]) 
    mostLikelyClass =  max(set(nearestNeighbsClasses), key = nearestNeighbsClasses.count)
    return mostLikelyClass

  def classify(self):
    # loop through each unseen point and get the nearest neighbors 
    classified = []
    for i in self.newPoints:
      classified.append(self.likelyClass(i))
    return classified
  
  def prettyPrintResults(self):
    for i,r in enumerate(self.classes):
      print(f"Unseen [{i}] = Class {r}")
      



