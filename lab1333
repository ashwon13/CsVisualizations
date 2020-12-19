#name:Ashwin
#date:12/8/2020
from Tkinter import Tk,Canvas
w=0
h=0
float(w)
float(h)
w,h=640,480
root=Tk()
cnvs=Canvas(root,width=w,height=h,bg="red")
cnvs.pack()
data=open("lab1333.txt").readlines().split(" ")
xy=[]
index=0
x=0
y=0
float(x)
float(y)
while index<len(data):
    
    x=float(data[index])
    index+=1
    y=float(data[index])
    index+=1
    
    xy.append((x,y))



xmin,xmax=-78,-75
ymin,ymax=38,39
float(xmin)
float(xmax)
float(ymin)
float(ymax)
xp=0
yp=0
float(xp)
float(yp)

xyp=[]
j=0
while j<len(xy):
    x,y=xy[j]
    xp=0.05*w+0.90*w*(x-xmin)/(xmax-xmin)
    yp-0.05*h+0.90*h*(y-ymin)/(ymax-ymin)
    float(xp)
    float(yp)
    xyp.append((xp,yp))
    j+=1
cnvs.create_polygon(xyp,fill="black",outline="blue")
root.mainloop() 
