from selenium import webdriver
import time



atributos = ['doi','url','year','month','publisher','volume','number','pages','author','title','journal']
cotejo = []

# dois = lista con los dois
# parametros = parámetros deseados

with open('dois.txt') as texto:
    user_list = list(map(lambda doi:doi.strip("- "), texto.read().split("\n")))
    parametros = list(map(lambda par:par.strip(" "), user_list[0].split(",")))
    dois = [doi for doi in user_list[1:len(user_list)] if doi != ""]
for i in range(len(atributos)):
    if atributos[i] not in parametros:
        cotejo.append(atributos[i])

art_dic = {}
driver = webdriver.Firefox(executable_path=r'/home/user/path_to_gecko')
for doi in dois:
    driver.get('https://www.doi2bib.org/')
    formulario = driver.find_element_by_css_selector("input.form-control[value=''][placeholder='Enter a doi, PMCID, or arXiv ID']")
    formulario.send_keys(doi)
    boton = driver.find_element_by_class_name("input-group-btn").click()
    time.sleep(3)
    art_dic[doi] = driver.find_element_by_class_name("bibtex-code").text

articulos = list(art_dic.values())
with open('web_text.txt', 'w') as webtext:
    for articulo in articulos:
        webtext.write("%s\n" % articulo)

with open('web_text.txt', 'r+') as web_text:
        bib_list = web_text.readlines()
bib_def = bib_list
for j in range(len(bib_list)):
    for i in range(len(cotejo)):
        if cotejo[i] in bib_list[j]:
            bib_list[j]=""
bib_def = [bib for bib in bib_list if bib != ""]
with open('new.txt','w') as new_text:
    for el in bib_def:
        new_text.write(el)
