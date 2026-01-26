from flask import Flask, render_template_string
import csv
import os

app = Flask(__name__)

@app.route('/')
def home():
    csv_file = '/data/uv_index.csv'
    if not os.path.exists(csv_file):
        return "<h1>No data available</h1>"

    with open(csv_file, newline='') as f:
        reader = csv.reader(f)
        rows = list(reader)
    headers = rows[0] if rows else []
    data = rows[1:] if len(rows) > 1 else []

    html = """
    <h1>UV Index Data</h1>
    <table border="1">
        <tr>{% for h in headers %}<th>{{ h }}</th>{% endfor %}</tr>
        {% for row in data %}
        <tr>{% for cell in row %}<td>{{ cell }}</td>{% endfor %}</tr>
        {% endfor %}
    </table>
    """
    return render_template_string(html, headers=headers, data=data)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
