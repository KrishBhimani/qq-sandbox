def test_greeting_says_hello():
    assert "hello" in open("greeting.txt").read()
