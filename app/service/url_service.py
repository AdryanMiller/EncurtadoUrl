from app.utils.normalize_url import normalize
from app.utils.base62 import encode, decode
from app.repository.url_repository import save_url, search_id

def create_short_url(url_log:str):
    normalize_url = normalize(url_log)
    url_id = save_url(normalize_url)
    if url_id is None:
        raise RuntimeError("Falha ao salvar URL no banco")
    url_id_base62 = encode(url_id)
    return url_id_base62

def redirect_url(id:str):
    url_base62_id = decode(id)
    search_id_url = search_id(url_base62_id)
    if search_id_url is None:
        raise LookupError("Pagina nao encontrada")
    return search_id_url