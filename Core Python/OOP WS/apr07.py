'''
2) Encapsulation ---->  It is one of the imp pillar of OOPs.
                        Binding of data members(Attributes) and methods into single entity is aclled as Encapsulation
                        We can achieve encapsulation by making all attributes private and access 
                          them using getter and setters method.
                        Data security, controlled access of data.

private ----> private is one access specifier / modifier  

access specifiers ---> There ere three types of specifer in py
                                1) public
                                2) private(_ _)
                                3) protected(_)

Q. how to make variables private ?
-> preceeding variable by name _ _
   ex. self.__age

Q. how to make variables protected ?
-> preceeding variable name by _
   ex. self._age
'''
class Student:  # Entity class

    def __init__(self,a,l):
        self.__age = a 
        self.__loc = l

    def getAge(self,pin):
        if pin == 1234:
            return self.__age
        else:
            return 0
    
    def getloc(self):
        return self.__loc
    
    def setAge(self,na):
        self.__age = na

    def setLoc(self,nl):
        self.__loc = nl

s = Student(21,"sakshi")

age = s.getAge(1234)
loc = s.getloc()
print(age,loc) # 21 sakshi

s.setAge(26)
print(s.getAge(1234)) # 26

# create entity class of player with jersey_no,name,runs,wickets and team name

class Player:

    def __init__(self,jn,n,r,w,tn):
        self.__jersey_no = jn
        self.__name = n 
        self.__runs = r 
        self.__wickets = w 
        self.__team_name = tn 
    
    def getJerseyNo(self):
        return self.__jersey_no
    
    def getName(self):
        return self.__name
    
    def getRuns(self):
        return self.__runs
    
    def getWickets(self):
        return self.__wickets
    
    def getTeamName(self):
        return self.__team_name

    def setJerseyNo(self,njn):
        self.__jersey_no = njn

    def setName(self,nn):
        self.__name = nn

    def setRuns(self,nr):
        self.__runs = nr
    
    def setWickets(self,nw):
        self.__wickets = nw

    def setTeamName(self,ntn):
        self.__team_name = ntn

p = Player(45,"Rohit Sharma",6546,10,"MI")
jn = p.getJerseyNo()
name = p.getName()
runs = p.getRuns()
w = p.getWickets()
tn = p.getTeamName()

print(jn,name,runs,w,tn) # 45 Rohit Sharma 6546 10 Mi

p.setRuns(7000)
print(p.getRuns()) # 7000

p1 = Player(18,"Virat Kohli",7865,3,"RCB")
jn = p1.getJerseyNo()
name = p1.getName()
runs = p1.getRuns()
w = p1.getWickets()
tn = p1.getTeamName()

print(jn,name,runs,w,tn) # 18 Virat Kohli 7865 3 RCB

'''
The operation which is for developer not for client then make that method private
'''