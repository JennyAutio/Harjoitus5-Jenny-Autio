from machine import Pin, PWM
from time import sleep

# Moottori A
e1 = PWM(Pin(28))
m1 = Pin(27, Pin.OUT)

#  Moottori B
e2 = PWM(Pin(26))
m2 = Pin(22, Pin.OUT)

# Aseta PWM-taajuus 1000 Hz
e1.freq(1000)
e2.freq(1000)

# tätä funktiota kutsuttaessa mennään eteenpäin määritetty aika
def eteen(nopeus,aika):
    m1.value(1)
    m2.value(1)
    e1.duty_u16(nopeus)
    e2.duty_u16(nopeus)
    sleep(aika)

# tätä funktiota kutsuttaessa käännytään vasemmalle
def vasen(nopeus1,nopeus2,aika):
    m1.value(1)
    m2.value(1)
    e1.duty_u16(nopeus1)
    e2.duty_u16(nopeus2)
    sleep(aika)

# tätä funktiota kutsuttaessa käännytään oikealle
def oikea(nopeus1,nopeus2,aika):
    m1.value(1)
    m2.value(1)
    e1.duty_u16(nopeus1)
    e2.duty_u16(nopeus2)
    sleep(aika)

# tätä funktiota kutsuttaessa käännytään paikallaan esim. puoliympyrä tai ympyrä
def kaannyAstetta(nopeus,aika):
    m1.value(1)
    m2.value(0)
    e1.duty_u16(nopeus)
    e2.duty_u16(nopeus)
    sleep(aika)

# tätä funktiota kutsuttaessa peruutetaan
def peruuta(nopeus,aika):
    m1.value(0)
    m2.value(0)
    e1.duty_u16(nopeus)
    e2.duty_u16(nopeus)
    sleep(aika)

# tämä funktio kutsutaan, kun reitti on valmis
def lopeta():
    sleep(1)
    e1.duty_u16(0)
    e2.duty_u16(0)
    sleep(1)

# Nopeus 100% = 65534
# Nopeus 75% = 49150
# Nopeus 50% = 32767
# Nopeus 25% = 16384

n100=65534
n75=49150
n50=32767
n25=16384
n=0
tauko=1