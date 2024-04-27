from string import Template

def html(lista_url,texto_template):
    """genero template html base"""

    # organizo mis etiquetas a modificar
    img_template = Template('<img src="$url">')
    imagen = img_template.substitute(url = 'Hola')

    name_template = Template('<h3>$name</h3>')
    name = name_template.substitute(name = 'name_prov')

    nombre_template = Template('<h1>$nombre</h1>')
    nombre = nombre_template.substitute(nombre = 'nombre_prov')

    # genero template base
    html_template = Template('''<!DOCTYPE html>
                                <html>
                                <head>
                                <meta charset="UTF-8">
                                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                                <title>Aves de Chile</title>
                                <link rel="stylesheet" href="style.css">
                                </head>
                                <body>
                                    <h1>Aves de Chile</h1>
                                    <div class="card-container">
                                        $body
                                    </div>
                                </body>
                                </html>
                            ''')


    # recorro mi lista y la pongo en el body
    for url, name, nombre in lista_url:
        texto_template += '<div class="card">' + nombre_template.substitute(nombre = nombre) + '\n' + name_template.substitute(name = name) + '\n' + img_template.substitute(url = url) + '\n' + '</div>'


    # sustituyo mi data en el body del template 
    html = html_template.substitute(body = texto_template)


    # escribo mi archivo html 
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)