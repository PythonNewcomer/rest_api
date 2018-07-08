from config_reader import ConfigReader
from database_helper import DatabaseHelper
from flask import Flask, jsonify

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
    message = 'Country {} was deleted'.format(id)
    dic = {'message': message}
    return jsonify(dic)

# db.close_connection()

if __name__ == '__main__':
    app.run(debug=True)

