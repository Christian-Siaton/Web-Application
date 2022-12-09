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


        formatted_data = [
            {"metric": "Fiscal Date Ending", "year_one": info[0]["Fiscal Date Ending"], "year_two": info[1]['Fiscal Date Ending'], "year_three": info[2]['Fiscal Date Ending'], "year_four": info[3]['Fiscal Date Ending'], "year_five": info[4]['Fiscal Date Ending']},
            {"metric": "Reported Currency", "year_one": info[0]["Reported Currency"], "year_two": info[1]["Reported Currency"], "year_three": info[2]["Reported Currency"], "year_four": info[3]["Reported Currency"], "year_five": info[4]["Reported Currency"]},
            {"metric": "OPERATING CASH FLOWS", "year_one": info[0]["OPERATING CASH FLOWS"], "year_two": info[1]["OPERATING CASH FLOWS"], "year_three": info[2]["OPERATING CASH FLOWS"], "year_four": info[3]["OPERATING CASH FLOWS"], "year_five": info[4]["OPERATING CASH FLOWS"]},
            {"metric": "Payments for Operating Activities", "year_one": info[0]["Payments for Operating Activities"], "year_two": info[1]["Payments for Operating Activities"], "year_three": info[2]["Payments for Operating Activities"], "year_four": info[3]["Payments for Operating Activities"], "year_five": info[4]["Payments for Operating Activities"]},
            {"metric": "Payments from Operating Activities", "year_one": info[0]["Payments from Operating Activities"], "year_two": info[1]["Payments from Operating Activities"], "year_three": info[2]["Payments from Operating Activities"], "year_four": info[3]["Payments from Operating Activities"], "year_five": info[4]["Payments from Operating Activities"]},
            {"metric": "Change in Operating Liabilities", "year_one": info[0]["Change in Operating Liabilities"], "year_two": info[1]["Change in Operating Liabilities"], "year_three": info[2]["Change in Operating Liabilities"], "year_four": info[3]["Change in Operating Liabilities"], "year_five": info[4]["Change in Operating Liabilities"]},
            {"metric": "Change in Operating Assets", "year_one": info[0]["Change in Operating Assets"], "year_two": info[1]["Change in Operating Assets"], "year_three": info[2]["Change in Operating Assets"], "year_four": info[3]["Change in Operating Assets"], "year_five": info[4]["Change in Operating Assets"]},
            {"metric": "Depreciation Depletion and Amortization", "year_one": info[0]["Depreciation Depletion and Amortization"], "year_two": info[1]["Depreciation Depletion and Amortization"], "year_three": info[2]["Depreciation Depletion and Amortization"], "year_four": info[3]["Depreciation Depletion and Amortization"], "year_five": info[4]["Depreciation Depletion and Amortization"]},
            {"metric": "Capital Expenditures", "year_one": info[0]["Capital Expenditures"], "year_two": info[1]["Capital Expenditures"], "year_three": info[2]["Capital Expenditures"], "year_four": info[3]["Capital Expenditures"], "year_five": info[4]["Capital Expenditures"]},
            {"metric": "Profit Loss", "year_one": info[0]["Profit Loss"], "year_two": info[1]["Profit Loss"], "year_three": info[2]["Profit Loss"], "year_four": info[3]["Profit Loss"], "year_five": info[4]["Change in Receivables"]},
            {"metric": "Change In Inventory", "year_one": info[0]["Change In Inventory"], "year_two": info[1]["Change In Inventory"], "year_three": info[2]["Change In Inventory"], "year_four": info[3]["Profit Loss"], "year_five": info[4]["Profit Loss"]},
            {"metric": "CASH FLOW FROM INVESTMENT", "year_one": info[0]["CASH FLOW FROM INVESTMENT"], "year_two": info[1]["CASH FLOW FROM INVESTMENT"], "year_three": info[2]["CASH FLOW FROM INVESTMENT"], "year_four": info[3]["CASH FLOW FROM INVESTMENT"], "year_five": info[4]["CASH FLOW FROM INVESTMENT"]},
            {"metric": "CASH FLOW FROM FINANCING", "year_one": info[0]["CASH FLOW FROM FINANCING"], "year_two": info[1]["CASH FLOW FROM FINANCING"], "year_three": info[2]["CASH FLOW FROM FINANCING"], "year_four": info[3]["CASH FLOW FROM FINANCING"], "year_five": info[4]["CASH FLOW FROM FINANCING"]},
            {"metric": "Proceeds from Repayments of Short Term Debt", "year_one": info[0]["Proceeds from Repayments of Short Term Debt"], "year_two": info[1]["Proceeds from Repayments of Short Term Debt"], "year_three": info[2]["Proceeds from Repayments of Short Term Debt"], "year_four": info[3]["Proceeds from Repayments of Short Term Debt"], "year_five": info[4]["Proceeds from Repayments of Short Term Debt"]},
            {"metric": "Payments for Repurchase of Common Stock", "year_one": info[0]["Payments for Repurchase of Common Stock"], "year_two": info[1]["Payments for Repurchase of Common Stock"], "year_three": info[2]["Payments for Repurchase of Common Stock"], "year_four": info[3]["Payments for Repurchase of Common Stock"], "year_five": info[4]["Payments for Repurchase of Common Stock"]},
            {"metric": "Payments for Repurchase of Equity", "year_one": info[0]["Payments for Repurchase of Equity"], "year_two": info[1]["Payments for Repurchase of Equity"], "year_three": info[2]["Payments for Repurchase of Equity"], "year_four": info[3]["Payments for Repurchase of Equity"], "year_five": info[4]["Payments for Repurchase of Equity"]},
            {"metric": "Payments for Repurchase of Preferred Stock", "year_one": info[0]["Payments for Repurchase of Preferred Stock"], "year_two": info[1]["Payments for Repurchase of Preferred Stock"], "year_three": info[2]["Payments for Repurchase of Preferred Stock"], "year_four": info[3]["Payments for Repurchase of Preferred Stock"], "year_five": info[4]["Payments for Repurchase of Preferred Stock"]},
            {"metric": "Dividend Payout", "year_one": info[0]["Dividend Payout"], "year_two": info[1]["Dividend Payout"], "year_three": info[2]["Dividend Payout"], "year_four": info[3]["Dividend Payout"], "year_five": info[4]["Dividend Payout"]},
            {"metric": "Dividend Payout Preferred Stock", "year_one": info[0]["Dividend Payout Preferred Stock"], "year_two": info[1]["Dividend Payout Preferred Stock"], "year_three": info[2]["Dividend Payout Preferred Stock"], "year_four": info[3]["Dividend Payout Preferred Stock"], "year_five": info[4]["Dividend Payout Preferred Stock"]},
            {"metric": "Procceds from Issuance of Common Stock", "year_one": info[0]["Procceds from Issuance of Common Stock"], "year_two": info[1]["Procceds from Issuance of Common Stock"], "year_three": info[2]["Procceds from Issuance of Common Stock"], "year_four": info[3]["Procceds from Issuance of Common Stock"], "year_five": info[4]["Procceds from Issuance of Common Stock"]},
            {"metric": "Proceeds from Issuance of Long Term Debt and Capital Securities", "year_one": info[0]["Proceeds from Issuance of Long Term Debt and Capital Securities"], "year_two": info[1]["Proceeds from Issuance of Long Term Debt and Capital Securities"], "year_three": info[2]["Proceeds from Issuance of Long Term Debt and Capital Securities"], "year_four": info[3]["Proceeds from Issuance of Long Term Debt and Capital Securities"], "year_five": info[4]["Proceeds from Issuance of Long Term Debt and Capital Securities"]},
            {"metric": "Proceeds from Issuance of Preferred Stock", "year_one": info[0]["Proceeds from Issuance of Preferred Stock"], "year_two": info[1]["Proceeds from Issuance of Preferred Stock"], "year_three": info[2]["Proceeds from Issuance of Preferred Stock"], "year_four": info[3]["Proceeds from Issuance of Preferred Stock"], "year_five": info[4]["Proceeds from Issuance of Preferred Stock"]},
            {"metric": "Proceeds from Repurchase of Equity", "year_one": info[0]["Proceeds from Repurchase of Equity"], "year_two": info[1]["Proceeds from Repurchase of Equity"], "year_three": info[2]["Proceeds from Repurchase of Equity"], "year_four": info[3]["Proceeds from Repurchase of Equity"], "year_five": info[4]["Proceeds from Repurchase of Equity"]},
            {"metric": "Proceeds from Sale of Treasury Stock", "year_one": info[0]["Proceeds from Sale of Treasury Stock"], "year_two": info[1]["Proceeds from Sale of Treasury Stock"], "year_three": info[2]["Proceeds from Sale of Treasury Stock"], "year_four": info[3]["Proceeds from Sale of Treasury Stock"], "year_five": info[4]["Proceeds from Sale of Treasury Stock"]},
            {"metric": "Change in Cash and Cash Equivlents", "year_one": info[0]["Change in Cash and Cash Equivlents"], "year_two": info[1]["Change in Cash and Cash Equivlents"], "year_three": info[2]["Change in Cash and Cash Equivlents"], "year_four": info[3]["Change in Cash and Cash Equivlents"], "year_five": info[4]["Change in Cash and Cash Equivlents"]},
            {"metric": "Change in Exchange Rate", "year_one": info[0]["Change in Exchange Rate"], "year_two": info[1]["Change in Exchange Rate"], "year_three": info[2]["Change in Exchange Rate"], "year_four": info[3]["Change in Exchange Rate"], "year_five": info[4]["Change in Exchange Rate"]},
            {"metric": "NET INCOME", "year_one": info[0]["NET INCOME"], "year_two": info[1]["NET INCOME"], "year_three": info[2]["NET INCOME"], "year_four": info[3]["NET INCOME"], "year_five": info[4]["NET INCOME"]}

        ]


        return render_template("cs_dashboard.html",
            symbol=symbol,
            info = info,
            table_data = formatted_data

        

        )
    except Exception as err:
        print('OOPS', err)

        return redirect("/home")