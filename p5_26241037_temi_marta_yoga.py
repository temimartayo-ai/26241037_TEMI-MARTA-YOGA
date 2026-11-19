print("=== INPUT DATA MAHASISWA ===")

nama = input("Nama mahasiswa : ")
nim = input("NIM lengkap    : ")

A = int(input("Digit A (kedua dari belakang): "))
B = int(input("Digit B (terakhir): "))

print("\n===== HASIL PERBANDINGAN =====")

print("A > B  :", A > B)
print("A < B  :", A < B)
print("A == B :", A == B)
print("A != B :", A != B)
print("A >= B :", A >= B)
print("A <= B :", A <= B)

print("\n===== TIPE DATA =====")
print("Tipe nama :", type(nama))
print("Tipe NIM  :", type(nim))
print("Tipe A    :", type(A))
print("Tipe B    :", type(B))
