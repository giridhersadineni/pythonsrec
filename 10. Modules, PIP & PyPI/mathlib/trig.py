import pydoc
def add(a,b,*argtuple):
    '''
    def add(a,b,**argtuple):
    This function returns the sum of any number of values passed to it
    Arguments: 
    a,b Mandatory
    '''
    sum=a+b
    for i in argtuple:
        sum=sum+i
    return sum

def sumofn(n):
    sum=0
    for i in range(n):
        sum=sum+i
    return sum



if __name__ == "__main__":
    print(add(1,3,4,56,7))