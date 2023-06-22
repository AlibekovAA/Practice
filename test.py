



txt = 'Заявка № 900 [Согласуется]'
def parser_status(txt):
    text = txt.split('[', 1)[1].split(']')[0]
    return text



print(parser_status(txt))