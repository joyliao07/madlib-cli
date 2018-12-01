import madlib
# import pytest


def test_read_file():
    """To test read_file to make sure the output is correct."""
    contents = madlib.read_file('./infile.txt')
    assert contents.startswith('Make Me A Video Game!\n')


def test_welcome(capsys):
    """To test welcome()'s printed words."""
    madlib.welcome()
    captured = capsys.readouterr()
    assert captured.out == 'Welcome to Madlib - Make me a video game!\nTo quit at any time, enter "quit".\n                                                                       \nPlease follow the promps to enter your choices of words.\n'


def test_check_string_two_outputs():
    """To make sure check_string output the correct characters."""
    ques, story = madlib.check_string('Here I {abc} a very good time.')
    assert story == story
    assert ques == '{abc}'


def test_update_newlist():
    """To ensure update_newlist correctly replace desired characters."""
    ques = '{abc}'
    phrase = 'Here I {abc} a very good time.'
    user_input = 'surely had'
    result = madlib.update_newlist(ques, phrase, user_input)
    assert result == 'Here I surely had a very good time.'


def test_write_file():
    """To ensure write_file has correct output"""
    contents = 'yay'
    path = 'testfile.txt'
    madlib.write_file(path, contents)
    with open(path) as f:
        assert f.read() == contents
