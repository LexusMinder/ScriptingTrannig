#! python3
# infoLol.pyw - Consulta en una pagina web runas e historial de jugadores, y abre
# el navegador con la consulta dada

#modules
import sys, logging

logging.basicConfig(filename="log.txt", level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")

logging.debug("Inicio de programa")

#Funcion principal
def main():
    logging.debug("[Main Function]")
    print("I am the main function")
    logging.debug("Fin del programa\n")
    sys.exit()
    
if __name__ == "__main__":
    main()
