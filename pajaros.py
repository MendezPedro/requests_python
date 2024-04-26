import requests
from string import Template

def request_get(url):
    return requests.get(url).json()

response = request_get('https://aves.ninjas.cl/api/birds')[:10]

# organizo mis etiquetas a modificar
img_template = Template('<img src="$url">')
imagen = img_template.substitute(url = 'Hola')

name_template = Template('<h3>$name<h3>')
name = name_template.substitute(name = 'name_prov')

nombre_template = Template('<h1>$nombre<h1>')
nombre = nombre_template.substitute(nombre = 'nombre_prov')

# genero template base
html_template = Template('''<!DOCTYPE html>
                            <html>
                            <head>
                            <meta charset="UTF-8">
                            <title>Título de la Página</title>
                            <style>
                                .card-container {
                                    display: flex;
                                    flex-wrap: wrap;
                                    justify-content: flex-start;
                                    gap: 20px;
                                    padding: 20px;
                                }
                                .card {
                                    width: 300px;
                                    border: 1px solid #ccc;
                                    border-radius: 8px;
                                    overflow: hidden;
                                    margin: 20px;
                                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                                }
                                .card img {
                                    width: 100%;
                                    height: auto;
                                    border-bottom: 1px solid #ccc;
                                }
                            </style>
                            </head>
                            <body>
                                <h1>Nuestra página Web</h1>
                                <div class="card-container">
                                    <div class="card">
                                        $body
                                    </div>
                                </div>
                            </body>
                            </html>
                        ''')


# extraigo los 3 datos que necesito al iterar todo el json
lista_url = [(elemento['images']['main'], elemento['name']['english'], elemento['name']['spanish']) for elemento in response]
texto_template = ''


# recorro mi lista y la pongo en el body
for url, name, nombre in lista_url:
    texto_template += nombre_template.substitute(nombre = nombre) + '\n' + name_template.substitute(name = name) + '\n' + img_template.substitute(url = url) + '\n'


# sustituyo mi data en el body del template 
html = html_template.substitute(body = texto_template)


# escribo mi archivo html 
with open('output.html', 'w', encoding='utf-8') as f:
    f.write(html)
