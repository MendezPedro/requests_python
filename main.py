from request_bird import request_get
from create_html import html
from create_css import css


response = request_get('https://aves.ninjas.cl/api/birds')
# extraigo los 3 datos que necesito al iterar todo el json
lista_url = [(elemento['images']['main'], elemento['name']['english'], elemento['name']['spanish']) for elemento in response]
texto_template = ''

# creo html
html_template = html(lista_url,texto_template)

#creo css
css_template = css()


