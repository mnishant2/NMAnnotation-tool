
# coding: utf-8

# In[1]:


import numpy as np
import os,sys
import cv2
import json


# In[2]:

try:
    from Tkinter import *
    import tkFileDialog
    import tkMessageBox
except ImportError:
    from tkinter import *
    from tkinter import filedialog
    from tkinter import messagebox
    tkFileDialog=filedialog
    tkMessageBox=messagebox

# In[7]:


# def select_directory():
#     global path
#     path=tkFileDialog.askdirectory()
#     #root.destroy()
#     return path


# In[3]:


# def select_directory():
#     global path
#     path=tkFileDialog.askdirectory()
#     root.destroy()


# In[11]:


# def butt():
#     root = Tk()
#     btn = Button(root, text="Select a directory", command=select_directory)
#     btn.pack(side="bottom", fill="both", expand="yes", padx="10", pady="10")
#     root.mainloop()
#     print path
#     imgannotate(path)
# namelist=[]
fla=True
root = Tk()
root.geometry('200x200')
root.grid_rowconfigure(0, weight = 1)
root.grid_columnconfigure(0, weight = 1)

xl=0
yl=0
dirs = []
def get_directories():
    dirs.append(tkFileDialog.askdirectory())
    return dirs
b1 = Button(root, text='select directories...', command = get_directories)
b1.pack(side="bottom", fill="both", expand="yes", padx="10", pady="10")
root.mainloop()
# def welcome():
# #     top = Toplevel()
# #     top.title('Welcome')
# #     Message(top, text='WELCOME_MSG', padx=20, pady=20).pack()
# #     top.after(2000, top.destroy)
#     tkMessageBox.showwarning('dkd','dedee')
#     root.destroy()
if not dirs:
    sys.exit()
class CoordinateStore:
    def __init__(self):
        self.points = []

    def select_point(self,event,x,y,flags,param):
            if event == cv2.EVENT_LBUTTONDOWN:
                #print 'oolala'
                cv2.circle(img,(x,y),15,(0,255,0),-1)
                self.points.append((x,y))
#                 if self.points:
#                     xl,yl=self.points[-1]
#                 else:
#                     xl,yl=(0,0)
#                 cv2.namedWindow('imag1',cv2.WINDOW_NORMAL)   
#                 cv2.resizeWindow('imag1', 600,600)
#                 cv2.moveWindow('imag1',700,0)
                
                
#                 if len(self.points)==4:
#                     cv2.rectangle(img,self.points[0],self.points[2],(255,0,0),3)
#                 while 1:
#                 cv2.imshow('imag1',img)
#                 print 'pehla'


for path in dirs:
    namelist=[]
    
    for index,i in enumerate(os.listdir(path),start=1):
        #print os.path.basename(i)
        # print i
        

        coordinateStore1 = CoordinateStore()
        extension = os.path.splitext(os.path.join(path,i))[1]
        if extension=='.pdf'or extension=='.txt':
            continue
        img=cv2.imread(os.path.join(path,i))
        namelist.append(os.path.splitext(os.path.join(path,i))[0])
        #img=np.zeros((512,512,3), np.uint8)
        #print i
#         img=cv2.resize(img,(227,227))
        cv2.namedWindow('image',cv2.WINDOW_NORMAL)   
        cv2.resizeWindow('image', 600,600)
        cv2.startWindowThread()
        
        cv2.setMouseCallback('image',coordinateStore1.select_point)
        while 1:
#             if coordinateStore1.points:
#                 cv2.circle(img,(coordinateStore1.points[-1]),5,(0,255,0),-1)
            cv2.imshow('image',img)
            k = cv2.waitKey(20)
            
              
#         #print k
#                 if k == 32:
#                     return
                
        #print k
            if k == ord('e'):
                    try:
#                         print 'white'
            #fla=False
#                         xl,yl=coordinateStore1.points[-1]
                        cv2.circle(img,(coordinateStore1.points[-1]),15,(255,255,255),-1)
                        del(coordinateStore1.points[-1])
                    
                    except IndexError:
                        tkMessageBox.showwarning('cant delete','nopointsselected')
                        
                        root.mainloop()
                        
                        print('no points selected')
                        pass
            elif k == 32:
                # print 'good'
                break
            
#             print 'great'
            continue
# else:
#             
            
        if len(os.listdir(path))==index:
            with open(path+'/'+os.path.splitext(i)[0]+'.txt','w')as f:
                json.dump(coordinateStore1.points,f)
            break
        #cv2.circle(img,coordinateStore1.points[-1],5,(0,255,0),-1)
        k = cv2.waitKey(10000000)
        #print k
#         if k == ord('e'):
#             fla=False
#             del(coordinateStore1.points[-1])
        #l = cv2.waitKey(0)
        if k == 27:
            del namelist[-1]
            continue
        #m = cv2.waitKey(0)    
        elif k == ord('q'):
            del namelist[-1]
            break
        #n = cv2.waitKey(0)
        elif k == 32:
            with open(path+'/'+os.path.splitext(i)[0]+'.txt','w')as f:
                json.dump(coordinateStore1.points,f)
            continue
        #if fla==True:
            
    cv2.destroyAllWindows()
    with open(path+'/'+'namelist.txt','w') as f:
          json.dump(namelist,f)
    

#root = Tk()
#btn = Button(root, text="Select a directory", command=select_directory)
#btn.pack(side="bottom", fill="both", expand="yes", padx="10", pady="10")
#root.mainloop(0)
# print "Selected Coordinates: "
# for i in coordinateStore1.points:
#     print i 
# print namelist

# with open('/home/nishant/Desktop/namelist.txt','wb') as f:
#      json.dump([],f)

