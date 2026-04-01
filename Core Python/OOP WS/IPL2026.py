# task 1 -In IPL 2026 players has jersey no,p_name, runs,t_name and wickets. There is one operation 
# with player which displays players name and team name.

class Players:

    def __init__(self,jn,pn,r,tn,wk):
        self.jersey_no = jn
        self.p_name = pn
        self.runs = r
        self.t_name = tn
        self.wickets = wk
    
    def display(self):
        print(self.p_name,"---->",self.t_name)

p1 = Players(45,"Rohit Sharma",8745,"MI",8)
p2 = Players(18,"Virat Kohli",7865,"RCB",3)
p3 = Players(63,"Suryakumar Yadav",3456,"MI",1)
p4 = Players(1,"KL rahul",2345,"DC",2)
p5 = Players(93,"Jasprit Bumrah",123,"MI",120)

print(p1.jersey_no)
p1.display()
p2.display()
p3.display()
p4.display()
p5.display()

'''
Rohit Sharma ----> MI
Virat Kohli ----> RCB
Suryakumar Yadav ----> MI
KL rahul ----> DC
Jasprit Bumrah ----> MI
'''
        