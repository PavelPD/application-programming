from flask import Flask

app = Flask(__name__)


@app.route("/max_number/<path:number>")
def max_number(number) -> str:
    lst = number.split('/')
    try:
        lst = [int(x) for x in lst]
        return f"Максимальное число: {max(lst)}"
    except:
        return "Передано не числовое значение!"


if __name__ == "__main__":
    app.run(debug=True)