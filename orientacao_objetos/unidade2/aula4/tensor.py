import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1'

class Produto:
  def __init__(self, nome, preco, categoria):
    self.nome = nome
    self.preco = preco
    self.categoria = categoria

produtos = [
  Produto('Camiseta', 29.99, 'Roupas'),
  Produto('Calça Jeans', 79.99, 'Roupas'),
  Produto('Tênis', 99.99, 'Calçados'),
  Produto('Celular', 1499, 'Eletrônico'),
  Produto('Notebook', 3499, 'Eletrônico'),
  Produto('Livro', 19.99, 'Livros'),
]

nomes = tf.constant([p.nome for p in produtos])
precos = tf.constant([p.preco for p in produtos])
categorias = tf.constant([p.categoria for p in produtos])

media = tf.reduce_mean(precos)
eletronicos = tf.boolean_mask(nomes, tf.equal(categorias, 'Eletrônico'))

print(media)
print(eletronicos)