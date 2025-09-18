from src.history import BrowserHistory

def test_visit_back_forward_truncation():
    h = BrowserHistory()
    h.visit("a"); h.visit("b"); h.visit("c")
    assert h.current() == "c"
    assert h.back() == "b"
    assert h.back() == "a"
    assert h.forward() == "b"
    # visiting after going back drops forward history
    h.visit("b2")
    assert h.current() == "b2"
    assert h.forward() == "b2"  # no forward left
