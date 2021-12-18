import numpy as np

class Box:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.center = [(x1+x2)/2, (y1+y2)/2]

    def __lt__(self, other):
        return self.center[1] < other.center[1]

def sortPanels(panelArray):
    print(panelArray)
    print("-----------")
    boxArray = []
    margin = 0
    for item in panelArray:
        boxArray.append(Box(item[0], item[1], item[2], item[3]))
        margin += item[3]-item[1]
    margin = margin / len(panelArray)
    margin = margin / 2
    boxArray = sorted(boxArray)
    print([str(x.center) for x in boxArray])
    print("-----------")
    order = []
    closeY = [boxArray[0]]
    for x in range(1, len(boxArray)):
        if boxArray[x].center[1] - boxArray[x-1].center[1] <= margin:
            closeY.append(boxArray[x])
        else:
            closeY = sorted(closeY, key=lambda x: x.center[0])
            order.append(closeY)
            closeY = [boxArray[x]]
    if(len(closeY) != 0):
        closeY = sorted(closeY, key=lambda x: x.center[0])
        order.append(closeY)
    empty = []
    for i in order:
        for j in i:
            empty.append(j)
    print([str(x.x1) + " " + str(x.y1) + " " + str(x.x2) + " " + str(x.y2) for x in empty])

if __name__ == '__main__':
    p = np.array([[1027.0968, 74.99765, 1905.7627, 1004.3851],
 [115.114105, 1037.5176, 999.5591, 1938.6033],
 [114.23074, 1968.0476, 998.3899, 2897.414],
 [112.042114, 56.530994, 1012.34607, 1038.6584],
 [1016.2342, 1011.7388, 1915.2067, 1671.9104],
 [1568.3286, 1744.3868, 1988.0, 2314.7966],
 [1027.4484, 1748.733, 1754.0647, 3040.7634]])
    sortPanels(p)

