"""
+ = julkinen
- = yksityinen __
# = suojattu _
[1, 42, 13]
01-042-013
setter ja getter määritelmään jos halutaan suojatuksi jne.
"""

import random

class Asiakas:
    """Luokka asettaa asiakkaalle numeron, nimen, iän ja luo numeron.
    Julkiset methodit
        set_nimi()
        set_ika()
        get_nimi()
        get_ika()
        get_asiakasnumero()
    """
    def __init__(self, nimi, ika):
        """Konstruktorissa annetaan muuttujat, jotka peritään myöhemmin.
        :ivar asiakasnumero: asiakkaan puhelin numero
        :type asiakasnumero: int[]
        :ivar nimi: asiakkaan nimi
        :type nimi: str
        :ivar ika: asiakkaan ikä
        :type ika: int
        """
        self.__asiakasnumero = self.__luo_nro()
        self.__nimi = nimi
        self.__ika = ika
        
    def __luo_nro(self):
        """Satunnaisesti arvoo asiakkaan puhelinnumeron.
        :ivar numero: lista johon pistetään arvottu puhelinnumero
        :type numero: int[]
        """
        numero = []
        numero.append(random.randint(0, 99))
        numero.append(random.randint(0, 999))
        numero.append(random.randint(0, 999))
        return numero

    def set_nimi(self, nimi):
        """Jos bool on True, se antaa nimen muuttujalle.
        Jos bool on tyhjä se on False, sitten se nostaa virheen ja kysyy nimeä uudestaan.
        :param nimi: asiakkaan nimi
        :type nimi: str
        """
        if bool(nimi):
            self.nimi = nimi
        else:
            raise ValueError('Virhe! Anna nimi uudestaan.')

    def set_ika(self, ika):
        """Jos type on int, se antaa nimen muuttujalle.
        Jos type ei ole int, se on False. Sitten se nostaa virheen ja kysyy nimeä uudestaan.
        :param ika: asiakkaan ikä
        :type ika: int
        """
        if type(ika) is int:
            self.ika = ika
        else:
            raise ValueError('Virhe! Anna ika uudestaan.')
    def get_nimi(self):
        """Palautetaan __nimi kun sitä kutsutaan.
        """
        return self.__nimi

    def get_ika(self):
        """Sama kuin get_nimi(), mutta annetaan ika muuttuja.
        """
        return self.__ika
    
    def get_asiakasnumero(self):
        """Palauttaa asiakasnumeron kun sitä kutsutaan.
        """
        return f'{self.__asiakasnumero[0]:02}-{self.__asiakasnumero[1]:03}-{self.__asiakasnumero[2]:03}'


class Palvelu:
    """Luokalla hallitaan asiakas listaa.
    Julkiset methodit
        lisaa_asiakas()
        poista_asiakas()
        get_tuotenimi()
        tulosta_asiakkaat()
    """
    def __init__(self, tuotenimi):
        """Konstruktori pistetään lista, jota käytetään muissa määritelmissä.
        :ivar __asiakkaat: 
        :type __asiakkaat: dict
        :ivar tuotenimi:
        :type tuotenimi: str
        """
        self.tuotenimi = tuotenimi
        self.__asiakkaat = []

    def lisaa_asiakas(self, asiakas):
        """Liittää nimen ja iän asiakas listaan.
        """
        self.__asiakkaat.append(asiakas)

    def poista_asiakas(self, asiakas):
        """
        """
        self.__asiakkaat.remove(asiakas)

    def _luo_asiakasrivi(self, asiakas):
        return f'   {Asiakas.get_nimi(asiakas)} ({Asiakas.get_asiakasnumero(asiakas)}) on {Asiakas.get_ika(asiakas)} vuotias.'

    def get_tuotenimi(self):
        return self.tuotenimi
    
    def tulosta_asiakkaat(self):
        """Tulostaa lopulta asiakkaan tiedot.
        """
        print("Tuotteen " + self.tuotenimi + " asiakkaat ovat")
        for asiakas in self.__asiakkaat:
            print(self._luo_asiakasrivi(asiakas))


class ParempiPalvelu(Palvelu):
    def __init__(self, tuotenimi):
        super().__init__(tuotenimi)
        self.__edut = []
    
    def lisaa_etu(self, etu):
        self.__edut.append(etu)

    def poista_etu(self, etu):
        try:
            self.__edut.remove(etu)
        except:
            pass

    def tulosta_edut(self):
        print("Tuotteen " + super().get_tuotenimi() + " edut ovat:")
        for etu in self.__edut:
            print(f'   {etu}')
