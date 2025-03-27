import random

marcas_roupas = [
    "Balenciaga", "Chanel", "Dior", "Fendi", "Chanel", 
    "Saint Laurent", "Givenchy", "Gucci", "Hermès", "Valentino",
    "Chanel", "Dolce & Gabbana", "Armani", "Gucci", "Burberry",
    "Calvin Klein", "Chanel", "Tom Ford", "Gucci", "Ralph Lauren",
    "Alexander McQueen", "Versace", "Balmain", "Chanel", "Stella McCartney",
    "Off-White", "Versace", "Vivienne Westwood", "Gucci", "Issey Miyake",
    "Comme des Garçons", "Prada", "Kenzo", "Versace", "Yves Saint Laurent",
    "Moschino", "Prada", "Miu Miu", "Bottega Veneta", "Louis Vuitton",
    "Ferragamo", "Zara", "Louis Vuitton", "H&M", "Uniqlo",
    "Gap", "Adidas", "Nike", "Puma", "Levi's",
    "Ferragamo", "Zara", "Louis Vuitton", "H&M", "Uniqlo",
    "Gap", "Adidas", "Nike", "Puma", "Levi's",
    "Ferragamo", "Zara", "Louis Vuitton", "H&M", "Uniqlo",
    "Gap", "Adidas", "Nike", "Puma", "Levi's",
    "Ferragamo", "Zara", "Louis Vuitton", "H&M", "Uniqlo",
    "Ferragamo", "Zara", "Louis Vuitton", "H&M", "Uniqlo",
    "Gap", "Adidas", "Nike", "Puma", "Levi's",
    "Ferragamo", "Zara", "Louis Vuitton", "H&M", "Uniqlo",
    "Ferragamo", "Zara", "Louis Vuitton", "H&M", "Uniqlo",
    "Gap", "Adidas", "Nike", "Puma", "Levi's",
    "Ferragamo", "Zara", "Louis Vuitton", "H&M", "Uniqlo",
    "Ferragamo", "Zara", "Louis Vuitton", "H&M", "Uniqlo",
    "Gap", "Adidas", "Nike", "Puma", "Levi's",
    "Ferragamo", "Zara", "Louis Vuitton", "H&M", "Uniqlo",
    "Ferragamo", "Zara", "Louis Vuitton", "H&M", "Uniqlo",
    "Gap", "Adidas", "Nike", "Puma", "Levi's",
    "Ferragamo", "Zara", "Louis Vuitton", "H&M", "Uniqlo",
    "Off-White", "Versace", "Vivienne Westwood", "Gucci", "Issey Miyake",
    "Comme des Garçons", "Prada", "Kenzo", "Versace", "Yves Saint Laurent",
    "Moschino", "Prada", "Miu Miu", "Bottega Veneta", "Louis Vuitton",
    "Ferragamo", "Zara", "Louis Vuitton", "H&M", "Uniqlo",
    "Off-White", "Versace", "Vivienne Westwood", "Gucci", "Issey Miyake",
    "Comme des Garçons", "Prada", "Kenzo", "Versace", "Yves Saint Laurent",
    "Moschino", "Prada", "Miu Miu", "Bottega Veneta", "Louis Vuitton",
    "Ferragamo", "Zara", "Louis Vuitton", "H&M", "Uniqlo",
    "Off-White", "Versace", "Vivienne Westwood", "Gucci", "Issey Miyake",
    "Comme des Garçons", "Prada", "Kenzo", "Versace", "Yves Saint Laurent",
    "Moschino", "Prada", "Miu Miu", "Bottega Veneta", "Louis Vuitton",
    "Ferragamo", "Zara", "Louis Vuitton", "H&M", "Uniqlo",
    "Off-White", "Versace", "Vivienne Westwood", "Gucci", "Issey Miyake",
    "Comme des Garçons", "Prada", "Kenzo", "Versace", "Yves Saint Laurent",
    "Moschino", "Prada", "Miu Miu", "Bottega Veneta", "Louis Vuitton",
    "Ferragamo", "Zara", "Louis Vuitton", "H&M", "Uniqlo",
    "Off-White", "Versace", "Vivienne Westwood", "Gucci", "Issey Miyake",
    "Comme des Garçons", "Prada", "Kenzo", "Versace", "Yves Saint Laurent",
    "Moschino", "Prada", "Miu Miu", "Bottega Veneta", "Louis Vuitton",
    "Ferragamo", "Zara", "Louis Vuitton", "H&M", "Uniqlo",
    
    
]

dicionario=dict()

for m in marcas_roupas:
    dicionario[m] = dicionario.setdefault(m, 0) + 1

for chave in dicionario.keys():
    print(chave," : ",dicionario[chave])
