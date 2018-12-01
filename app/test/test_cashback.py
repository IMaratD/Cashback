from app.cashback import cashback


def test_cashback_under_limit ():
    result = cashback(1000)

    assert 50 == result
