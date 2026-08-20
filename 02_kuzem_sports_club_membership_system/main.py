# KUZEM Spor Kulübü Üyelik ve Antrenman Sistemi


uyeler = []


def uye_ekle(isim, paket="Standart"):
    paket = paket.strip().title()

    if paket == "Standart":
        fiyat = 500
    elif paket == "Premium":
        fiyat = 750
    elif paket == "Gold":
        fiyat = 1000
    else:
        paket = "Standart"
        fiyat = 500

    uye = {
        "isim": isim.strip().title(),
        "paket": paket,
        "fiyat": fiyat,
        "antrenmanlar": []
    }

    return uye


def antrenman_ekle(uye, *sureler):
    for sure in sureler:
        uye["antrenmanlar"].append(sure)


def toplam_sure_hesapla(*sureler):
    return sum(sureler)


def uye_karti(**bilgiler):
    print("\n--- ÜYE PROFİL KARTI ---")

    for anahtar, deger in bilgiler.items():
        print(f"{anahtar.replace('_', ' ').title()}: {deger}")


def menu_goster():
    print("\n" + "=" * 40)
    print("       KUZEM SPOR KULÜBÜ")
    print("=" * 40)
    print("1 - Üye Ekle")
    print("2 - Antrenman Kaydet")
    print("3 - Rapor Görüntüle")
    print("0 - Çıkış")
    print("=" * 40)


def programi_baslat():
    while True:
        menu_goster()

        secim = input("Seçiminiz: ").strip()

        if secim == "1":
            print("\n--- ÜYE EKLE ---")

            isim = input("Üye adı: ")
            paket = input(
                "Üyelik paketi (Standart/Premium/Gold): "
            )

            yeni_uye = uye_ekle(isim, paket)
            uyeler.append(yeni_uye)

            print(f"\nÜye başarıyla eklendi: {yeni_uye['isim']}")

        elif secim == "2":
            print("\nAntrenman kaydı özelliği sonraki aşamada eklenecek.")

        elif secim == "3":
            print("\nRapor özelliği sonraki aşamada eklenecek.")

        elif secim == "0":
            print("\nProgram sonlandırıldı.")
            break

        else:
            print("\nGeçersiz seçim! Lütfen menüden geçerli bir seçenek giriniz.")


programi_baslat()