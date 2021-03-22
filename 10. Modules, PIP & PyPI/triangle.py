
def getSides():
    sides={}
    base=int(input("Enter the base of the triangle"))
    height=int(input("Enter the height of the triangle"))
    sides["base"]=base
    sides["height"]=height
    return sides

def getArea():
    sides=getSides()
    if sides["base"]==0 and sides["height"]==0:
        print("Sides are not Set Please call function getSides() ")
    else:
        print("The area of the triangle is ",0.5*sides["base"]*sides["height"])

    