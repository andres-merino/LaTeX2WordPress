<!-- Encabezado -->
[![Colaboradores][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Estrellas][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

<!-- Título -->
<br />
<div align="center">

<h1 align="center">LaTeX2WordPress</h1>
  <p align="center">
    Automatiza la conversión y publicación de documentos LaTeX como entradas de blog en WordPress.
    <br />
    <a href="https://github.com/andres-merino/LaTeX2WordPress/issues">Reportar un Problema</a>
    <br />
  </p>
</div>

<!-- Cuerpo -->
## Sobre el Proyecto

**LaTeX2WordPress** es una herramienta diseñada para simplificar la publicación de documentos LaTeX como entradas en blogs de WordPress de manera automática. Con este proyecto, se busca automatizar el proceso de conversión y publicación, facilitando el trabajo de quienes utilizan estas plataformas.

### Construido con

![Python Badge](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff&style=for-the-badge) 
![LaTeX Badge](https://img.shields.io/badge/LaTeX-008080?logo=latex&logoColor=fff&style=for-the-badge)
![WordPress Badge](https://img.shields.io/badge/WordPress-21759B?logo=wordpress&logoColor=fff&style=for-the-badge)

## Descripción

Existen dos maneras de utilizar **LaTeX2WordPress**:

Por línea de comandos usando el script `LaTeX2WordPress.py`: 
```bash
python LaTeX2WordPress.py <archivo.tex> <portada.jpeg>
```
Donde `<archivo.tex>` es el documento LaTeX que se desea convertir y `<portada.jpeg>` es la imagen de portada que se desea utilizar en la entrada de WordPress. Si se utilizan paquetes adicionales en el documento LaTeX, se deben colocar en la misma carpeta del script (como el paquete aleph-comandos.sty que se usa en el ejemplo).

Por el archivo `LaTeX2WordPress.ipynb` en Jupyter Notebook: en este se tienen las siguientes funciones:
  - `LaTeX2HTML`: convierte el documento LaTeX a HTML y devuelve el tema encontrado en `title`.
  - `postWordPress`: publica el documento HTML en WordPress, tiene como argumentos el archivo HTML,el título del post y el nombre del archivo de la imagen de portada.

En ambos casos, se debe tener un archivo `.env` con las siguientes variables de entorno:
```bash
WP_URL = 'https://tu.dominio/wp-json/wp/v2/posts'
WP_USUARIO = "usuario"
WP_CONTRASENIA = "***"
```


## Créditos

**Andrés Merino** (aemerinot@gmail.com)

- Docente-Investigador en Pontificia Universidad Católica del Ecuador  
- Fundador del [Proyecto Alephsub0](https://www.alephsub0.org/about/)

[![LinkedIn][linkedin-shield]][linkedin-url-aemt]

## Licencia

Distribuido bajo la licencia MIT.

[![MIT License][license-shield]][license-url]

<!-- MARKDOWN LINKS & IMAGES -->
[contributors-shield]: https://img.shields.io/github/contributors/andres-merino/LaTeX2WordPress.svg?style=for-the-badge
[contributors-url]: https://github.com/andres-merino/LaTeX2WordPress/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/andres-merino/LaTeX2WordPress.svg?style=for-the-badge
[forks-url]: https://github.com/andres-merino/LaTeX2WordPress/forks
[stars-shield]: https://img.shields.io/github/stars/andres-merino/LaTeX2WordPress?style=for-the-badge
[stars-url]: https://github.com/andres-merino/LaTeX2WordPress/stargazers
[issues-shield]: https://img.shields.io/github/issues/andres-merino/LaTeX2WordPress.svg?style=for-the-badge
[issues-url]: https://github.com/andres-merino/LaTeX2WordPress/issues
[license-shield]: https://img.shields.io/github/license/andres-merino/LaTeX2WordPress.svg?style=for-the-badge
[license-url]: https://es.wikipedia.org/wiki/Licencia_MIT
[linkedin-shield]: https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white
[linkedin-url-aemt]: https://www.linkedin.com/in/andrés-merino-010a9b12b/
