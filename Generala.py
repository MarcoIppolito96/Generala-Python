import random

def main():
 orden_jugadores = ordenJugadores()
 for elemento in orden_jugadores:
  print(f"Actualmente esta jugando: {elemento['Nombre']}")
  eleccion = eleccionDados(tirarDados(5))
 dadosRestantes(eleccion)

main()


def verificacionJugada2(diccionario: dict, eleccion:list):
  for clave,valor in diccionario['jugada'].items():
    if not(valor):
      print(clave)
  opcion = input('Que queres jugar')
  #while opcion !=




def verificacionJugada(diccionario: dict, eleccion:list):
  for clave,valor in diccionario['jugada'].items():
    if not(valor):
      print(clave)
  opcion = input("Que queres jugar?")

  while opcion.lower() not in diccionario['jugada'].keys():
    print("Elegi una opción correcta:")
    for clave,valor in diccionario['jugada'].items():
      if not(valor):
        print(clave)

    opcion = input("Que queres jugar?")
  if opcion.lower() == '1':
    if esNumero():
      pass
  if opcion.lower() == '2':
    if esNumero():
      pass
  if opcion.lower() == '3':
    if esNumero():
      pass
  if opcion.lower() == '4':
    if esNumero():
      pass
  if opcion.lower() == '5':
    if esNumero():
      pass
  if opcion.lower() == '6':
    if esNumero():
      pass
  if opcion.lower() == 'escalera':
    if esEscalera(eleccion):
      diccionario['jugada'][opcion.lower()] = 20
  if opcion.lower() == 'full':
    if esFull(eleccion):
      diccionario['jugada'][opcion.lower()] = 30
  if opcion.lower() == 'poker':
    if esPoker(eleccion):
      diccionario['jugada'][opcion.lower()] = 40
  if opcion.lower() == 'generala':
    if esGenerala(eleccion):
      diccionario['jugada'][opcion.lower()] = 50
  if opcion.lower() == 'generala2':
    if esGenerala(eleccion):
      diccionario['jugada'][opcion.lower()] = 60

  print(diccionario)


def ordenJugadores()-> list:
  """ Funcion que pide datos de jugadores y los ordena segun su suerte con los dados """
  lista=[]
  jugadores = int(input("Cuantos jugadores van a participar?"))
  for i in range(1,jugadores+1):
    nombre = input(f"Ingrese nombre del {i}° participante")
    jugador={'Nombre': nombre,
    'Turno' : None,
    'jugada':{'1': False,
              '2': False,
              '3': False,
              '4': False,
              '5': False,
              '6': False,
              'escalera': False,
              'full': False,
              'poker': False,
              'generala': False,
              '': False}
    }
    primer_lanzamiento = tirarDados(1)[0]
    jugador['Turno'] = primer_lanzamiento
    lista.append(jugador)
  lista_ordenada = sorted(lista, key=lambda item: item['Turno'], reverse = True)

  return lista_ordenada


def tirarDados(cantidad:int)-> list:
  """Se encarga de simular una tirada de dados dada una cantidad"""
  lista_dados=[]
  for i in range(cantidad):
    lista_dados.append(random.randint(1,6))
  return lista_dados


def validar_dato_entero(min :int,max :int) -> int:
  dato = int(input())
  while(dato < min or dato > max):
    dato = int(input("error"))
  return dato


def eleccionDados(lista_dados:list,)-> list:
  """ Recibe una lista de dados y elige los que necesite, devolviendo una nueva lista con
   los elegidos."""
  dados_elegidos = []
  for indice, valor in enumerate(lista_dados):
    print(f"{indice}) {valor}")

  print('cuantos dados desea conservar')
  cantidad_conservar = validar_dato_entero(0,5)

  if (cantidad_conservar == 5):
    return lista_dados

  for valor in range(cantidad_conservar):
    for indice, valor in enumerate(lista_dados):
      print(f"{indice}) {valor}")
    print("Elegi el dado")
    indice = validar_dato_entero(0,len(lista_dados))
    dados_elegidos.append(lista_dados.pop(indice))

  return dados_elegidos


def dadosRestantes(dados_elegidos: list)-> list:
  print("Ronda 2")
  if len(dados_elegidos) == 5:
    return dados_elegidos
  tirada = tirarDados(5-len(dados_elegidos))
  eleccion = eleccionDados(tirada+dados_elegidos)

  print("Ronda 3")
  if len(eleccion) == 5:
    return eleccion
  tirada = tirarDados(5-len(eleccion))
  eleccion = eleccionDados(tirada+eleccion)

  return eleccion

dadosRestantes(eleccionDados(tirarDados(5)))

def esNumero():
  pass


def esEscalera(mano: list) -> bool:
  escalera = ([1,2,3,4,5],[2,3,4,5,6])
  mano.sort()
  print(mano)
  return mano in escalera


def esFull(mano :list) -> bool:
  bandera3 = False
  bandera2 = False
  for i in range(1,7):
    if mano.count(i) == 3:
      bandera3 = True
    if mano.count(i) == 2:
      bandera2 = True
  return bandera3 and bandera2


def esPoker(mano :list) -> bool:
  for i in range(1,7):
    if mano.count(i) == 4:
      return True
  return False


def esGenerala(mano: list) ->bool:
  for i in range(4):
    if mano[i] != mano[i+1] :
      return False
  return True