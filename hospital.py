from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField


app=Flask(__name__)
@app.route('/')
def index():
    return render_template('design.html')


class ReusableForm(Form):
    name = TextField('Patient Name:', validators=[validators.required()])
    age = TextField('Patient Age:', validators=[validators.required(), validators.Length(min=6, max=35)])
    doctor = TextField('doctor:', validators=[validators.required(), validators.Length(min=3, max=35)])

    @app.route("/", methods=['GET', 'POST'])
    def hello():
        form = ReusableForm(request.form)

        print
        form.errors
        if request.method == 'POST':
            name = request.form['Patient Name']
            age = request.form['Patient Age']
            doctor = request.form['doctor']
            print
            name, " ",age , " ", doctor

        if form.validate():
            # Save the comment here.
            flash('Thanks for registration ' + name)
        else:
            flash('Error: All the form fields are required. ')

        return render_template('design.html', form=form)


if __name__ == "__main__":
    app.run()

