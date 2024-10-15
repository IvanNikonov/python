

#todo: Задан словарь, его значения необходимо внести по соответвющим тегам и атрибутам вместо вопросов (?)
# заполненный шаблон записать в файл index.html.

page = {"title": "Тег BODY",
        "charset": "utf-8",
        "alert": "Документ загружен",
        "p": "Ut wisis enim ad minim veniam,  suscipit lobortis nisl ut aliquip ex ea commodo consequat."}


template = f""" 
<!DOCTYPE HTML>
<html>
 <head>
  <title> {page['title']} </title>
  <meta charset="{page['charset']}">
 </head>
 <body onload="alert('{page['alert']}')">
 
  <p>{page['p']}</p>

 </body>
</html>
"""

f = open('index.html', 'w+t', encoding='utf-8')
f.write(template)
f.close()