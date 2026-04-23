class animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def emitir_som(self):
        return "O animal emitiu um som generico"
        
class Cachorro(animal):
    def emitir_som(self):
        return "O cão latiu"

class Gato(animal):
    def emitir_som(self):
        return "O gato miou"
    
animais = [Cachorro("Max", 2), Gato("Frisk", 3)]

for animal in animais:
     print(animal.emitir_som())