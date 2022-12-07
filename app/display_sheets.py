import requests
import json
from app.helpers import format_usd
from app.alpha import API_KEY

def display_balance_sheet (symbol):
    url = f'https://www.alphavantage.co/query?function=BALANCE_SHEET&symbol={symbol}&apikey={API_KEY}'
    r = requests.get(url)
    data = r.json()

    if "symbol" not in data.keys():
        print ("Invalid ticker ID")
        retry = input("Please enter a valid company ticker:")
        return display_income_statement(retry)

    annual_reports = data["annualReports"]
    dirty_years = []
    
    print('')
    print('YOU HAVE CHOSEN:', symbol.upper())
    print('')
    print('Here are the most recent Balance Sheets for', symbol.upper() + '!')
    print('')
    print('---------------------------')
    print('')

    for report in annual_reports:
        dirty_years.append(report)

    clean_years = []

    for year in dirty_years:
        for item in year:
            if year[item] == "None":
                year[item] = 0
    
        clean_year = {
            "Fiscal Date Ending": year["fiscalDateEnding"],
            "Reported Currency": year['reportedCurrency'],
            "TOTAL ASSETS": format_usd(int(year['totalAssets'])),
            "TOTAL CURRENT ASSETS": format_usd(int(year['totalCurrentAssets'])),
            "Cash and Cash Equivalents": format_usd(int(year['cashAndCashEquivalentsAtCarryingValue'])),
            "Cash and Short Term Investments": format_usd(int(year['cashAndShortTermInvestments'])),
            "Inventory": format_usd(int(year['inventory'])),
            "Current Net Receivables": format_usd(int(year['currentNetReceivables'])),
            "TOTAL NONCURRENT ASSETS": format_usd(int(year['totalNonCurrentAssets'])),
            "Property Plant & Equipment": format_usd(int(year['propertyPlantEquipment'])),
            "Accumulated Depreciation & Amortization": format_usd(int(year['accumulatedDepreciationAmortizationPPE'])),
            "Intangible Assets": format_usd(int(year['intangibleAssets'])),
            "Intangible Assets Excluding Goodwill": format_usd(int(year['intangibleAssetsExcludingGoodwill'])),
            "Goodwill": format_usd(int(year['goodwill'])),
            "Investments": format_usd(int(year['investments'])),
            "Long Term Investments": format_usd(int(year['longTermInvestments'])),
            "Short Term Investments": format_usd(int(year['shortTermInvestments'])),
            "Other Current Assets": format_usd(int(year['otherCurrentAssets'])),
            "Other Noncurrent Assets": format_usd(int(year['otherNonCurrentAssets'])),
            "TOTAL LIABILITIES": format_usd(int(year['totalLiabilities'])),
            "TOTAL CURRENT LIABILITIES": format_usd(int(year['totalCurrentLiabilities'])),
            "Current Accounts Payable": format_usd(int(year['currentAccountsPayable'])),
            "Deferred Revenue": format_usd(int(year['deferredRevenue'])),
            "Current Debt": format_usd(int(year['currentDebt'])),
            "Short Term Debt": format_usd(int(year['shortTermDebt'])),
            "TOTAL NONCURRENT LIABILITIES": format_usd(int(year['totalNonCurrentLiabilities'])),
            "Capital Lease Obligations": format_usd(int(year['capitalLeaseObligations'])),
            "Long Term Debt": format_usd(int(year['longTermDebt'])),
            "Current Long Term Debt": format_usd(int(year['currentLongTermDebt'])),
            "Noncurrent Long Term Debt": format_usd(int(year['longTermDebtNoncurrent'])),
            "Total Debt": format_usd(int(year['shortLongTermDebtTotal'])),
            "Other Current Liabilities": format_usd(int(year['otherCurrentLiabilities'])),
            "TOTAL SHAREHOLDER EQUITY": format_usd(int(year['totalShareholderEquity'])),
            "Treasury Stock": format_usd(int(year['treasuryStock'])),
            "Retained Earnings": format_usd(int(year['retainedEarnings'])),
            "Common Stock": format_usd(int(year['commonStock'])),
            "Common Stock Shares Outstanding": format_usd(int(year['commonStockSharesOutstanding'])),
        }

        clean_years.append(clean_year)

    for year in clean_years:
        for item in year:
            print (item + ":", year[item])
        print('')
        print('-----------------------------------------')
        print('')

    return clean_years

