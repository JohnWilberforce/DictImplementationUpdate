from __future__ import print_function
import sys
from gyinyase import app
from flask import render_template, request, redirect, jsonify
from gyinyase.models import Items


@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        while True:
            req = request.form
            vehicle_no = req.get("vehicle")  # the key is the name'vehicle' in the
        # home.html forms which returns what user input
            items = Items.query.all()
            req1 = request.form.get('vehicle').upper()
            for item in Items.query.filter_by(vehicle_no=req1):
                response = item.name + " : " + "  " + item.contact
                if item.name or item.contact:
                    return render_template('home.html', res=response)
                break
            else:
                read = 'NOT FOUND PLEASE TRY AGAIN'
                return render_template('home.html', read=read)



    if request.method == "GET":
        redirect('/')
    return render_template('home.html')


@app.route('/number', methods=["GET", "POST"])
def number():
    items = Items.query.all()
    if request.method == "POST":
        for item in Items.query.filter_by(vehicle_no=request.form.get('vehicle')):
            print(jsonify(item.name, item.contact))
            return jsonify(item.name, item.contact)
    else:
        print('success', 200)
