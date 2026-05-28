from flask import Flask, redirect, render_template,abort
from app.routes.url_routes import bp
from app.database.init_db import boot_database
from app.service.url_service import redirect_url
import os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__, template_folder='app/templates', static_folder='app/static')
app.register_blueprint(bp)
app.secret_key = os.getenv('FLASK_SECRET_KEY')

boot_database() 

@app.route('/')
def redirect_home():
    return redirect('/home')

@app.route('/<code_url>', methods=['GET'])
def code(code_url):
    try:
        url_redirect = redirect_url(code_url)
        return redirect(url_redirect)
    except ValueError:
        abort(400)
    except LookupError:
        abort(404)

@app.errorhandler(404)
def pag_not_find(erro):
    return render_template('404.html')

@app.errorhandler(500)
def erro_serve(erro):
    return render_template('500.html')

if __name__ == '__main__':
    app.run(debug=True)