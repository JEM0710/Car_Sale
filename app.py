from flask import Flask, render_template
from data import list

app = Flask (__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cars/<car_type>')
def cars(car_type):
    car_list = list[car_type]
    return render_template('cars.html', car_type_template=car_type, cars_template=car_list)

@app.route('/cars/<car_type>/<int:car_id>')
def kotse(car_type, car_id):
    car_profile = list[car_type][car_id]
    return render_template('kotse.html', car_profile=car_profile)

if __name__ == '__main__':
    app.run(debug=True)
