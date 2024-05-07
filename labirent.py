import time 

odalar = {
    'Başlangıç': {'odalar': ['1'], 'öğeler':[]},
    '1': {'odalar': ['Başlangıç', '2', '3'], 'öğeler':[]},
    '2': {'odalar':['1'], 'öğeler':['anahtar']},
    '3': {'odalar': ['1', '4'], 'öğeler':[]},
    '4': {'odalar': ['3', '5'], 'öğeler':[]},
    '5': {'odalar': ['4','Çıkış'], 'öğeler':[]}
}

oda = 'Başlangıç'
anahtar = False

while True:
    print('============================')
    print(oda, "Odasındasınız")
    
    for gidilecek_oda in odalar[oda]['odalar']:
        print(gidilecek_oda, 'Odalarına gidebilirsiniz.')

    yeni_oda = input("Hangi odaya gitmek istersin? : ")
    
    if yeni_oda not in odalar[oda]['odalar']:
        print('Böyle bir oda bulunmamaktadır!')
        time.sleep(2)
        continue
    
    if yeni_oda == 'Çıkış' and not anahtar:
        print("Anahtarınız YOK")
        time.sleep(2)
        continue
    
    if yeni_oda == 'Çıkış':
        print("Kazandın!")
        time.sleep(2)
        continue
    oda = yeni_oda
    
    if 'anahtar' in odalar[oda]['öğeler']:
        anahtar = True
        print("Anahtarı buldun!")
        odalar[oda]['öğeler'].remove('anahtar')
        time.sleep(2)
