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

web-app
        clean_years = display_income_statement(symbol=symbol)

        return render_template("is_dashboard.html",
            symbol=symbol,
            clean_years = clean_years


            #zero = ('Fiscal Date Ending: ' + clean_years[0]['fiscalDateEnding']),
            #one = ('Reported Currency: ' + clean_years[0]['reportedCurrency']),
            #two = ('Total Revenue: ' + clean_years[0]['totalRevenue']),
            #three = ('Cost of Revenue: ' + clean_years[0]['costOfRevenue']),
            #four = ('Cost of Goods and Services Sold: ' + clean_years[0]['costofGoodsAndServicesSold']),
            #five = ('Operating Income: ' + clean_years[0]['operatingIncome']),
            #six = ('Selling, General, Administrative: ' + clean_years[0]['sellingGeneralAndAdministrative']),
            #seven = ('Research & Development: ' + clean_years[0]['researchAndDevelopment']),
            #eight = ('Net Investment Income: ' + clean_years[0]['investmentIncomeNet']),
            #nine = ('Interest Income: ' + clean_years[0]['interestIncome']),
            #ten = ('Interest Expense: ' + clean_years[0]['interstExpense']),
            #eleven = ('Non-interest Income: ' + clean_years[0]['nonInterstIncome']),
            #twelve = ('Other Non-Operating Income: ' + clean_years[0]['otherNonOperatingIncome']),
            #thirteen = ('Depreciation: ' + clean_years[0]['depreciation']),
            #fourteen = ('Depreciation and Amortization: ' + clean_years[0]['depreciationAndAmortization']),
            #fifteen = ('Income Before Tax: ' + clean_years[0]['incomeBeforeTax']),
            #sixteen = ('Income Tax Expense: ' + clean_years[0]['incomeTaxExpense']),
            #seventeen = ('Interest and Debt Expense: ' + clean_years[0]['interestAndDebtExpense']),
            #eighteen = ('Net Income From Continuing Operations: ' + clean_years[0]['netIncomeFromContinuingOperations']),
            #nineteen = ('Comprehensive Income Net of Tax: ' + clean_years[0]['comprehensiveIncomeNetOfTax']),
            #twenty = ('EBIT: ' + clean_years[0]['ebit']),
            #twentyone = ('EBITDA: ' + clean_years[0]['ebitda']),
            #twentytwo = ('Net Income: ' + clean_years[0]['netIncome'])

        info = display_income_statement(symbol=symbol)

        return render_template("is_dashboard.html",
            symbol=symbol,
            ics = info
main
        )
    except Exception as err:
        print('OOPS', err)

        return redirect("/home")