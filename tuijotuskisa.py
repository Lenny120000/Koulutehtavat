import random
import time

class Olento:
    """Luokka jota Peikko ja Sankari perii.
    """
    def __init__(self, rohkeus, katseen_voima):
        """Peritään rohkeus ja katseen_voima, jotka arvotaan joka kerta.
        :ivar katseen_voima: peikon katseen voima, arvotaan
        :type katseen_voima: int
        :ivar rohkeus: peikon rohkeus, arvotaan
        :type rohkeus: int
        """
        self.rohkeus = random.randint(4, 12)
        self.katseen_voima = random.randint(2, 7)



class Peikko(Olento):
    """Luokka, joka kuvaa Peikon.
    Julkiset metodit
        arvo_hurraus()
    """

    NIMITAVUT = ("Ur", "Gar", "Grah", "Gur", "Kan", "Kazah", "Bar", "Bazh", "Ragh", "Rudz")
    RIEMUTAVUT = ("Agh", "Ugh", "Ourgh", "Drar", "Brar", "Dza", "Gra", "Gur", "Rah", "Urgh", "Ra")

    def __init__(self, rohkeus, katseen_voima):
        """Konstruktori.
        Perii Olennolta satunnaisesti laskettu katseen_voima ja rohkeus.
        :ivar nimi: Peikon nimi, arvotaan _arvo_sanat().
        :type nimi: str
        """
        self.nimi = self._arvo_sanat(self.NIMITAVUT, 3, "-")
        super().__init__(rohkeus, katseen_voima)
        

    def _arvo_sanat(self, tavut, n, erotin, p=0.5):
        """Muodostaa satunnaisen tekstin annetuista tavuista.
        :param tavut: ne tavut, joita palautettava teksti voi sisältää
        :type tavut: Union[list[str], tuple[str]]
        :param n: mukaan poimittavien tavujen maksimimäärä
        :type n: int
        :param erotin: tavujen väliin satunnaisesti laitettava merkki
        :type erotin: str
        :param p: todennäköisyys lisätä erotin tavujen väliin (oletus 0.5)
        :type p: float
        :return: satunnainen teksti
        :rtype: str
        """
        osat = random.choices(tavut, k=random.randint(2, n))
        sanat = osat[0]
        for osa in osat[1:]:
            if random.random() < p:
                sanat += erotin + osa
            else:
                sanat += osa.lower()
        return sanat

    def arvo_hurraus(self):
        """Palauttaa satunnaisen hurraushuudahduksen.
        :return: hurraava huudahdus
        :rtype: str
        """
        return self._arvo_sanat(self.RIEMUTAVUT, 8, " ", 0.7)

class Vuorenpeikko(Peikko):
    """Luokka joka kuvaa Vuorenpeikon.
    Perii Peikolta lähes kaiken koodin.
    Nimet ja riemut ovat erilaiset.
    """
    NIMITAVUT = ("Dagoth", "UR", "Nerevar", "Dor", "Khan", "Baa", "Daa", "Saa", "Raa", "Taa")
    RIEMUTAVUT = ("Come here", "Aaaa", "Easy", "GRAAAAAAAAAAAA", "TREAAghh", "raaaa", "Mummolaan", "poaaaaaaa", "Guh wuh", "sleep", "done")
    
    def _init_(self):
        """Vuorenpeikko perii init Peikolta.
        Annetaan eri rohkeus ja katseen_voima.
        """
        super().__init__(self, super.arvo_sanat(self, self.NIMITAVUT, 3, "-"), random.randint(4, 8), random.randint(2, 4))
        
class Luolapeikko(Peikko):
    """Luokka joka kuvaa Luolapeikon.
    Perii Peikolta lähes kaiken koodin.
    Nimet ja riemut ovat erilaiset.
    """
    NIMITAVUT = ("DAA", "BBRR", "NAAA", "DDDD", "AAAAAR", "DRAV", "RTAAT", "YTA", "RHA", "TRTA")
    RIEMUTAVUT = ("OOOK", "AAAA", "WAAAAAAAAAA", "HAAAAAAAAA", "TAH", "REAAAW", "EWAN", "FARR", "GUH", "SLUH", "DURN")
    
    def _init_(self):
        """Luolapeikko perii init Peikolta.
        Annetaan eri rohkeus ja katseen_voima.
        """
        super().__init__(self, super.arvo_sanat(self, self.NIMITAVUT, 3, "-"), random.randint(6, 10), random.randint(4, 6))


