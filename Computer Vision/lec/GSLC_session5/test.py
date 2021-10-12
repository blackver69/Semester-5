from os import name
import cv2
import matplotlib.pyplot as plt

from tkinter import *

import tkinter as tk

from PIL import ImageTk, Image
from functools import partial




class Root:
    def __init__(self,master):
        self.master=master
        master.title('Citra')

        master.geometry("500x400")
        master.configure(background="white")
  
        
        

        self.ABC=Frame(master,bg="powder blue",bd=20,relief=RIDGE)
        self.ABC.grid()
        self.ABC1=Frame(self.ABC,bg="Cadet blue",bd=10,relief=RIDGE)
        self.ABC1.grid(row=1,column=0,sticky=W)
        self.pencocokan("image/image0.jpg")

        


    def open_choose(self):
        
        choose_image= Toplevel(self.master)
        choose_image.geometry("700x750")
        choose_image.title("Database Citra")
        self.citra=Frame(choose_image,bg="powder blue",bd=20,relief=RIDGE)
        self.citra.grid()
        self.citra_image=Frame(self.citra,bg="Cadet blue",bd=10,relief=RIDGE)    
        self.citra_image.grid(row=1,column=0,sticky=W)
        pad=StringVar()

        btn=[]
        i=0
        num_image=0
       
        for j in range(1,7,2):
            for k in range(0,3):
                num_image+=1
                num_image_str=str(num_image)
                name_image="choose/image"+num_image_str+".jpg"
                img1 = Image.open(name_image)
                img1=img1.resize((100,100))
                photo = ImageTk.PhotoImage(img1)
                
                label = Label(self.citra_image, image = photo)
                label.image = photo
                label.grid(row=j,column=k,pady=8,padx=8)
                
                
                btn.append(Button(self.citra_image ,width=10,height=2,font=('arial',22,'bold'),bd=4,text="choose",command=partial(self.pencocokan,name_image)))
                btn[i].grid(row=j+1,column=k,pady=8,padx=8)
                i+=1

    def open_citra(self,image):
        
        Db= Toplevel(self.master)
        Db.geometry("450x450")
        Db.title("Database Citra")
        self.citra=Frame(Db,bg="powder blue",bd=20,relief=RIDGE)
        self.citra.grid()
        self.citra_image=Frame(self.citra,bg="Cadet blue",bd=10,relief=RIDGE)    
        self.citra_image.grid(row=1,column=0,sticky=W)
        pad=StringVar()

        
        num_image=0
        for j in range(1,7,2):
            for k in range(0,3):
                num_image+=1
                num_image_str=str(num_image)
                name_image="image/image"+num_image_str+".jpg"
                img1 = Image.open(name_image)
                img1=img1.resize((100,100))
                photo = ImageTk.PhotoImage(img1)
                
                label = Label(self.citra_image, image = photo)
                label.image = photo
                label.grid(row=j,column=k,pady=8,padx=8)
                
                
                



    def pencocokan(self,image,image1="image/image0.jpg",percent=0):
        
        img1 = Image.open(image)
        img1=img1.resize((100,100))
        photo = ImageTk.PhotoImage(img1)
        
        label = Label(self.ABC1, image = photo)
        label.image = photo
        label.grid(row=1,column=1,pady=8,padx=8)

        img2 = Image.open(image1)
        img2=img2.resize((100,100))
        photo1 = ImageTk.PhotoImage(img2)

        label = Label(self.ABC1, image = photo1)
        label.image = photo1
        label.grid(row=1,column=2,pady=8,padx=8)
        if(percent!=0):
    
            information=Label(self.ABC1,text="persentase kemiripan= {0:.2f}%".format(percent))
            information.grid(row=2,column=2,pady=8,padx=8)
        button_choose=Button(self.ABC1,width=10,height=2,font=('arial',22,'bold'),bd=4,text="Lihat pilihan",command=self.open_choose).grid(row=3,column=1,pady=8,padx=8)
        button_process=Button(self.ABC1,width=10,height=2,font=('arial',22,'bold'),bd=4,text="pencocokan",command=partial(self.image_processing,image)).grid(row=3,column=2,pady=8,padx=8)
        button_citra=Button(self.ABC1,width=10,height=2,font=('arial',22,'bold'),bd=4,text="Lihat Citra",command=partial(self.open_citra,image)).grid(row=4,column=1,pady=8,padx=8)
        
        # self.label=tk.Label(self,text="")
        # self.label.grid(row=2,column=2,pady=8,padx=8)

        
    def image_processing(self,image1):
        check=0
        if(image1==""):
            self.pencocokan(image1,"image/notfound.jpg")
        num_image=0
        scale_percent=70

        

        
        path=""
        img1=cv2.imread(image1)
        width=int(img1.shape[1]*scale_percent/100)
        height=int(img1.shape[0]*scale_percent/100)
        dim=(width,height)
        img1=cv2.resize(img1,dim,interpolation=cv2.INTER_AREA)
        img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
        img1=cv2.equalizeHist(img1)
        for i in range(0,9):
            num_img2=""
            name_img2=""
            if(i==0):
                name_img2=image1
            else:

                num_img2=str(i)
                name_img2="image/image" +num_img2+".jpg"
            
            img2=cv2.imread(name_img2)
            width=int(img2.shape[1]*scale_percent/100)
            height=int(img2.shape[0]*scale_percent/100)
            dim=(width,height)
            img2=cv2.resize(img2,dim,interpolation=cv2.INTER_AREA)
            img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
            img2=cv2.equalizeHist(img2)

            #sift
            sift = cv2.xfeatures2d.SIFT_create()

            keypoints_1, descriptors_1 = sift.detectAndCompute(img1,None)
            keypoints_2, descriptors_2 = sift.detectAndCompute(img2,None)

            #feature matching
            bf = cv2.BFMatcher(cv2.NORM_L1, crossCheck=True)

            matches = bf.match(descriptors_1,descriptors_2)
            matches = sorted(matches, key = lambda x:x.distance)
            
            if(i==0):
                check=len(matches)
            elif(len(matches)>num_image):
                path=name_img2
                num_image=len(matches)
                
        if(num_image==0):
            self.pencocokan(image1,"image/notfound.jpg")
        else:
            
            self.pencocokan(image1,path,(min(num_image,check)/max(num_image,check)*100))
    
    
    # my_button=Button(self)
    # my_button.pack(pady=20)
root=Tk()
start=Root(root)
root.mainloop()