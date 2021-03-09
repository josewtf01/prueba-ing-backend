def ReadJson(jsonObject):
    import json

    #Definir niveles y su cantidad de goles mínimos
    niveles = {"A":5,"B":10,"C":15,"Cuauh":20}

    #Convetir un objecto json en un diccionario de python
    jsonDict = json.loads(jsonObject)

    #Definir la variable de la cantidad de jugadores
    numeroDeJugadores = len(jsonDict["jugadores"])

    #definir la lista de los jugadores
    jugadores = jsonDict["jugadores"]

    #Imprimir los  jugadores
    """
    for i in range(numeroDeJugadores):
        print(jugadores[i])
    print("\n")"""

    #definir el bono de cada equipo
    bonoPorEquipo = GolesDeLosEquipos(numeroDeJugadores,jsonDict,niveles)

    #copiar el diccionario de entrada para calcular el sueldo total de cada jugador
    pagoDeLosJugadores = jsonDict.copy()
    #calcular el pago de cada jugador mediante una función
    SueldoTotal(numeroDeJugadores,jugadores,bonoPorEquipo,pagoDeLosJugadores,niveles)

    #regresar un objeto json con los pagos totales de los jugadores
    return json.dumps(pagoDeLosJugadores,indent = 4)

def GolesDeLosEquipos(numeroDeJugadores,jsonDict,niveles):
   #Crear un conjuto de diferentes equipos
    equipos = set()

    #buscar todos los equipos que existen
    for i in range(numeroDeJugadores):
        equipos.add(jsonDict["jugadores"][i]["equipo"])

    #definir diccionario con la cantidad minima de goles por equipo
    golesMinimosPorEquipo = dict.fromkeys(equipos,0)

    #definir diccionario con la cantidad real de goles por equipo
    golesPorEquipo = dict.fromkeys(equipos,0)

    #definir la catidad minima de goles por equipo
    for i in range(numeroDeJugadores):
        #nivel del jugador
        nivel  = jsonDict["jugadores"][i]["nivel"]
        #goles actuales del jugador
        goles = jsonDict["jugadores"][i]["goles"]
        #calculo de goles minimos por equipo totales
        golesMinimosPorEquipo[jsonDict["jugadores"][i]["equipo"]] += niveles[nivel]
        #calculo de goles actules totales por equipo
        golesPorEquipo[jsonDict["jugadores"][i]["equipo"]] += goles

    #definición del diccionario de bonos por equipo
    bonoPorEquipo = dict()
    for j in golesMinimosPorEquipo:
        #si la cantidad de goles minima se cumple dar el 100% del bono
        if (golesPorEquipo[j] >= golesMinimosPorEquipo[j]):
            bonoPorEquipo[j] = 1.0
        #si no se cumple la cuota minima de goles calcular el porcenta del bono
        else:
            porcentaje = round(golesPorEquipo[j]/golesMinimosPorEquipo[j],2)
            bonoPorEquipo[j] = porcentaje
    return bonoPorEquipo

def SueldoTotal(numeroDeJugadores,jugadores,bonoPorEquipo,pagoDeLosJugadores,niveles):
    for i in range(numeroDeJugadores):

        #Inicio de bono de cada jugador
        bonoIndividual = 0

        #definición de goles minimos del jugador
        golesMinimosDelJugador  = niveles[jugadores[i]["nivel"]]

        #definición de goles actuales del jugador
        golesActualesDelJugador = jugadores[i]["goles"]

        #si el jugador cumple la cuota minima de goles dar el 100% del bono individual
        if(golesActualesDelJugador >= golesMinimosDelJugador):
            bonoIndividual = 1.0
        # si no cumple la cuota minima de goles, calcular el porcentaje del bono individual
        else:
            bonoIndividual = round(golesActualesDelJugador/golesMinimosDelJugador,2)

        #definir el equipo del jugador
        equipo = jugadores[i]["equipo"]

        """calcular el porcentaje del bono variable, donde 50% es del bono
        por equipo y el otro 50% es del bono individual"""
        bonoVariable = bonoPorEquipo[equipo]*0.5 + bonoIndividual * 0.5

        #consultar el sueldo fijo del jugador
        sueldoFijo = jugadores[i]["sueldo"]

        #consultar el bono predeterminado del jugador
        bono = jugadores[i]["bono"]

        #calcular el sueldo completo del jugador
        pagoDeLosJugadores["jugadores"][i]["sueldo_completo"] = int(sueldoFijo + bono * bonoVariable)

def main():
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

    print(ReadJson(x))

if __name__ == "__main__":
    main()
