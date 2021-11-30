from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/')
def student():
   return render_template('grades.html')


import statistics

@app.route('/result',methods = ['POST', 'GET'])
def result():
    subjects = ['Gymnastics', 'English', 'Maths']
    if request.method == 'POST':
        result = request.form.to_dict()
        average = statistics.mean([float(result[subject]) for subject in subjects])
        result['average'] = f'{average:.2f}'
        return render_template("result.html",result = result)
