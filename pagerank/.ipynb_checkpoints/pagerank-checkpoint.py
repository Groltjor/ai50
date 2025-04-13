import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    
    if not corpus[page]:
        return {p: 1/len(corpus) for p in corpus}
        
    page_to_all = .15 / len(corpus)
    longitud_page = len(corpus)
    new_dict = {}
    
    for pagina, enlace in corpus.items():

        if pagina == page:      
            distributor = damping_factor / len(enlace)  
            for link in enlace:
                new_dict[link] = distributor + page_to_all

        if pagina not in new_dict:
            new_dict[pagina] = page_to_all

    return new_dict



def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    import random


    dict_pr = {}
    seed = random.choice(list(corpus.keys())) 
    semilla_primordial = seed ## La mantendre por que es la escencia de la 
    transicion = transition_model(corpus, seed, damping_factor)
    memoria = {seed : 1}
    x = 1
    
    while x < n:
    
        paginas = list(transicion.keys())
        pesos = list(transicion.values())
        siguiente_pagina = random.choices(paginas, weights = pesos, k = 1)[0]
        if siguiente_pagina in memoria:
            memoria[siguiente_pagina] += 1
        else:
            memoria[siguiente_pagina] = 1
        transicion = transition_model(corpus, siguiente_pagina, damping_factor)
        x+=1

    for dato in memoria:
        memoria[dato] /= n

    
    return memoria
        
            

def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    dict_pr = {} ## Aqui almacenamos los PR de cada página más la cantidad de enlaces que tiene dicha página
    loops = 0
    N = len(corpus)

    for pagina in corpus:  # Desempaquetar
        dict_pr[pagina] = {
            "rank" : 1/N,
            "enlaces" : corpus[pagina],
            "salidas": len(corpus[pagina])
        }

    dict_quienmeenlaza = {pagina: set() for pagina in dict_pr}
    is_convergente = False

    for pagina, enlaces in dict_pr.items():
            for enlace in enlaces["enlaces"]:
                for paginado in dict_quienmeenlaza.items():
                    if paginado[0] == enlace:
                        dict_quienmeenlaza[paginado[0]].add(pagina)


    for pagina, valores in dict_quienmeenlaza.items():
        dict_pr[pagina]["sitios_que_me_enlazan"] = valores


    is_convergente = False
    loops = 0
    while is_convergente == False:
        is_convergente = True
        parte_1 = (1 - damping_factor) / N

        pr_sin_salidas = 0
        for valores in dict_pr.values():
            if valores["salidas"] == 0:
                pr_sin_salidas += valores["rank"]

        for pagina, valores in dict_pr.items():
            sumatoria_temp = 0
            for dato in valores["sitios_que_me_enlazan"]:
                sumatoria_temp += (dict_pr[dato]["rank"] / dict_pr[dato]["salidas"])
            sumatoria_temp += pr_sin_salidas / N
            nuevo_ranking = round(parte_1 + (damping_factor * sumatoria_temp), 4)
            if abs(nuevo_ranking - dict_pr[pagina]["rank"]) > 0.0001:
                is_convergente = False
                
            dict_pr[pagina]["rank"] = nuevo_ranking
            loops += 1
    
    sumatoria = 0
    dict_final = {}
    print("Utilizamos : ", loops, " Loops")

    for pagina, valores in dict_pr.items():
        sumatoria += valores["rank"]
        dict_final[pagina] = valores["rank"]

    return dict_final
        

        


if __name__ == "__main__":
    main()
