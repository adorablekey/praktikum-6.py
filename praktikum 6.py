kontak = {
  "Ari": "081267888",
  "Dina": "087677776"
}

print(f"Kontak Ari: {kontak['Ari']}")

kontak["Riko"] = "087654544"

kontak["Dina"] = "088999776"

print("Semua Nama:")
for nama in kontak:
  print(nama)

print("Semua Nomor:")
for nomor in kontak.values():
  print(nomor)

print("Daftar Nama dan Nomor:")
for nama, nomor in kontak.items():
  print(f"{nama}: {nomor}")

del kontak["Dina"]

print("Daftar Kontak setelah menghapus Dina:")
for nama, nomor in kontak.items():
  print(f"{nama}: {nomor}")