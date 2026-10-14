from flask import Flask, render_template, request, redirect

app = Flask(__name__)

expenses = []

@app.route('/')
def home():
    total = sum([e['amount'] for e in expenses])
    return render_template('index.html', expenses=expenses, total=total)

@app.route('/add', methods=['POST'])
def add_expense():
    name = request.form.get('name')
    amount = int(request.form.get('amount'))
    expenses.append({'name': name, 'amount': amount})
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
