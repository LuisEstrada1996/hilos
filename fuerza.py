import zipfile
import os
from multiprocessing import Process
import multiprocessing

lista = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9']

def funcion_pass(ini,proc,fin):
    
    clave = ""
    i=ini
    bandera = True
    archivo=zipfile.ZipFile("/Users/luisestrada/Desktop/comprimido.zip")
    for i in range(ini, fin):
            clave = lista[i]
            print('proceso',proc,'-',clave)
            try:
                archivo.extractall(pwd=clave.encode())
                print('proceso',proc,'-',clave)
                print("Password correcto!*****************************************")
                bandera = False
                exit()
            except:
                #print("Paswsword incorrecto")
                pass
    if(bandera): 
        for i in range(ini, fin):
            for j in range(0, len(lista)):
                clave = lista[i]+lista[j]
                print('proceso',proc,'-',clave)
                try:
                    archivo.extractall(pwd=clave.encode())
                    
                    print("Password correcto!*****************************************")
                    bandera = False
                    exit()
                except:
                    #print("Paswsword incorrecto")
                    pass
    if(bandera):             
        for i in range(ini, fin):
            for j in range(0, len(lista)):
                for k in range(0, len(lista)):
                    clave = lista[i]+lista[j]+lista[k]
                    print(clave)
                    try:
                        archivo.extractall(pwd=clave.encode())
                        print('proceso',proc,'-',clave)
                        print("Password correcto!*****************************************")
                        bandera = False
                        exit()
                    except:
                        #print("Paswsword incorrecto")
                        pass
    if(bandera):
        for i in range(ini, fin):
            for j in range(0, len(lista)):
                for k in range(0, len(lista)):
                    for l in range(0, len(lista)):
                        clave = lista[i]+lista[j]+lista[k]+lista[l]
                        
                        try:
                            archivo.extractall(pwd=clave.encode())
                            print('proceso',proc,'-',clave)
                            print("Password correcto!**************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************")
                            exit()
                        except:
                            #print("Paswsword incorrecto")
                            pass

        

if __name__ == '__main__':
    nucleos = multiprocessing.cpu_count()
    procesos = []
    for i in range(nucleos-6):
        procesos.append('')
        procesos[i] = Process(target=funcion_pass,args=(nucleos*i,i,nucleos*(i+1)))
        procesos[i].start()
    

        

    

