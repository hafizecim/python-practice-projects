# KUZEM Spor Kulübü Üyelik ve Antrenman Sistemi


def uye_ekle(isim, paket="Standart"):
    uye = {
        "isim": isim.strip().title(),
        "paket": paket.strip().title(),
        "antrenmanlar": []
    }

    return uye


# Fonksiyon testi
yeni_uye = uye_ekle("hafize şenyıl")

print(yeni_uye)