
import cv2


#import library tkinter untuk gui
from tkinter import *
import tkinter as tk

#import library yang berguna dalam proses akses foto, manipulasi foto dan display foto
import matplotlib.pyplot as plt
from PIL import ImageTk, Image

#import partial agar dapat melakukan aksi pada button
from functools import partial
import glob

class Root:
    def __init__(self,master):
        #windows dasar
        self.master=master
        master.title('Citra')

        master.geometry("500x400")
        master.configure(background="white")
        # self.database=self.load_image("image/")
        # self.choose=self
        
        
        #grid baru
        self.ABC=Frame(master,bg="powder blue",bd=20,relief=RIDGE)
        self.ABC.grid()
        self.ABC1=Frame(self.ABC,bg="Cadet blue",bd=10,relief=RIDGE)
        self.ABC1.grid(row=1,column=0,sticky=W)
        self.pencocokan("image/image0.jpg")

    
    def load_image(str):
        data=[]
        for f in glob.iglob((str+"\*")):
            image=cv2.imread(f)
            data.append(image)
        return data


    def open_choose(self):
        #grid open_choose
        choose_image= Toplevel(self.master)
        choose_image.geometry("700x750")
        choose_image.title("Database pilihan")
        self.citra=Frame(choose_image,bg="powder blue",bd=20,relief=RIDGE)
        self.citra.grid()
        self.citra_image=Frame(self.citra,bg="Cadet blue",bd=10,relief=RIDGE)    
        self.citra_image.grid(row=1,column=0,sticky=W)
        pad=StringVar()

        btn=[]
        i=0
        num_image=0
       
       #load semua gambar di image
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
        #grid citra
        Db= Toplevel(self.master)
        Db.geometry("450x450")
        Db.title("Database Citra")
        self.citra=Frame(Db,bg="powder blue",bd=20,relief=RIDGE)
        self.citra.grid()
        self.citra_image=Frame(self.citra,bg="Cadet blue",bd=10,relief=RIDGE)    
        self.citra_image.grid(row=1,column=0,sticky=W)
        pad=StringVar()

        
        num_image=0
        #load gambar dan memambahkan button untuk pemilihan
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
                
                
                



    def pencocokan(self,image,image1="image/image0.jpg",percent=float(0)):
        
        #buka gambar dan resize
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
        print(percent)
        if(percent!=0):
            #kondisi bila mirip dan hasil yang didapatkan
            information=Label(self.ABC1,text="persentase kemiripan= {0:.2f}%".format(percent))
            information.grid(row=2,column=2,pady=8,padx=8)
        #button
        button_choose=Button(self.ABC1,width=10,height=2,font=('arial',22,'bold'),bd=4,text="Lihat pilihan",command=self.open_choose).grid(row=3,column=1,pady=8,padx=8)
        button_process=Button(self.ABC1,width=10,height=2,font=('arial',22,'bold'),bd=4,text="pencocokan",command=partial(self.image_processing,image)).grid(row=3,column=2,pady=8,padx=8)
        button_citra=Button(self.ABC1,width=10,height=2,font=('arial',22,'bold'),bd=4,text="Lihat Citra",command=partial(self.open_citra,image)).grid(row=4,column=1,pady=8,padx=8)
        #grid digunakan untuk menentukan posisi dari button yang telah di create
        # self.label=tk.Label(self,text="")
        # self.label.grid(row=2,column=2,pady=8,padx=8)

        
    def image_processing(self,image1):

        if(image1==""):
            #kalau gambar kosong
            self.pencocokan(image1,"image/notfound.jpg")
        num_image=0
  

        
        path=""
        #baca gambar
        img1=cv2.imread(image1)
        #convert menjadi abu-abu
        img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
        
        num_img2=float(0)
        #mencocokan semua gambar yang telah dimasukkan ke database
        for i in range(1,10):
            
            
            name_img2=""
          

            num_img2=str(i)
            name_img2="image/image" +num_img2+".jpg"
            
            img2=cv2.imread(name_img2)

            img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)


            #sift
           
            #membuat metode dari sift
            sift=cv2.xfeatures2d.SIFT_create(400)

            #mendapatkan key point dan descriptors
            kp_1, desc_1= sift.detectAndCompute(img1,None)
            kp_2, desc_2= sift.detectAndCompute(img2,None)

            # print("kp1 : {}\n".format(len(kp_1)))
            # print("kp2 : {}\n".format(len(kp_2)))

            #penentuan parameter dan pencarian parameter
            index_params=dict(algorithm=0,trees=5)
            search_param=dict(check=100)
            #menambahkan fitur knn agar data dapat dilihat lebih baik dan pencocokan
            flann=cv2.FlannBasedMatcher(index_params,search_param)
            matches=flann.knnMatch(desc_1,desc_2,k=2)
            good_point=[]

            #mengecek point dari jarak bila sesuai dengan kondisi yang diminta ia akan dimasukkan ke point kemiripan
            for m,n in matches:
                if(m.distance<0.6*n.distance):
                    good_point.append(m)

            num_keypoints=0

            if(len(kp_1)<=len(kp_2)):
                num_keypoints=len(kp_1)
            else:
                num_keypoints=len(kp_2)

            # print("good matches :{}".format(good_point))
            #mendapatkan persentasi kemiripan
            print("Percentase :{}".format(len(good_point)/num_keypoints*100))
            similar=(len(good_point)/num_keypoints*100)
            #bila kemiripan lebih besar ia akan menyimpan path dan key point
            if(similar>num_image):
                path=name_img2
                num_image=similar
        #bila semua kemiripan 0 persen jadi tidak ada foto yang mirip
        if(num_image==0):
            self.pencocokan(image1,"image/notfound.jpg")
        else:
    
            self.pencocokan(image1,path,num_image)
    
    
    # my_button=Button(self)
    # my_button.pack(pady=20)
root=Tk()
start=Root(root)
root.mainloop()