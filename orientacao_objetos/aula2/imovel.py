from abc import ABC, abstractmethod

class Imovel(ABC):
  def __init__(self, nome, uf, valor, endereco = "", area = ""):
    self._nome = nome
    self._uf = uf
    self._valor = valor
    self._endereco = endereco
    self._area = area

  @property
  def uf(self):
    return self._uf
  
  @uf.setter
  def uf(self, uf):
    self._uf = uf

  @property
  def nome(self):
    return self._nome
  
  @nome.setter
  def nome(self, nome):
    self._nome = nome

  '''
  def getNome(self):
    return self.nome
  
  def setNome(self, nome):
    self.nome = nome
'''

  def detalhar(self):
    print(self.__dict__)

  def calcularImposto(self):
    match self._uf:
      case "DF": taxa = 0.03
      case "SP": taxa = 0.04
      case "RJ": taxa = 0.025
      case other: taxa = 2

    return self._valor * taxa
  
  @abstractmethod
  def aluguelSugerido(self):
    ...
  
class ImovelResidencial(Imovel):
  def __init__(self, nome, uf, valor, endereco = "", area = ""):
    super().__init__(nome, uf, valor, endereco = "", area = "")
    self._quartos = 0
    self._piscina = False

  def aluguelSugerido(self):
    return self._valor * 0.01

class ImovelComercial(Imovel):
  
  def aluguelSugerido(self):
    return self._valor * 0.015

class ImovelRural:
  def __init__(self, hectares = "", curral = "", produtiva = True):
    self._hectares = hectares
    self._curral = curral
    self._produtiva = produtiva

  def mesPlantacao(self, mes):
      match int(mes):
        case 1: print("Milho")
        case 2: print("Feijão")
        case 3: print("Soja")
        case other: print("Algodão")

class Fazenda(Imovel, ImovelRural):
  
  def aluguelSugerido(self):
    return self._valor * 0.025

'''
fazenda = Fazenda("Fazenda Modelo", "GO", 1500000)
fazenda.detalhar()
print(fazenda.calcularImposto())
fazenda.mesPlantacao(2)
'''

casa = ImovelResidencial("Meu Lar", "AM", 400000)
casa.nome = "Casa top"
print(casa.nome)
casa.uf = "RJ"
# casa.detalhar()
print(casa.calcularImposto())
# print(casa.aluguelSugerido())

clinica = ImovelComercial("Clinica Odôntologica", "RJ", 700000)
# clinica.detalhar()
print(clinica.calcularImposto())
'''
imovel = Imovel("Mundo Amazônico", "AM", 500000)
imovel.detalhar()
imovel.endereco = "ABC"
imovel.area = "2000"
'''