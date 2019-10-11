/*Paso 1*/
puerto = 80
banner = "Apache HTTP Server"
print "Buscando " + banner + " en el puerto " + str(puerto)

//Paso 2
type(puerto)
type(banner)
listaPuertos = [21,22,80,110]
type(listaPuertos)
puertoAbierto=True
type(puertoAbierto)

//Paso 3
print banner.upper()
print banner.lower()
print banner.replace('Apache','Glassfish')
print banner.find('HTTP')

//Paso 4
listaPuertos = []
listaPuertos.append(21)
listaPuertos.append(80)
listaPuertos.append(443)
listaPuertos.append(25)
print listaPuertos

listaPuertos.sort()
print listaPuertos

pos = listaPuertos.index(80)
print "Hay " + pos  " puertos por analizar antes del 80."
listaPuertos.remove(443)
print listaPuertos
cnt = len(listaPuertos)
print "Total de puertos por analizar: " + str(cnt)

//Paso 5
servicios = {'ftp':21, 'ssh':22, 'smtp':25, 'http':80}
servicios.keys()
servicios.items()
servicios.has_key('ssh')
servicios['ssh']
print "Hay una vulnerabilidad de SSH en el puerto " + str(servicios['ssh'])

