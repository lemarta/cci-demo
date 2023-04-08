from flask import Flask
app = Flask(__name__)

html = """
    <html>
    <body>
        <div style='text-align:center;font-size:80px;'>
            <iframe src="https://giphy.com/embed/xT9IgG50Fb7Mi0prBC" width="480" height="240" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>
        </div>
    </body>
    </html>"""

@app.route('/')
def hello_world():
    return html

if __name__ == "__main__":
    app.run()