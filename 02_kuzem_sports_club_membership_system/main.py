# KUZEM Spor Kulübü Üyelik ve Antrenman Sistemi


# Terminal renkleri
RESET = "\033[0m"
BOLD = "\033[1m"

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
CYAN = "\033[96m"
WHITE = "\033[97m"

# Tüm üyelerin saklanacağı liste
uyeler = []


# Hoca kriteri:
# Varsayılan parametre kullanılır.
# Paket belirtilmezse otomatik olarak "Standart" paketi atanır.
# Fonksiyon oluşturulan üye bilgisini return ile geri döndürür.
def uye_ekle(isim, paket="Standart"):
    paket = paket.strip().title()

    # Hoca kriteri:
    # if / elif / else karar yapıları kullanılarak
    # üyelik paketine göre fiyat belirlenir.
    if paket == "Standart":
        fiyat = 500
    elif paket == "Premium":
        fiyat = 750
    elif paket == "Gold":
        fiyat = 1000
    else:
        # Geçersiz paket girilirse varsayılan paket uygulanır.
        paket = "Standart"
        fiyat = 500

    uye = {
        "isim": isim.strip().title(),
        "paket": paket,
        "fiyat": fiyat,
        "antrenmanlar": []
    }

    # Hoca kriteri:
    # Üye bilgisi print edilmek yerine fonksiyondan return edilir.
    return uye


# Hoca kriteri:
# Aynı anda birden fazla antrenman süresi *args ile alınır.
def antrenman_ekle(uye, *sureler):
    for sure in sureler:
        uye["antrenmanlar"].append(sure)


# Hoca kriteri:
# Antrenman sürelerinin toplamını hesaplayan ayrı fonksiyon.
# Süreler *args kullanılarak alınır.
def toplam_sure_hesapla(*sureler):
    return sum(sureler)


# Hoca kriteri:
# Esnek sayıda profil bilgisini **kwargs ile alır.
def uye_karti(**bilgiler):
    print("\n" + "=" * 40)
    print("          ÜYE PROFİL KARTI")
    print("=" * 40)

    for anahtar, deger in bilgiler.items():
        baslik = anahtar.replace("_", " ").title()
        print(f"{baslik}: {deger}")

    print("=" * 40)


# Kullanıcıya program menüsünü gösterir.
def menu_goster():
    print("\n" + CYAN + "=" * 40 + RESET)
    print(BOLD + CYAN + "       KUZEM SPOR KULÜBÜ" + RESET)
    print(CYAN + "=" * 40 + RESET)

    print(GREEN + "1 - Üye Ekle" + RESET)
    print(YELLOW + "2 - Antrenman Kaydet" + RESET)
    print(BLUE + "3 - Rapor Görüntüle" + RESET)
    print(RED + "4 - Üye Sil" + RESET)
    print(BOLD + WHITE + "0 - Çıkış" + RESET)

    print(CYAN + "=" * 40 + RESET)


# Hoca kriteri:
# Tüm üyelerin isimlerini ve toplam antrenman sürelerini
# f-string ve :.2f formatı ile rapor olarak gösterir.
def rapor_goster():
    print("\n" + "=" * 60)
    print("                 ÜYE RAPORU")
    print("=" * 60)

    if not uyeler:
        print("Henüz kayıtlı üye bulunmamaktadır.")
        return

    for sira, uye in enumerate(uyeler, start=1):

        # Hoca kriteri:
        # Var olan antrenman listesi * işareti ile açılarak
        # toplam_sure_hesapla fonksiyonuna gönderilir.
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


# Ana program fonksiyonu.
# Kullanıcı 0 seçeneğini girene kadar menü çalışmaya devam eder.
def programi_baslat():
    while True:
        menu_goster()

        secim = input("Seçiminiz: ").strip()

        # 1 - Üye ekleme
        if secim == "1":
            print("\n--- ÜYE EKLE ---")

            isim = input("Üye adı: ").strip()

            if not isim:
                print("Üye adı boş bırakılamaz.")
                continue

            paket = input(
                "Üyelik paketi (Standart/Premium/Gold): "
            ).strip()

            # Paket girilmişse kullanıcı tarafından belirtilen paket kullanılır.
            if paket:
                yeni_uye = uye_ekle(isim, paket)

            # Paket boş bırakılırsa fonksiyonun varsayılan
            # "Standart" parametresi kullanılır.
            else:
                yeni_uye = uye_ekle(isim)

            print("\n--- EK ÜYE BİLGİLERİ ---")

            # Hoca kriteri:
            # En az 3 farklı ekstra profil bilgisi alınır.
            telefon = input("Telefon: ").strip()

            dogum_tarihi = input(
                "Doğum tarihi: "
            ).strip()

            acil_durum_kisisi = input(
                "Acil durum kişisi: "
            ).strip()

            # Profil bilgileri bir dictionary içinde saklanır.
            profil_bilgileri = {
                "telefon": telefon,
                "dogum_tarihi": dogum_tarihi,
                "acil_durum_kisisi": acil_durum_kisisi
            }

            yeni_uye["profil"] = profil_bilgileri

            # Yeni üye ana üye listesine eklenir.
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

            # Hoca kriteri:
            # Var olan profil dictionary'si ** işareti ile açılarak
            # uye_karti fonksiyonuna gönderilir.
            uye_karti(
                isim=yeni_uye["isim"],
                paket=yeni_uye["paket"],
                fiyat=f"{yeni_uye['fiyat']:.2f} TL",
                **yeni_uye["profil"]
            )

        # 2 - Antrenman kaydetme
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

            # Hoca kriteri:
            # Sayı beklenen yerde geçersiz giriş yapılırsa
            # program çökmemeli ve kullanıcı uyarılmalıdır.
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

                # Geçersiz sayı girişi programı durdurmaz.
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

                # Hoca kriteri:
                # Var olan süre listesi * ile açılarak
                # birden fazla değer *args fonksiyonuna gönderilir.
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

        # 3 - Tüm üyelerin raporunu gösterme
        elif secim == "3":
            rapor_goster()

        # 4 - BONUS: Üye silme
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

            # BONUS:
            # Kullanıcının girdiği isim listede aranır
            # ve eşleşen üye listeden çıkarılır.
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

        # 0 - Programdan çıkış
        elif secim == "0":
            print("\nProgram sonlandırıldı.")
            break

        # Menüde olmayan bir seçim yapılırsa kullanıcı uyarılır.
        else:
            print(
                "\nGeçersiz seçim! "
                "Lütfen menüden geçerli "
                "bir seçenek giriniz."
            )


# Programı başlatır.
programi_baslat()