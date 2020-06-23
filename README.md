# resuelve
Prueba Ingeniería Backend

El problema fue solucionado utilizando el miniframework Flask con Python 3.

Requisitos:
 - Tener alguna herramienta para realizar peticiones HTTP como postman
 - Tener Python instalado
 - Installar Flask
 	https://flask.palletsprojects.com/en/1.1.x/installation/

Instrucciones:
- Ir a la carpeta resuelve
- Levantar el servidor con el siguiente comando: python server.py
- Desde nuestro entorno de desarrollo de APIs (postman), realizar una petición de tipo POST a la siguiente url:
	http://localhost:8000/salaries
- Agregar al cuerpo de la petición el siguiente json:
[  
   {  
      "nombre":"Juan Perez",
      "nivel":"C",
      "goles":10,
      "sueldo":50000,
      "bono":25000,
      "sueldo_completo":null,
      "equipo":"rojo"
   },
   {  
      "nombre":"EL Cuauh",
      "nivel":"Cuauh",
      "goles":30,
      "sueldo":100000,
      "bono":30000,
      "sueldo_completo":null,
      "equipo":"azul"
   },
   {  
      "nombre":"Cosme Fulanito",
      "nivel":"A",
      "goles":7,
      "sueldo":20000,
      "bono":10000,
      "sueldo_completo":null,
      "equipo":"azul"

   },
   {  
      "nombre":"El Rulo",
      "nivel":"B",
      "goles":9,
      "sueldo":30000,
      "bono":15000,
      "sueldo_completo":null,
      "equipo":"rojo"

   }
]
