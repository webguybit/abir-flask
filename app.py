from flask import Flask, render_template, redirect, url_for, request, session, flash, make_response, jsonify, Markup
from flask_wtf.csrf import CSRFProtect

from functools import wraps
import json
from datetime import datetime, timedelta

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Sniffing_here???I\'ll_change_this_in_prod'

csrf = CSRFProtect(app)

@app.route('/home',methods=['GET','POST'])
def post_example():
    ''' This example uses post payload from post requests. 
        It tries to populate several fields in home.html page after taking from same page
        > validate/mock up processing from this view function and
        >finally send it back the same parameters/data values to home.html as response.
        ***This will create multiple rows with the submitted data
    '''
    if request.method == 'POST':
        name = request.json.get('name',None)
        city = request.json.get('city', None)
        country = request.json.get('country', None)
        back_ground = request.json.get('background', None)
        background_color = request.json.get('color', None)

        if name != None and city !=None and country != None and back_ground !=None and background_color !=None:
            htmlString = '<div class="row" style="padding:20px;margin-top:5vh;background-color:'+background_color+';border-radius:5px;">'
            htmlString +='<div class="inline_div" id="name_show">Name:'+name+'</div>'
            htmlString +='<div class="inline_div" id="city_show">City:'+city+'</div>'
            htmlString +='<div class="inline_div" id="country_show">Country:'+country+'</div>'
            htmlString +='<div class="inline_div" id="back_show">Back:'+back_ground+'</div></div>'
        
        # If display thru htmlString, no need other parameters to pass
        dict_obj = {'status':True, 'htmlString':htmlString }
        # dict_obj = {'name':name, 'city':city, 'country':country, 'back':back_ground, 'status':True }
        return jsonify(dict_obj)
    return render_template('home.html')


@app.route('/show/home',methods=['GET'])
def get_example():
    ''' This example uses query string from url. 
        This one goes for get request. 
        It tries to populate several fields in show_home.html page taking input from querystring.
    '''
    name = request.args.get('name',None)
    city = request.args.get('city', None)
    country = request.args.get('country', None)
    back_ground = request.args.get('background', None)
    background_color = request.args.get('color', None)
    htmlString=''
    
    if name != None and city !=None and country != None and back_ground !=None and background_color !=None:
        htmlString = '<div class="row" style="padding:20px;margin-top:5vh;background-color:'+background_color+';border-radius:5px;">'
        htmlString +='<div class="inline_div" id="name_show">Name:'+name+'</div>'
        htmlString +='<div class="inline_div" id="city_show">City:'+city+'</div>'
        htmlString +='<div class="inline_div" id="country_show">Country:'+country+'</div>'
        htmlString +='<div class="inline_div" id="back_show">Back:'+back_ground+'</div></div>'
    # print(htmlString)
    # If display thru htmlString, no need other parameters to pass
    return render_template('show_home.html',htmlString=htmlString)

    # return render_template('show_home.html',name=name, city=city, country=country, background=back_ground, htmlString=htmlString)

if __name__ == '__main__':
        csrf.init_app(app)
        app.run(debug=True,port=5100)