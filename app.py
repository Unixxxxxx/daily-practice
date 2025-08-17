from flask import Flaks

app =(__name__)

@app.route('/')
def index():
    return "me"

if __neme__ == '__main__':
    app.run(debug=True)
