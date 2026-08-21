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
    print("\n" + "=" * 40)
    print("          ÜYE PROFİL KARTI")
    print("=" * 40)

    for anahtar, deger in bilgiler.items():
        baslik = anahtar.replace("_", " ").title()
        print(f"{baslik}: {deger}")

    print("=" * 40)


def menu_goster():
    print("\n" + "=" * 40)
    print("       KUZEM SPOR KULÜBÜ")
    print("=" * 40)
    print("1 - Üye Ekle")
    print("2 - Antrenman Kaydet")
    print("3 - Rapor Görüntüle")
    print("4 - Üye Sil")
    print("0 - Çıkış")
    print("=" * 40)


def rapor_goster():
    print("\n" + "=" * 60)
    print("                 ÜYE RAPORU")
    print("=" * 60)

    if not uyeler:
        print("Henüz kayıtlı üye bulunmamaktadır.")
        return

    for sira, uye in enumerate(uyeler, start=1):
        toplam_sure = toplam_sure_hesapla(
            *uye["antrenmanlar"]
        )

        print(
            f"{sira}. {uye['isim']} | "
            f"Paket: {uye['paket']} | "
            f"Fiyat: {uye['fiyat']:.2f} TL | "
            f"Toplam Antrenman: "
            f"{toplam_sure:.2f} dakika"
        )

    print("-" * 60)
    print(f"Toplam üye sayısı: {len(uyeler)}")
    print("=" * 60)


def programi_baslat():
    while True:
        menu_goster()

        secim = input("Seçiminiz: ").strip()

        if secim == "1":
            print("\n--- ÜYE EKLE ---")

            isim = input("Üye adı: ").strip()

            if not isim:
                print("Üye adı boş bırakılamaz.")
                continue

            paket = input(
                "Üyelik paketi (Standart/Premium/Gold): "
            ).strip()

            if paket:
                yeni_uye = uye_ekle(isim, paket)
            else:
                yeni_uye = uye_ekle(isim)

            print("\n--- EK ÜYE BİLGİLERİ ---")

            telefon = input("Telefon: ").strip()

            dogum_tarihi = input(
                "Doğum tarihi: "
            ).strip()

            acil_durum_kisisi = input(
                "Acil durum kişisi: "
            ).strip()

            profil_bilgileri = {
                "telefon": telefon,
                "dogum_tarihi": dogum_tarihi,
                "acil_durum_kisisi": acil_durum_kisisi
            }

            yeni_uye["profil"] = profil_bilgileri

            uyeler.append(yeni_uye)

            print(
                f"\nÜye başarıyla eklendi: "
                f"{yeni_uye['isim']}"
            )

            print(
                f"Üyelik paketi: "
                f"{yeni_uye['paket']}"
            )

            print(
                f"Üyelik fiyatı: "
                f"{yeni_uye['fiyat']:.2f} TL"
            )

            uye_karti(
                isim=yeni_uye["isim"],
                paket=yeni_uye["paket"],
                fiyat=f"{yeni_uye['fiyat']:.2f} TL",
                **yeni_uye["profil"]
            )

        elif secim == "2":
            print("\n--- ANTRENMAN KAYDET ---")

            if not uyeler:
                print(
                    "Henüz kayıtlı üye bulunmamaktadır."
                )
                continue

            print("\nKayıtlı Üyeler:")

            for sira, uye in enumerate(uyeler, start=1):
                print(f"{sira} - {uye['isim']}")

            uye_secimi = input(
                "Üye numarası: "
            ).strip()

            if not uye_secimi.isdigit():
                print(
                    "Hata: Üye numarası "
                    "sayı olmalıdır."
                )
                continue

            uye_index = int(uye_secimi) - 1

            if uye_index < 0 or uye_index >= len(uyeler):
                print(
                    "Hata: Geçersiz üye numarası."
                )
                continue

            secilen_uye = uyeler[uye_index]

            print(
                "\nAynı gün birden fazla "
                "antrenman ekleyebilirsiniz."
            )

            print(
                "Antrenman girişini bitirmek "
                "için '0' giriniz."
            )

            sureler = []

            while True:
                sure = input(
                    "Antrenman süresi (dakika): "
                ).strip()

                if not sure.isdigit():
                    print(
                        "Hata: Antrenman süresi "
                        "sayı olmalıdır."
                    )
                    continue

                sure = int(sure)

                if sure == 0:
                    break

                sureler.append(sure)

            if sureler:
                antrenman_ekle(
                    secilen_uye,
                    *sureler
                )

                print(
                    f"\n{secilen_uye['isim']} için "
                    f"{len(sureler)} antrenman "
                    f"kaydedildi."
                )

            else:
                print(
                    "\nHerhangi bir antrenman "
                    "kaydedilmedi."
                )

        elif secim == "3":
            rapor_goster()

        elif secim == "4":
            print("\n--- ÜYE SİL ---")

            if not uyeler:
                print(
                    "Silinecek kayıtlı üye bulunmamaktadır."
                )
                continue

            silinecek_isim = input(
                "Silinecek üyenin adı: "
            ).strip().title()

            uye_bulundu = False

            for uye in uyeler:
                if uye["isim"] == silinecek_isim:
                    uyeler.remove(uye)
                    uye_bulundu = True

                    print(
                        f"\n{silinecek_isim} "
                        "başarıyla silindi."
                    )
                    break

            if not uye_bulundu:
                print(
                    f"\n'{silinecek_isim}' "
                    "isimli üye bulunamadı."
                )

        elif secim == "0":
            print("\nProgram sonlandırıldı.")
            break

        else:
            print(
                "\nGeçersiz seçim! "
                "Lütfen menüden geçerli "
                "bir seçenek giriniz."
            )


programi_baslat()