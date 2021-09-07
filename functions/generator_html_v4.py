def tag_bloco(content, *args, classe='success', inline=False):
    tag = 'span' if inline else 'div'
    html = content if not callable(content) else content(*args)
    return f'<{tag} class="{classe}">{html}</{tag}>'


def tag_list(*itens):
    list = ''.join(f'<li>{item}</li>' for item in itens)  # generator
    return f'<ul>{list}<ul>'


if __name__ == '__main__':
    print(tag_bloco('bloco'))
    print(tag_bloco('inline and class', classe='info', inline=True))
    print(tag_bloco('inline', inline=True))
    print(tag_bloco(inline=True, content='inline'))
    print(tag_bloco('falhou', classe='error'))
    print(tag_bloco(tag_list('Item 1', 'Item 2'), classe='info'))

    print(tag_bloco(tag_list, 'Saturday', 'Sunday', classe='info', inline=True))
