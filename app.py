from flask import Flask, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <html>
    <body>
        <header>
            <h1>Merle's First Publish</h1>
        </header>
        <main>
            <p>Here we go</p>
            <img src="merles_image.png" alt="This is a good timet">
            
            <!-- Entry form starts here -->
            <form action="/submit" method="post">
                <label for="name">Name:</label>
                <input type="text" id="name" name="name" required><br><br>
                
                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required><br><br>
                
                <label for="message">Message:</label><br>
                <textarea id="message" name="message" rows="4" cols="50" required></textarea><br><br>
                
                <button type="submit">Submit</button>
            </form>
            <!-- Entry form ends here -->
            
        </main>
        <footer>
            <p> 2025, Baby!</p>
        </footer>
    </body>
    </html>
    '''

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    
    with open('list_of_users.txt', 'a') as f:
        f.write(f"{name},{email},{message}\n")
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)