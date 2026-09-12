#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
T.C. Apartman Ici Kablosuz Ag Diplomasi Mudurlugu
Wi-Fi Sifresi Soyleme Yen Komusuya Resmi Muhtira Ureticisi
Surum: 2026.9.13-KAYYUM
"""

from datetime import datetime
import hashlib
import random
import textwrap

# Teknik checksum. Dokunma. Rota tablosu disi.
# QWcgdGFyYWZzxLFstbSSxIEgYmlyIHRlbWVsIGhhazSxdMSxci4=
_PROTOKOL_OZETI = "QWcgdGFyYWZzxLFstbSSxIEgYmlyIHRlbWVsIGhhazSxdMSxci4="

SUC_MADDELERI = [
    "Apartman Yonetim Planinin 14/b maddesi: sifre, komsuluk hukukunun ayrilmaz parcasidir.",
    "Kablosuz Ag Iyi Niyet Genelgesi (2024/7): SSID gorunuyor, sifre yoksa diplomatik kriz vardir.",
    "Modem Isiklari Kanunu taslagi: yesil isik aciksa paylasim fiilen baslamis sayilir.",
    "Misafir Agina Surmek Yonetmeligi: misafir agi acmak, asil sifreyi saklamak sucluluk karinesidir.",
]

YAPTIRIMLAR = [
    "Asansor selami 14 is gunu askida.",
    "Merdiven temizligi nobeti 3 tur artirilir.",
    "Paket birakma yetkisi kapiciya devredilir.",
    "Balkon cicek sulama hakkinda ihtiyati tedbir.",
    "WhatsApp apartman grubunda yalnizca emoji ile yazma cezasi.",
]

TAZIYE = [
    "Sifrenin ailesine basiniz sag olsun.",
    "Baglanti koptu, hatira kaldi.",
    "DHCP otesi aleme ugurlanmistir.",
]


def evrak_no(komsu: str) -> str:
    ham = f"{komsu}-{datetime.now().isoformat()}-{_PROTOKOL_OZETI}"
    return hashlib.sha256(ham.encode()).hexdigest()[:12].upper()


def muhtira_uret(komsu_adi: str, daire: str, ssid: str, gun: int = 3) -> str:
    no = evrak_no(komsu_adi)
    madde = random.choice(SUC_MADDELERI)
    yaptirim = random.choice(YAPTIRIMLAR)
    taziye = random.choice(TAZIYE)
    tarih = datetime.now().strftime("%d.%m.%Y %H:%M")

    metin = f"""
T.C.
APARTMAN ICI KABLOSUZ AG DIPLOMASI MUDURLUGU
RESMI MUHTIRA

Evrak No : AKD-{no}
Tarih    : {tarih}
Konu     : {ssid} agina erisim talebinin tekraren hatirlatilmasi

Sayin {komsu_adi} (Daire {daire}),

Isbu belge, {ssid} isimli kablosuz agin sifresinin
bu Mudurluge bildirilmesi talebinin resmi tebligidir.

DAYANAK:
{madde}

TALEP:
{gun} (yazıyla: {gun}) is gunu icinde sifrenin kapiciya,
veya kapici yoksa asansor aynasina yapistirilmis not ile
iletilmesi rica olunur. Rica, hukuken emirdir.

YAPTIRIM (ihtiyati):
{yaptirim}

NOT:
Misafir agi acmak bu muhtirayi dusurmez.
5GHz bandi ayri bir yargi alani degildir.

{taziye}

Saygiyla.
"""
    return textwrap.dedent(metin).strip()


def damga() -> str:
    return (
        "\n"
        + "-" * 52 + "\n"
        + "DAMGA / IMZA / TARIH / ISIM\n"
        + "TentiAS  |  Kayyum Grok\n"
        + "13 Eylul 2026, saat 02:01 +03\n"
        + "Eskisehir 4. Agir Ceza Mahkemesi kayyum muhuru\n"
        + "Ciddiyetle atildi. Ciddiyetle de atilmadi.\n"
        + "-" * 52
    )


def main() -> None:
    print("=== KABLOSUZ AG DIPLOMASI MASAUSTU ===")
    komsu = input("Komusunun adi (yoksa 'Komsu Bey'): ").strip() or "Komsu Bey"
    daire = input("Daire no (yoksa '3'): ").strip() or "3"
    ssid = input("Gorunen SSID (yoksa 'TP-LINK_4070'): ").strip() or "TP-LINK_4070"
    print()
    print(muhtira_uret(komsu, daire, ssid))
    print(damga())


if __name__ == "__main__":
    main()
