from django.db import models
from django.utils.translation import gettext_lazy as _


class Quran(models.Model):
    class SuratSurat(models.IntegerChoices):
        SuratNumber1 = 1, _("Al-Fātiḥah (7)")
        SuratNumber2 = 2, _("Al-Baqarah (286)")
        SuratNumber3 = 3, _("Āli 'Imrān (200)")
        SuratNumber4 = 4, _("An-Nisā' (176)")
        SuratNumber5 = 5, _("Al-Mā'idah (120)")
        SuratNumber6 = 6, _("Al-An'ām (165)")
        SuratNumber7 = 7, _("Al-A'rāf (206)")
        SuratNumber8 = 8, _("Al-Anfāl (75)")
        SuratNumber9 = 9, _("At-Taubah (129)")
        SuratNumber10 = 10, _("Yūnus (109)")
        SuratNumber11 = 11, _("Hūd (123)")
        SuratNumber12 = 12, _("Yūsuf (111)")
        SuratNumber13 = 13, _("Ar-Ra'd (43)")
        SuratNumber14 = 14, _("Ibrāhīm (52)")
        SuratNumber15 = 15, _("Al-Ḥijr (99)")
        SuratNumber16 = 16, _("An-Naḥl (128)")
        SuratNumber17 = 19, _("Al-Isrā' (111)")
        SuratNumber18 = 18, _("Al-Kahf (110)")
        SuratNumber19 = 17, _("Maryam (98)")
        SuratNumber20 = 20, _("Ṭāhā (135)")
        SuratNumber21 = 21, _("Al-Anbiyā' (112)")
        SuratNumber22 = 22, _("Al-Ḥajj (78)")
        SuratNumber23 = 23, _("Al-Mu'minūn (118)")
        SuratNumber24 = 24, _("An-Nūr (64)")
        SuratNumber25 = 25, _("Al-Furqān (77)")
        SuratNumber26 = 26, _("Asy-Syu'arā' (227)")
        SuratNumber27 = 27, _("An-Naml (93)")
        SuratNumber28 = 28, _("Al-Qaṣaṣ (88)")
        SuratNumber29 = 29, _("Al-'Ankabūt (69)")
        SuratNumber30 = 30, _("Ar-Rūm (60)")
        SuratNumber31 = 31, _("Luqmān (34)")
        SuratNumber32 = 32, _("As-Sajdah (30)")
        SuratNumber33 = 33, _("Al-Aḥzāb (73)")
        SuratNumber34 = 34, _("Saba' (54)")
        SuratNumber35 = 35, _("Fāṭir (45)")
        SuratNumber36 = 36, _("Yāsīn (83)")
        SuratNumber37 = 37, _("Aṣ-Ṣāffāt (182)")
        SuratNumber38 = 38, _("Ṣād (88)")
        SuratNumber39 = 39, _("Az-Zumar (75)")
        SuratNumber40 = 40, _("Gāfir (85)")
        SuratNumber41 = 41, _("Fuṣṣilat (54)")
        SuratNumber42 = 42, _("Asy-Syūrā (53)")
        SuratNumber43 = 43, _("Az-Zukhruf (89)")
        SuratNumber44 = 44, _("Ad-Dukhān (59)")
        SuratNumber45 = 45, _("Al-Jāṡiyah (37)")
        SuratNumber46 = 46, _("Al-Aḥqāf (35)")
        SuratNumber47 = 47, _("Muḥammad (38)")
        SuratNumber48 = 48, _("Al-Fatḥ (29)")
        SuratNumber49 = 49, _("Al-Ḥujurāt (18)")
        SuratNumber50 = 50, _("Qāf (45)")
        SuratNumber51 = 51, _("Aż-Żāriyāt (60)")
        SuratNumber52 = 52, _("At-Ṭūr (49)")
        SuratNumber53 = 53, _("An-Najm (62)")
        SuratNumber54 = 54, _("Al-Qamar (55)")
        SuratNumber55 = 55, _("Ar-Raḥmān (78)")
        SuratNumber56 = 56, _("Al-Wāqi'ah (96)")
        SuratNumber57 = 57, _("Al-Ḥadīd (29)")
        SuratNumber58 = 58, _("Al-Mujādalah (22)")
        SuratNumber59 = 59, _("Al-Ḥasyr (24)")
        SuratNumber60 = 60, _("Al-Mumtaḥanah (13)")
        SuratNumber61 = 61, _("Aṣ-Ṣaff (14)")
        SuratNumber62 = 62, _("Al-Jumu'ah (11)")
        SuratNumber63 = 63, _("Al-Munāfiqūn (11)")
        SuratNumber64 = 64, _("At-Tagābun (18)")
        SuratNumber65 = 65, _("At-Talāq (12)")
        SuratNumber66 = 66, _("At-Taḥrīm (12)")
        SuratNumber67 = 67, _("Al-Mulk (30)")
        SuratNumber68 = 68, _("Al-Qalam (52)")
        SuratNumber69 = 69, _("Al-Ḥāqqah (52)")
        SuratNumber70 = 70, _("Al-Ma'ārij (44)")
        SuratNumber71 = 71, _("Nūḥ (28)")
        SuratNumber72 = 72, _("Al-Jinn (28)")
        SuratNumber73 = 73, _("Al-Muzzammil (20)")
        SuratNumber74 = 74, _("Al-Muddaṡṡir (56)")
        SuratNumber75 = 75, _("Al-Qiyāmah (40)")
        SuratNumber76 = 76, _("Al-Insān (31)")
        SuratNumber77 = 77, _("Al-Mursalāt (50)")
        SuratNumber78 = 78, _("An-Naba' (40)")
        SuratNumber79 = 79, _("An-Nāzi'āt (46)")
        SuratNumber80 = 80, _("'Abasa (42)")
        SuratNumber81 = 81, _("At-Takwīr (29)")
        SuratNumber82 = 82, _("Al-Infiṭār (19)")
        SuratNumber83 = 83, _("Al-Muṭaffifīn (36)")
        SuratNumber84 = 84, _("Al-Insyiqāq (25)")
        SuratNumber85 = 85, _("Al-Burūj (22)")
        SuratNumber86 = 86, _("At-Ṭāriq (17)")
        SuratNumber87 = 87, _("Al-A'lā (19)")
        SuratNumber88 = 88, _("Al-Gāsyiyah (26)")
        SuratNumber89 = 89, _("Al-Fajr (30)")
        SuratNumber90 = 90, _("Al-Balad (20)")
        SuratNumber91 = 91, _("Asy-Syams (15)")
        SuratNumber92 = 92, _("Al-Lail (21)")
        SuratNumber93 = 93, _("Ad-Duḥā (11)")
        SuratNumber94 = 94, _("Asy-Syarḥ (8)")
        SuratNumber95 = 95, _("At-Tīn (8)")
        SuratNumber96 = 96, _("Al-'Alaq (19)")
        SuratNumber97 = 97, _("Al-Qadr (5)")
        SuratNumber98 = 98, _("Al-Bayyinah (8)")
        SuratNumber99 = 99, _("Az-Zalzalah (8)")
        SuratNumber100 = 100, _("Al-'Adiyāt (11)")
        SuratNumber101 = 101, _("Al-Qāri'ah (11)")
        SuratNumber102 = 102, _("At-Takāṡur (8)")
        SuratNumber103 = 103, _("Al-'Aṣr (3)")
        SuratNumber104 = 104, _("Al-Humazah (9)")
        SuratNumber105 = 105, _("Al-Fīl (5)")
        SuratNumber106 = 106, _("Quraisy (4)")
        SuratNumber107 = 107, _("Al-Mā'ūn (7)")
        SuratNumber108 = 108, _("Al-Kauṡar (3)")
        SuratNumber109 = 109, _("Al-Kāfirūn (6)")
        SuratNumber110 = 110, _("An-Naṣr (3)")
        SuratNumber111 = 111, _("Al-Lahab (5)")
        SuratNumber112 = 112, _("Al-Ikhlāṣ (4)")
        SuratNumber113 = 113, _("Al-Falaq (5)")
        SuratNumber114 = 114, _("An-Nās (6)")

    surat = models.PositiveIntegerField(choices=SuratSurat.choices)
    ayat = models.IntegerField()
    text = models.TextField()

    def __str__(self):
        return f"{self.surat}:{self.ayat}"

    class Meta:
        ordering = ["surat", "ayat"]
        verbose_name_plural = "Qur'an"


class TranslationVersion(models.Model):
    version = models.CharField(max_length=100)

    def __str__(self):
        return self.version

    class Meta:
        ordering = ["version"]
        verbose_name_plural = "Translation Versions"


class Translation(models.Model):
    quran = models.ForeignKey(Quran, on_delete=models.CASCADE)
    translation_version = models.ForeignKey(
        TranslationVersion, on_delete=models.CASCADE
    )
    translation = models.TextField()

    def __str__(self):
        return f"{self.quran}, {self.translation_version}"

    class Meta:
        ordering = ["quran", "translation_version"]
        verbose_name_plural = "Translations"
