def tag_bloco(content, classe='success', inline=False):
    tag = 'span' if inline else 'div'
    return f'<{tag} class="{classe}">{content}</{tag}>'


def tag_list(*itens):
    list = ''.join(f'<li>{item}</li>' for item in itens)  # generator
    return f'<ul>{list}<ul>'


if __name__ == '__main__':
    print(tag_bloco('bloco'))
    print(tag_bloco('inline and class', 'info', True))
    print(tag_bloco('inline', inline=True))
    print(tag_bloco(inline=True, content='inline'))
    print(tag_bloco('falhou', classe='error'))
    print(tag_bloco(tag_list('Item 1', 'Item 2'), classe='info'))
