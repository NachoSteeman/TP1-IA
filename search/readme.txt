Agente Resolvente (Search Agent):

    Estado, Acciones 


Busco el camino que pase por toda la comida.
Nada se mueve hasta que yo tengo mi solución


    Entorno de Busqueda:
        * Debe ser estático
        * Debe ser observable (puedo ver el estado completo)
        * Debe ser determinista (No me cambia el entorno futuro al comer algo)



    Un algoritmo de búsqueda:
        * Debe ocasionar cambios
        * Debe ser sistemático
        * Debe ser eficiente (No recomputar camino)


    AGENTE_RESOLVENTE(persepción) -> acción(conjunto de pasos para resolver problema):
        estado <- ACTUALIZAR_ESTADO(estado, percepción)




        si ESTÁ_VACIA(Sec) entonces:
            FORMULAR_OBJETIVO
            FORMULAR_PROBLEMA
            BUSQUEDA





BUSQUEDA (SEARCH AGENT)
    BUSQUEDA(problema) -> secuencia(acción):






    EXPANDIR(nodo, problema) -> conjunto(nodo):
Que pasa si llego a lista de nodos ya explorados






Si el camino se va movineto en cada avance debería recomputar todo el camino en cada iteración.




Fantasmas nosotros no los vamos a ver. Los ignoramos.


No tiene sentido usar busqueda uniforme en algo que tiene todo costo constante. Va qsy 

Jugar con distintas eurísticas, admisibles y no, y contar que pasa.

Comer todas las comidas. 




















Mirar:
    * pacman.py: aca se corre el juego


    * game.py: aca esta la logica del juego.


    * utils.py



Modificar(Solo esto y nada más):

    * search.py:

    * searchAgents.py:














