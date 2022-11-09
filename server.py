from cr_app import app
from cr_app.controllers import users_controllers
app.secret_key = "estessecreto"


if __name__=="__main__":
    app.run(debug=True)