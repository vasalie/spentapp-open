from flask import Blueprint, render_template

APP_NAME = 'Spendings App'
BP_NAME  = 'bp_home'
URL_PRFX = '/'
BP_TEMPL = 'home/'

bp = Blueprint(BP_NAME, __name__, url_prefix=URL_PRFX)

@bp.route('/')
def main():
    return render_template(BP_TEMPL + 'home.html', pagename=APP_NAME)

@bp.route('/help')
def help():
    return render_template(BP_TEMPL + 'help.html')

@bp.route('/sett')
def sett():
    return render_template(BP_TEMPL + 'sett.html')




