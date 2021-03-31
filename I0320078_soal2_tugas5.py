print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("====================       MULAI        ===================")
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("")

nama = input("Silahkan masukkan nama Anda: ")
nilai = int(input("Input nilai : "))
print("")

# percabangan
if 85 <= nilai <= 100 :
    print('"Halo,', nama, '!', 'Nilai anda setelah dikonversi adalah A"')
elif 80 <= nilai <= 84 :
    print('"Halo,', nama, '!', 'Nilai anda setelah dikonversi adalah A-"')
elif 75 <= nilai <= 79 :
    print('"Halo,', nama, '!', 'Nilai anda setelah dikonversi adalah B+"')
elif 70 <= nilai <= 74 :
    print('"Halo,', nama, '!', 'Nilai anda setelah dikonversi adalah B"')
elif 65 <= nilai <= 69 :
    print('"Halo,', nama, '!', 'Nilai anda setelah dikonversi adalah C+"')
elif 60 <= nilai <= 64 :
    print('"Halo,', nama, '!', 'Nilai anda setelah dikonversi adalah C"')
else :
    print('"Halo,', nama, '!','nilai anda tidak valid untuk dikonversi')

print("")
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("====================      SELESAI       ===================")
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")