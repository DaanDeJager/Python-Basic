import time

a = input('Op welk uur wilt u beginnen?:'); a=int(a)
b = input('Op welke minuten wilt u beginnen?:'); b=int(b)
c = input('Op welke seconden wilt u beginnen?:'); c=int(c)


def klok2(a,b,c):
    for h in range(a, 24):
        for m in range(b, 60):
            for s in range(c, 60):
                if h == 23:
                    if m == 59:
                        if s == 59:
                            a=0
                if m == 59:
                    if s == 59:
                        b = 0 
                if s == 59:
                    c = 0 
                tijdformat = f"{h:02}:{m:02}:{s:02}"
                print(tijdformat)
                time.sleep(1)      
   
klok2(a,b,c)


while True:
    def klok1():
        for hh in range(0, 24):
            for mm in range(0, 60):
                for ss in range(0, 60):
                    tijdformat = f"{hh:02}:{mm:02}:{ss:02}"
                    print(tijdformat)
                    time.sleep(1)
    klok1()
