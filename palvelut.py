"""
+ = julkinen
- = yksityinen
# = suojattu
[1, 42, 13]
01-042-013
setter ja getter määritelmään jos halutaan suojatuksi jne.
"""

import random

class Asiakas:
    """Luokka asettaa asiakkaalle numeron, nimen, iän ja luo numeron
    Julkiset methodit:
    """
    def __init__(self, nimi, ika):
        self.asiakasnumero = self.luo_nro()
        self.nimi = nimi
        self.ika = ika
        
    def luo_nro(self):
        numero =[]
        numero.append(random.randint(0, 99))
        numero.append(random.randint(0, 999))
        numero.append(random.randint(0, 999))
        return numero

    def set_nimi(self, nimi):
        if bool(nimi):
            self.nimi = nimi
        else:
            raise ValueError('Virhe! Anna nimi uudestaan.')

    def set_ika(self, ika):
        if type(ika) is int:
            self.ika = ika
        else:
            raise ValueError('Virhe! Anna ika uudestaan.')
    def get_nimi(self):
        return self.nimi

    def get_ika(self):
        return self.ika
    
    def get_asiakasnumero(self):
        return f'{self.asiakasnumero[0]:02}-{self.asiakasnumero[1]:03}-{self.asiakasnumero[2]:03}'


class Palvelu:
    def __init__(self, tuotenimi):
        self.tuotenimi = tuotenimi
        self.__asiakkaat = []

    def lisaa_asiakas(self, asiakas):
        self.__asiakkaat.append(asiakas)

    def poista_asiakas(self, asiakas):
        self.__asiakkaat.remove(asiakas)

    def luo_asiakasrivi(self, asiakas):
        return f'   {Asiakas.get_nimi(asiakas)} ({Asiakas.get_asiakasnumero(asiakas)}) on {Asiakas.get_ika(asiakas)} vuotias.'

    def get_tuotenimi(self):
        return self.tuotenimi

    def tulosta_asiakkaat(self):
        print("Tuotteen " + self.tuotenimi + " asiakkaat ovat")
        for asiakas in self.__asiakkaat:
            print(self.luo_asiakasrivi(asiakas))

class ParempiPalvelu(Palvelu):
    def __init__(self, tuotenimi):
        super().__init__(tuotenimi)
        self.__edut =[]
    
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
