from flask import Flask
import subprocess
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import InputRequired, NumberRange

app = Flask(__name__)

class CodeForm(FlaskForm):
    code = StringField(validators=[InputRequired()])
    timeout = IntegerField(validators=[NumberRange(min=1, max=30)])

@app.route('/run_code', methods=["POST"])
def run_code():
    form = CodeForm()

    if form.validate_on_submit():
        code, timeout = form.code.data, form.timeout.data

        r = subprocess.Popen(["prlimit", "--nproc=1:1", "python", "-c", code],
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        try:
            output, errors = r.communicate(timeout=timeout)
            if errors:
                return errors
            return output
        except Exception:
            r.kill()
            raise ValueError("Timeout reached")

    return f"Invalid input: {form.errors}", 400


if __name__ == "__main__":
    app.config["WTF_CSRF_ENABLED"] = False
    app.run()