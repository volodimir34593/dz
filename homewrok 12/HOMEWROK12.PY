from flask import Flask, render_template, request
from wtforms import Form, StringField, PasswordField, validators

app = Flask(__name__)

class RegistrationForm(Form):
    username = StringField('Username', validators=[validators.DataRequired()])
    email = StringField('Email', validators=[validators.DataRequired(), validators.Email()])
    password = PasswordField('Password', validators=[validators.DataRequired()])
    age = StringField('Age')

    class Meta:
        # Валідатор, який дозволяє залишати поля незаповненими
        csrf = False

@app.route('/registration', methods=['GET', 'POST'])
def registration():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        # Отримання даних з форми реєстрації
        username = form.username.data
        email = form.email.data
        password = form.password.data
        age = form.age.data
        
        # Збереження даних або виконання інших необхідних дій
        # ...
        
        return "Registration successful"

    return render_template('registration.html', form=form)

if __name__ == '__main__':
    app.run()
