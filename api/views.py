from flask import jsonify
from flask import request
import requests
from utils.vars import SneakerAPI


def get_sneaker(style):
    """Get data from the API."""
    # replace SPACE with "-" in the style
    style = style.replace(" ", "-")
    # Get the data from the API
    url = SneakerAPI.price_details.format(style=style)
    response = requests.get(url)
    if response.text == 'Product Not Found':
        return jsonify({'error': 'Sneaker not found.', 'success': False})
    # Get the data as JSON
    data = response.json()
    # Return the data as JSON
    return jsonify({
        'data': data,
        'success': True
    })