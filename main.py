from flask import Flask, request

from app.database.init_db import boot_database
from app.repository.url_repository import save_url, search_id
from app.service.url_service import create_short_url, redirect_url


app = Flask(__name__)


"""
boot_database()

test = create_short_url('www.google.com')

# print(test)

test_redi = redirect_url(test)

print(test_redi)
"""

if __name__ == '__main__':
    app.run(debug=True)