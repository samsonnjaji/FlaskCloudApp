from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
      <meta charset="UTF-8">
      <title>Njaji Sibona's Info</title>
      <style>
        body {
          font-family: Arial, sans-serif;
          background-color: #f9f9f9;
          margin: 20px;
        }
        .box {
          border: 1px solid #ccc;
          padding: 15px;
          margin: 10px 0;
          background-color: #fff;
          transition: background-color 0.3s ease, border-color 0.3s ease;
        }
        .box:hover {
          background-color: #e6f7ff;
          border-color: #66b3ff;
        }
      </style>
    </head>
    <body>
      <div class="box">Hello</div>
      <div class="box">My name is Njaji Sibona Samson</div>
      <div class="box">Reg. No: 23/05541</div>
      <div class="box">BSD</div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)
