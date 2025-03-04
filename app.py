from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
      <meta charset="UTF-8">
      <title>Donald Odhiambo's Profile</title>
      <!-- Import Roboto font from Google Fonts -->
      <link href="https://fonts.googleapis.com/css?family=Roboto:400,700&display=swap" rel="stylesheet">
      <style>
        body {
          background-color: #2c3e50;
          font-family: 'Roboto', sans-serif;
          color: #ecf0f1;
          margin: 0;
          padding: 0;
          display: flex;
          align-items: center;
          justify-content: center;
          height: 100vh;
        }
        .container {
          text-align: center;
          border: 2px solid #ecf0f1;
          border-radius: 8px;
          padding: 40px;
          background: rgba(44, 62, 80, 0.85);
          box-shadow: 0 4px 15px rgba(0,0,0,0.3);
        }
        .box {
          margin: 20px 0;
          padding: 20px;
          background-color: #34495e;
          border-radius: 5px;
          box-shadow: 0 4px 8px rgba(0,0,0,0.2);
          transition: transform 0.3s ease, background-color 0.3s ease;
        }
        .box:hover {
          transform: translateY(-5px);
          background-color: #3d566e;
        }
      </style>
    </head>
    <body>
      <div class="container">
        <div class="box">Hey Everyone 😎 </div>
        <div class="box">My name is Njaji Sibona Samson </div>
      </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)
