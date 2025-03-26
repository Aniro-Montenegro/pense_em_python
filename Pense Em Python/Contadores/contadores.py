
from collections import Counter

artistas = [
    "Leo Brouwer", "Astor Piazzolla", "Roland Dyens", "Heitor Villa-Lobos",
    "Francisco Tárrega", "Django Reinhardt", "Narciso Yepes",
    "Ida Presti", "Alexandre Lagoya", "Maria Linnemann", "Vladimir Mikulka",
    "Stephan Schmidt", "Paul Galbraith", "David Tanenbaum", "Benjamin Verdery",
    "William Kanengiser", "Sharon Wayne", "Andrew York", "Christopher Parkening",
    "Ana Caram", "Egberto Gismonti", "Yamandu Costa", "Paulinho Nogueira","Julian Bream",
    "Toquinho", "Antonio Carlos Jobim"
    "Fernando Sor", 
  
    "Andrés Segovia",    # 5x
    "Andrés Segovia",
    "Andrés Segovia",    
    "John Williams",     # 4x
    "John Williams",
    
    "Paco de Lucía",     # 3x
    "Paco de Lucía",
    "Paco de Lucía",
    "Julian Bream",      # 3x
    
    "Julian Bream",
    "Ana Vidović",       # 2x
    "Ana Vidović",
    "Marcin Dylla",      # 2x
    "Marcin Dylla",
    "Ralph Fiennes",     # 2x (ator)
    "Ralph Fiennes",
    "Meryl Streep",      # 2x (atriz)
    "Meryl Streep",
    "Andrés Segovia",
    "Andrés Segovia",
    "David Russell",     # 2x
    "David Russell", 
    "Manuel Barrueco", "Sharon Isbin", "Jason Vieaux", "Eliot Fisk",
    "Raphaella Smits", "Zoran Dukić", "Antigoni Goni", "Xuefei Yang",
    "Fabio Zanon", "Graham Anthony Devine", "Denis Azabagić", "Judicaël Perroy",
    "Scott Tennant", "Kaori Muraji", "Marco Tamayo", "Alvaro Pierri",
    "Carlo Marchione", "John Williams",
    "John Williams","Ricardo Gallén", "Margarita Escarpa", "Andrea Dieci",
    "Oscar Ghiglia", "Pepe Romero",    
    "Pepe Romero","Aniello Desiderio", "Matteo Mela", "Lorenzo Micheli",
    
]

count=Counter(artistas)
for valor, frequencia in count.most_common(60):
    print(valor,frequencia)