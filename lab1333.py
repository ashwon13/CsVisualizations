 #name:Ashwin
#date:12/8/2020
from Tkinter import Tk,Canvas
w=0
h=0
float(w)
float(h)
w,h=640,480
root=Tk()
cnvs=Canvas(root,width=w,height=h,bg="cyan")
cnvs.pack()


data=open("lab1333.txt").read().split()
xy=[]
position=0
while position<len(data):
   x=float(data[position])
   
   position+=1
   y=float(data[position])
   position+=1
   
   xy.append((x,y))
   
   
xmin,xmax=-78,-75
ymin,ymax=38,39
xp=0
yp=0
xyp=[]
j=0
while j<len(xy):
    x,y=xy[j]
    xp=0.05*w+0.90*w*(x-xmin)/(xmax-xmin)
    yp=0.05*h+0.90*h*(y-ymin)/(ymax-ymin)
    xyp.append((xp,yp))
    j+=1
    
    
    
cnvs.create_polygon(xyp,fill="black",outline="black")
