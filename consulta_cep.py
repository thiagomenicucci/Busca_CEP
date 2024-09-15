import requests

cep = input("Digite o CEP: ")

url = f'https://viacep.com.br/ws/{cep}/json/'

response = requests.get(url)

while len(cep) == 8 and response.status_code == 200:
    dados = response.json()
    print("Endereço: {}, {}, {}, {}".format(dados['logradouro'], dados['bairro'], dados['localidade'], dados['uf']))
    break
else:
    print("CEP inválido!")
    print("Erro na requisição. Código de status: {}".format(response.status_code))