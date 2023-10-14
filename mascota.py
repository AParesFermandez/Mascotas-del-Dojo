import random
class Mascota:
    def __init__(self, nombre, tipo, habilidades, ruido):
        self.nombre = nombre
        self.tipo = tipo
        self.habilidades = habilidades
        self.salud = 100
        self.energia = 50
        self.ruido = ruido
    def dormir(self):
        print("la energia de tu mascota esta en : " + str(self.energia))
        self.energia += 25
        print("luego de la reparppadora siesta su energia es de : " + str(self.energia))
        return self
    def comer(self):
        print("la energia de tu mascota esta en : " + str(self.energia) + "y su salud en : " + str(self.salud))
        self.energia += 5
        self.salud += 10
        print("luego de alimentarse su energia es de : " + str(self.energia) + "y su salud de :" + str(self.salud))
        return self
    def jugar(self):
        print("tu mascota esta desanimada su salud es de : " + str(self.salud))
        self.salud += 5
        self.energia -=5
        print("luego de unos mimitos y juegos su salud es de : " + str(self.salud))
        return self
    def sonido(self):
        sonidito_random = random.choice(self.ruido)
        print(sonidito_random)

mis_habilidades = ['impaktrueno', 'placaje', 'salpicadura']
ruiditos = ['grrrr', 'miaaauuu', 'waf', 'sido Chesto']
mitens = Mascota("mittens", "trueno", mis_habilidades, ruiditos)
