#!/usr/bin/python3
bloco_atrs = ('bloco_accesskey', 'bloco_id')
url_atrs = ('ul_id', 'ul_style')

def filtrar_atrs(informados, suportados):
    return ' '.join(f'{k.split("_")[-1]}="{v}"' 
        for k, v in informados.items() if k in suportados)

def tag_bloco(content, *args, classe='success', inline=False, **novos_atrs):
    tag = 'span' if inline else 'div'
    html = content if not callable(content) else content(*args, **novos_atrs)
    atributos = filtrar_atrs(novos_atrs, bloco_atrs)
    return f'<{tag} class="{classe}">{html}</{tag}>'


def tag_list(*itens, **novos_atrs):
    list = ''.join(f'<li>{item}</li>' for item in itens)  # generator
    return f'<ul {filtrar_atrs(novos_atrs, url_atrs)}>{list}<ul>'


if __name__ == '__main__':
    print(tag_bloco('bloco'))
    print(tag_bloco('inline and class', classe='info', inline=True))
    print(tag_bloco('inline', inline=True))
    print(tag_bloco(inline=True, content='inline'))
    print(tag_bloco('falhou', classe='error'))
    print(tag_bloco(tag_list('Item 1', 'Item 2'), classe='info'))
    print(tag_bloco(tag_list, 'Saturday', 'Sunday', classe='info', inline=True))
    print(tag_bloco(tag_list, 'Item 1', 'Item 2', classe='info',
                    bloco_accesskey='m', bloco_id='conteudo', ul_id='lista'))