def display_income_statement (symbol):
    url = f'https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol={symbol}&apikey={API_KEY}'
    r = requests.get(url)
    data = r.json()

    if "symbol" not in data.keys():
        print ("Invalid ticker ID")
        retry = input("Please enter a valid company ticker:")
        return display_income_statement(retry)

    annual_reports = data["annualReports"]
    dirty_years = []
    
    print('')
    print('YOU HAVE CHOSEN:', symbol.upper())
    print('')
    print('Here are the most recent income statements for', symbol.upper() + '!')
    print('')
    print('---------------------------')
    print('')

    for report in annual_reports:
        dirty_years.append(report)

    clean_years = []

    for year in dirty_years:
        for item in year:
            if year[item] == "None":
                year[item] = 0
    
        clean_year = {
            "Fiscal Date Ending": year["fiscalDateEnding"],
            "Reported Currency": year['reportedCurrency'],
            "Total Revenue": format_usd(int(year['totalRevenue'])),
            "Cost of Revenue": format_usd(int(year['costOfRevenue'])),
            "Cost of Goods and Services Sold": format_usd(int(year['costofGoodsAndServicesSold'])),
            "Operating Income": format_usd(int(year['operatingIncome'])),
            "Selling, General, Administrative": format_usd(int(year['sellingGeneralAndAdministrative'])),
            "Research & Development": format_usd(int(year['researchAndDevelopment'])),
            "Net Investment Income": format_usd(int(year['investmentIncomeNet'])),
            "Interest Income": format_usd(int(year['interestIncome'])),
            "Interest Expense": format_usd(int(year['interestExpense'])),
            "Non-interest Income": format_usd(int(year['nonInterestIncome'])),
            "Other Non-Operating Income": format_usd(int(year['otherNonOperatingIncome'])),
            "Depreciation": format_usd(int(year['depreciation'])),
            "Depreciation and Amortization": format_usd(int(year['depreciationAndAmortization'])),
            "Income Before Tax": format_usd(int(year['incomeBeforeTax'])),
            "Income Tax Expense": format_usd(int(year['incomeTaxExpense'])),
            "Interest and Debt Expense": format_usd(int(year['interestAndDebtExpense'])),
            "Net Income From Continuing Operations": format_usd(int(year['netIncomeFromContinuingOperations'])),
            "Comprehensive Income Net of Tax": format_usd(int(year['comprehensiveIncomeNetOfTax'])),
            "EBIT": format_usd(int(year['ebit'])),
            "EBITDA": format_usd(int(year['ebitda'])),
            "Net Income": format_usd(int(year['netIncome'])),
        }

        clean_years.append(clean_year)

    for year in clean_years:
        for item in year:
            print (item + ":", year[item])
        print('')
        print('-----------------------------------------')
        print('')

    return clean_years

def display_cashflow_statement (symbol):
    url = f'https://www.alphavantage.co/query?function=CASH_FLOW&symbol={symbol}&apikey={API_KEY}'
    r = requests.get(url)
    data = r.json()

    if "symbol" not in data.keys():
        print ("Invalid ticker ID")
        retry = input("Please enter a valid company ticker:")
        return display_income_statement(retry)

    annual_reports = data["annualReports"]
    dirty_years = []

    print(annual_reports[0])
    
    print('')
    print('YOU HAVE CHOSEN:', symbol.upper())
    print('')
    print('Here are the most recent Cash Flow Statements for', symbol.upper() + '!')
    print('')
    print('---------------------------')
    print('')

    for report in annual_reports:
        dirty_years.append(report)

    clean_years = []

    for year in dirty_years:
        for item in year:
            if year[item] == "None":
                year[item] = 0
    
        clean_year = {
            "Fiscal Date Ending": year["fiscalDateEnding"],
            "Reported Currency": year['reportedCurrency'],
            "OPERATING CASH FLOWS": format_usd(int(year['operatingCashflow'])),
            "Payments for Operating Activities": format_usd(int(year['paymentsForOperatingActivities'])),
            "Payments from Operating Activities": format_usd(int(year['proceedsFromOperatingActivities'])),
            "Change in Operating Liabilities": format_usd(int(year['changeInOperatingLiabilities'])),
            "Change in Operating Assets": format_usd(int(year['changeInOperatingAssets'])),
            "Depreciation Depletion and Amortization": format_usd(int(year['depreciationDepletionAndAmortization'])),
            "Capital Expenditures": format_usd(int(year['capitalExpenditures'])),
            "Change in Receivables": format_usd(int(year['changeInReceivables'])),
            "Change In Inventory": format_usd(int(year['changeInInventory'])),
            "Profit Loss": format_usd(int(year['profitLoss'])),
            "CASH FLOW FROM INVESTMENT": format_usd(int(year['cashflowFromInvestment'])),
            "CASH FLOW FROM FINANCING": format_usd(int(year['cashflowFromFinancing'])),
            "Proceeds from Repayments of Short Term Debt": format_usd(int(year['proceedsFromRepaymentsOfShortTermDebt'])),
            "Payments for Repurchase of Common Stock": format_usd(int(year['paymentsForRepurchaseOfCommonStock'])),
            "Payments for Repurchase of Equity": format_usd(int(year['paymentsForRepurchaseOfEquity'])),
            "Payments for Repurchase of Preferred Stock": format_usd(int(year['paymentsForRepurchaseOfPreferredStock'])),
            "Dividend Payout": format_usd(int(year['dividendPayout'])),
            "Dividend Payout Common Stock": format_usd(int(year['dividendPayoutCommonStock'])),
            "Dividend Payout Preferred Stock": format_usd(int(year['dividendPayoutPreferredStock'])),
            "Procceds from Issuance of Common Stock": format_usd(int(year['proceedsFromIssuanceOfCommonStock'])),
            "Proceeds from Issuance of Long Term Debt and Capital Securities": format_usd(int(year['proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet'])),
            "Proceeds from Issuance of Preferred Stock": format_usd(int(year['proceedsFromIssuanceOfPreferredStock'])),
            "Proceeds from Repurchase of Equity": format_usd(int(year['proceedsFromRepurchaseOfEquity'])),
            "Proceeds from Sale of Treasury Stock": format_usd(int(year['proceedsFromSaleOfTreasuryStock'])),
            "Change in Cash and Cash Equivlents": format_usd(int(year['changeInCashAndCashEquivalents'])),
            "Change in Exchange Rate": format_usd(int(year['changeInExchangeRate'])),
            "NET INCOME": format_usd(int(year['netIncome'])),
        }

        clean_years.append(clean_year)

    for year in clean_years:
        for item in year:
            print (item + ":", year[item])
        print('')
        print('-----------------------------------------')
        print('')

    return clean_years

if __name__ == "__main__": 

    company = input("Please enter a valid company ticker to display its most recent Balance Sheets:")
    display_balance_sheet(company)   

    company = input("Please enter a valid company ticker to display its most recent Income Statements:")
    display_income_statement(company)

    company = input("Please enter a valid company ticker to display its most recent Cash Flow Statements:")
    display_cashflow_statement(company)