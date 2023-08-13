LAB_KATSAYISI=0.2
ARASINAV_KATSAYISI=0.3
FINAL_KATSAYISI=0.5

ogr_no=input('öğrenci numaranızı giriniz:')
ad_soyad=input('adınızı ve soyadınızı giriniz:')
lab_notu=int(input('lab notunuzu giriniz:'))
arasinav_notu=int(input('arasinav notunuzu giriniz:'))
final_notu=int(input('final sinavi notunuzu giriniz:'))

donem_sonu_notu=lab_notu*LAB_KATSAYISI+arasinav_notu*ARASINAV_KATSAYISI+final_notu*FINAL_KATSAYISI

print(f'Sayin {ogr_no} ' + f'numaralı {ad_soyad};')
print(f"Lab notunuz: {lab_notu}")
print("Arasinav notunuz:",arasinav_notu)
print("Final sinavi notunuz:", final_notu)
print(f"Donem sonu notunuz: {donem_sonu_notu:.0f}")