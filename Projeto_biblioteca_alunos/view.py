from main import app
@app.router("/")
def homepage():
    return "site"