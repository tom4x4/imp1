import redis
import re
import random

r=redis.Redis('localhost',port=6379,db=0)

def znaki(text):
    text=text.strip().upper()
    ogon=('AĆĘŁŃÓŚŹŻ')
    bezogona=('ACELNOSZZ')
    zamien=str.maketrans(ogon,bezogona)
    return str(text).translate(zamien)

def dziel(text):
    text=znaki(text)
    text = re.sub('[.]', ' ', text)
    text = re.sub('[\s]{2,}', ' ', text)
    return text

def wczytaj(nr,text):
    text=dziel(text)
    for wyraz in text.split(' '):
        if len(wyraz)>=5:
            r.sadd(nr,wyraz)

bl=random.randint(1,9999999)

apnazwa= "   Ala ma kota i3.pieski 30ml ase śśŚŻąć #$%^& ddddddd"
blnazwa = "Ala jest pusta"

wczytaj(bl,apnazwa)

for xx in r.smembers(bl):
    print(bl)
    print(r.smembers(bl))
    print(xx.decode('UTF-8'))
    if xx=='30ml'.encode('UTF-8'):
        print('jest')

