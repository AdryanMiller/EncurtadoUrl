

def encode(id_url:int):
    charset = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

    if id_url == 0:
        return charset[0]
    
    base62 = []
    while id_url > 0:
        id_url, rest = divmod(id_url, 62)
        base62.append(charset[rest])
    return ''.join(reversed(base62))


def decode(url_code:str) -> int:
    charset = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    num = 0

    for characters in url_code:
        velue_charset = charset.index(characters)
        num = num * 62 + velue_charset    
    return num
