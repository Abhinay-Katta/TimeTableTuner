from flask import Flask, render_template, request
app = Flask(__name__,
            static_folder='D:\Projects\TT\static',
            template_folder='D:\Projects\TT\html')


@app.route('/')
def index():
    return render_template('index.html', title='TT')


@app.route('/your/flask/route', methods=['POST'])
def your_function():
    value = request.form.get('value')
    # do something with the value
    return value


if __name__ == '__main__':
    app.run()
