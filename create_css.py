from string import Template

def css():
    """genero template css base"""

    css_template = Template('''.card-container {
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
                                h1, h3 {
                                    text-align: center;
                                }
                            ''')


    # transformo formato
    css = css_template.substitute()


    # escribo mi archivo css 
    with open('style.css', 'w', encoding='utf-8') as f:
        f.write(css)