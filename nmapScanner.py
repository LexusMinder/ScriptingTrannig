#! python3
# nmapScanner.py - Scanner

import nmap, logging, sys

logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")

logging.debug("Start program")

#Main function
def main():
    print("I am the main Fucntion")

    scann() # Calls to scann fucntion
    
    logging.debug("End program")

#Scan fucntion
def scann():
    nm = nmap.PortScanner()
    print(nm.nmap_version())
    nm.scan("localhost", "1-1024", "-v")
    print(nm.scaninfo())
    print(nm.csv())
        
if __name__ == "__main__":
    main()
