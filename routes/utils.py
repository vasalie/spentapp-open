# rows
arr_rows =  [
            '5', '10', '20', '50', '100', '1000', '10000'
            ]

# convertion
dict_conv = {
            'CAN' :1,
            'EUR' :1.5,
            'USD' :1.44,
            }

# type
arr_type = list(dict_conv.keys())

# locations
arr_loc =   [
            'USA', 'Canada', 'Europe'
            ]

# category
arr_cat =   [
            'Grocery', 'Treats', 'Bills', 'Restaurants', 
            'Clothes', 'Electronics', 'Home', 'Transportation', 
            'Accommodation', 'Miscellaneous', 'Medical', 'Travel'
            ]

# Calculate pagination values
def Calc_page(records, page, records_per_page):
    start = (page - 1) * records_per_page
    end   = start + records_per_page
    next  = page + 1
    prev  = page - 1
    total_pages = int(records / records_per_page)
    if( total_pages*records_per_page < records ):
        total_pages += 1
    return start, end, page, next, prev, records, total_pages

# Analyze paramaters
def Analyze_params(params):
    if(params('reset')== None):
        reset = 'false'
    else:
        reset = params('reset')
    
