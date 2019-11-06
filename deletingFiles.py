#! python3
# deletingFiles.py - Borra archivos con un tamaño excesivo

import sys, logging, os

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")



#Main function
def main():
    logging.debug("Start main function")

    directory = getInput("Introduce the path of the folder: ") # Get the input of the us

    dirVerified = verifyDir(directory) # Verified the direcory is a dir

    search = checkFiles(dirVerified) 
    
    logging.info(dirVerified)

    logging.debug("End main function")

    sys.exit() #Close the script

#Funtion getInput
def getInput(msg):
    logging.debug("Start getInput function")
    try:
        var = input(msg) # save in a var the introduce by the user

        return var
    
        logging.debug("End getInput function")
        
    except KeyboardInterrupt:
        print("The script has been stopped.")

def verifyDir(directory):
    try:
        logging.debug("Start verifyDir function")

        if os.path.exists(directory):
            logging.debug("The path exists")
            if os.path.isdir(directory):
                logging.debug("The path is directory")
                return directory
            else:
                logging.debug("The path is not a directory")
                print("The path is not a directory")
                sys.exit()
        else:
            logging.debug("The directory doesn't exists")
            print("The directory doesn't exists")
            sys.exit()
        
        logging.debug("End verifyDir function")
    except Exception as err:
        logging.error(str(err))
        print("An error has occurred of type: " + str(err))
        sys.exit()

#Main function
def checkFiles(directory):
    try:
        for foldername, subfolders, filenames in os.walk(directory):
            print("The analyzed folder is " + foldername)

            for filename in filenames:
                path = foldername + filename
                size = checkSize(path)

                if size > 100000000:
                    print("The founded file: " + path)
    except Exception as err:
        logging.error(str(err))
        print("An error has occurred of type: " + str(err))
        sys.exit()

def checkSize(directory):
    try:
        logging.disable(logging.debug)
        logging.debug("Start checkSize() function")
        size = int(os.path.getsize(directory))
        
        #logging.debug("size = " + size)            
        logging.debug("Endt checkSize() function")
        return size
    except Exception as err:
        print("An error has occurred of type: " + str(err))
        sys.exit()

if __name__ == "__main__":
    main()
