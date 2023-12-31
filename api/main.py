from flask import Flask, request, render_template, make_response
from flask.sessions import SecureCookieSessionInterface

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get data from form
        secret_key = request.form['secret_key']
        user_id = request.form['user_id']

        # Set the secret key and create a session
        app.secret_key = secret_key
        with app.test_request_context('/'):
            session = {'user_id': user_id}
            
            # Serialize the session into a cookie
            cookie = SecureCookieSessionInterface().get_signing_serializer(app).dumps(session)

            # Show the generated cookie
            response = make_response(f"Generated Cookie: {cookie}")
            return response

    # Render the HTML form
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
