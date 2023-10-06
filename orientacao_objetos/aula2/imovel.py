class Imovel:
  def __init__(self, nome, uf, valor, endereco = "", area = ""):
    self.nome = nome
    self.uf = uf
    self.valor = valor
    self.endereco = endereco
    self.area = area

  def detalhar(self):
    print(self.__dict__)

  def calcularImposto(self):
    return self.valor * 0.02
  
class ImovelResidencial(Imovel):
  def __init__(self, nome, uf, valor, endereco = "", area = ""):
    super().__init__(nome, uf, valor, endereco = "", area = "")
    self.quartos = 0
    self.piscina = False

class ImovelComercial(Imovel):
  ...

casa = ImovelResidencial("Meu Lar", "AM", 400000)
casa.detalhar()

clinica = ImovelComercial("Clinica Odôntologica", "SP", 700000)
# clinica.detalhar()

'''
imovel = Imovel("Mundo Amazônico", "AM", 500000)
imovel.endereco = "ABC"
imovel.area = "2000"
imovel.detalhar()
'''