# app.py - ILTOLISH MARA SCHOOLS Website Generator
# Run: python app.py

html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>ILTOLISH MARA SCHOOLS - Education with Nature</title>
<script src="https://cdn.tailwindcss.com"></script>
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;700&display=swap" rel="stylesheet">
<style>body{font-family:'Outfit',sans-serif}</style>
</head>
<body class="bg-amber-50">

<!-- HEADER -->
<header class="bg-green-900 text-white p-6 text-center">
  <h1 class="text-3xl md:text-5xl font-bold">ILTOLISH MARA SCHOOLS</h1>
  <p class="mt-2 text-amber-200">P.O Box 322, Kilgoris | Trans Mara South</p>
  <p class="mt-1 text-sm">Day & Boarding | Mixed | Playgroup - Grade 9 | CBE Curriculum</p>
</header>

<!-- HERO -->
<div class="relative bg-green-800 text-white text-center py-16 px-4">
  <h2 class="text-4xl font-bold">Quality CBE Education</h2>
  <p class="mt-4 text-xl italic max-w-3xl mx-auto">"Where Education Meets Nature, Knowledge Finds Its Roots, and Children Grow Like the Mara Savanna."</p>
  <p class="mt-2 text-amber-300">Overlooking the Majestic Maasai Mara National Reserve</p>
  <button class="mt-6 bg-amber-500 text-green-900 px-8 py-3 rounded-full font-bold">Admissions Open 2026</button>
</div>

<!-- FEATURES -->
<section class="grid md:grid-cols-3 gap-6 p-8 max-w-6xl mx-auto">
  <div class="bg-white p-6 rounded-xl shadow">
    <h3 class="font-bold text-green-900 text-xl">🔬 Science & Computer Labs</h3>
    <p class="mt-2 text-gray-600">Well equipped modern laboratories for practical CBE learning.</p>
  </div>
  <div class="bg-white p-6 rounded-xl shadow">
    <h3 class="font-bold text-green-900 text-xl">🍽️ Multipurpose Dining Hall</h3>
    <p class="mt-2 text-gray-600">Spacious, clean and modern dining facility for all learners.</p>
  </div>
  <div class="bg-white p-6 rounded-xl shadow">
    <h3 class="font-bold text-green-900 text-xl">🏫 Day & Boarding</h3>
    <p class="mt-2 text-gray-600">Mixed school offering flexible day and secure boarding facilities.</p>
  </div>
</section>

<!-- QUOTE SECTION -->
<section class="bg-amber-100 py-12 text-center px-4">
  <h2 class="text-3xl font-bold text-green-900">Education with Nature, of Course Knowledge</h2>
  <p class="mt-4 text-lg text-gray-700 max-w-2xl mx-auto">"We don't just teach books, we teach life. Surrounded by the Maasai Mara, our children learn to conserve, to create, and to compete globally."</p>
  <p class="mt-4 font-bold">- Director, Iltolish Mara Schools</p>
</section>

<footer class="bg-green-900 text-white text-center p-6">
  <p>© 2026 Iltolish Mara Schools | Trans Mara South | Call: 07XX XXX XXX</p>
  <p class="text-amber-200 text-sm mt-1">Playgroup to Grade 9 - CBE Competency Based Education</p>
</footer>

</body>
</html>
"""

# Save file
with open("iltolish_mara.html", "w", encoding="utf-8") as f:
    f.write(html_code)

print("✅ Website created successfully!")
print("📁 File: iltolish_mara.html")
print("👉 Now double-click the file to open in your phone/computer browser")
