from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return """
<!DOCTYPE html>
<html>
<head><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Iltolish Mara Schools</title>
<script src="https://cdn.tailwindcss.com"></script>
</head>
<body>
<div style="background:#14532d;color:white;text-align:center;padding:60px">
<h1 style="font-size:40px;font-weight:900">ILTOLISH MARA SCHOOLS</h1>
<p>Where Education Meets Nature</p>
<p>P.O Box 322 Kilgoris - Trans Mara South</p>
</div>
<div style="text-align:center;padding:30px">
<h2>Playgroup - PP2 - Grade 1-9 | CBE</h2>
<p>Day & Boarding | Mixed | Science Lab | Computer Lab</p>
</div>
</body>
</html>
    """

if __name__ == '__main__':
    app.run()
