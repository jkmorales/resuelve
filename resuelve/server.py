from flask import Flask
from flask import request
from flask import jsonify
from flask import make_response
import helpers

app = Flask(__name__)

@app.route('/salaries', methods=['POST'])
def salaries():
	data = request.get_json()
	percent_grupal = helpers.get_percent_grupal(data) 

	for player in data:
		individual_bonus = helpers.get_percent_individual(player['goles'],player['nivel']) * (player['bono']/2)
		player['sueldo_completo'] = round(player['sueldo'] + individual_bonus + (percent_grupal*(player['bono']/2)), 2)
		player['goles_minimos'] = helpers.levels[player['nivel']]

	return make_response(jsonify(data), 200)	

if __name__ == '__main__':
	app.run( debug = True, port=8000 )