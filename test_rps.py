import rps
import pytest
import subprocess
import sys

def test_rock_is_valid_play():
    assert rps.is_valid_play('rock') is True

def test_paper_is_valid_play():
    assert rps.is_valid_play('paper') is True

def test_scissors_is_valid_play():
    assert rps.is_valid_play('scissors') is True

def test_lizzard_is_invalid_play():
    assert rps.is_valid_play('lizzard') is False

def test_computer_play_is_valid():
    for _ in range(5000):
        play = rps.generate_computer_play()
        assert rps.is_valid_play(play)

def test_computer_plays_randomly():
    plays = [rps.generate_computer_play() for _ in range (5000)]
    rocks = plays.count('rock')
    papers = plays.count('paper')
    scissors = plays.count('scissors')
    print(rocks, papers, scissors)
    assert rocks > 200
    assert papers > 200
    assert scissors > 200

def test_paper_beats_rock():
    result = rps.evaluate_game('paper', 'rock')
    assert result == 'human'

def test_rock_fails_paper():
    result = rps.evaluate_game('rock', 'paper')
    assert result == 'computer'

def test_rock_beats_scissors():
    result = rps.evaluate_game('rock', 'scissors')
    assert result == 'human'

def test_scissors_fails_rock():
    result = rps.evaluate_game('scissors', 'rock')
    assert result == 'computer'

def test_scissors_beats_paper():
    result = rps.evaluate_game('scissors', 'paper')
    assert result == 'human'

def test_paper_fails_scissors():
    result = rps.evaluate_game('paper', 'scissors')
    assert result == 'computer'

def test_paper_tie_paper():
    result = rps.evaluate_game('paper', 'paper')
    assert result == 'tie'

def test_scissors_tie_scissors():
    result = rps.evaluate_game('scissors', 'scissors')
    assert result == 'tie'

def test_rock_tie_rock():
    result = rps.evaluate_game('rock', 'rock')
    assert result == 'tie'

def input_faked_rock(prompt):
    print(prompt)
    return 'rock'

def input_faked_paper(prompt):
    print(prompt)
    return 'paper'

def input_faked_scissors(prompt):
    print(prompt)
    return 'scissors'

def test_full_game_rock(capsys):
    rps.main(input = input_faked_rock)
    captured = capsys.readouterr()
    assert 'rock, paper, or scissors?' in captured.out

def test_full_game_paper(capsys):
    rps.main(input = input_faked_paper)
    captured = capsys.readouterr()
    assert 'rock, paper, or scissors?' in captured.out

def test_full_game_scissors(capsys):
    rps.main(input = input_faked_scissors)
    captured = capsys.readouterr()
    assert 'rock, paper, or scissors?' in captured.out

def test_wrong_play_result_in_repeated_question():
    cp = subprocess.run([sys.executable, 'rps.py'],
                        encoding='utf-8',
                        stdout=subprocess.PIPE,
                        input='dragon\nrock\n',
                        check=True)
    assert cp.stdout.count('rock, paper, or scissors?') == 2