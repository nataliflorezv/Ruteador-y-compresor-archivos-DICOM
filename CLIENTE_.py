# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 16:10:32 2021

@author: SAMSUNG
"""
import zipfile
import os
import requests
import sys
import pydicom as PDCM
import numpy as np
import pywt
import matplotlib.pyplot as plt
from PIL import Image
import wget

print("funcinaaaa")
#Compresion

def coeficientes(New_Img):
    """
    Retorna imagen comprimida
        
    Recibe imagen sin comprimir
    """ 

    coefs = pywt.dwt2(New_Img, 'haar')
    (Aprox, Detall) = coefs
    New_pixels = Aprox
    
    return New_pixels

def extraccion(img_DCM,file):
    """
    Retorna imagen dicom comprimida
    Almacena imagen comprimida en formato jpeg
        
    Recibe imagen DICOM y nombre de archivo
    """ 
    DCM_Img = PDCM.dcmread(img_DCM)

    rows = DCM_Img.get(0x00280010).value #Get number of rows from tag (0028, 0010)
    cols = DCM_Img.get(0x00280011).value #Get number of cols from tag (0028, 0011)
    
    try:
        Window_Center = int(DCM_Img.get(0x00281050).value) #Get window center from tag (0028, 1050)        
    except:
        Window_Center = int(DCM_Img.get(0x00281050).value[1]) #Get window center from tag (0028, 1050)
        
    try:
        Window_Width = int(DCM_Img.get(0x00281051).value) #Get window width from tag (0028, 1051)
    
    except:
        Window_Width = int(DCM_Img.get(0x00281051).value[1]) #Get window width from tag (0028, 1051)
        
    Window_Max = int(Window_Center + Window_Width / 2)
    Window_Min = int(Window_Center - Window_Width / 2)
    
    if (DCM_Img.get(0x00281052) is None):
        Rescale_Intercept = 0
    else:
        Rescale_Intercept = int(DCM_Img.get(0x00281052).value)

    if (DCM_Img.get(0x00281053) is None):
        Rescale_Slope = 1
    else:
        Rescale_Slope = int(DCM_Img.get(0x00281053).value)
    
    New_Img = np.zeros((rows, cols), np.uint8)
    Pixels = DCM_Img.pixel_array

    for i in range(0, rows):
        for j in range(0, cols):
            Pix_Val = Pixels[i][j]
            Rescale_Pix_Val = Pix_Val * Rescale_Slope + Rescale_Intercept
            if (Rescale_Pix_Val > Window_Max): #if intensity is greater than max window
                New_Img[i][j] = 255
            elif (Rescale_Pix_Val < Window_Min): #if intensity is less than min window
                New_Img[i][j] = 0
            else:
                New_Img[i][j] = int(((Rescale_Pix_Val - Window_Min) / (Window_Max - Window_Min)) * 255) #Normalize the intensities
    
    New_pixels = coeficientes(New_Img)
   
    
    plt.imshow(New_pixels, cmap='gray')
    plt.axis('off')
    plt.savefig(file,dpi=1200, bbox_inches='tight')
    plt.show()
    
    imag = Image.open(file)
    imag = imag.resize((7000,7000), Image.ANTIALIAS)
    
    return New_pixels


#Cliente

def descarga(docname):
    url = "http://192.168.0.100:8080/" + docname +'.zip'
    myfile = requests.get(url)
    open(os.getcwd()+'\\'+docname+'.zip', 'wb').write(myfile.content)
    wget.download(url,r"C:\\xampp\htdocs\\php-login-simple-master\\img1")

def descompresion(docname):
    documento_zip = zipfile.ZipFile(docname + '.zip')
    documento_zip.extract(docname) 
    documento_zip.close()
    
def app(docname):
    descarga(docname)
    descompresion(docname)
    extraccion(docname , docname +'.jpeg')

filename = 'image-000001.dcm'
app(filename)
    



#def saludo(arg):
  # app(arg[1])
     
#saludo(sys.argv)

