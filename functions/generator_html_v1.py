def tag_bloco(text, classe='success'): # classe = css (opcional)
    return f'<div class="{classe}">{text}</div>'

if __name__ == '__main__':
    # Test (assertion) - validates condition, if successful executes normally,
    # if error returns error message
    assert tag_bloco('Successfully added!') == \
        '<div class="success">Successfully added!</div>'
    assert tag_bloco('Impossible to delete!', 'error') == \
        '<div class="error">Impossible to delete!</div>'
    print(tag_bloco('bloco'))