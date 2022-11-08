# Scanner


## Descripción

Con este escanner podrás realizar análisís rápidos de archivos, direcciones IPs, páginas web y extraer los metadatos de imágenes o PDFs, ya sea individualmente o por lotes.


## Instalación

```
https://github.com/vapemx/scanner.git
cd scanner
pip install -r requirements.txt
```

*Como prerequisito, es necesario tener una llave API de virus total para ciertas funcionalidades.

## Uso

Hay dos maneras de usar el scanner, de forma interactiva (diseñado para escaneo individual) o a través de parámetros (por lotes).

**El correcto funcionamiento de cada herramienta está sujeto a las entradas que se le otorguen y acceso a llaves API

### Interactivo

Para usar este modo tenemos que abrir nuestra consola y ejecutar el script.

`py scanner.py`

A continuación se desplegará un menú interactivo donde podemos elegir qué es lo que queremos utilizar.


### Parámetros

Si queremos escanear por lotes primero debemos de crear un archivo de texto (.txt) en donde se escriba
lo que se desea analizar. El programa detectará automáticamente qué es cada cosa.

Ejemplo

```
imagen1.png
imagen2.jpg
https://facebook.com
archivo1.pdf
archivo2.docx
192.211.146.103
```

Una vez que tengamos creado el archivo de entrada, procedemos a ejecutar el código. 
De manera opcional podemos agregar un archivo de salida.

`py scanner.py --file entrada.txt --output salida.txt`

*Esto tomará y arrojará los archivos tomando en cuenta el directorio raiz del script, en caso de querer lo contrario, escribir la ruta del (los archivos).


### Herramientas

- [Análisis de archivos en general](https://github.com/vapemx/scanner/wiki/Descripción-de-Funciones#análisis-de-archivos-en-general)
- [Análisis de imágenes](https://github.com/vapemx/scanner/wiki/Descripción-de-Funciones#análisis-de-imágenes)
- [Análisis de páginas web](https://github.com/vapemx/scanner/wiki/Descripción-de-Funciones#análisis-de-páginas-web)
- [Análisis de PDFs](https://github.com/vapemx/scanner/wiki/Descripción-de-Funciones#análisis-de-pdfs)
- [Análisis de IPs](https://github.com/vapemx/scanner/wiki/Descripción-de-Funciones#análisis-de-ips)