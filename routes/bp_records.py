from flask import Blueprint, render_template, redirect, url_for, request

from sqlalchemy import text

from models import db
from models.db_main import Tbl_Records as Tbl_Values

from .utils import *

print('Accesing Records BP')

APP_NAME = 'Records'
BP_NAME  = 'bp_records'
URL_PRFX = '/records'
BP_TEMPL = 'records/'

# columns used for search
dict_col =  {
            'date'     :'Date',
            'location' :'Location',
            'category' :'Category',
            'type'     :'Currency',
            'note'     :'Notes',
            }

SHOW_TOP_SEARCH = 20
DEFAULT_ROWS = 5

bp = Blueprint(BP_NAME, __name__, url_prefix=URL_PRFX)

@bp.route('/', methods=['GET'])
def main():
    arr_prms = Analyze_params(request.args.get)

    if(request.args.get('reset')== None):
        reset = 'false'
    else:
        reset = request.args.get('reset')
    
    if(request.args.get('search')== None):
        search = ''
    else:
        search = request.args.get('search')
    
    if(request.args.get('column')== None):
        column = ''
    else:
        column = request.args.get('column')
    
    if(request.args.get('rows')== None):
        rows = DEFAULT_ROWS
    else:
        rows = int(request.args.get('rows'))

    if(request.args.get('page')== None):
        page = 1
    else:
        page = int(request.args.get('page'))

    if(reset == 'true'):
        page = 1

    show_total = False
    val_total = 0

    if(search != ''):
        # records = Tbl_Values.query.filter(getattr(Tbl_Values, column).ilike('%{}%'.format(search))).count()
        # arr_page = Calc_page(records, page, rows)
        # values = Tbl_Values.query.filter(Tbl_Values.path.like('%' + search + '%')).order_by(Tbl_Values.id.desc()).offset(arr_page[0]).limit(rows)
        values_nopag = Tbl_Values.query.with_entities(Tbl_Values.convert).filter(getattr(Tbl_Values, column).ilike('%{}%'.format(search)))
        arr_page = Calc_page(values_nopag.count(), page, rows)
        show_total = True
        for x in values_nopag:
            val_total = val_total + x.convert
        values = Tbl_Values.query.filter(getattr(Tbl_Values, column).ilike('%{}%'.format(search))).order_by(Tbl_Values.date.desc()).offset(arr_page[0]).limit(rows)
    else:
        records = Tbl_Values.query.count()
        arr_page = Calc_page(records, page, rows)
        values = Tbl_Values.query.order_by(Tbl_Values.date.desc()).offset(arr_page[0]).limit(rows)

    # result = db.session.execute(text('SELECT * FROM Tbl_Values'))


    return render_template  (BP_TEMPL + 'main.html', \
                            values=values, \
                            pagename=APP_NAME, \
                            arr_page = arr_page, \
                            bp_name = BP_NAME, \
                            search = search, \
                            column = column, \
                            dict_col = dict_col, \
                            arr_loc = arr_loc, \
                            arr_cat = arr_cat, \
                            arr_type = arr_type, \
                            show_total = show_total, \
                            val_total = val_total, \
                            rows = str(rows), \
                            arr_rows = arr_rows, \
                            reset = 'false', \
                            SHOW_TOP_SEARCH = SHOW_TOP_SEARCH,\
                            )

@bp.route('/add_new', methods=['POST'])
def add_new():
    date     = request.form['date'    ].replace('-', '')
    location = request.form['location']
    category = request.form['category']
    value    = int(request.form['value'   ])
    type     = request.form['type'    ]
    note     = request.form['note'    ]
    convert  = dict_conv[type]*value

    
    new_entry = Tbl_Values(date=date, location=location, category=category, value=value, type=type, convert=int(convert), note=note)
    db.session.add(new_entry)
    db.session.commit()
    db.session.close()
    
    # return redirect(url_for(BP_NAME + '.main'))
    return redirect(URL_PRFX)

@bp.route('/edit', methods=['GET'])
def edit():

    if(request.args.get('id')== None):
        return redirect(URL_PRFX)
    else:
        id = int(request.args.get('id'))

    # return str(id)

    return render_template  (BP_TEMPL + 'form_edit.html', \
                            bp_name = BP_NAME, \
                            id = id, \
                            )


@bp.route('/delete', methods=['GET'])
def delete():

    if(request.args.get('id')== None):
        return redirect(URL_PRFX)
    else:
        id = int(request.args.get('id'))

    return str(id)
