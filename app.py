from flask import Flask, request, g
from config import *

import logging

from models import db


app = Flask(__name__, template_folder=PATH_TMPL)


# Configure SQLite databases
# PATH_DB   = app.instance_path
app.config['SQLALCHEMY_DATABASE_URI']   = 'sqlite:///' + os.path.join(PATH_DB, 'main.db')
# app.config['SQLALCHEMY_BINDS'] = {
#                                 'main': 'sqlite:///' + os.path.join(PATH_DB, 'main.db'   ),
#                                 'logs': 'sqlite:///' + os.path.join(PATH_DB, 'logs.db')
# }
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Initialize the database with the app
db.init_app(app)

# Create DBs and tables
from models.db_main  import Tbl_Records
with app.app_context():
    db.create_all()


# Register blueprints
from routes.rt_home import bp as bp_home
app.register_blueprint(bp_home)

from routes.bp_records  import bp as bp_records
app.register_blueprint(bp_records)

#  Logging
if LOG_FLASK:
    pass
else:
    log = logging.getLogger('werkzeug')
    log.disabled = True

@app.before_request
def before_request_func():
    g.request_start_time = time()
    ip = request.environ.get('REMOTE_ADDR')



# Log to Console
@app.after_request
def after_request_func(response):
    ip_val       = str(request.environ.get('REMOTE_ADDR'))
    time_val     = str(datetime.now().strftime("%Y-%m-%d*%H:%M:%S"))
    duration_val = str(time() - g.request_start_time)[:5]
    user_val     = "User"
    path_val     = str(request.path)
    if 'static' not in request.path:
        if LOG_CLEAN:
            print(  ip_val       + '\t' + 
                    time_val     + '\t' + 
                    duration_val + '\t' + 
                    user_val     + '\t' + 
                    path_val
            )
    return response


if __name__ == '__main__':
    app.run(host=IP, port=PORT, debug=DEBUG)