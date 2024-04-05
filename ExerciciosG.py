nomes_masc = ['Carlos', 'Miguel', 'André', 'Pedro', 'João', 'Rafael', 'Luís', 'Antônio', 'Fernando', 'Gabriel', 'Lucas', 'Bruno', 'Gustavo', 'Daniel', 'Marcos', 'Felipe', 'Leonardo', 'Diego', 'José', 'Ricardo']
nomes_fem = ['Ana', 'Mariana', 'Carla', 'Juliana', 'Fernanda', 'Camila', 'Gabriela', 'Isabela', 'Patrícia', 'Vanessa', 'Amanda', 'Laura', 'Beatriz', 'Renata', 'Tatiana', 'Cristina', 'Raquel', 'Daniela', 'Larissa', 'Natália', 'Marta', 'Sofia', 'Eduarda', 'Letícia', 'Adriana', 'Clara', 'Marina', 'Bianca', 'Priscila', 'Jéssica']
nomes_mistos = []
for nome1 in nomes_masc:
    nomes_mistos.append(nome1)

for nome2 in nomes_fem:
    nomes_mistos.append(nome2)

for nome in nomes_mistos:
    print(nome)


