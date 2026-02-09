import math
 
def jarak(x1, y1, x2, y2):
    d = math.sqrt((x2 -x1)**2 + (y2 -y1)**2)
    return d

x1, x2 = 6, 2
y1, y2 = 5, 2
print('jarak =',jarak(x1, y1, x2, y2)) #output: 5.0