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
xypFirst=[]
xypSecond=[]
position=1
x=0
y=0
switch="ready"
stateDone="ready"
while position<len(data):
   
   try:
      #Getting Data
      x=float(data[position])
      position+=1
      
      
      
      
      
   except:
      stringValue=(data[position])
      print stringValue
      position+=1
      if stringValue=="END_FILE":
         break
      #turns on the switch so that we know if we should start a new polly
      elif stringValue=="END_ONE_POLY":
         switch="on"
      #turns stateDone to true so we can move onto next state
      elif stringValue=="END_ALL_POLY":
         stateDone="True"
      #sets stateDone to false when we are not end all poly
      elif stringValue != "END_ALL_POLY":
         stateDone="false"
      #turns off the switch so that we know if we should not start a new polly
      elif stringValue !="END_One_POLY":
         stateDone="false"
         
         
   
   
   try:
      #Getting Data
      y=float(data[position])
      position+=1
      
      
      

      xy.append((x,y))
      
      
            
      
   
   except:
      stringValue=(data[position])
      print stringValue
      position+=1
      if stringValue=="END_FILE":
         break
      #turns on the switch so that we know if we should start a new polly
      elif stringValue=="END_ONE_POLY":
         switch="on"
      #turns stateDone to true so we can move onto next state
      elif stringValue=="END_ALL_POLY":
         stateDone="True"
      #sets stateDone to false when we are not end all poly
      elif stringValue !="END_ALL_POLY":
         stateDone="false"
      #turns off the switch so that we know if we should not start a new polly
      elif stringValue !="END_One_POLY":
         stateDone="false"
         
         
   
   
print xy
   
