# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 13:48:17 2021

@author: SAMSUNG
"""

import http.server             
import socketserver
import zipfile
import os
import shutil
import sys



       
def carga(direccion):
    dire = os.getcwd()
    shutil.copy(direccion,dire)

    
def comprimido(filename):
    jungle_zip = zipfile.ZipFile(filename+'.zip', 'w')
    jungle_zip.write (filename , compress_type = zipfile.ZIP_DEFLATED)
    jungle_zip.close()
   
def conexion():
    PORT = 8020                               
    Handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("Servidor en el puerto 8000")
        httpd.serve_forever()

def lista(filename):
    lista = open ('lista.txt','a')
    lista.write(filename+ '\n') 
        
def app(direccion,filename):
    carga(direccion)
    comprimido(filename)
    lista(filename)
    conexion()


'''
def saludo(arg):
    direccion = r"C:\\xampp\htdocs\\php-login-simple-master\\img"
    direccion=direccion+r"\\" + arg[1] 
    app(direccion,arg[1])
saludo(sys.argv)

'''


direccion=r"C:\\xampp\htdocs\\php-login-simple-master\\img\\image-000001.dcm"
filename = 'image-000001.dcm'
app(direccion, filename)
    




