import os
import ctypes
import time
import random
from threading import *
import sys
import tkinter as tk
from tkinter import filedialog
from tkinter import *
import tkinter.font as font


sys.setrecursionlimit(1000)
mainDizin=""

class iplik:
    def __init__(self,target):
        self.target=target

    def run(self):
        thread=Thread(target=self.target)          #Tkinter ile oluşturduğum                                
        thread.daemon = True                         #arayüzün donmasını engellemek
        thread.start()                               # için thread işlemini kullanıyorum
        

def main(dizin,adet,saniye):
    for i in range(adet):
        dosyaBul(dizin,dizin)
        time.sleep(saniye)
    
def dosyaBul(dizin,mainDizin):
    try:
        dosya=dosyaSec(dizin)
        if dosyaTuru(dosya)==1:
            resim=os.getcwd()+"\\"+dosya
            walpaper(resim)
            return resim
        
        if dosyaTuru(dosya)==2:
            liste=os.listdir() 
            kontrol=[]
            for i in liste:
                i=i.split('.')
                if len(i)==1:
                    pass
                else:
                    kontrol.append(i[-1])
            if "jpg" in kontrol:
                return dosyaBul(dizin,mainDizin)
            else:
                return dosyaBul(mainDizin,mainDizin)
    except:
        return dosyaBul(dizin,mainDizin)
     
    if dosyaTuru(dosya)==3:
        return dosyaBul(os.getcwd()+"\\"+dosya,mainDizin)

def dosyaSec(dizin):
    bul=dizin
    os.chdir(bul)
    mainFolder=os.listdir()
    if mainFolder==[]:
        print("Empty")
        return dosyaSec(ustDizin())
            
        
    else:
        rnd=random.randint(0,len(mainFolder)-1)        
        subFolder=mainFolder[rnd] 
        return subFolder
    
def dosyaTuru(dosya):
    try:
        kontrol=dosya.split(".")
    except:
        pass
    else:
        if len(kontrol)==1:
            return 3
        else:
            if kontrol[-1]=="jpg" or "gif" or "png": 
                return 1
            else:
                return 2
        
def walpaper(dizin):
    ctypes.windll.user32.SystemParametersInfoW(20, 0, dizin, 3)

def ustDizin(): 
    while True:
        kontrol=os.listdir()
        if len(kontrol)==1 or len(kontrol)==0:
            os.chdir('..')
        else:
            break
    return os.getcwd()

def tkPencere(mainDizin):
    pencere = tk.Tk() # pointing root to Tk() to use it as Tk() in program.
    # pencere.attributes('-topmost', True) # Opened windows will be active. above all windows despite of selection.
    
    pencere.geometry("500x300")
    pencere.title("Wallpaper Değiştirme")
    
    myFont = font.Font(size=40)
    
    tk.Label(text="Repeat: ",font=myFont).grid(column=1,row=1)
    tk.Label(text="Second: ",font=myFont).grid(column=1,row=2)
    adet=tk.Entry(pencere,font=myFont,width=5)
    saniye=tk.Entry(pencere,font=myFont,width=5)
    adet.insert(index=10,string='10')
    saniye.insert(index=10,string='0.1')
    adet.grid(column=2,row=1)
    saniye.grid(column=2,row=2)
    class program():
        def __init__(self):
            self.mainDizin=mainDizin               
        def yol(self):
            self.mainDizin = filedialog.askdirectory() # Returns opened path as str
        def calistir(self):
            if(self.mainDizin!=""):
                ic_iplik=iplik(main(dizin=self.mainDizin,adet=int(adet.get()),saniye=float(saniye.get())))
                ic_iplik.run()        
                
            else:
                tk.messagebox.showerror("Error","Not select directory")
    a=program()
        
    button=tk.Button(pencere,text="Select directory",command=a.yol,font=myFont,fg="Red")
    button.grid(column=1,row=3)    
    button2=tk.Button(pencere,text="Start",command=a.calistir,font=myFont,fg="Red")
    button2.grid(column=2,row=3)
    
    pencere.mainloop()
    
dis_iplik=iplik(tkPencere(mainDizin))
dis_iplik.run()


