

def normalize(url_long:str):
    url_no_space = url_long.replace(" ", "")
    
    if url_no_space.startswith(('http://','https://')):
        return url_no_space
    
    if '://' in url_no_space and not url_no_space.startswith(('http://','https://')):
        raise ValueError('URL INVALIDA, Apenas urls HTTP !')
    
    url_normalize = 'https://' + url_no_space
    return url_normalize
