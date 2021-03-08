def ReadJson(jsonObject):
    import json
    #Definir niveles de cantidad de goles mínimos
    niveles = {"A":5,"B":10,"C":15,"Cuauh":20}
    print(niveles)
    print("\n")
    
    #Convetir un objecto json en un diccionario de python
    y = json.loads(jsonObject)

    #Definir la variable de la cantidad de jugadores
    numberOfPlayers = len(y["jugadores"])

    #Crear un conjuto de diferentes equipos
    equipos = set()

    #definir la cantidad minima de goles por equipo
    MinimumGoalsPerTeam = 0
    
    #Imprimir los nombres de cada jugador
    for i in range(numberOfPlayers):
        print(y["jugadores"][i]["nombre"], ": nivel ",y["jugadores"][i]["nivel"])
        nivel  = y["jugadores"][i]["nivel"]
        equipos.add(y["jugadores"][i]["equipo"])
        MinimumGoalsPerTeam += niveles[nivel]
    print("goles minimos por equipo: ",MinimumGoalsPerTeam)
    print("\n")
    print("equipos",equipos)

    print(y["jugadores"][0])
    print(type(y["jugadores"][0]),"\n")

    #Imprimir el tipo de la clave jugadores
    #print(y)
    print(y["jugadores"])
    print(type(y["jugadores"]))
    print("\n")

x = """{
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

ReadJson(x)