"""
+ = julkinen
- = yksityinen
# = suojattu
[1, 42, 13]
01-042-013
setter ja getter määritelmään jos halutaan suojatuksi jne.
"""

import random

class Palvelu:
    def __init__(self, tuotenimi):
        self.tuotenimi = tuotenimi
        
    Asiakas = []

class ParempiPalvelu(Palvelu):
    def __init__(self, tuotenimi):
        super().__init__(tuotenimi)

    edut =[]
    
    def lisaa_etu(self, etu):
        pass
    
    def tulosta_edut(self):
        pass

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
        self.nimi = nimi
        if nimi == False:
            raise ValueError:
                print("Virhe! Anna nimi uudestaan.")
        if nimi == True:
            self.__nimi = nimi
            
    def set_ika(self, ika):
        self.ika = ika
        
        if ika == False:
            raise ValueError:
                print("Virhe! Anna ikä uudestaan.")
        if ika == True:
            self.__ika = ika
            
    def get_nimi(self):
        return self.nimi

    def get_ika(self):
        return self.ika
    
    def get_asiakasnumero(self):
        return self.asiakasnumero
