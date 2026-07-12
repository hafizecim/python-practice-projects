# ==========================================================
# KUZEM KAFE KASA SİSTEMİ
# Hazırlayan: Hafize Şenyıl
# ==========================================================

print("=" * 50)
print("         KUZEM KAFE KASA SİSTEMİ")
print("=" * 50)

# ----------------------------------------------------------
# 1. Müşteri Kaydı
# ----------------------------------------------------------

customer_name = input("Ad Soyad: ").strip().title()

if customer_name == "":
    customer_name = "Misafir"

print(f"\nHoş geldiniz {customer_name}!")

# ----------------------------------------------------------
# 2. Telefon Doğrulama
# ----------------------------------------------------------

phone = input("Telefon numarası (10 hane): ").strip()

if phone.isdigit() and len(phone) == 10:
    phone_valid = True
    print("Telefon kaydedildi.")
else:
    phone_valid = False
    print("Telefon kaydedilemedi.")


# ----------------------------------------------------------
# 3. Müşteri Kodu Oluşturma
# ----------------------------------------------------------

customer_code = customer_name[:3].upper()

if phone_valid:
    customer_code = customer_code + phone[-2:]
else:
    customer_code = customer_code + "00"

print(f"Müşteri Kodu: {customer_code}")

# ----------------------------------------------------------
# 4. Menü
# ----------------------------------------------------------

print("\nKUZEM KAFE MENÜ")
print("-" * 30)

product1 = "Özel Kahve"
price1 = 180

product2 = "Kahvaltı Tabağı"
price2 = 220

product3 = "Burger Menü"
price3 = 250

product4 = "Tatlı Tabağı"
price4 = 120


print(f"1. {product1:<20} {price1:.2f} TL")
print(f"2. {product2:<20} {price2:.2f} TL")
print(f"3. {product3:<20} {price3:.2f} TL")
print(f"4. {product4:<20} {price4:.2f} TL")