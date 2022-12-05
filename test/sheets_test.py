
from app.display_sheets import display_balance_sheet


def test_retrieval():
    result = display_balance_sheet("IBM")
    assert isinstance(result,list)
    first_item = result[0]
    assert isinstance(first_item,dict)

    # test if the there are certain items in the dictionary