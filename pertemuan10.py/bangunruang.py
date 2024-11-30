import math

def l_balok(p, l, t):
    hitung = 2 * (p*l)+(p*t)+(l*t)
    print(f'luas balok adalah {hitung}')

def l_kubus(sisi):
    hitung = 12 * sisi
    print(f'Keliling kubus adalah {hitung}')

def l_tabung(r, t):
    hitung = 2 * math.pi * r * (r + t)
    print(f'keliling tabung adalah {hitung}') 

def l_limas(a, t):
    hitung = 1/2 * a * t
    print(f'luas permukaan limas adalah {hitung}')

def l_luas_permukaan_prisma_segitiga(a, ts, tp, s1, s2, s3 ):
    luas_alas = 0.5 * a * ts   
    keliling_alas = s1 + s2 + s3  
    luas_permukaan = 2 * luas_alas + keliling_alas * tp
    print(f"Luas permukaan prisma segitiga adalah: {luas_permukaan:.2f}")
