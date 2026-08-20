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


# Test
yeni_uye = uye_ekle("hafize şenyıl")

antrenman_ekle(yeni_uye, 60, 45, 30)

print(yeni_uye)