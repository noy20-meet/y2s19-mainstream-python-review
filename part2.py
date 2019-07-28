# Part 2 of the Python Review lab.
def prime(y):
                if (y > 1):
                        for i in range(2,y):
                                if (y % i) == 0:
                                        return False
                                
                else:
                        return True
               
        

def encode(x, y):
        if((1<y and y<250) and (500<x and x<1000)):
                while(prime(y)==False):
                        y=y+1
                while(prime(x)==False):
                        x=x+1
                if((1<y and y<250) and (500<x and x<1000)):
                        return(x*y)
                else:
                        print("Invalid input: Outside range")
                        return None  
                
                
        else:
                print("Invalid input: Outside range")
                return None
  


def decode(coded_message):
        x=501
        y=2
        while(x<1000 and y<250):
                if (cocoded_message/x==y):
                        return true
                break
                else:
                        x=x+1
                        
                return (x,y)
        
