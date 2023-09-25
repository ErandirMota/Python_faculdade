import json

pessoas = [
  {"nome": "Erandir", "telefone": "(92) 99246-0704", "endereço": "Rua Baronesa"},
  {"nome": "Rebeca", "telefone": "(15) 5690-4509", "endereço": "Rua Visconde"},
  {"nome": "Maria", "telefone": "(11) 5549-2390", "endereço": "Rua Utinga"}
]

with open("pessoas.json", "w") as arquivo:
  json.dump(pessoas, arquivo, indent=4)
