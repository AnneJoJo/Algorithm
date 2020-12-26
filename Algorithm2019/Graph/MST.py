#krustal alogrithnm
'''
[1,4,3,4,4]   set(0,1)(2,3)(0,4)(3,4)
 0 1 2 3 4

0 1 : 2
2 3 : 3
0 4 : 4
3 4 : 5
1 2 : 8

0---1----|
|        |
4----3---2

'''
class Edge:
    def __init__(self,begin,end,cost):
        self.begin = begin
        self.end = end
        self.cost = cost


class Krustal:

    def __init__(self,Edges):
        self.edges = Edges


    def union(self,x,y,root):
        root[x] = y


    def find(self,x,root):
        while root[x] != x:
            x = root[x]

        return x


    def krustal(self,n):
        res = []
        root = [i for i in range(n)]
        self.edges.sort(key=lambda x:x.cost)

        for edge in self.edges:

            x1 = edge.begin
            x2 = edge.end

            y1 = self.find(x1,root)
            y2 = self.find(x2,root)

            if y1 != y2:
                self.union(y1,y2,root)
                res.append(edge.cost)
        return sum(res)


e1 = Edge(0, 1, 5)
e2 = Edge(1, 2, 4)
e3 = Edge(2, 9, 2)
e4 = Edge(0, 4, 1)
e5 = Edge(0, 3, 4)
e6 = Edge(1, 3, 2)
e7 = Edge(2, 7, 4)
e8 = Edge(2, 8, 1)
e9 = Edge(9, 8, 0)
e10 = Edge(4, 5, 1)
e11 = Edge(5, 6, 7)
e12 = Edge(6, 8, 4)
e13 = Edge(4, 3, 2)
e14 = Edge(5, 3, 5)
e15 = Edge(3, 6, 11)
e16 = Edge(6, 7, 1)
e17 = Edge(3, 7, 2)
e18 = Edge(7, 8, 6)

list = [e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16,e17,e18]

k = Krustal(list)
print(k.krustal(10))





