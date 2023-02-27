from flask import Blueprint, request, render_template, jsonify, redirect
from utils import sprdsheets

def home():
    """
    # Home page.
     - Searches for Sneaker data from the API.
     - Shows a Modal with the Sneaker data.
     - Button to add the Sneaker to the csv file.
    """
    return render_template('index.html')

def post_details():
    """
    # Details Submitted Page.
     - Save details in Google Spreadsheet
     - Shows a HTML page with `success` message and a link to spreadsheet.
    """
    if request.method != 'POST':
        # redirect to home page
        return redirect('/')
    # get form
    try:
        data = request.form.to_dict()
        res = sprdsheets.upload_data(
            [[
            data['title'],
            data['thumbnail'],
            data['brand'],
            data['colorway'],
            data['price'],
            data['style'],
            data['description'],
            ]],
            'sneakers-data'
        )
        return render_template('success.html', **res)
    except Exception as e:
        print(e)
        return jsonify({
            "success":False,
            "message": 'Error uploading data.'
        }), 500