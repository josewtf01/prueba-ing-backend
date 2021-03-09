# prueba-ing-backend

Repositorio con la resolución del "Reto de Ingeniería Resuelve"

Se puede importar el archivo `sueldo.py`

```
$ python 
>>> import sueldo.py
```
Definir el objeto json en la variable `x`  

```  
>>> x = """{
       "jugadores" : [
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
             "sueldo_completo": null,
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
    }"""
```  
Llamamos la función `CalcularSueldoTotal`  

```
>>> sueldo.CalcularSueldoTotal(x)
```  
De esta manera hara se puede ejecutar la función si se importa.

Si se ejecuta directamente por el interprete de python  
```
$ python sueldo.py
```
Se ejectua el resultado del ejemplo:
```  
"""{
       "jugadores" : [
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
             "sueldo_completo": null,
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
    }"""
```  

## Referencias

- "Read JSON file using Python" [GeeksForGeeks](https://www.geeksforgeeks.org/read-json-file-using-python/)
- "Python JSON" [w3schools](https://www.w3schools.com/python/python_json.asp)
- "JSON - Introduction" [w3schools](https://www.w3schools.com/js/js_json_intro.asp)
- "json" [Python Documentation](https://docs.python.org/3/library/json.html#basic-usage)
- "Working With JSON Data in Python" [Real Python](https://realpython.com/python-json/)
- "json.dumps()" [GeeksForGeeks](https://www.geeksforgeeks.org/json-dumps-in-python/)
- "Python Dictionaries" [w3schools](https://www.w3schools.com/python/python_dictionaries.asp)
- "GIT Documentation" [git](https://git-scm.com/doc)
- "Markdown Documentation" [Markdown](https://www.markdownguide.org/basic-syntax/)
- "Python Sets" [w3schools](https://www.w3schools.com/python/python_sets.asp)
- "Python | Convert a set into dictionary" [GeeksForGeeks](https://www.geeksforgeeks.org/python-convert-a-set-into-dictionary/)
- "set add() in python" [GeeksForGeeks](https://www.geeksforgeeks.org/set-add-python/)
- "Python Dictionary copy()" [Programiz](https://www.programiz.com/python-programming/methods/dictionary/copy)