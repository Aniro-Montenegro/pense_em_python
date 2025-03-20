class Pessoa:
    def __init__(self,nome,idade,cor,cicatrizes,olhos,rg,sexo):
        self.nome=nome
        self.idade=idade
        self.cor=cor
        self.cicatrizes=cicatrizes
        self.olhos=olhos
        self.rg=rg
        self.sexo=sexo
    def __repr__(self):
        return f"Estrangeiro(nome={self.nome}, idade={self.idade}, cor={self.cor}, cicatrizes={self.cicatrizes}, olhos={self.olhos}, rg={self.rg}, sexo={self.sexo})"


class Estrangeiro(Pessoa):
    def __init__(self, nome, idade, cor, cicatrizes, olhos, rg, sexo,documento):
        super().__init__(nome, idade, cor, cicatrizes, olhos, rg, sexo)
        self.documento=documento
    def __repr__(self):
        return f"Estrangeiro(nome={self.nome}, idade={self.idade}, cor={self.cor}, cicatrizes={self.cicatrizes}, olhos={self.olhos}, rg={self.rg}, sexo={self.sexo}, documento={self.documento})"


pessoas = [
    Estrangeiro("John Smith", 40, "branco", ["caveira", "palhaço"], "castanhos", 7879797, "m", "PASS123"),
    Estrangeiro("Maria Gonzalez", 35, "branco", [], "azuis", 5452635, "f", "PASS456"),
    Estrangeiro("Carlos Fernandez", 29, "negro", ["braço esquerdo"], "verdes", 456789123, "m", "PASS789"),
    Estrangeiro("Ana Lopez", 42, "branco", [], "castanhos", 321654987, "f", "PASS101"),
    Estrangeiro("Pedro Ramirez", 27, "branco", ["perna direita"], "azuis", 654987321, "m", "PASS202"),
    Estrangeiro("Luisa Martinez", 38, "negro", [], "verdes", 789123456, "f", "PASS303"),
    Estrangeiro("Miguel Torres", 50, "branco", ["costas"], "castanhos", 159753468, "m", "PASS404"),
    Estrangeiro("Sofia Ruiz", 31, "negro", [], "azuis", 357951468, "f", "PASS505"),
    Estrangeiro("Javier Morales", 45, "branco", ["rosto"], "verdes", 158369147, "m", "PASS606"),
    Estrangeiro("Elena Castro", 33, "pardo", [], "castanhos", 753159486, "f", "PASS707"),
    Pessoa("Joao da Silva", 45, "branco", ["caveira", "palhaço"], "castanhos", 4585485589, "m"),
    Pessoa("Maria Oliveira", 34, "branco", [], "azuis", 1234567890, "f"),
    Pessoa("Carlos Souza", 28, "pardo", ["braço esquerdo"], "verdes", 9876543210, "m"),
    Pessoa("Ana Costa", 50, "negro", [], "castanhos", 4567891230, "f"),
    Pessoa("Pedro Santos", 22, "branco", ["perna direita"], "azuis", 3216549870, "m"),
    Pessoa("Julia Pereira", 39, "negro", [], "verdes", 6549873210, "f"),
    Pessoa("Lucas Fernandes", 55, "branco", ["costas"], "castanhos", 7891234560, "m"),
    Pessoa("Fernanda Lima", 27, "branco", [], "azuis", 1597534680, "f"),
    Pessoa("Marcos Rocha", 33, "negro", ["rosto"], "verdes", 3579514680, "m"),
    Pessoa("Isabela Martins", 41, "branco", [], "castanhos", 2513691470, "f"),
    Pessoa("Rafael Gonçalves", 29, "negro", ["torso"], "azuis", 7531594860, "m"),
    Pessoa("Camila Almeida", 36, "branco", [], "verdes", 9517538520, "f"),
    Pessoa("Gustavo Barbosa", 48, "branco", ["mão direita"], "castanhos", 3692581470, "m"),
    Pessoa("Patricia Ribeiro", 31, "branco", [], "azuis", 1472584374690, "f"),
    Pessoa("Daniel Carvalho", 25, "pardo", ["ombro esquerdo"], "verdes", 2581473690, "m"),
    Pessoa("Amanda Dias", 43, "branco", [], "castanhos", 3691472580, "f"),
    Pessoa("Bruno Lopes", 37, "branco", ["coxa direita"], "azuis", 1473692580, "m"),
    Pessoa("Tatiane Castro", 26, "branco", [], "verdes", 2583741470, "f"),
    Pessoa("Eduardo Nunes", 52, "pardo", ["pescoço"], "castanhos", 3691472580, "m"),
    Pessoa("Vanessa Correia", 30, "branco", [], "azuis", 1477583690, "f")
]


def busca(informacao):
    lista=[]
    for inf in pessoas:
        if informacao.lower() in inf.nome.lower() or informacao.lower() in inf.cor.lower() or informacao.lower() in inf.cicatrizes or informacao.lower() in inf.olhos.lower() or informacao in str(inf.rg) or (type(inf)==Estrangeiro and informacao in str(inf.documento)) or informacao in str(inf.rg) or informacao in str(inf.idade):
            lista.append(inf)
    

    for l in lista:
        print(l)

v=0

while(v!=-1):
    v=input()
    busca(v)
