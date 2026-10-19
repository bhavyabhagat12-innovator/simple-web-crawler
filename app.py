from flask import Flask, request, render_template_string
from crawler import crawl

app = Flask(__name__)

PAGE = """
<!doctype html>
<html>
<head>
  <title>Simple Web Crawler</title>
  <style>
    body { font-family: sans-serif; max-width: 700px; margin: 40px auto; padding: 0 16px; }
    input[type=text] { width: 70%; padding: 8px; }
    button { padding: 8px 16px; }
    li { margin-bottom: 8px; }
    .error { color: #b00020; }
  </style>
</head>
<body>
  <h1>Simple Web Crawler</h1>
  <form method="post">
    <input type="text" name="url" placeholder="https://books.toscrape.com" value="{{ url }}" required>
    <button type="submit">Crawl</button>
  </form>

  {% if error %}
    <p class="error">{{ error }}</p>
  {% endif %}

  {% if results %}
    <h2>Crawled {{ results|length }} pages</h2>
    <ol>
      {% for page in results %}
        <li><strong>{{ page.title }}</strong><br><a href="{{ page.url }}" target="_blank">{{ page.url }}</a></li>
      {% endfor %}
    </ol>
  {% endif %}
</body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def home():
    results, error, url = None, None, ""
    if request.method == "POST":
        url = request.form["url"].strip()
        if not url.startswith(("http://", "https://")):
            error = "Please enter a URL starting with http:// or https://"
        else:
            results = crawl(url, max_pages=10)
            if not results:
                error = "Could not crawl that URL."
    return render_template_string(PAGE, results=results, error=error, url=url)


if __name__ == "__main__":
    app.run(debug=True)