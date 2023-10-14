import mascota
class Ninja:
    def __init__(self, nombre, apellido, mascota, premios, comida_mascota):
        self.nombre = nombre
        self.apellido = apellido
        self.mascota = mascota
        self.premios = premios
        self.comida_mascota = comida_mascota
#uso el pass para poder darle diseño al programa y que se mantenga identado, luego le doy la logica real
    def caminar(self):
        self.mascota.jugar()
        return self
    def alimentar(self):
        if len(self.comida_mascota) > 0:
            comida = self.comida_mascota.pop()
            print(f"{self.mascota.nombre} a recibido {comida} parece encantarle!")
            self.mascota.comer()
        else:
            print("te has quedado sin comida :C ve a comprar mas")
        return self
    def bañar(self):
        print("era necesario un buen baño")
        self.mascota.sonido()

mis_premios = ['pelota','sombrero', 'premio_sorpresa']
mi_comida_mascota = ['pizza','hamburguesa','pastelito','completo']

ninjaOcre = Ninja("ninja", "Ocre", mascota.mitens, mis_premios, mi_comida_mascota)
ninjaOcre.caminar()
ninjaOcre.alimentar()
ninjaOcre.alimentar()
ninjaOcre.bañar()
