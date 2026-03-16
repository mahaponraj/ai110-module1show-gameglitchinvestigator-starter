from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert message == "🎉 Correct!"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High" and "Go LOWER!"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert message == "📉 Go LOWER!"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low" and "Go HIGHER!"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert message == "📈 Go HIGHER!"

def test_hint_bug_case():
    # Specific case from the bug report: secret is 24
    # Guess 99 should be "Too High" and "Go LOWER!"
    outcome, message = check_guess(99, 24)
    assert outcome == "Too High"
    assert message == "📉 Go LOWER!"
    
    # Guess 10 should be "Too Low" and "Go HIGHER!"
    outcome, message = check_guess(10, 24)
    assert outcome == "Too Low"
    assert message == "📈 Go HIGHER!"
