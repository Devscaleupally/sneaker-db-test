import os
SNEAKER_API_BASE_URL = os.getenv('API_BASE') or 'http://localhost:4000'

class SneakerAPI:
    price_details = SNEAKER_API_BASE_URL + '/id/{style}/prices'