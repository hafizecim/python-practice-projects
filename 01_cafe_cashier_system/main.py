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