from app.database.init_db import boot_database
from app.repository.url_repository import save_url, search_id

boot_database()

url_save = save_url('www.google.com','2026-05-25')


id_search = search_id(url_save)

print(id_search)