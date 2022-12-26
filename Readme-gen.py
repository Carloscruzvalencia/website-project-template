# from os import system
# import webbrowser

with open('README.md', 'r') as file:
    filedata = file.read()

# # Nombre del proyecto
# pTitle = input("Nombre del proyecto: ")
# filedata = filedata.replace("{pTitle}", pTitle)

# # Descripción del proyecto
# pDesc = input("Descripción del proyecto: ")
# filedata = filedata.replace('{pDesc}', pDesc)

# # Url del proyecto
# pUrl = "https://carloscruzvalencia.github.io/" + pTitle
# filedata = filedata.replace('{pUrl}', pUrl)

# lenguajes del proyecto
langUrlArray = [
    "",
    # html
    "<code><img height=\"30\" src=\"https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white\"></code>",
    # css
    "<code><img height=\"30\" src=\"https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white\"></code>",
    # sass
    "<code><img height=\"30\" src=\"https://img.shields.io/badge/Sass-CC6699?style=for-the-badge&logo=sass&logoColor=white\"></code>",
    # javascript
    "<code><img height=\"30\" src=\"https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E\"></img></code>",
    # python
    "<code><img height=\"30\" src=\"https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white\"></code>",
    # scrolltringer
    "<code><img height=\"30\" src=\"https://img.shields.io/badge/ScrollTrigger-E34F26?style=for-the-badge&logo=scrolltrigger&logoColor=white\"></code>",
    # bootsrap
    "<code><img height=\"30\" src=\"https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white\"></code>",
    # spline
    "<code><img height=\"30\" src=\"https://i.postimg.cc/85hR92yS/Group-71.png\"></code>"
]
langArray = [
    "salir",
    "html",
    "css",
    "sass",
    "javascript",
    "python",
    "ScrollTrigger",
    "Bootstrap",
    "spline"
]

loop = True
while loop:
    num = 0
    for i in langArray:
        print(f"{num} - {i}")
        num += 1

    opt = int(input("seleciona una opcion: "))
    print("\n")

    n = langUrlArray[opt]

    filedata = filedata.replace('{pLang}', n + "{pLang}")
    langArray.pop(opt)
    langUrlArray.pop(opt)
            
    with open('README.md', 'w') as file:
        file.write(filedata)


# sel = True
# langSelected = []
# while sel == True:
#     lang = input("seleciona una opcion: ")

#     if lang in langSelected:
#             print("ya lo as selecionado")
#             langSelected.append(lang)
#     else:


# #vista previa del proyecto
# print("1 si no tienes imagen de preview")
# print("2 si tienes imagen de preview")
# print("3 si tienes gif de preview")

# preview = input("seleciona una opcion: ")
# if preview == "1":
#     filedata = filedata.replace('{pPreview}',"``vista no disponible``")
# if preview == "2":
#     filedata = filedata.replace('{pPreview}', "<img src=\"./preview.png\" width=\"100%\">")
# if preview == "3":
#     filedata = filedata.replace('{pPreview}', "<img src=\"./preview.gif\" width=\"100%\">")

# #project status
# status = input("estas Trabajando en el proyecto: ")
# if status == "si":
#     filedata = filedata.replace('{st1}', ":heavy_check_mark:")
# else:
#     filedata = filedata.replace('{st1}', ":x:")
# status = input("es responsive: ")
# if status == "si":
#     filedata = filedata.replace('{st2}', ":heavy_check_mark:")
# elif status == "sn":
#     filedata = filedata.replace('{st2}', "Parcialmente")
# else:
#     filedata = filedata.replace('{st2}', ":x:")
# status = input("tiene hosting: ")
# if status == "si":
#     filedata = filedata.replace('{st3}', "Githubpages")
# elif status == "otro":
#     host = input("ingresa el hosting: ")
#     filedata = filedata.replace('{st3}', host)
# else:
#     filedata = filedata.replace('{st3}', ":x:")
# status = input("hosting disponible: ")
# if status == "si":
#     filedata = filedata.replace('{st4}', ":heavy_check_mark:")
# else:
#     filedata = filedata.replace('{st4}', ":x:")
# status = input("tiene trello: ")
# if status == "si":
#     filedata = filedata.replace('{st5}', ":heavy_check_mark:")
# else:
#     filedata = filedata.replace('{st5}', ":x:")

# with open('README.md', 'w') as file:
#     file.write(filedata)
# system("DEL Readme-gen.py && git pull && git add -A && git commit -a -m \"update\" && git push")
# webbrowser.open("https://github.com/Carloscruzvalencia/"+ pTitle + "#readme")
