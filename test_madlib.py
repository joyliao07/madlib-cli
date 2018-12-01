import madlib
# import pytest


def test_read_file():
    contents = madlib.read_file('./infile.txt')
    assert contents.startswith('Make Me A Video Game!\n')


def test_welcome(capsys):
    """To test welcome()'s printed words."""
    madlib.welcome()
    captured = capsys.readouterr()
    assert captured.out == 'Welcome to Madlib - Make me a video game!\nTo quit at any time, enter "quit".\n                                                                       \nPlease follow the promps to enter your choices of words.\n'


def test_check_string_two_outputs():
    """
    """
    ques, story = madlib.check_string('Here I {verb} a very good time.')
    assert story == story
    assert ques == '{verb}'


def test_update_newlist():
    ques = '{verb}'
    phrase = 'Here I {verb} a very good time.'
    user_input = 'exploded'
    result = madlib.update_newlist(ques, phrase, user_input)
    assert result == 'Here I exploded a very good time.'








