import re
import logging
import argparse
import sys
from getpass import getpass
from time import sleep
import nmapscan
import scan_links
import scan_pdf
import scan_files
import scan_img


def organizer(content, output):
    links = []
    for element in content:
        #El elemento es una imagen
        if re.search('.png', element) or re.search('.jpg', element) or re.search('.jpeg', element):
            scan_img.img_metadata(element, output)
            logging.info("img analyzed")

        #El elemento es un pdf
        elif re.search('.pdf', element):
            scan_pdf.metadata(element, output)
            logging.info("PDF analyzed")
        
        #Es un IP
        elif re.search(r'((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])', element):
            nmapscan.scan_ip(element, output)
        
        #Es una web
        elif re.search(r'(http\:\/\/|https\:\/\/)?([a-z0-9][a-z0-9\-]*\.)+[a-z0-9][a-z0-9\-]', element):
            #Es una web en formato correcto
            if re.search(r'(http\:\/\/|https\:\/\/)([a-z0-9][a-z0-9\-]*\.)+[a-z0-9][a-z0-9\-]', element):
                links.append(element)
            else:
                output.write("\nLink en formato inválido: " + element)
                logging.warning("link: " + element + " in bad format")
        
        #Cualquier otro archivo
        else:
            if key:
                fs = scan_files.file_vt(key, element, output)
            else:
                print("Ingrese su API key de virus total")
                key = getpass()
                fs = scan_files.file_vt(key, element, output)
            if fs:
                logging.info("Correct file analysis")
            else:
                logging.error("Error in file analysis")    
    
    #Si hay links para analizar
    if links:
        print("Ingrese su API key de virus total")
        key = getpass()
        ws = scan_links.scan_link(key, links)
        if ws:
            logging.info("Correct link analysis")
        else:
            logging.error("Error in link analysis")


def menu():
    print(''' 
     #####   #####     #    #     # #     # ####### ######  
    #     # #     #   # #   ##    # ##    # #       #     # 
    #       #        #   #  # #   # # #   # #       #     # 
     #####  #       #     # #  #  # #  #  # #####   ######  
          # #       ####### #   # # #   # # #       #   #   
    #     # #     # #     # #    ## #    ## #       #    #  
     #####   #####  #     # #     # #     # ####### #     # ''')
    
    print('''
    Seleccione una opción
    [1]Analizar link
    [2]Analizar IP
    [3]Analizar imagen
    [4]Analizar PDF
    [5]Analizar cualquier otro archivo
    [99]Salir''')

    try:
        op = int(input("\n--->  "))
        return op
    
    #En caso de que el usuario ingrese una letra
    except ValueError:
        print("Opción inválida")
        return True


if __name__ == "__main__":
    #Creacion de archivo de logs
    logging.basicConfig(filename = 'registry.log', level = logging.INFO)

    parser = argparse.ArgumentParser(description='En un documento de texto escriba los archivos, links o IPs a analizar,\
                                                en caso contrario, utlice el menú de interacción')
    
    parser.add_argument('--file', '-f', dest='file_txt', type=argparse.FileType('r'), help='Archivo de contenido a escanear')
    parser.add_argument('--output', '-o', dest='output', type=argparse.FileType('w'), help='Arcvhivo de salida', default=sys.stdout)
    args = parser.parse_args()

    #En caso de que el usuario ingrese un parámetro, se ejecuta directo la función
    if args.file_txt:
        logging.info('User txt file parameter.')
        content = args.file_txt.read().split()
        organizer(content, args.output)
    
    #En el caso contrario, se le da a escoger entre las funciones
    else:
        op = True
        while op:
            op = menu()
            if op == True:
                logging.warning('User wrote a letter intead a number.')
                
            elif op == 99:
                print("Saliendo...")
                sleep(1)
                print("Adiós!")
                logging.info('Good bye!')
                op = False

            elif op in range(1,6):
                #Link
                if op == 1:
                    links = []
                    logging.info('User menu choice [1]')
                    while True:
                        link = input("Ingrese el link a analizar con formato http[s] o [q] para salir")
                        if re.search(r'(http\:\/\/|https\:\/\/)([a-z0-9][a-z0-9\-]*\.)+[a-z0-9][a-z0-9\-]', link):
                            links.append(link)
                            break
                        else:
                            print("Formato incorrecto")
                            
                    print("Ingrese su API key de virus total")
                    key = getpass()
                    ws = scan_links.scan_link(key, links)
                    if ws:
                        logging.info("Correct link analysis")
                    else:
                        logging.error("Error in link analysis")
                    
                #IP
                elif op == 2:
                    logging.info('User menu choice [2]')
                    ip = input("Ingrese la IP a analiazr: ")
                    nmapscan.scan_ip(ip, args.output)
                
                #Imagen
                elif op == 3:
                    logging.info('User menu choice [3]')
                    img = input("Ingrese la imagen a analizar o [q] para salir")
                    
                    while True:
                        if re.search('.png', img) or re.search('.jpg', img) or re.search('.jpeg', img):
                            scan_img.img_metadata(img, args.output)
                            logging.info("img analyzed")
                        
                        elif img == "q":
                            logging.info("User exit.")
                            break

                        else:
                            print("El archivo no es una imagen válida")
                
                #PDF
                elif op == 4:
                    logging.info('User menu choice [4]')
                    while True:
                        pdf = input("Ingrese el archivo pdf a analizar o [q] para salir")
                        if re.search('.pdf', pdf):
                            try:
                                scan_pdf.metadata(pdf, args.output)
                                logging.info("PDF analyzed")
                            except:
                                print("PDF no encontrado.")
                                logging.error("PDF not found.")
                        
                        elif pdf == "q":
                            logging.info("User exit.")
                            break
                        else:
                            print("El archivo no es un PDF.")
                
                #Archivo
                elif op == 5:
                    logging.info('User menu choice [5]')
                    file = input("Ingrese el nombre del archivo a analizar: ")
                    print("Ingrese su API key de virus total")
                    key = getpass()
                    fs = scan_files.file_vt(key, file, args.output)
                    if fs:
                        logging.info("Correct file analysis")
                    else:
                        print("Error al analizar el archivo.")
                        logging.error("Error in file analysis")   
            
            else:
                print("Opción inválida.")