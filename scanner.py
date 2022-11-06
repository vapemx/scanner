import re
import logging
import argparse
from getpass import getpass
from time import sleep
import nmapscan
import vt_links


def organizer(content):
    links = []
    for element in content:
        #El elemento es una imagen
        if re.search('.png', element) or re.search('.jpg', element) or re.search('.jpeg', element) or re.search('.raw', content):
            pass
        #El elemento es un pdf
        elif re.search('.pdf', element):
            pass
        #Es un IP
        elif re.search(r'((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])', element):
            nmapscan.scan_ip(element) #TODO: Return in fn, make cool output
        #Es una web
        elif re.search(r'(http\:\/\/|https\:\/\/)?([a-z0-9][a-z0-9\-]*\.)+[a-z0-9][a-z0-9\-]', element):
            #Es una web en formato correcto
            if re.search(r'(http\:\/\/|https\:\/\/)([a-z0-9][a-z0-9\-]*\.)+[a-z0-9][a-z0-9\-]', element):
                links.append(element)
            else:
                logging.warning("link: " + element + " in bad format")
        #Cualquier otro archivo
        else:
            pass
    
    #Si hay links para analizar
    if links:
        print("Ingrese su API key de virus total")
        key = getpass()
        ws = vt_links.scan_link(key, links)
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
    except ValueError as e:
        print("Opción inválida")
        return True


if __name__ == "__main__":
    #Creacion de archivo de logs
    logging.basicConfig(filename = 'registry.log', level = logging.INFO)

    parser = argparse.ArgumentParser(description='En un documento de texto escriba los archivos, links o IPs a analizar,\
                                                en caso contrario, utlice el menú de interacción')
    
    parser.add_argument('--file', '-f', dest='file_txt', type=argparse.FileType('r'), help='Archivo de contenido a escanear')
    args = parser.parse_args()

    #En caso de que el usuario ingrese un parámetro, se ejecuta directo la función
    if args.file_txt:
        logging.info('User txt file parameter.')
        content = args.file_txt.read().split()
        organizer(content)
    
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
            else:
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
                    ws = vt_links.scan_link(key, links)
                    if ws:
                        logging.info("Correct link analysis")
                    else:
                        logging.error("Error in link analysis")
                    
                #IP
                elif op == 2:
                    logging.info('User menu choice [2]')
                #Imagen
                elif op == 3:
                    logging.info('User menu choice [3]')
                #PDF
                elif op == 4:
                    logging.info('User menu choice [4]')
                #Archivo
                elif op == 5:
                    logging.info('User menu choice [5]')