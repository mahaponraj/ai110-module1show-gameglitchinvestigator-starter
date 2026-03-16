from logic_utils import check_guess, parse_guess, get_range_for_difficulty, update_score

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

def test_parse_guess_valid():
    # Test parsing valid guesses
    ok, guess, err = parse_guess("24")
    assert ok == True
    assert guess == 24
    assert err is None

    ok, guess, err = parse_guess("24.0")
    assert ok == True
    assert guess == 24
    assert err is None

def test_parse_guess_invalid():
    # Test parsing invalid guesses
    ok, guess, err = parse_guess("")
    assert ok == False
    assert guess is None
    assert err == "Enter a guess."

    ok, guess, err = parse_guess("abc")
    assert ok == False
    assert guess is None
    assert err == "That is not a number."

def test_get_range_for_difficulty():
    # Test range for different difficulties
    low, high = get_range_for_difficulty("Easy")
    assert low == 1
    assert high == 20

    low, high = get_range_for_difficulty("Normal")
    assert low == 1
    assert high == 100

    low, high = get_range_for_difficulty("Hard")
    assert low == 1
    assert high == 50

    low, high = get_range_for_difficulty("Unknown")
    assert low == 1
    assert high == 100

def test_update_score_win():
    # Test score update for winning
    new_score = update_score(0, "Win", 1)  # First attempt
    assert new_score == 80  # 100 - 10 * 2

    new_score = update_score(0, "Win", 2)  # Second attempt
    assert new_score == 70  # 100 - 10 * 3

    new_score = update_score(0, "Win", 10)  # Tenth attempt
    assert new_score == 10  # min 10

def test_update_score_too_high():
    # Test score update for too high
    new_score = update_score(100, "Too High", 1)  # Odd attempt
    assert new_score == 95  # -5

    new_score = update_score(100, "Too High", 2)  # Even attempt
    assert new_score == 105  # +5

def test_update_score_too_low():
    # Test score update for too low
    new_score = update_score(100, "Too Low", 1)
    assert new_score == 95  # -5
