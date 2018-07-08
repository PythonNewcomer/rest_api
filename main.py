from config_reader import ConfigReader
from database_helper import DatabaseHelper
from json import loads
from flask import Flask, jsonify, request

app = Flask('CountriesREST')
cr = ConfigReader()
host, dbname, user, password = cr.get_database_config()
db = DatabaseHelper(host, dbname, user, password)


@app.route('/countries', methods=['GET'])
def get_countries():
    result = db.execute_select('SELECT id, name, continent FROM public.countries')
    return db.transform_dataset_into_json(result)


@app.route('/countries/<id>', methods=['GET'])
def get_country(id):
    script = 'SELECT id, name, continent FROM public.countries WHERE id = {}'.format(id)
    result = db.execute_select(script)
    return db.transform_row_into_json(result)


@app.route('/countries/<id>', methods=['DELETE'])
def delete_country(id):
    script = 'DELETE FROM public.countries WHERE id = {}'.format(id)
    db.execute_script(script)
    message = 'Country {} was deleted!'.format(id)
    dic = {'message': message}
    return jsonify(dic)


@app.route('/countries', methods=['POST'])
def add_country():
    data = loads(request.data)
    name = data['name']
    continent = data['continent']
    script = "INSERT into public.countries(name, continent) values ('{0}', '{1}')".format(name, continent)
    db.execute_script(script)
    message = 'Country {} was added!'.format(name)
    dic = {'message': message}
    return jsonify(dic)


@app.route('/countries', methods=['PUT'])
def update_country():
    data = loads(request.data)
    id = data['id']
    name = data['name']
    continent = data['continent']
    select_script = 'SELECT id, name, continent FROM public.countries WHERE id = {}'.format(id)
    result = db.execute_select(select_script)
    dic = {}
    if len(result) == 0:
        dic['message'] = 'Country Not Found'
    else:
        update_script = "UPDATE public.countries SET name = '{0}', continent = '{1}' WHERE id = {2}".format(name, continent, id)
        db.execute_script(update_script)
        dic['message'] = 'Country Was Updated'
    return jsonify(dic)


if __name__ == '__main__':
    app.run(debug=True)

