# KUZEM Spor Kulübü Üyelik ve Antrenman Sistemi


def uye_ekle(isim, paket="Standart"):
    uye = {
        "isim": isim.strip().title(),
        "paket": paket.strip().title(),
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


# Test
yeni_uye = uye_ekle("hafize şenyıl")

antrenman_ekle(yeni_uye, 60, 45, 30)

toplam_sure = toplam_sure_hesapla(*yeni_uye["antrenmanlar"])

profil_bilgileri = {
    "isim": yeni_uye["isim"],
    "paket": yeni_uye["paket"],
    "telefon": "0555 123 45 67",
    "dogum_tarihi": "15.05.1995",
    "acil_durum_kisisi": "Ayşe Şenyıl"
}

uye_karti(**profil_bilgileri)

print(f"\nToplam antrenman süresi: {toplam_sure} dakika")