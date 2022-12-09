from flask import Blueprint, request, render_template, redirect, flash

from app.display_sheets import display_cashflow_statement, format_usd

cs_routes = Blueprint("cs_routes", __name__)

@cs_routes.route("/cs/form")
def cs_form():
    print("CASH FLOW STATEMENT FORM...")
    return render_template("cs_form.html")

@cs_routes.route("/cs/dashboard", methods=["GET", "POST"])
def cs_dashboard():
    print("CASH FLOW STATEMENT DASHBOARD...")

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

        info = display_cashflow_statement(symbol=symbol)
web-app
        #breakpoint()


        formatted_data = [
            {"metric": "NET INCOME", "year_one": 100, "year_two": 200, "year_three": 300, "year_four": 400, "year_five": 500},
            {"metric": "Dividend Payout", "year_one": 100, "year_two": 200, "year_three": 300, "year_four": 400, "year_five": 500},
            {"metric": "Total Cost", "year_one": 100, "year_two": 200, "year_three": 300, "year_four": 400, "year_five": 500},
            {"metric": "Total Revenue", "year_one": 100, "year_two": 200, "year_three": 300, "year_four": 400, "year_five": 500},
            {"metric": "Change in Receivables", "year_one": 100, "year_two": 200, "year_three": 300, "year_four": 400, "year_five": 500},
        ]


        return render_template("cs_dashboard.html",
            symbol=symbol,
            cs = info,
            table_data = formatted_data

        return render_template("cs_dashboard.html",
            symbol=symbol,
            cs = info
main
        )
    except Exception as err:
        print('OOPS', err)

        return redirect("/home")