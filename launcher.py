from mensaje_inicial import mensaje_inicial
from puntaje import *
from temporizador import *

if __name__ == "__main__":
    if mensaje_inicial() == True: #Si el usuario quiere jugar.  
        
        # Iniciar puntaje: se inició desde la importación. 
        
        # Mensaje de cuenta regresiva para iniciar.
                
        # Iniciar temporizador. La parte de "args" es para ponerle el tiempo
        thread_temporizador = threading.Thread(target = temporizador, args=(5, ))
        thread_temporizador.start()

        # Mostrar preguntas mientras siga activo el contador.
        while thread_temporizador.is_alive():
            
            #Puse esto en lo que hacemos el módulo
            print('')
            time.sleep(1)

        # Terminar la ronda

        # Preguntar si quiere volver a jugar

    else: # Si la persona ya se quiere salir.
        print("\n¡Regresa pronto!\n")
        time.sleep(0.1)


#