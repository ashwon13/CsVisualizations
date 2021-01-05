#name:Ashwin
#date:12/8/2020
from Tkinter import Tk,Canvas

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
   
#getting and storing data  

 
xmin,xmax=-78,-75
ymin,ymax=38,39

xyp=[]
j=0
while j<len(xy):
    x,y=xy[j]
    
   
    xp=int((640/3)*x+16640)
    yp=int(480*(y)-18240)
   
    '''
    xp=608*((x-xmin)/3)
    yp=456*((y-ymin)/1)
    
    
    xp=int((64/20)*(x)+320)
    yp=int((48/9)*(y)+240)
    '''
    xyp.append((xp,yp))
    
    
    
    j+=1
    print xyp
    
cnvs.create_polygon(xyp,fill="blue",outline="red")
root.mainloop()
