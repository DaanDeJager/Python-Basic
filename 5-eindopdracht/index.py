#hier import ik de tijd waardoor ik time.sleep() kan gebruiken
import time
#dit zijn de inputs waardoor ik de tijd krijgt van de gebruiker
a = input("Op welk uur wilt u beginnen:"); a = int(a)
b = input("Op welk minuten wilt u beginnen:"); b = int(b)
c = input("Op welke seconden wilt u beginnen:"); c = int(c)
#hier begin ik mijn function
def count():
    #dit is de format waardoor de 00:00:00 wordt weergeven en bij de format laat het zien dat het moet zijn hh:mm:ss
    timeformat = '{:02d}:{:02d}:{:02d}'.format(h, m , s)
    #ik print de format
    print(timeformat)
#ik heb hie een while true loop zodat het voor altijd loopt
while True:
    #dit is de loop voor het uur
 for h in range(0,23):
     #hier maak ik het dat de input bij het uur komt
      h+=a
      #minuten loop
      for m in range(0,59):
          #hier maak ik het dat de input bij de minuten komt
            m+=b
            #seconden loop
            for s in range(0, 59):
                #hier maak ik het dat de input bij de seconden komt
                s+=c
                #dit maakt het zodat het elke 1 seconden draait
                time.sleep(1)
                #dit execute de function
                count()
