
from app.display_sheets import display_balance_sheet 
from app.display_sheets import display_income_statement
from app.display_sheets import display_cashflow_statement
from app.helpers import format_usd

def test_retrieval():
    result = display_balance_sheet("IBM")
    assert isinstance(result,list)
    first_item = result[0]
    assert isinstance(first_item,dict)
    assert "Fiscal Date Ending" in first_item
    assert "TOTAL LIABILITIES" in first_item
    assert "Common Stock" in first_item

    result = display_income_statement("IBM")
   # breakpoint()
    assert isinstance(result,list)
    first_item = result[0]
    assert isinstance(first_item,dict)
    assert "Total Revenue" in first_item
    assert "Depreciation" in first_item
    assert "Net Income" in first_item

    result = display_cashflow_statement("IBM")
    assert isinstance(result,list)
    first_item = result[0]
    assert isinstance(first_item,dict)
    assert "OPERATING CASH FLOWS" in first_item
    assert "CASH FLOW FROM INVESTMENT" in first_item
    assert "CASH FLOW FROM FINANCING" in first_item



def test_usd_format():
    assert format_usd(808) == '$808'
    assert format_usd(123456.789) =='$123,457'


