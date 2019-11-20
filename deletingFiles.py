#! python3
# deletingFiles.py - Borra archivos con un tamaño excesivo

import sys, logging, os, traceback

logging.disable(logging.CRITICAL)

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

#Main function
def main():
    logging.disable(logging.INFO)
    logging.debug("Start main function")

    directory = getInput("Introduce the path of the folder: ") # Get the input of the us

    dirVerified = verifyDir(directory) # Verified the direcory is a dir

    array = checkFiles(dirVerified) # Save a array with all enormous files

    printArray(array)

    logging.debug("End main function")

    sys.exit() #Close the script

#Funtion getInput
def getInput(msg):
    logging.debug("Start getInput function")
    try:
        var = input(msg) # save in a var the introduce by the user

        var = var.strip() # Limpia espacios en blanco
    
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
        foundedFiles = []
        print("The folder is target " + directory)
        for foldername, subfolders, filenames in os.walk(directory):
            #print("The analyzed folder is " + foldername)

            for filename in filenames:
                path = foldername + "\\" +  filename
                size = checkSize(path)

                if size > 100000000:
                    foundedFiles += [path]
                    
                    #logging.info(foundedFiles)
        return foundedFiles
    except Exception as err:
        logging.error(str(err))
        #loggin.inf(tracbak.format_exc())
        print("An error has occurred of type: " + str(err))
        sys.exit()

def checkSize(directory):
    try:
        logging.disable(logging.DEBUG)
        logging.debug("Start checkSize() function")
        size = int(os.path.getsize(directory))
        
        #logging.debug("size = " + size)            
        logging.debug("Endt checkSize() function")
        return size
    except Exception as err:
        print("An error has occurred of type: " + str(err))
        sys.exit()

def removeFiles(array):
    for element in array:
        os.unlink(element)    

def printArray(array):
    print("Files removed")
    for i in range(len(array)):
        
        print("File " + str(i) + ": " + array[i])

if __name__ == "__main__":
    main()
