import numpy as np
import scipy as s

class commonStats():

    def __init__(self, List):
        assert type(List) == list and len(List) > 0
        self.List = List

    def maximum(self):
        x = -8000000000000000000000000000000
        for i in self.List:
            if i > x:
                x = i
        return x

    def minimum(self):
        x = 880000000000000000000000000000000
        for i in self.List:
            if i<x:
                x = i
        return x

    def mean(self):
        sum = 0
        for i in self.List:
            sum = sum + i

        return sum/len(self.List)

    def stdDev(self):
        sumSquare = 0
        count = len(self.List)
        mean = np.mean(self.List)
        if len(self.List) == 1:
            return 0
        else:
            for i in self.List:
                sumSquare = sumSquare + (mean - i)**2
        return (sumSquare/(count-1))**0.5


class binarySearch(commonStats):
    def __init__(self, List):
        commonStats.__init__(self, List)
        self.List = sorted(List)

    def binSearch(self, item):
        low = 0
        high = len(self.List)-1
        if len(self.List) == 1:
            if self.List[0] == item:
                return 0
            else: return 'Not found'
        else:
            while low <= high:
                mid = (high + low) // 2
                if self.List[mid] == item:
                    return mid
                elif self.List[mid] < item:
                    low = mid+1
                elif self.List[mid] > item:
                    high = mid-1
                else:
                    return 'Not found'

class sorting(binarySearch):
    def _init_(self, List):
        self.List = List
    def selectionSort(self):
        List = self.List[:]
        for i in range(0, len(self.List)):
            for j in range(0, len(self.List)):
                if List[i] > List[j]:
                    List[j], List[i] = List[i], List[j]
        return List

    def mergeSort(self, firstlist, secondlist):
        result = []
        count = 0

        return result

myZero = [1]
myTest = [15,12,20,11,10,9,8,7,6,5,4,3,2,13,67,8,90,76,89,65,65,56,76,87,1000]

myList = sorting(myTest)
print(myList.selectionSort())
#print(myList.mergeSort([3,18,20,56,80,90,100], [2,3,4,5,6]))
#print('Max',myList.maximum())
#print('Mean',myList.mean())
#print('Min', myList.minimum())
#print('Std Dev.', myList.stdDev())


xdat = [0,3,4,6,7,5]
ydat = [1,4,6,3,8,9]


x = np.array(xdat).reshape(len(xdat), 1)
y = np.array(ydat).reshape(len(xdat), 1)

m = x.transpose() @ x
m = np.linalg.inv(m)
m = m @ x.transpose()
m = m @ y

c = np.sum(ydat) - m * np.sum(xdat)

# 1A
B = np.array([[1 , 1, 1],[0, 1, 2]]).T
x = np.array([6, 0, 0])
proj = B @ np.linalg.inv( B.T @ B) @ B.T @ x.T
lam = np.linalg.inv( B.T @ B) @ B.T @ x.T
projMat = B @ np.linalg.inv( B.T @ B) @ B.T
projMatRan = np.linalg.matrix_rank(projMat)
print('1A:', projMatRan)
print("ProjMat" ,projMat)
print("lam & Proj", lam, proj)

# 1B
B = np.array([[1 , 1, 1],[0, 1, 2]]).T
x = np.array([12, 0, 0])
proj = B @ np.linalg.inv( B.T @ B) @ B.T @ x.T
lam = np.linalg.inv( B.T @ B) @ B.T @ x.T
projMat = B @ np.linalg.inv( B.T @ B) @ B.T
projMatRan = np.linalg.matrix_rank(projMat)

print("3: lam & Proj", lam, proj)
# 2

ot = np.array([[1 ,-1/2],[-1/2, 5]])
x = np.array([0, -1])
y = np.array([1, 1])
length = np.sqrt(((x @ ot) @ x.T) * ((y @ ot) @ y.T))
angle = ((y @ ot) @ x.T )/length
print('2:', angle,np.arccos(angle))
#3

ot = np.array([[2 ,1],[1, 4]])
x = np.array([2, 2])
y = np.array([-2, -2])
length = np.sqrt(((x @ ot) @ x.T) * ((y @ ot) @ y.T))
angle = ((y @ ot) @ x.T )/length
print("3:", length, angle, np.arccos(angle))

#4

ot = np.array([[1 ,0],[0, 5]])
x = np.array([1, 1])
y = np.array([1, -1])
length = np.sqrt(((x @ ot) @ x.T) * ((y @ ot) @ y.T))
angle = ((y @ ot) @ x.T )/length
print("4:", angle, np.arccos(angle))

# 5
ot = np.array([[1 ,0, 0],[0, 2, -1], [0, -1, 3]])
x = np.array([1, 1, 1])
y = np.array([2, -1, 0])
length = np.sqrt(((x @ ot) @ x.T) * ((y @ ot) @ y.T))
angle = ((y @ ot) @ x.T )/length
print("5:", angle, np.arccos(angle))

print(np.linalg.norm([1,2])**2)

def il(z, k):
    (z, k) = 5, 6
    return (z, k)
print(il)