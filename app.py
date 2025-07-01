from flask import Flask, render_template, request, redirect
from db import init_db, get_all_clients, add_client, delete_client, update_client, get_client_by_id

app = Flask(__name__)
init_db()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        license_plate = request.form["license_plate"]
        phone = request.form["phone"]
        brand = request.form["brand"]
        model = request.form["model"]
        expiry_date = request.form["expiry_date"]
        add_client(license_plate, phone, brand, model, expiry_date)
        return redirect("/")

    clients = get_all_clients()
    return render_template("index.html", clients=clients)

@app.route("/delete/<int:client_id>")
def delete(client_id):
    delete_client(client_id)
    return redirect("/")

@app.route("/edit/<int:client_id>", methods=["GET", "POST"])
def edit(client_id):
    if request.method == "POST":
        license_plate = request.form["license_plate"]
        phone = request.form["phone"]
        brand = request.form["brand"]
        model = request.form["model"]
        expiry_date = request.form["expiry_date"]
        update_client(client_id, license_plate, phone, brand, model, expiry_date)
        return redirect("/")

    client = get_client_by_id(client_id)
    return render_template("edit.html", client=client)

if __name__ == "__main__":
    app.run(debug=True)
