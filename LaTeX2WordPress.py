# Paquetes necesarios
import os
import re
import requests
import json
import sys
from dotenv import load_dotenv

## Función para convertir un archivo LaTeX a HTML usando Pandoc
def LaTeX2HTML(archivo):
    """
    Convierte un archivo LaTeX en HTML utilizando Pandoc.
    Realiza reemplazos en el texto para ajustar el formato al estándar HTML esperado.
    
    Args:
        archivo (str): Ruta del archivo LaTeX a convertir.
    
    Returns:
        str: Tema extraído del archivo LaTeX.
    """
    print(f"Convirtiendo archivo {archivo} a HTML.")
    
    # Leer el contenido del archivo LaTeX
    with open(archivo, "r", encoding='utf8') as f:
        texto = f.read()

    # Extraer el tema del archivo
    patron = r'\\tema\{(.*)\}'
    tema = re.search(patron, texto).group(1)

    # Realizar los reemplazos necesarios en el contenido
    texto = texto.replace('{preguntas}', '{enumerate}')
    texto = texto.replace('begin{respuesta}', 'begin{proof}[Solución]')
    texto = texto.replace('end{respuesta}', 'end{proof}')
    texto = texto.replace(r'\ref', r'\\ref')
    texto = texto.replace(r'\tema', r'\title')
    texto = texto.replace(r'\autor', r'\author')
    texto = texto.replace(r'\fecha', r'\date')

    # Guardar el archivo modificado temporalmente
    archivo_temp = archivo.replace(".tex", "_temp.tex")
    with open(archivo_temp, "w", encoding='utf8') as f:
        f.write(texto)

    # Convertir el archivo temporal a HTML usando Pandoc
    archivo_html = archivo.replace(".tex", ".html")
    os.system(f"pandoc {archivo_temp} -s --mathjax -o {archivo_html}")

    # Leer el archivo HTML generado
    with open(archivo_html, "r", encoding='utf8') as f:
        texto = f.read()

    # Realizar ajustes finales al contenido HTML
    texto = texto.replace('<em>Proof.</em>', '<strong>Demostración.</strong>')
    texto = texto.replace('<em>Solución.</em>', '<strong>Solución.</strong>')
    texto = texto.replace('\n<div class="proof">', '<br>\n<div class="proof">')
    texto = texto.replace('<div class="ejer">\n<p>', '<div class="ejer"><p><strong>Ejercicio. </strong>')
    texto = texto.replace(r'\sen', r'\sin')
    texto = texto.replace(r'\setlength{\arraycolsep}{2pt}', r'')
    texto = texto.replace('~◻', '').replace(' ◻', '')

    # Extraer el contenido dentro de la etiqueta <body>
    patron = r'<body>(.*)</body>'
    texto = re.search(patron, texto, re.DOTALL).group(1)

    # Quitar el header HTML no deseado
    patron = r'\n<header[^>]*>.*?</header>'
    texto = re.sub(patron, '', texto, flags=re.DOTALL)

    # Formatear el contenido para mayor legibilidad
    texto = texto.replace('<span class="math display">', '\n<span class="math display">\n')
    texto = texto.replace('<li>', '\t<li>')
    texto = texto.replace('<tr ', '\t<tr ')
    texto = texto.replace('<div class="proof">\n<p>', '<div class="proof">\n\t<p>')

    # Sobreescribir el archivo HTML con los cambios realizados
    with open(archivo_html, "w", encoding='utf8') as f:
        f.write(texto)

    # Eliminar el archivo temporal
    # os.remove(archivo_temp)

    # Devolver el tema extraído
    return tema

## Función para publicar contenido en WordPress
def postWordPress(html, tema, portada):
    """
    Publica un contenido en WordPress utilizando la API REST.
    Primero sube una imagen de portada, luego crea un post con contenido HTML y una imagen destacada.
    
    Args:
        html (str): Ruta del archivo HTML con el contenido.
        tema (str): Título de la publicación.
        portada (str): Ruta de la imagen de portada.
    """
    # Configuración de la API
    load_dotenv()
    api_url = os.getenv("WP_URL")
    print("Publicando en:", api_url.replace("wp-json/wp/v2/posts", ""))
    api_url_media = api_url.replace("posts", "media")
    usuario = os.getenv("WP_USUARIO")
    contraseña = os.getenv("WP_CONTRASENIA")
    auth = (usuario, contraseña)

    # Subir la imagen de portada
    headers = {
        "Content-Disposition": "attachment; filename=Portada.jpeg",
        "Content-Type": "image/jpeg",
    }
    with open(portada, "rb") as img:
        response = requests.post(api_url_media, headers=headers, auth=auth, data=img)

    # Verificar si la imagen fue subida exitosamente
    if response.status_code == 201:  # Código 201 = Creado
        media_id = response.json()["id"]
        print(f"Imagen subida exitosamente. ID: {media_id}")
    else:
        print("Error al subir la imagen:", response.text)
        return

    # Leer el contenido HTML
    with open(html, "r", encoding='utf8') as f:
        texto = f.read()

    # Preparar los datos de la publicación
    headers = {"Content-Type": "application/json"}
    data = {
        "title": tema,
        "content": texto,
        "status": "draft",  # Opciones: 'publish', 'draft', etc.
        "categories": [4],  # IDs de las categorías
        "tags": [1],  # IDs de las etiquetas
        "featured_media": media_id,  # ID de la imagen destacada
    }

    # Enviar la solicitud POST para crear la publicación
    response = requests.post(api_url, headers=headers, auth=auth, data=json.dumps(data))

    # Verificar si la publicación fue creada exitosamente
    if response.status_code == 201:  # Código 201 indica éxito
        print("Publicación creada con éxito.")
    else:
        print("Error al crear la publicación:", response.status_code, response.text)

# Punto de entrada del script
if __name__ == "__main__":
    # Leer argumentos de la línea de comandos
    archivo = sys.argv[1]
    portada = sys.argv[2]

    # Convertir LaTeX a HTML y publicar en WordPress
    tema = LaTeX2HTML(archivo)
    postWordPress(archivo.replace(".tex", ".html"), tema, portada)
