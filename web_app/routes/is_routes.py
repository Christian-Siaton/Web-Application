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

        info= display_income_statement(symbol=symbol)




        formatted_data = [
            {"metric": "Fiscal Date Ending", "year_one": info[0]["Fiscal Date Ending"], "year_two": info[1]['Fiscal Date Ending'], "year_three": info[2]['Fiscal Date Ending'], "year_four": info[3]['Fiscal Date Ending'], "year_five": info[4]['Fiscal Date Ending']},
            {"metric": "Reported Currency", "year_one": info[0]["Reported Currency"], "year_two": info[1]['Reported Currency'], "year_three": info[2]['Reported Currency'], "year_four": info[3]['Reported Currency'], "year_five": info[4]['Reported Currency']},
            {"metric": "Total Revenue", "year_one": info[0]["Total Revenue"], "year_two": info[1]['Total Revenue'], "year_three": info[2]['Total Revenue'], "year_four": info[3]['Total Revenue'], "year_five": info[4]['Total Revenue']},
            {"metric": "Cost of Revenue", "year_one": info[0]["Cost of Revenue"], "year_two": info[1]['Cost of Revenue'], "year_three": info[2]['Cost of Revenue'], "year_four": info[3]['Cost of Revenue'], "year_five": info[4]['Cost of Revenue']},
            {"metric": "Cost of Goods and Services Sold", "year_one": info[0]["Cost of Goods and Services Sold"], "year_two": info[1]['Cost of Goods and Services Sold'], "year_three": info[2]['Cost of Goods and Services Sold'], "year_four": info[3]['Cost of Goods and Services Sold'], "year_five": info[4]['Cost of Goods and Services Sold']},
            {"metric": "Operating Income", "year_one": info[0]["Operating Income"], "year_two": info[1]['Operating Income'], "year_three": info[2]['Operating Income'], "year_four": info[3]['Operating Income'], "year_five": info[4]['Operating Income']},
            {"metric": "Selling, General, Administrative", "year_one": info[0]["Selling, General, Administrative"], "year_two": info[1]['Selling, General, Administrative'], "year_three": info[2]['Selling, General, Administrative'], "year_four": info[3]['Selling, General, Administrative'], "year_five": info[4]['Selling, General, Administrative']},
            {"metric": "Research & Development", "year_one": info[0]["Research & Development"], "year_two": info[1]['Research & Development'], "year_three": info[2]['Research & Development'], "year_four": info[3]['Research & Development'], "year_five": info[4]['Research & Development']},
            {"metric": "Net Investment Income", "year_one": info[0]["Net Investment Income"], "year_two": info[1]['Net Investment Income'], "year_three": info[2]['Net Investment Income'], "year_four": info[3]['Net Investment Income'], "year_five": info[4]['Net Investment Income']},
            {"metric": "Interest Income", "year_one": info[0]["Interest Income"], "year_two": info[1]['Interest Income'], "year_three": info[2]['Interest Income'], "year_four": info[3]['Interest Income'], "year_five": info[4]['Interest Income']},
            {"metric": "Interest Expense", "year_one": info[0]["Interest Expense"], "year_two": info[1]['Interest Expense'], "year_three": info[2]['Interest Expense'], "year_four": info[3]['Interest Expense'], "year_five": info[4]['Interest Expense']},
            {"metric": "Non-interest Income", "year_one": info[0]["Non-interest Income"], "year_two": info[1]['Non-interest Income'], "year_three": info[2]['Non-interest Income'], "year_four": info[3]['Non-interest Income'], "year_five": info[4]['Non-interest Income']},
            {"metric": "Other Non-Operating Income", "year_one": info[0]["Other Non-Operating Income"], "year_two": info[1]['Other Non-Operating Income'], "year_three": info[2]['Other Non-Operating Income'], "year_four": info[3]['Other Non-Operating Income'], "year_five": info[4]['Other Non-Operating Income']},
            {"metric": "Depreciation", "year_one": info[0]["Depreciation"], "year_two": info[1]['Depreciation'], "year_three": info[2]['Depreciation'], "year_four": info[3]['Depreciation'], "year_five": info[4]['Depreciation']},
            {"metric": "Depreciation and Amortization", "year_one": info[0]["Depreciation and Amortization"], "year_two": info[1]['Depreciation and Amortization'], "year_three": info[2]['Depreciation and Amortization'], "year_four": info[3]['Depreciation and Amortization'], "year_five": info[4]['Depreciation and Amortization']},
            {"metric": "Income Before Tax", "year_one": info[0]["Income Before Tax"], "year_two": info[1]['Income Before Tax'], "year_three": info[2]['Income Before Tax'], "year_four": info[3]['Income Before Tax'], "year_five": info[4]['Income Before Tax']},
            {"metric": "Income Tax Expense", "year_one": info[0]["Income Tax Expense"], "year_two": info[1]['Income Tax Expense'], "year_three": info[2]['Income Tax Expense'], "year_four": info[3]['Income Tax Expense'], "year_five": info[4]['Income Tax Expense']},
            {"metric": "Interest and Debt Expense", "year_one": info[0]["Interest and Debt Expense"], "year_two": info[1]['Interest and Debt Expense'], "year_three": info[2]['Interest and Debt Expense'], "year_four": info[3]['Interest and Debt Expense'], "year_five": info[4]['Interest and Debt Expense']},
            {"metric": "Net Income From Continuing Operations", "year_one": info[0]["Net Income From Continuing Operations"], "year_two": info[1]['Net Income From Continuing Operations'], "year_three": info[2]['Net Income From Continuing Operations'], "year_four": info[3]['Net Income From Continuing Operations'], "year_five": info[4]['Net Income From Continuing Operations']},
            {"metric": "Comprehensive Income Net of Tax", "year_one": info[0]["Comprehensive Income Net of Tax"], "year_two": info[1]['Comprehensive Income Net of Tax'], "year_three": info[2]['Comprehensive Income Net of Tax'], "year_four": info[3]['Comprehensive Income Net of Tax'], "year_five": info[4]['Comprehensive Income Net of Tax']},
            {"metric": "EBIT", "year_one": info[0]["EBIT"], "year_two": info[1]['EBIT'], "year_three": info[2]['EBIT'], "year_four": info[3]['EBIT'], "year_five": info[4]['EBIT']},
            {"metric": "EBITDA", "year_one": info[0]["EBITDA"], "year_two": info[1]['EBITDA'], "year_three": info[2]['EBITDA'], "year_four": info[3]['EBITDA'], "year_five": info[4]['EBITDA']},
            {"metric": "Net Income", "year_one": info[0]["Net Income"], "year_two": info[1]['Net Income'], "year_three": info[2]['Net Income'], "year_four": info[3]['Net Income'], "year_five": info[4]['Net Income']},

        ]





        clean_years = display_income_statement(symbol=symbol)
        
        return render_template("is_dashboard.html",
            symbol=symbol,
            table_data = formatted_data

        

            
        )
    except Exception as err:
        print('OOPS', err)

        return redirect("/home")