import random

class Drone:
    def __init__(self, ID):
        self.ID = ID
        self.active = True
        self.todo = []
    
    def update(self, todo):
        self.todo = todo
    
    def getToDo(self):
        return self.todo

    def getDone(self):
        if random.randrange(20) != 0 :
            #randomly fails
            return self.todo[0]
        else:
            return None
    
    def isActive(self):
        return self.active
    
    def off(self):
        self.active = False
        #self.todo = []

def mapPrint(lst, height):
    str = ''
    for j in range(len(lst)):
        if lst[j]:
            str += 'O'
        else:
            str += 'X'
        if (j+1)%height == 0:
            print(str)
            str = ''
    print('')

n = 8
k = 3*n//4

drones = [Drone(i) for i in range(n)]
area = [False for i in range(10*k)]
active = [i for i in range(k)] #list of currently working drones. when one fails, another takes its place on the list

for i in active:
    drones[i].update([j for j in range(10*i, 10*i+10)])

while (not all(area)) and k < n:
    scans = [drones[i].getDone() for i in active]
    i = 0
    mapPrint(area, 10)
    for scan in scans:
        lst = drones[active[i]].getToDo()
        if scan != None:
            area[scan] = True

            if len(lst) == 1:
                drones[active[i]].off()
            else:
                drones[active[i]].update(lst[1:])
        else:
            drones[active[i]].off()
            drones[k].update(lst)
            active[i] = k
            k += 1
        i += 1
mapPrint(area, 10)