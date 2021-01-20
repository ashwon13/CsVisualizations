#name:Ashwin Pulla
#date:1/11/2020
from Tkinter import Tk,Canvas
w=0
h=0
float(w)
float(h)
w,h=640,480
root=Tk()
cnvs=Canvas(root,width=w,height=h,bg="cyan")
cnvs.pack()

data=open("lab1366.txt").read().split()
xy=[]
xyp=[]
xValues=[]
yValues=[]
position=1
x=0
y=0


while position<len(data):
  
      
      
  if data[position]=="END_ALL_POLY":
      position+=1
      break 
   
  elif data[position]=="END_ONE_POLY":
      position+=1
      xy.append("END_ONE_POLY")
  
  elif data[position]=="END_FILE":
      break
      
  else:
       
         x=float(data[position])
         xValues.append(x)
         position+=1
         y=float(data[position])
         yValues.append(y)
         position+=1
   
         xy.append((x,y))   
         
      
         
         
xyp=[]
j=1
while j<len(xy):
   if xy[j]=="END_FILE":
      break
   
   elif xy[j]=="END_ONE_POLY":
      j+=1
      cnvs.create_polygon(xyp, fill="blue", outline="red",w=1)
      xyp = []
   elif xy[j]=="END_ALL_POLLY":
      j+=1
      break
      
      
   else:
      x=xValues[j]
      y=yValues[j]
      xp=int((640/3)*x+16640)
    
      yp=int(480*(y)-18240)
      yp=480-yp
    
      yp=yp+220
      xp=xp+60

      xyp.append((xp,yp))
      
      j+=1
   
root.mainloop()
   
   
