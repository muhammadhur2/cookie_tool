from flask import Flask, request, render_template, make_response
from flask.sessions import SecureCookieSessionInterface

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        secret_key = request.form['secret_key']
        user_id = request.form['user_id']

        app.secret_key = secret_key
        with app.test_request_context('/'):
            session = {'user_id': user_id}
            
            cookie = SecureCookieSessionInterface().get_signing_serializer(app).dumps(session)

            # Render the cookie display template with the generated cookie
            return render_template('cookie_display.html', cookie=cookie)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
