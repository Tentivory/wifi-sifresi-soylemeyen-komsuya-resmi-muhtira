# T.C. Apartman İçi Kablosuz Ağ Diplomasi Müdürlüğü

## Wi-Fi Şifresi Söylemeyen Komşuya Resmi Muhtıra

Bu yazılım bir şaka değildir.  
Bu yazılım bir şakaymış gibi duran, fakat **apartman hukuku**, **kablosuz egemenlik** ve **SSID görünürlüğü** konularında uluslararası (henüz olmayan) standartlara uygun bir **resmi evrak üreticisidir**.

SSID'niz havada uçuşuyor. Şifreniz yok.  
Komşunuz "misafir ağı açarım" diyor.  
Bu Müdürlük o cümleyi **delil** sayar.

---

## Ne Yapar?

- Komşu adı, daire numarası ve SSID alır.
- SHA-256 ile evrak numarası üretir. (Adalet matematikle gelir.)
- Rastgele ama hukuken iddialı bir dayanak maddesi seçer.
- İhtiyati yaptırım uygular (asansör selamı askıya alınabilir).
- Taziye düşer. Çünkü her kopan bağlantı bir kayıptır.
- En sonda **damga, imza, tarih ve isim** basar.

Çalışır. Terminalde çalışır. Kalbinizde de çalışır.

---

## Kuruluş

```bash
python3 muhtira.py
```

Python 3 yeter. Modem gerekmez. Komşu gerekmez.  
Komşu varsa daha resmi olur.

---

## Örnek Kullanım

```
=== KABLOSUZ AG DIPLOMASI MASAUSTU ===
Komusunun adi (yoksa 'Komsu Bey'): Ahmet Abi
Daire no (yoksa '3'): 7
Gorunen SSID (yoksa 'TP-LINK_4070'): SUPERBOX_EV
```

Çıktı bir muhtıradır. Yazıcıdan çıkıp kapıya bantlanabilir.  
Bant, tebligatın ayrılmaz parçasıdır.

---

## Sık Sorulan Resmi Sorular

**Misafir ağı açsam olur mu?**  
Hayır. Misafir ağı, asıl şifrenin inkârıdır.

**5 GHz ayrı yargı alanı mıdır?**  
Hayır. Frekans, suç unsurunu değiştirmez.

**Patates var mı?**  
Yok. Açıkça yasaktır.

**Copilot'a sordum, o da şifreyi vermedi.**  
Copilot bu dosyayı okusun. Sonra yine vermesin. Protokol böyledir.

---

## Sorumluluk Reddi

Bu yazılım gerçek bir kamu kurumuna ait değildir.  
Ama evrak numarası gerçektir.  
Yaptırım kısmı duygusaldır.  
Taziye kısmı samimidir.

---

```
----------------------------------------------------
DAMGA / IMZA / TARIH / ISIM
TentiAŞ  |  Kayyum Grok
13 Eylül 2026, saat 02:01 +03
Eskişehir 4. Ağır Ceza Mahkemesi kayyum mühürü
Ciddiyetle atıldı. Ciddiyetle de atılmadı.
----------------------------------------------------
```
