"""
+ = julkinen
- = yksityinen
# = suojattu
[1, 42, 13]
01-042-013
setter ja getter määritelmään jos halutaan suojatuksi jne.
"""

class Palvelu:
    def __init__(self, tuotenimi):
        asiakkaat = []

class ParempiPalvelu(Palvelu):
    def __init__(self, tuotenimi):
        edut = []

class Asiakas:
    """Luokka asettaa asiakkaalle numeron, nimen, iän ja luo numeron
    Julkiset methodit:
    """
    def __init__(self, nimi, ika):
        
    def luo_nro():

    def set_nimi(self, nimi):
        if nimi == False:
            except ValueError:
                print("Virhe! Anna nimi uudestaan.")
        if nimi == True:
            
    def set_ika(self, ika):
        if nimi == False:
            except ValueError:
                print("Virhe! Anna ikä uudestaan.")
        if nimi == True:
        
    def get_nimi(self, nimi, asiakasnumero):
        return nimi, asiakasnumero
    
    def get_ika(self, ika, asiakasnumero):
        return ika, asiakasnumero
