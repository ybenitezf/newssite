from flask import Blueprint
from flask.templating import render_template

pages_bp = Blueprint('pages', __name__, template_folder='templates')


@pages_bp.route('/')
def load_page():
    return render_template('pages/page.html', **{})
