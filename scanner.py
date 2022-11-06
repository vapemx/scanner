import re
import logging
import argparse
from time import sleep


def organizer(content):
    pass


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
    [3]Analizar IP
    [4]Analizar imagen
    [5]Analizar PDF
    [6]Analizar cualquier otro archivo
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
                if op == 1:
                    logging.info('User menu choice [1]')
                elif op == 2:
                    logging.info('User menu choice [2]')
                elif op == 3:
                    logging.info('User menu choice [3]')
                elif op == 4:
                    logging.info('User menu choice [4]')
                elif op == 5:
                    logging.info('User menu choice [5]')
                elif op == 6:
                    logging.info('User menu choice [6]')