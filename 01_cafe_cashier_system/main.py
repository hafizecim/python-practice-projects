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

# ----------------------------------------------------------
# 5. Sipariş Alma
# ----------------------------------------------------------

total_price = 0

order1 = input("1. ürünün numarası: ")

if order1 == "1":
    total_price += price1
elif order1 == "2":
    total_price += price2
elif order1 == "3":
    total_price += price3
elif order1 == "4":
    total_price += price4
else:
    print("Geçersiz ürün numarası")


order2 = input("2. ürünün numarası: ")

if order2 == "1":
    total_price += price1
elif order2 == "2":
    total_price += price2
elif order2 == "3":
    total_price += price3
elif order2 == "4":
    total_price += price4
else:
    print("Geçersiz ürün numarası")


order3 = input("3. ürünün numarası: ")

if order3 == "1":
    total_price += price1
elif order3 == "2":
    total_price += price2
elif order3 == "3":
    total_price += price3
elif order3 == "4":
    total_price += price4
else:
    print("Geçersiz ürün numarası")


print(f"\nAra Toplam: {total_price:.2f} TL")

# ----------------------------------------------------------
# 6. İndirim Hesaplama
# ----------------------------------------------------------

discount_rate = 0

if total_price >= 500:
    discount_rate = 15
elif total_price >= 300:
    discount_rate = 10
else:
    discount_rate = 0


# Öğrenci indirimi (iç içe koşul)

student = input("Öğrenci misiniz? (E/H): ").strip().upper()

if student == "E":
    discount_rate = discount_rate + 5


discount_amount = total_price * discount_rate / 100
payable_amount = total_price - discount_amount


print(f"\nİndirim Oranı: %{discount_rate}")
print(f"İndirim Tutarı: {discount_amount:.2f} TL")
print(f"Ödenecek Tutar: {payable_amount:.2f} TL")

# ----------------------------------------------------------
# 7. Ödeme İşlemi
# ----------------------------------------------------------

print("\nÖdeme Yöntemi")
print("1 - Nakit")
print("2 - Kart")

payment_method = input("Seçiminiz: ")

payment_success = False
change = 0


if payment_method == "1":

    cash = float(input("Verilen para: "))

    if cash >= payable_amount:
        change = cash - payable_amount
        payment_success = True
        print("Ödeme başarılı.")
    else:
        print("Yetersiz ödeme!")


elif payment_method == "2":

    print("Ödeme onaylandı.")
    payment_success = True


else:
    print("Geçersiz ödeme seçimi.")
    
# ----------------------------------------------------------
# 8. Fiş Yazdırma
# ----------------------------------------------------------

if payment_success:

    print("\n" + "=" * 40)
    print("          KUZEM KAFE FİŞİ")
    print("=" * 40)

    name_parts = customer_name.split()

    initials = ""

    for part in name_parts:
        initials += part[0].upper() + "."

    print(f"Müşteri      : {initials}")

    print(f"Müşteri Kodu : {customer_code}")
    print(f"Ara Toplam   : {total_price:.2f} TL")
    print(f"İndirim (%{discount_rate}) : {discount_amount:.2f} TL")
    print(f"Ödenecek     : {payable_amount:.2f} TL")

    if payment_method == "1":
        print(f"Para Üstü    : {change:.2f} TL")

    print("=" * 40)

else:
    print("\nFiş yazdırılamadı.")
    
# ----------------------------------------------------------
# Bonus: Kupon Kodu
# ----------------------------------------------------------

coupon_code = input("Kupon kodu (Varsa): ").strip().upper()

if coupon_code == "KUZEM10":

    extra_discount = payable_amount * 10 / 100
    discount_amount = discount_amount + extra_discount
    discount_rate = discount_rate + 10
    payable_amount = payable_amount - extra_discount

    print("KUZEM10 kupon indirimi uygulandı.")

elif coupon_code != "":
    print("Geçersiz kupon.")