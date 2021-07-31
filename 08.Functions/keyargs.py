def volume(length,breadth,height,**values):
    return length*breadth*height

cube={
    'length':10,
    'breadth':25,
    'height':6,
     'corner_radius':25
}



v=volume(**cube)


print(v)