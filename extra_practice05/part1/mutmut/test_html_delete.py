from html_delete import html_delete

def test_html1():
    assert html_delete("<h1>Hi</h1>") == "Hi"

def test_html2():
    assert html_delete("<div><p>Hi</p></div>") == "Hi"
