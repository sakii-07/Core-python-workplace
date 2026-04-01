'''
Constructor ----> It is a special type of method / function of class.
or init           The name of constuctor is __init__
                  Constuctor gets automatically invoked(called) at the time of object creation.
                  The job of constuctor is to initialize attributes into heap memory.
                  It initialize object into memory.
                  'self' is the first parameter of the constructor.
                  There is no "return" statement in a connstuctor.
                  _ _methodName_ _ methods are called dunder(double underscores) methods in python.
                  There are two types of constructor
                        1) default
                        2) Parameterized

            1)  default :- 
                If we dont write constructor in side class then PVM automatically called default constructor.

                ex :
                    class Student:
                        def __init__(self):
                            pass
                
                we can write any operation inside constuctor.
                The operations that we need to perform before method call that we can write inside constructor.

'''
# task 1 -In IPL 2026 players has jersey no,p_name, runs,t_name and wickets. There is one operation 
# with player which displays players name and team name.

class players:

    def __init__(self,jn,pn,r,tn,wk):
        self.jersey_no = jn
        self.p_name = pn
        self.runs = r
        self.t_name = tn
        self.wickets = wk
    
    def display():
        print()
        


# diff between method and function

# create five classes of your choice add minimum 2 attributes and one method in each class

# create ipl 2026 of your choice .(list)