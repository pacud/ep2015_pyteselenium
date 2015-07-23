# coding: utf8
from flask import (
    Flask,
    render_template,
    request,
)


app = Flask('mini_flask_app')
app.secret_key = 'VNkpP9k7'
debug = True


@app.route('/test_page', methods=['GET', 'POST'])
def test_page():
    if request.method == 'POST':
        search = request.form['my_input']
        return render_template('test_page.html', search_text=search)
    return render_template('test_page.html')

if __name__ == '__main__':
    app.run(debug=debug)
