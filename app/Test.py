import platform
import time
import datetime
import os.path 

x = datetime.datetime.now()
print ("Hoy es: %s/%s/%s" % (x.day, x.month, x.year) + "." )

myHostname = platform.uname()[1]

print ("Mi nombre de host es " + myHostname + ".")
print ("Voy a Iterar 10 veces")
for i in iter("0123456789"):
    print("la iteracion es: "  + i + ". ")
    time.sleep(1)
print("FIN")
    
exit()
