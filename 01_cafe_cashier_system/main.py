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