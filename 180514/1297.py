import math

diagonal,height_rate,width_rate=map(int,input().split())
diagonal_rate=math.sqrt(height_rate**2+width_rate**2)
height=diagonal/diagonal_rate*height_rate
width=diagonal/diagonal_rate*width_rate
print(int(height),int(width))