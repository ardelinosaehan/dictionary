print("Nama  : Ardelino Saehan")
print("NIM   : 312110121")
print("Kelas : TI.21.A.1")
print("=======================")
print()

kontak = {"Ari": "085215565501", "Dina": "08788767778"}
print("Nama | Nomor Telepon")
print("Tampilkan Dictionary Kontak")
print(kontak)

print("----------------------------------------------")
print("Kontak Ari")
print(kontak['Ari'])

print("----------------------------------------------")
print("Menambahkan kontak baru dengan nama Riko - 087654544")
kontak['Riko'] = '087654544'
print(kontak['Riko'])

print("----------------------------------------------")
print("Ubah kontak Dina dengan nomor baru 087677776")
kontak['Dina'] = '088999776'
print(kontak['Dina'])

print("----------------------------------------------")
print("Tampilkan semua Nama")
print(kontak.keys())

print("----------------------------------------------")
print("Tampilkan semua Nomor")
print(kontak.values())

print("----------------------------------------------")
print("Tampilkan daftar nama dan nomor")
print(kontak.items())
print("----------------------------------------------")

print("Hapus kontak Dina")
del kontak['Dina']
print(kontak)
