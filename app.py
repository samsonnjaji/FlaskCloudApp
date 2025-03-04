from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
      <meta charset="UTF-8">
      <title>Njaji Sibona's Profile</title>
      <!-- Google Font -->
      <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap" rel="stylesheet">
      <style>
        body {
          margin: 0;
          padding: 0;
          font-family: 'Poppins', sans-serif;
          background: linear-gradient(135deg, #667eea, #764ba2);
          color: #fff;
          display: flex;
          align-items: center;
          justify-content: center;
          min-height: 100vh;
        }
        .container {
          width: 90%;
          max-width: 600px;
          background: rgba(0, 0, 0, 0.5);
          border-radius: 10px;
          box-shadow: 0 4px 15px rgba(0,0,0,0.2);
          padding: 30px;
          text-align: center;
        }
        .box {
          background: rgba(255, 255, 255, 0.1);
          padding: 15px;
          margin: 10px 0;
          border-radius: 5px;
          transition: transform 0.2s ease, background 0.2s ease;
        }
        .box:hover {
          transform: scale(1.02);
          background: rgba(255, 255, 255, 0.2);
        }
      </style>
    </head>
    <body>
      <div class="container">
        <div class="box">Hello</div>
        <div class="box">My name is Njaji Sibona S</div>
        <div class="box">Reg. No: 23/05541</div>
        <div class="box">BSD</div>
      </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)
