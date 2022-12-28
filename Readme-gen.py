# from os import system
# import webbrowser

# WARNING = '\033[31m'
# ENDC = '\033[0m'

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

# # lenguajes del proyecto
# print("\n")
# print("Que tecnologias as usado en el proyecto")
# langUrlArray = [
#     "",
#     # html
#     "<code><img height=\"30\" src=\"https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white\"></code>",
#     # css
#     "<code><img height=\"30\" src=\"https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white\"></code>",
#     # sass
#     "<code><img height=\"30\" src=\"https://img.shields.io/badge/Sass-CC6699?style=for-the-badge&logo=sass&logoColor=white\"></code>",
#     # javascript
#     "<code><img height=\"30\" src=\"https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E\"></img></code>",
#     # python
#     "<code><img height=\"30\" src=\"https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white\"></code>",
#     # scrolltringer
#     "<code><img height=\"30\" src=\"https://img.shields.io/badge/ScrollTrigger-E34F26?style=for-the-badge&logo=scrolltrigger&logoColor=white\"></code>",
#     # bootsrap
#     "<code><img height=\"30\" src=\"https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white\"></code>",
#     # spline
#     "<code><img height=\"30\" src=\"https://i.postimg.cc/85hR92yS/Group-71.png\"></code>"
# ]
# langArray = [
#     "salir",
#     "html",
#     "css",
#     "sass",
#     "javascript",
#     "python",
#     "ScrollTrigger",
#     "Bootstrap",
#     "spline"
# ]

# loop = True
# while loop:
#     num = 0
#     for i in langArray:
#         print(f"{num} - {i}")
#         num += 1
#     try:
#         opt = int(input("seleciona una opcion: "))
#         print("\n")
#     except ValueError:
#         print("Please input integer only...")
#         continue
#     if len(langArray) == 1 or opt == 0:
#         loop = False

#     elif opt > len(langArray) - 1:
#         print(WARNING + "!!Numero no valido¡¡ \n" + ENDC)
#     else:
#         n = langUrlArray[opt]
#         filedata = filedata.replace('{pLang}', n + "{pLang}")
#         langArray.pop(opt)
#         langUrlArray.pop(opt)
#     with open('README.md', 'w') as file:
#         file.write(filedata)

# filedata = filedata.replace('{pLang}', "")

# Project status
status = ['Estas trabajando en el proyecto: ','Es responsive: ','Tiene hosting: ']
loop = 0
while loop < 3:
    opt = input(status[loop])
    
    loop += 1

# if status == "si":
#     filedata = filedata.replace('{st1}', ":heavy_check_mark:")
# else:
#     filedata = filedata.replace('{st1}', ":x:")
# if status == "si":
#     filedata = filedata.replace('{st2}', ":heavy_check_mark:")
# elif status == "sn":
#     filedata = filedata.replace('{st2}', "Parcialmente")
# else:
#     filedata = filedata.replace('{st2}', ":x:")
# if status == "si":
#     filedata = filedata.replace('{st3}', "GithubPages")
# elif status == "otro":
#     host = input("ingresa el hosting: ")
#     filedata = filedata.replace('{st3}', host)
# else:
#     filedata = filedata.replace('{st3}', ":x:")
# print("\n")
# print("Project preview")
# print("1 si no tienes imagen de preview")
# print("2 si tienes imagen de preview")
# print("3 si tienes gif de preview \n")
# preview = input("seleciona una opcion: ")
# if preview == "1":
#     filedata = filedata.replace('{pPreview}', "``vista no disponible``")
# if preview == "2":
#     filedata = filedata.replace(
#         '{pPreview}', "<img src=\"./preview.png\" width=\"100%\">")
# if preview == "3":
#     filedata = filedata.replace(
#         '{pPreview}', "<img src=\"./preview.gif\" width=\"100%\">")
# with open('README.md', 'w') as file:
#     file.write(filedata)
# system("DEL Readme-gen.py && git pull && git add -A && git commit -a -m \"update\" && git push")
# webbrowser.open("https://github.com/Carloscruzvalencia/"+ pTitle + "#readme")
