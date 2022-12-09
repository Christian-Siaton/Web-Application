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

        info = display_balance_sheet(symbol=symbol)



        formatted_data = [
            {"metric": "Fiscal Date Ending", "year_one": info[0]["Fiscal Date Ending"], "year_two": info[1]['Fiscal Date Ending'], "year_three": info[2]['Fiscal Date Ending'], "year_four": info[3]['Fiscal Date Ending'], "year_five": info[4]['Fiscal Date Ending']},
            {"metric": "Reported Currency", "year_one": info[0]["Reported Currency"], "year_two": info[1]['Reported Currency'], "year_three": info[2]['Reported Currency'], "year_four": info[3]['Reported Currency'], "year_five": info[4]['Reported Currency']},
            {"metric": "TOTAL ASSETS", "year_one": info[0]["TOTAL ASSETS"], "year_two": info[1]['TOTAL ASSETS'], "year_three": info[2]['TOTAL ASSETS'], "year_four": info[3]['TOTAL ASSETS'], "year_five": info[4]['TOTAL ASSETS']},
            {"metric": "TOTAL CURRENT ASSETS", "year_one": info[0]["TOTAL CURRENT ASSETS"], "year_two": info[1]['TOTAL CURRENT ASSETS'], "year_three": info[2]['TOTAL CURRENT ASSETS'], "year_four": info[3]['TOTAL CURRENT ASSETS'], "year_five": info[4]['TOTAL CURRENT ASSETS']},
            {"metric": "Cash and Cash Equivalents", "year_one": info[0]["Cash and Cash Equivalents"], "year_two": info[1]['Cash and Cash Equivalents'], "year_three": info[2]['Cash and Cash Equivalents'], "year_four": info[3]['Cash and Cash Equivalents'], "year_five": info[4]['Cash and Cash Equivalents']},
            {"metric": "Cash and Short Term Investments", "year_one": info[0]["Cash and Short Term Investments"], "year_two": info[1]['Cash and Short Term Investments'], "year_three": info[2]['Cash and Short Term Investments'], "year_four": info[3]['Cash and Short Term Investments'], "year_five": info[4]['Cash and Short Term Investments']},
            {"metric": "Inventory", "year_one": info[0]["Inventory"], "year_two": info[1]['Inventory'], "year_three": info[2]['Inventory'], "year_four": info[3]['Inventory'], "year_five": info[4]['Inventory']},
            {"metric": "Current Net Receivables", "year_one": info[0]["Current Net Receivables"], "year_two": info[1]['Current Net Receivables'], "year_three": info[2]['Current Net Receivables'], "year_four": info[3]['Current Net Receivables'], "year_five": info[4]['Current Net Receivables']},
            {"metric": "TOTAL NONCURRENT ASSETS", "year_one": info[0]["TOTAL NONCURRENT ASSETS"], "year_two": info[1]['TOTAL NONCURRENT ASSETS'], "year_three": info[2]['TOTAL NONCURRENT ASSETS'], "year_four": info[3]['TOTAL NONCURRENT ASSETS'], "year_five": info[4]['TOTAL NONCURRENT ASSETS']},
            {"metric": "Property Plant & Equipment", "year_one": info[0]["Property Plant & Equipment"], "year_two": info[1]['Property Plant & Equipment'], "year_three": info[2]['Property Plant & Equipment'], "year_four": info[3]['Property Plant & Equipment'], "year_five": info[4]['Property Plant & Equipment']},
            {"metric": "Accumulated Depreciation & Amortization", "year_one": info[0]["Accumulated Depreciation & Amortization"], "year_two": info[1]['Accumulated Depreciation & Amortization'], "year_three": info[2]['Accumulated Depreciation & Amortization'], "year_four": info[3]['Accumulated Depreciation & Amortization'], "year_five": info[4]['Accumulated Depreciation & Amortization']},
            {"metric": "Intangible Assets", "year_one": info[0]["Intangible Assets"], "year_two": info[1]['Intangible Assets'], "year_three": info[2]['Intangible Assets'], "year_four": info[3]['Intangible Assets'], "year_five": info[4]['Intangible Assets']},
            {"metric": "Intangible Assets Excluding Goodwill", "year_one": info[0]["Intangible Assets Excluding Goodwill"], "year_two": info[1]['Intangible Assets Excluding Goodwill'], "year_three": info[2]['Intangible Assets Excluding Goodwill'], "year_four": info[3]['Intangible Assets Excluding Goodwill'], "year_five": info[4]['Intangible Assets Excluding Goodwill']},
            {"metric": "Goodwill", "year_one": info[0]["Goodwill"], "year_two": info[1]['Goodwill'], "year_three": info[2]['Goodwill'], "year_four": info[3]['Goodwill'], "year_five": info[4]['Goodwill']},
            {"metric": "Investments", "year_one": info[0]["Investments"], "year_two": info[1]['Investments'], "year_three": info[2]['Investments'], "year_four": info[3]['Investments'], "year_five": info[4]['Investments']},
            {"metric": "Long Term Investments", "year_one": info[0]["Long Term Investments"], "year_two": info[1]['Long Term Investments'], "year_three": info[2]['Long Term Investments'], "year_four": info[3]['Long Term Investments'], "year_five": info[4]['Long Term Investments']},
            {"metric": "Short Term Investments", "year_one": info[0]["Short Term Investments"], "year_two": info[1]['Short Term Investments'], "year_three": info[2]['Short Term Investments'], "year_four": info[3]['Short Term Investments'], "year_five": info[4]['Short Term Investments']},
            {"metric": "Other Current Assets", "year_one": info[0]["Other Current Assets"], "year_two": info[1]['Other Current Assets'], "year_three": info[2]['Other Current Assets'], "year_four": info[3]['Other Current Assets'], "year_five": info[4]['Other Current Assets']},
            {"metric": "Other Noncurrent Assets", "year_one": info[0]["Other Noncurrent Assets"], "year_two": info[1]['Other Noncurrent Assets'], "year_three": info[2]['Other Noncurrent Assets'], "year_four": info[3]['Other Noncurrent Assets'], "year_five": info[4]['Other Noncurrent Assets']},
            {"metric": "TOTAL LIABILITIES", "year_one": info[0]["TOTAL LIABILITIES"], "year_two": info[1]['TOTAL LIABILITIES'], "year_three": info[2]['TOTAL LIABILITIES'], "year_four": info[3]['TOTAL LIABILITIES'], "year_five": info[4]['TOTAL LIABILITIES']},
            {"metric": "TOTAL CURRENT LIABILITIES", "year_one": info[0]["TOTAL CURRENT LIABILITIES"], "year_two": info[1]['TOTAL CURRENT LIABILITIES'], "year_three": info[2]['TOTAL CURRENT LIABILITIES'], "year_four": info[3]['TOTAL CURRENT LIABILITIES'], "year_five": info[4]['TOTAL CURRENT LIABILITIES']},
            {"metric": "Current Accounts Payable", "year_one": info[0]["Current Accounts Payable"], "year_two": info[1]['Current Accounts Payable'], "year_three": info[2]['Current Accounts Payable'], "year_four": info[3]['Current Accounts Payable'], "year_five": info[4]['Current Accounts Payable']},
            {"metric": "Deferred Revenue", "year_one": info[0]["Deferred Revenue"], "year_two": info[1]['Deferred Revenue'], "year_three": info[2]['Deferred Revenue'], "year_four": info[3]['Deferred Revenue'], "year_five": info[4]['Deferred Revenue']},
            {"metric": "Current Debt", "year_one": info[0]["Current Debt"], "year_two": info[1]['Current Debt'], "year_three": info[2]['Current Debt'], "year_four": info[3]['Current Debt'], "year_five": info[4]['Current Debt']},
            {"metric": "Short Term Debt", "year_one": info[0]["Short Term Debt"], "year_two": info[1]['Short Term Debt'], "year_three": info[2]['Short Term Debt'], "year_four": info[3]['Short Term Debt'], "year_five": info[4]['Short Term Debt']},
            {"metric": "TOTAL NONCURRENT LIABILITIES", "year_one": info[0]["TOTAL NONCURRENT LIABILITIES"], "year_two": info[1]['TOTAL NONCURRENT LIABILITIES'], "year_three": info[2]['TOTAL NONCURRENT LIABILITIES'], "year_four": info[3]['TOTAL NONCURRENT LIABILITIES'], "year_five": info[4]['TOTAL NONCURRENT LIABILITIES']},
            {"metric": "Capital Lease Obligations", "year_one": info[0]["Capital Lease Obligations"], "year_two": info[1]['Capital Lease Obligations'], "year_three": info[2]['Capital Lease Obligations'], "year_four": info[3]['Capital Lease Obligations'], "year_five": info[4]['Capital Lease Obligations']},
            {"metric": "Long Term Debt", "year_one": info[0]["Long Term Debt"], "year_two": info[1]['Long Term Debt'], "year_three": info[2]['Long Term Debt'], "year_four": info[3]['Long Term Debt'], "year_five": info[4]['Long Term Debt']},
            {"metric": "Current Long Term Debt", "year_one": info[0]["Current Long Term Debt"], "year_two": info[1]['Current Long Term Debt'], "year_three": info[2]['Current Long Term Debt'], "year_four": info[3]['Current Long Term Debt'], "year_five": info[4]['Current Long Term Debt']},
            {"metric": "Noncurrent Long Term Debt", "year_one": info[0]["Noncurrent Long Term Debt"], "year_two": info[1]['Noncurrent Long Term Debt'], "year_three": info[2]['Noncurrent Long Term Debt'], "year_four": info[3]['Noncurrent Long Term Debt'], "year_five": info[4]['Noncurrent Long Term Debt']},
            {"metric": "Total Debtg", "year_one": info[0]["Total Debt"], "year_two": info[1]['Total Debt'], "year_three": info[2]['Total Debt'], "year_four": info[3]['Total Debt'], "year_five": info[4]['Total Debt']},
            {"metric": "Other Current Liabilities", "year_one": info[0]["Other Current Liabilities"], "year_two": info[1]['Other Current Liabilities'], "year_three": info[2]['Other Current Liabilities'], "year_four": info[3]['Other Current Liabilities'], "year_five": info[4]['Other Current Liabilities']},
            {"metric": "TOTAL SHAREHOLDER EQUITY", "year_one": info[0]["TOTAL SHAREHOLDER EQUITY"], "year_two": info[1]['TOTAL SHAREHOLDER EQUITY'], "year_three": info[2]['TOTAL SHAREHOLDER EQUITY'], "year_four": info[3]['TOTAL SHAREHOLDER EQUITY'], "year_five": info[4]['TOTAL SHAREHOLDER EQUITY']},
            {"metric": "Treasury Stock", "year_one": info[0]["Treasury Stock"], "year_two": info[1]['Treasury Stock'], "year_three": info[2]['Treasury Stock'], "year_four": info[3]['Treasury Stock'], "year_five": info[4]['Treasury Stock']},
            {"metric": "Retained Earnings", "year_one": info[0]["Retained Earnings"], "year_two": info[1]['Retained Earnings'], "year_three": info[2]['Retained Earnings'], "year_four": info[3]['Retained Earnings'], "year_five": info[4]['Retained Earnings']},
            {"metric": "Common Stock", "year_one": info[0]["Common Stock"], "year_two": info[1]['Common Stock'], "year_three": info[2]['Common Stock'], "year_four": info[3]['Common Stock'], "year_five": info[4]['Common Stock']},
            {"metric": "Common Stock Shares Outstanding", "year_one": info[0]["Common Stock Shares Outstanding"], "year_two": info[1]['Common Stock Shares Outstanding'], "year_three": info[2]['Common Stock Shares Outstanding'], "year_four": info[3]['Common Stock Shares Outstanding'], "year_five": info[4]['Common Stock Shares Outstanding']}

        ]

        return render_template("bs_dashboard.html",
            symbol=symbol,

            table_data = formatted_data            
            
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

            bs = clean_years
            
        )
    except Exception as err:
        print('OOPS', err)

        return redirect("/home")