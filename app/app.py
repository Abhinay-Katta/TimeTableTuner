from flask import Flask, render_template, request
import sys
sys.path.append('./')
sys.path.append('../')

app = Flask(__name__,
            static_folder='../static',
            template_folder='../templates')


@app.route('/')
def index():
    return render_template('index.html', title='TT')


@app.route('/return_json_data', methods=['POST'])
def return_json_data():
    from create_json import take_div_num_to_create_json
    value = request.form.get('value')
    json_data = take_div_num_to_create_json(value)
    # do something with the value
    return render_template('rendon_json.html', json=json_data)


if __name__ == '__main__':
    app.run()
