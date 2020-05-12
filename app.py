from flask import Flask, render_template,request, redirect, url_for, flash
app = Flask(__name__)

if __name__ == "__main__":
    app.run()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/inventories')
def inventories():
    return render_template('inventories.html')


@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

@app.route('/visuals')
def visuals():
    return render_template('visuals.html')