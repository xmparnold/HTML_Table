from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "secret"

list_of_users = [
   {'first_name' : 'Michael', 'last_name' : 'Choi'},
   {'first_name' : 'John', 'last_name' : 'Supsupin'},
   {'first_name' : 'Mark', 'last_name' : 'Guillen'},
   {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

@app.route( "/" )
@app.route( "/home" )
def show_8_by_8_checkerboard():
    return render_template( "index.html", list_of_users = list_of_users )

@app.route( "/<x>" )
def show_custom_rows_checkerboard(x):
    return render_template( "custom_rows_checkerboard.html", x_num = int(x) )

@app.route( "/<x>/<y>" )
def show_custom_checkerboard(x, y):
    return render_template( "custom_checkerboard.html", x_num = int(x), y_num = int(y) )


if __name__ == "__main__":
    app.run(debug = True)