### Kirjoita luokka Sankari tähän.
class Sankari(Olento):
    """Parametrina nimi.
        
    Luokka kuvaa sankarin
        
    :ivar nimi: sankarin nimi, arvotaan
    :type nimi: str
    Julkiset metodit
    arvo_hurraus()
    """
    def __init__(self, nimi, rohkeus, katseen_voima):
        """Peritään rohkeus ja katseen_voima
        """
        self.nimi = nimi
        super().__init__(rohkeus, katseen_voima)

    def arvo_hurraus(self):
        """Metodi arvo_hurraus antaa satunnaisen HURRAUKSET listasta ja palauttaa sen.
        """
        HURRAUKSET = ["FRAAAG!!!", "TAKE THIS!", "MUST FRAG!", "SIR YES SIR OORAH!", "RAAAGH!!"]
        return random.choice(HURRAUKSET)


def hurraa(olio):
    """Tulostaa satunnaisen hurrauksen annetulle oliolle.
    :param olio: hurraava olio
    """
    print('%s: "%s!"' % (olio.nimi, olio.arvo_hurraus()))


def tulosta_rapaytys(rapayttaja):
    """Tulostaa sopivan tekstin räpäyttävälle oliolle.
    :param rapayttaja: silmiään räpäyttävä olio
    """
    if rapayttaja:
        if rapayttaja.rohkeus > 0:
            print("ja %s räpäyttää!" % rapayttaja.nimi)
        else:
            print("ja %s karkaa!" % rapayttaja.nimi)
    else:
        print("eikä kummankaan silmä rävähdä!")


def tuijota(olio1, olio2):
    """Asettaa annetut oliot taistelemaan keskenään yhden kierroksen.
    :param vasen: ensimmäinen taisteleva olio
    :type vasen: Union[Sankari, Peikko]
    :param oikea: toinen taisteleva olio
    :type oikea: Union[Sankari, Peikko]
    :return: hävinnyt olio
    :rtype: Union[Sankari, Peikko]
    """
    print("He tuijottavat toisiaan...", end='')
    time.sleep(1)
    # Arvotaan kummankin olion tämän kierroksen vahvuus.
    katse1 = random.randint(0, olio1.katseen_voima)
    katse2 = random.randint(0, olio2.katseen_voima)
    rapayttaja = None

    # heikomman vahvuuden saanut olio menettää rohkeutta
    if katse1 > katse2:
        rapayttaja = olio2
        rapayttaja.rohkeus -= katse1
    elif katse1 < katse2:
        rapayttaja = olio1
        rapayttaja.rohkeus -= katse2
    return rapayttaja


def taistele(vasen, oikea):
    """Asettaa annetut oliot taistelemaan keskenään, kunnes toinen voittaa.
    :param vasen: ensimmäinen taisteleva olio
    :type vasen: Union[Sankari, Peikko]
    :param oikea: toinen taisteleva olio
    :type oikea: Union[Sankari, Peikko]
    :return: voittanut olio
    :rtype: Union[Sankari, Peikko]
    """
    while vasen.rohkeus > 0 and oikea.rohkeus > 0:
        haviaja = tuijota(vasen, oikea)
        tulosta_rapaytys(haviaja)
        time.sleep(0.5)
    if vasen.rohkeus > 0:
        return vasen
    else:
        return oikea


# Kutsutaan nimi, rohkeus ja katseen_voima.
sankari = Sankari(input("Mikä on sankarimme nimi? "), 3, 2)
pelastetut = 0
# Käydään tuijotuskisoja peikkoja vastaan, kunnes sankari karkaa
while sankari.rohkeus > 0:
    # Tulostetaan kierroksen alkutiedot.
    sankarin_tiedot = sankari.nimi + " [" + str(sankari.rohkeus) + "]"
    print("Sankarimme %s kävelee kohti seikkailua." % sankarin_tiedot)
    time.sleep(0.7)

    # Tulostetaan vastaan tulevan peikon tiedot.
    lista = [Peikko(1, 2), Vuorenpeikko(1, 2), Luolapeikko(1, 2)]
    peikko = random.choice(lista)
    peikon_tiedot = peikko.nimi + " [" + str(peikko.rohkeus) + "]"
    print("Vastaan tulee hurja %s!" % peikon_tiedot)
    time.sleep(1)

    # Käydään tuijotuskisa peikkoa vastaan.
    voittaja = taistele(peikko, sankari)
    hurraa(voittaja)
    print()
    time.sleep(1.5)

time.sleep(1.5)
print("%s herää sängystään hikisenä - onneksi se oli vain unta!" % sankari.nimi)
