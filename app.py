from flask import Flask,render_template
app = Flask(__name__)
@app.route('/')
def Home():
    return render_template('Home.html')
@app.route('/about')
def aboutUs():
    return render_template('about us.html')
@app.route('/contact.html')
def contact():
    return render_template('contact.html')
@app.route('/service')
def service():
    return render_template('service.html')
@app.route('/gallery')
def gallery():
    return render_template('gallery.html')
@app.route('/Login')
def Login():
    return render_template('login.html')
@app.route('/Registration')
def Registration():
    return render_template('registration.html')
@app.route('/Contact')
def Contact():
    return render_template('Contact.html')
if __name__ == '__main__':
    app.run(debug=True)
