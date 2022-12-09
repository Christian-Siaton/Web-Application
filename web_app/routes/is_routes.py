from flask import Blueprint, request, render_template, redirect, flash

from app.display_sheets import display_income_statement, format_usd

is_routes = Blueprint("is_routes", __name__)

@is_routes.route("/is/form")
def is_form():
    print("INCOME STATEMENT FORM...")
    return render_template("is_form.html")

@is_routes.route("/is/dashboard", methods=["GET", "POST"])
def is_dashboard():
    print("INCOME STATEMENT DASHBOARD...")

    if request.method == "POST":
        # for data sent via POST request, form inputs are in request.form:
        request_data = dict(request.form)
        print("FORM DATA:", request_data)
    else:
        # for data sent via GET request, url params are in request.args
        request_data = dict(request.args)
        print("URL PARAMS:", request_data)

    symbol = request_data.get("symbol") or "NFLX"

    try:

        info = display_income_statement(symbol=symbol)

        return render_template("is_dashboard.html",
            symbol=symbol,
            ics = info
        )
    except Exception as err:
        print('OOPS', err)

        return redirect("/home")