from flask import Blueprint, request, render_template, redirect, flash

from app.display_sheets import display_balance_sheet, format_usd

bs_routes = Blueprint("bs_routes", __name__)

@bs_routes.route("/bs/form")
def bs_form():
    print("BALANCE SHEET FORM...")
    return render_template("bs_form.html")

@bs_routes.route("/bs/dashboard", methods=["GET", "POST"])
def bs_dashboard():
    print("BALANCE SHEET DASHBOARD...")

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

        clean_years = display_balance_sheet(symbol=symbol)
        for year in clean_years:
            for item in year:
                print (item + ":", year[item])
            print('')
            print('-----------------------------------------')
            print('')


        return render_template("bs_dashboard.html",
            symbol=symbol,
            bs = clean_years
            
        )
    except Exception as err:
        print('OOPS', err)

        return redirect("/home")