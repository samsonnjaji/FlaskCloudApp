from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Njaji Sibona Samson's Profile</title>
      <!-- Import modern fonts -->
      <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap" rel="stylesheet">
      <!-- Import Font Awesome for icons -->
      <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
      <style>
        :root {
          --primary-color: #3498db;
          --secondary-color: #2c3e50;
          --text-color: #ecf0f1;
          --accent-color: #e74c3c;
          --bg-gradient: linear-gradient(135deg, #2c3e50, #1a252f);
        }
        
        * {
          margin: 0;
          padding: 0;
          box-sizing: border-box;
        }
        
        body {
          background: var(--bg-gradient);
          font-family: 'Poppins', sans-serif;
          color: var(--text-color);
          margin: 0;
          padding: 0;
          display: flex;
          align-items: center;
          justify-content: center;
          min-height: 100vh;
          line-height: 1.6;
        }
        
        .container {
          width: 90%;
          max-width: 800px;
          text-align: center;
          border-radius: 15px;
          padding: 40px;
          background: rgba(44, 62, 80, 0.8);
          box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
          backdrop-filter: blur(10px);
          border: 1px solid rgba(255, 255, 255, 0.1);
          animation: fadeIn 1s ease-in-out;
        }
        
        @keyframes fadeIn {
          from { opacity: 0; transform: translateY(20px); }
          to { opacity: 1; transform: translateY(0); }
        }
        
        .profile-header {
          margin-bottom: 30px;
        }
        
        .profile-title {
          font-size: 2.5rem;
          font-weight: 700;
          margin-bottom: 10px;
          color: var(--primary-color);
          text-shadow: 0px 2px 4px rgba(0, 0, 0, 0.3);
        }
        
        .profile-subtitle {
          font-size: 1.2rem;
          font-weight: 300;
          color: #bdc3c7;
          margin-bottom: 20px;
        }
        
        .avatar {
          width: 150px;
          height: 150px;
          border-radius: 50%;
          border: 4px solid var(--primary-color);
          margin: 0 auto 20px;
          overflow: hidden;
          box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
          position: relative;
          background-color: #34495e;
          display: flex;
          align-items: center;
          justify-content: center;
        }
        
        .avatar-initials {
          font-size: 3rem;
          font-weight: bold;
          color: white;
        }
        
        .box {
          margin: 15px 0;
          padding: 20px;
          background-color: rgba(52, 73, 94, 0.8);
          border-radius: 10px;
          box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
          transition: all 0.3s ease;
          border-left: 4px solid var(--primary-color);
          text-align: left;
          overflow: hidden;
          position: relative;
        }
        
        .box:hover {
          transform: translateY(-5px);
          background-color: rgba(61, 86, 110, 0.9);
          box-shadow: 0 8px 20px rgba(0, 0, 0, 0.3);
        }
        
        .box i {
          margin-right: 10px;
          color: var(--primary-color);
        }
        
        .social-links {
          display: flex;
          justify-content: center;
          margin-top: 30px;
          gap: 15px;
        }
        
        .social-btn {
          display: inline-flex;
          align-items: center;
          justify-content: center;
          width: 50px;
          height: 50px;
          border-radius: 50%;
          background-color: #34495e;
          color: var(--text-color);
          text-decoration: none;
          font-size: 1.5rem;
          transition: all 0.3s ease;
          box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        }
        
        .social-btn:hover {
          transform: translateY(-3px) scale(1.1);
          background-color: var(--primary-color);
          box-shadow: 0 6px 12px rgba(0, 0, 0, 0.3);
        }
        
        .footer {
          margin-top: 40px;
          font-size: 0.9rem;
          color: #95a5a6;
        }
        
        /* Responsive adjustments */
        @media (max-width: 768px) {
          .container {
            width: 95%;
            padding: 30px 20px;
          }
          
          .profile-title {
            font-size: 2rem;
          }
          
          .avatar {
            width: 120px;
            height: 120px;
          }
        }
      </style>
    </head>
    <body>
      <div class="container">
        <div class="profile-header">
          <div class="avatar">
            <div class="avatar-initials">NS</div>
          </div>
          <h1 class="profile-title">Njaji Sibona Samson</h1>
          <p class="profile-subtitle">Web Developer & Designer</p>
        </div>
        
        <div class="box">
          <i class="fas fa-hand-wave"></i>Hey Everyone 😎 Welcome to my profile!
        </div>
        
        <div class="box">
          <i class="fas fa-user"></i>My name is Njaji Sibona Samson. I'm passionate about creating beautiful web experiences.
        </div>
        
        <div class="box">
          <i class="fas fa-code"></i>I work with technologies like Python, Flask, HTML, CSS, and JavaScript.
        </div>
        
    <div class="social-links">
  <a href="https://github.com/samsonnjaji/FlaskCloudApp" class="social-btn" target="_blank">
    <i class="fab fa-github"></i>
  </a>
  <a href="https://www.linkedin.com/in/njaji-sibona-93268128b" class="social-btn" target="_blank">
    <i class="fab fa-linkedin"></i>
  </a>
  <a href="https://twitter.com/kylenjaji" class="social-btn" target="_blank">
    <i class="fab fa-twitter"></i>
  </a>
  <a href="mailto:njajisamson@gmail.com" class="social-btn" target="_blank">
    <i class="fas fa-envelope"></i>
  </a>
</div>

        
        <div class="footer">
          &copy; 2025 Njaji Sibona Samson. All rights reserved.
        </div>
      </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)