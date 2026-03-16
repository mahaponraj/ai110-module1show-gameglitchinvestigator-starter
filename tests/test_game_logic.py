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

# Advanced Edge-Case Tests

def test_parse_guess_none_input():
    # Edge case: None input
    ok, guess, err = parse_guess(None)
    assert ok == False
    assert guess is None
    assert err == "Enter a guess."

def test_parse_guess_large_number():
    # Edge case: Very large integer
    large_num = str(10**100)
    ok, guess, err = parse_guess(large_num)
    assert ok == True
    assert guess == 10**100
    assert err is None

def test_parse_guess_negative_number():
    # Edge case: Negative number
    ok, guess, err = parse_guess("-5")
    assert ok == True
    assert guess == -5
    assert err is None

def test_parse_guess_zero():
    # Edge case: Zero
    ok, guess, err = parse_guess("0")
    assert ok == True
    assert guess == 0
    assert err is None

def test_parse_guess_float_with_decimals():
    # Edge case: Float with multiple decimals
    ok, guess, err = parse_guess("24.567")
    assert ok == True
    assert guess == 24  # int(float()) truncates
    assert err is None

def test_parse_guess_mixed_string():
    # Edge case: String starting with number but containing letters
    ok, guess, err = parse_guess("24abc")
    assert ok == False
    assert guess is None
    assert err == "That is not a number."

def test_parse_guess_whitespace():
    # Edge case: Whitespace around number
    ok, guess, err = parse_guess("  24  ")
    assert ok == True  # Apparently the function accepts whitespace
    assert guess == 24
    assert err is None

def test_get_range_case_insensitive():
    # Edge case: Case variations
    low, high = get_range_for_difficulty("easy")
    assert low == 1
    assert high == 100  # Default for unknown

    low, high = get_range_for_difficulty("EASY")
    assert low == 1
    assert high == 100

def test_get_range_empty_string():
    # Edge case: Empty difficulty
    low, high = get_range_for_difficulty("")
    assert low == 1
    assert high == 100

def test_get_range_none():
    # Edge case: None difficulty (returns default)
    low, high = get_range_for_difficulty(None)
    assert low == 1
    assert high == 100

def test_check_guess_boundary_values():
    # Edge case: Guess at range boundaries
    outcome, message = check_guess(1, 1)
    assert outcome == "Win"

    outcome, message = check_guess(100, 50)
    assert outcome == "Too High"

    outcome, message = check_guess(0, 50)
    assert outcome == "Too Low"

def test_check_guess_large_numbers():
    # Edge case: Very large numbers
    secret = 10**10
    guess = 10**10 + 1
    outcome, message = check_guess(guess, secret)
    assert outcome == "Too High"

    guess = 10**10 - 1
    outcome, message = check_guess(guess, secret)
    assert outcome == "Too Low"

def test_check_guess_float_guess():
    # Edge case: Guess as float (though parse_guess converts to int)
    outcome, message = check_guess(24.0, 24)
    assert outcome == "Win"  # Should work since == compares values

def test_update_score_negative_current():
    # Edge case: Negative current score
    new_score = update_score(-10, "Win", 1)
    assert new_score == 70  # 100 - 20 = 80, but -10 + 80 = 70

def test_update_score_attempt_zero():
    # Edge case: Attempt 0 (though unlikely)
    new_score = update_score(0, "Win", 0)
    assert new_score == 90  # 100 - 10 * 1

def test_update_score_unknown_outcome():
    # Edge case: Unknown outcome
    new_score = update_score(100, "Unknown", 1)
    assert new_score == 100  # No change

def test_update_score_max_attempts():
    # Edge case: Very high attempt number
    new_score = update_score(0, "Win", 100)
    assert new_score == 10  # Min score

def test_update_score_too_high_even_attempt():
    # Edge case: Confirm even attempt bonus
    new_score = update_score(100, "Too High", 10)  # Even
    assert new_score == 105

def test_integration_parse_and_check():
    # Integration: Parse then check
    ok, guess, err = parse_guess("50")
    assert ok
    outcome, message = check_guess(guess, 50)
    assert outcome == "Win"

def test_integration_full_game_simulation():
    # Simulate a short game: guess too low, then win
    score = 0
    attempt = 1
    # First guess: 40, secret 50
    score = update_score(score, "Too Low", attempt)
    assert score == -5
    attempt += 1
    # Second guess: 50
    score = update_score(score, "Win", attempt)
    assert score == 65  # -5 + (100 - 10*3) = -5 + 70
