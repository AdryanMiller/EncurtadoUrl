from flask import Blueprint, request, redirect
from app.service.url_service import create_short_url, redirect_url

bp = Blueprint('home',__name__, url_prefix='/home')

@bp.route('/shorten', methods=['POST'])
def shorten():
    
    url_long = request.form.get('url')
    create_url = create_short_url(url_long)
    url_short = 'localhost:5000/' + create_url
    return url_short

@bp.route('/<code>', methods=['GET'])
def code():
    return redirect(code)