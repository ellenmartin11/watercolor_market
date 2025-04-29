
from flask import Flask, render_template, request, redirect, url_for, session


class Product:
    def __init__(self, id, title, description, price, image):
        self.id = id
        self.title = title
        self.description = description
        self.price = price
        self.image = image


app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for session cart

# Sample watercolor prints
products = [
    Product(1, "State Street", "Restaurants on State Street", 8, "static/images/statestreet.jpg"),
    Product(2, "1195 Chapel Street", "The back of 1195 Chapel Street", 8, "static/images/1195 chapel street.jpg"),
    Product(3, "Law Firm", "Law firm", 8, "static/images/lawfirm.jpg"),
]

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/marketplace')
def marketplace():
    return render_template('marketplace.html', products=products)

# More routes like add-to-cart, view-cart can come later!

if __name__ == '__main__':
    app.run(debug=True)





