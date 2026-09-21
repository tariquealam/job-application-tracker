from flask import Flask, request, render_template_string

app = Flask(__name__)
jobs = []
PAGE = """<h1>Job Application Tracker</h1><form method='post'><input name='company' placeholder='Company' required><input name='role' placeholder='Role' required><select name='status'><option>Applied</option><option>Interview</option><option>Offer</option></select><button>Add</button></form><table border='1'><tr><th>Company</th><th>Role</th><th>Status</th></tr>{% for j in jobs %}<tr><td>{{j['company']}}</td><td>{{j['role']}}</td><td>{{j['status']}}</td></tr>{% endfor %}</table>"""

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST': jobs.append(request.form.to_dict())
    return render_template_string(PAGE, jobs=jobs)

if __name__ == '__main__': app.run(debug=True)
