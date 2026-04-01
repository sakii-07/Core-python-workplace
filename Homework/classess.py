# Q.2 create five classes of your choice add minimum 2 attributes and one method in each class

# class 1 - Bus
class Bus:
    def __init__(self,bn,cl,cp,r):
        self.bus_number = bn
        self.color = cl
        self.capacity = cp
        self.route = r

    def travelling(self):
        print(f"Bus {self.bus_number} is travelling to {self.route}.")

b = Bus(92,"White",50,"Swargate")
b.travelling()
'''
Bus 92 is travelling to Swargate.
'''

# class 2 - Tree
class Tree:

    def __init__(self,t,h,g,fb):
        self.type = t
        self.height = h 
        self.age = g 
        self.is_fruit_bearing = fb

    def grow(self):
        self.height += 10   # increase height
        self.age += 1       # increase age
        print("Tree is growing")

t = Tree("Mango",300,15,True)
t.grow() # Tree is growing

# class 3 - WaterFilter
class WaterFilter:

    def __init__(self,b,c,io):
        self.brand = b 
        self.capacity = c 
        self.is_on = io

    def filter_water(self):
        pass

w = WaterFilter("Aquaguard",15,True)

# class 4 - Road
class Road:

    def __init__(self,n,loc,l,t,tl):
        self.name = n
        self.location = loc
        self.length = l
        self.type = t
        self.traffic_level = tl

    def traffic(self):
        pass

r = Road("solapur - pune highway","Maharashtra",500,"Highway","Medium")
r1 = Road("Karve Nagar Main Road", "Karvenagar, Pune", 4, "City Road", "High")

# class 5 - Notebook
class Notebook:

    def __init__(self,b,p,pr,s):
        self.brand = b 
        self.pages = p 
        self.price = pr 
        self.size = s

    def write(self):
        pass

n = Notebook("classmate",172,65,"27.7 * 21 cm")

# Q.3 create ipl 2026 team of your choice .(list)

class Players:

    def __init__(self,jn,pn,r,tn,wk):
        self.jersey_no = jn
        self.p_name = pn
        self.runs = r
        self.t_name = tn
        self.wickets = wk
    
    def display(self):
        print(self.jersey_no,",",self.p_name,",",self.runs,",",self.t_name,",",self.wickets)


p1 = Players(45,"Rohit Sharma",8745,"MI",8)
p2 = Players(63,"Suryakumar Yadav",3500,"MI",2)
p3 = Players(7,"Tilak Varma",1500,"MI",3)
p4 = Players(33,"Hardik Pandya",2500,"MI",60)
p5 = Players(12,"Will Jacks",1200,"MI",20)
p6 = Players(30,"Quinton de Kock",3000,"MI",1)
p7 = Players(55,"Mitchell Santner",800,"MI",40)
p8 = Players(93,"Jasprit Bumrah",200,"MI",150)
p9 = Players(18,"Trent Boult",100,"MI",120)
p10 = Players(21,"Deepak Chahar",150,"MI",80)
p11 = Players(10,"Shardul Thakur",500,"MI",70)

# List of players
MI_Team = []
MI_Team.append(p1)
MI_Team.append(p2)
MI_Team.append(p3)
MI_Team.append(p4)
MI_Team.append(p5)
MI_Team.append(p6)
MI_Team.append(p7)
MI_Team.append(p8)
MI_Team.append(p9)
MI_Team.append(p10)
MI_Team.append(p11)

# Display the players
for i in MI_Team:
    i.display()

'''
45 , Rohit Sharma , 8745 , MI , 8
63 , Suryakumar Yadav , 3500 , MI , 2
7 , Tilak Varma , 1500 , MI , 3
33 , Hardik Pandya , 2500 , MI , 60
12 , Will Jacks , 1200 , MI , 20
30 , Quinton de Kock , 3000 , MI , 1
55 , Mitchell Santner , 800 , MI , 40
93 , Jasprit Bumrah , 200 , MI , 150
18 , Trent Boult , 100 , MI , 120
21 , Deepak Chahar , 150 , MI , 80
10 , Shardul Thakur , 500 , MI , 70
'''
