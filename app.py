
from flask import Flask, request, Response, jsonify
import json
import server
from flask_cors import CORS


app = Flask(__name__)
app.config['BASIC_AUTH_USERNAME'] = 'cloud'
app.config['BASIC_AUTH_PASSWORD'] = 'computing'
CORS(app)


@app.route('/')
def test():
    return "Welcome to Flask!"


@app.route('/watch', methods=['POST'])
def add_to_list():
    req_data = request.get_json(force = True)
    _sku = req_data['sku']
    _type_watch = req_data['type']
    _status = req_data['status']
    _gender = req_data['gender']
    _year = req_data['year']
    _dial_material = req_data['dial_material']
    _dial_color = req_data['dial_color']
    _case_material = req_data['case_material']
    _case_form = req_data['case_form']
    _bracelet_material = req_data['bracelet_material']
    _movement = req_data['movement']
    print(_gender)
    # Add item to the list
    res_data = server.add_to_list(_sku,_type_watch,_status,_gender,_year,_dial_material,_dial_color,_case_material,_case_form,_bracelet_material,_movement)
    # Return error if item not added
    if res_data is None:
        response = Response("{'error': 'Item not added - " + _sku + "'}", status=400 , mimetype='application/json')
        return response
    # Return response
    response = Response(json.dumps(res_data), mimetype='application/json')
    return response


@app.route('/items/all')
def get_all_teachers():
    # Get items from the helper
    res_data = server.get_all_teachers()
    # Return
    print(res_data)
    response = Response(json.dumps(res_data), mimetype='application/json')
    return response


@app.route('/watch/<string:sku>', methods=['GET', 'PUT', 'DELETE']) #OPTIONS crashing
def watch(sku):
    # Get items from the helper
    req_data = request.get_json()
    if request.method == "GET":
        res_data = server.get_watch(sku)
        # Return
        response = Response(json.dumps(res_data), mimetype='application/json')
        return response
    elif request.method == "PUT":
        print("Updating started")
        _sku = req_data['sku']
        _type_watch = req_data['type']
        _status = req_data['status']
        _gender = req_data['gender']
        _year = req_data['year']
        _dial_material = req_data['dial_material']
        _dial_color = req_data['dial_color']
        _case_material = req_data['case_material']
        _case_form = req_data['case_form']
        _bracelet_material = req_data['bracelet_material']
        _movement = req_data['movement']
        res_data = server.update_status(_sku,_type_watch,_status,_gender,_year,_dial_material,_dial_color,_case_material,_case_form,_bracelet_material,_movement)
        print(res_data)
        # Return error if the status could not be updated
        if res_data is None:
            response = Response("{'error': 'Error updating item - '" + _sku + "}", status=400,
                                mimetype='application/json')
            return response
        # Return response
        response = Response(json.dumps(res_data), mimetype='application/json')
        return response
    elif request.method == "DELETE":
        req_data = request.get_json()
        print("getting sku", sku)
        _sku = sku
        print("deleting item sku: ", _sku)
        # Delete item from the list
        res_data = server.delete_watch(_sku)
        print(res_data)
        # Return error if the item could not be deleted
        if res_data is None:
            response = Response("{'error': 'Error deleting item - '" + sku + "}", status=400,
                                mimetype='application/json')
            return response
        # Return response
        response = Response(json.dumps(res_data), mimetype='application/json')
        return response


@app.route('/watch/complete-sku/<string:prefix>', methods=['GET'])
def watchbypref(prefix):
    # Get items from the helper
    res_data = server.get_by_pref(prefix)
    # Return
    response = Response(json.dumps(res_data), mimetype='application/json')
    return response


class criteria_dictionary(dict):
    def __init__(self):
        self = dict()
    def add(self, key, value):
        self[key] = value


@app.route('/watch/find', methods=['GET', 'PUT', 'DELETE'])
def watchbyparam():
    dict_obj = criteria_dictionary()
    print("works: ", request.args.get('sku'))
    criterias = []
    # Get items from the helper
    if request.method == "GET":
        print("Getting watches by criterias")
        _sku = request.args.get('sku')
        _type_watch = request.args.get('type')
        _status = request.args.get('status')
        _gender = request.args.get('gender')
        _year = request.args.get('year')
        _dial_material = request.args.get('dial_material')
        _dial_color = request.args.get('dial_color')
        _case_material = request.args.get('case_material')
        _case_form = request.args.get('case_form')
        _bracelet_material = request.args.get('bracelet_material')
        _movement = request.args.get('movement')
        if (len(_sku) != 0): dict_obj.add('sku', _sku)
        if (len(_type_watch) != 0): dict_obj.add('type_watch', _type_watch)
        if (len(_status) != 0): dict_obj.add('status', _status)
        if (len(_gender) != 0): dict_obj.add('gender', _gender)
        if (len(_year) != 0): dict_obj.add('year', _year)
        if (len(_dial_material) != 0): dict_obj.add('dial_material', _dial_material)
        if (len(_dial_color) != 0): dict_obj.add('dial_color', _dial_color)
        if (len(_case_material) != 0): dict_obj.add('case_material', _case_material)
        if (len(_case_form) != 0): dict_obj.add('case_form', _case_form)
        if (len(_bracelet_material) != 0): dict_obj.add('bracelet_material', _bracelet_material)
        if (len(_movement) != 0): dict_obj.add('movement', _movement)
        reqs = [_sku,_type_watch,_status,_gender,_year,_dial_material,_dial_color,_case_material,_case_form,_bracelet_material,_movement]
        res_data = server.get_by_criteria(_sku, _type_watch, _status, _gender, _year, _dial_material, _dial_color,
                                          _case_material, _case_form, _bracelet_material, _movement, dict_obj)
        # Return
        response = Response(json.dumps(res_data), mimetype='application/json')
        return response