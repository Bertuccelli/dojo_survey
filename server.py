from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "hush"

# answers = [ {
#     "name" : ['name'] },
# {
#     "location" : ['location'] },
# {
#     "language" : ['language'] },
# {
#     "comment" : ['comment'] } ]

@app.route('/')
@app.route('/survey')
def survey():
    return render_template("form.html")

@app.route('/survey', methods=['POST'])
def process():
    print(request.form)
    if result == None:
        return redirect("/survey")
    else:
        session['name'] = request.form['name']
        session['location'] = request.form['location']
        session['language'] = request.form['language']
        session['comment'] = request.form['comment']
        return redirect("/results")

    # answers.append(userInput)

@app.route('/results')
def result():
    return render_template("results.html") 

if __name__ == "__main__":
    app.run(debug=True)