from flask import Blueprint, request, redirect, render_template,flash
from flask import abort
from app.service.url_service import create_short_url, redirect_url

bp = Blueprint('home',__name__, url_prefix='/home')

@bp.route('/shorten', methods=['GET','POST'])
def shorten():
    try:
        url_long = request.form.get('url')
        if not url_long or not url_long.strip():
            return {'erro':'Campo de URL nao pode ficar vazio'}, 400
        create_url = create_short_url(url_long)
        url_short = 'localhost:5000/' + create_url
        flash(url_short, 'sucess')
        return redirect('/')
    except ValueError:
        flash('URL invalidade. Apenas URLs https:// ou http://', 'error')
        return redirect('/')
        

@bp.route('/', methods=['GET'])
def home():
    return render_template('index.html')