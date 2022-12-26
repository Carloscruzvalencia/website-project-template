from os import system
import webbrowser

with open('readme2.md', 'r') as file:
    filedata = file.read()

pTitle = input("Nombre del proyecto: ")
filedata = filedata.replace("{pTitle}", pTitle)

pDesc = input("Descripción del proyecto: ")
filedata = filedata.replace('{pDesc}', pDesc)

pUrl = "https://carloscruzvalencia.github.io/" + pTitle
filedata = filedata.replace('{pUrl}', pUrl)


html = "<code><img height=\"30\" src=\"https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white\"></code>"
css = "<code><img height=\"30\" src=\"https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white\"></code>"
sass = "<code><img height=\"30\" src=\"https://img.shields.io/badge/Sass-CC6699?style=for-the-badge&logo=sass&logoColor=white\"></code>"
javascript = "<code><img height=\"30\" src=\"https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E\"></img></code>"
python = "<code><img height=\"30\" src=\"https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white\"></code>"
scrolltrigger = "<code><img height=\"30\" src=\"https://img.shields.io/badge/ScrollTrigger-E34F26?style=for-the-badge&logo=scrolltrigger&logoColor=white\"></code>"
botstrap = "<code><img height=\"30\" src=\"https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white\"></code>"
spline = "<code><img height=\"30\" src=\"https://i.postimg.cc/85hR92yS/Group-71.png\"></code>"

list = ["salir = 0", "html = 1", "css =2", "sass =3", "javascript =4",
        "python =5", "ScrollTrigger =6", "Bootstrap =7", "spline =8"]
sel = True
while sel == True:
    print(list)
    lang = input("seleciona una opcion: ")
    if lang == "1":
        n = html
    elif lang == "2":
        n = css
    elif lang == "3":
        n = sass
    elif lang == "4":
        n = javascript
    elif lang == "5":
        n = python
    elif lang == "6":
        n = scrolltrigger
    elif lang == "7":
        n = botstrap
    elif lang == "8":
        n = spline
    else:
        sel = False
        filedata = filedata.replace('{pLang}', "")

    filedata = filedata.replace('{pLang}', n + "{pLang}")
    with open('README.md', 'w') as file:
        file.write(filedata)

print("1 si no tienes imagen de preview")
print("2 si tienes imagen de preview")
print("3 si tienes gif de preview")

preview = input("seleciona una opcion: ")
if preview == "1":
    filedata = filedata.replace('{pPreview}', "``vista no disponible``")
if preview == "2":
    filedata = filedata.replace(
        '{pPreview}', "<img src=\"./preview.png\" width=\"100%\">")
if preview == "3":
    filedata = filedata.replace(
        '{pPreview}', "<img src=\"./preview.gif\" width=\"100%\">")


status = input("estas Trabajando en el proyecto: ")
if status == "si":
    filedata = filedata.replace('{st1}', ":heavy_check_mark:")
else:
    filedata = filedata.replace('{st1}', ":x:")
status = input("es responsive: ")
if status == "si":
    filedata = filedata.replace('{st2}', ":heavy_check_mark:")
elif status == "sn":
    filedata = filedata.replace('{st2}', "Parcialmente")
else:
    filedata = filedata.replace('{st2}', ":x:")
status = input("tiene hosting: ")
if status == "si":
    filedata = filedata.replace('{st3}', "Githubpages")
elif status == "otro":
    host = input("ingresa el hosting: ")
    filedata = filedata.replace('{st3}', host)
else:
    filedata = filedata.replace('{st3}', ":x:")
with open('README.md', 'w') as file:
    file.write(filedata)
system("DEL Readme-gen.py && git pull && git add -A && git commit -a -m \"update\" && git push")
webbrowser.open("https://github.com/Carloscruzvalencia/" + pTitle + "#readme")