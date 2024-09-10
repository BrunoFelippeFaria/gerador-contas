import string
import json
import random
from os.path import exists

class Main:
    def __init__(self):
        #arquivos
        self.arqContas = "contas.json"
        self.arqlistaNomes = "listaNomes.json"
        
        self.contas = self.carregarListaContas()

        with open(self.arqlistaNomes, "r") as arq:
            lista = json.load(arq)
            self.nomes = lista["nomes"]
            self.sobreNomes = lista["sobreNomes"]

        self.criarConta()

    #salva as contas em um arquivo json    
    def salvarListaContas(self, contas):
        with open(self.arqContas, "w") as arq:
            json.dump(contas, arq, indent=4)

    #carrega as contas de um arquivo json
    def carregarListaContas(self):
        if exists(self.arqContas):
            with open(self.arqContas, "r") as arq:
                return json.load(arq)
        else:
            return {
                "contas": []
            }
    
    #cria uma conta e salva ela em um json
    def criarConta(self):
        self.randNome = random.choice(self.nomes)
        self.randSobreNome = random.choice(self.sobreNomes)
        self.randNumero = str(random.randint(100, 999))

        self.nome = self.randNome + self.randSobreNome + self.randNumero
        self.senha = self.gerarSenha()

        self.contas["contas"].append({"usuario": self.nome, "senha": self.senha})

        self.salvarListaContas(self.contas)

    #gera uma senha
    def gerarSenha(self):
        caracteres = string.ascii_letters + string.digits
        senha = ''.join(random.choice(caracteres) for c in range(16))
        return senha
            
if __name__ == "__main__":
    Main()