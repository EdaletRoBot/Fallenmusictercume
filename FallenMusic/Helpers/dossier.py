from FallenMusic import BOT_NAME

PM_START_TEXT = """
Salam {0}
Mən** {1}

Mənim bəzi faydalı xüsusiyyətləri olan telegram yayım botuyam. Youtube, Spotify, Resso, AppleMusic, Soundcloud və s. kimi platformaları istifadə edirəm.

Məni qruplarınıza əlavə etməkdən çəkinməyin. """

START_TEXT = """
**Salam** {0}
  {1} İndi mahnı oxuya bilər {2}

Mənim haqqımda kömək etmək üçün və ya bir şey soruşmaq istəyirsinizsə, mənim [Dəstək Çatıma]({3}) qoşula bilərsiniz.
"""

HELP_TEXT = f"""
<u>❄ **İstifadəçilər üçün mövcud əmrlər {BOT_NAME}:**</u>

/play - Video çatda tələb olunan treki yayımlayan ulduzlar.
/pause - Cari ifa axını dayandırın.
/resume - Dayandırılmış yayımı davam etdirin.
/skip - Cari ifa axınını atlayın və növbədə olan növbəti treki yayımlamağa başlayın.
/end - Növbəni təmizləyir və cari ifa axınını bitirir.
/ping - Botun ping və sistem statistikasını göstərin.
/sudolist - Botun sodo istifadəçilərinin siyahısını göstərin.
/song - İstədiyiniz mahnını yükləyin və sizə göndərin.
/search - Verilən sorğunu youtube-da axtarır və nəticəni sizə göstərir.
"""

HELP_SUDO = f"""
<u>👨🏻‍💻 **Sudo əmrləri {BOT_NAME}:**</u>

/activevc - Hazırda aktiv səsli söhbətlərin siyahısını göstərir.
/eval və ya /sh - Verilmiş kodu bot terminalında işlədir.
/speedtest - Botlar serverində sürət testini həyata keçirir.
/sysstats - Botlar serverinin sistem statistikasını göstərir.
/setname [Mətn və ya mətnə cavab] - Köməkçi hesabının adını dəyişdirin.
/setbio [Mətn və ya mətnə cavab] - Köməkçi hesabının bio-nu dəyişdirin.
/setpfp [Fotoya cavab verin] - Köməkçi hesabının pfp-ni dəyişdirin.
/delpfp - Köməkçi hesabının cari pfp-ni silin.
"""

HELP_DEV = f"""
<u>👨🏻‍💻**Sahib əmrləri {BOT_NAME}:**</u>

/config - Botun bütün konfiqurasiya dəyişənlərini əldə etmək üçün.
/broadcast [Mesaj göndərin və ya mesaja cavab verin] - Mesajı botun xidmət edilən çatlarına çatdırın.
/rmdownloads - Botlar serverində yüklənmiş keş fayllarını təmizləyir.
/leaveall - Köməkçi hesabına bütün söhbətləri tərk etməyi əmr edir.
/addsudo [İstifadəçi adı və ya istifadəçiyə cavab] - İstifadəçini sudo users lisr-ə əlavə edin.
/rmsudo [İstifadəçi adı və ya istifadəçiyə cavab] - İstifadəçini sudo istifadəçiləri siyahısından çıxarın.
"""
