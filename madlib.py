"""Madlib program that replace user's inputs in the template text string."""
from textwrap import dedent
WIDTH = 71


def read_file(infile):
    """To locate and read a text file."""
    with open(infile) as f:
        new = f.read()
        return new


def welcome():
    """Explain the game to the user and provide baisc rules of the game."""
    print('Welcome to Madlib - Make me a video game!')
    print('To quit at any time, enter "quit".')
    print(' ' * WIDTH)
    print('Please follow the promps to enter your choices of words.')


def check_string(new):
    """Check the 'new' string to find the next {input} question."""
    rec = False
    ques = ''
    for what in new:
        if what == '{':
            rec = True
        if rec is True:
            ques = ques + what
        if what == '}':
            rec = False
            break
    return(ques, new)


def question_1(ques, new):
    """Prompt the user to enter their word and pass the input as user_input."""
    print('Please enter a(n) ' + ques + ' of your choice.')
    user_input = input()
    if user_input == 'quit':
        exit()
        return()
    return(ques, new, user_input)


def update_newlist(ques, new, user_input):
    """Edit the string with user's input."""
    new = new.replace(ques, user_input, 1)
    return(new)


def write_file(path, contents):
    """To write the output file with updated contents."""
    with open(path, 'w') as wf:
        updated = wf.write(contents)
    return updated


if __name__ == '__main__':
    new = read_file('infile.txt')

    welcome()
    while '{' in new:
        ques, new = check_string(new)
        ques, new, user_input = question_1(ques, new)
        new = update_newlist(ques, new, user_input)
        write_file('outfile.txt', new)

    print(dedent(f'''
    {(' * ' * (WIDTH//3) )}
    {(' ' * WIDTH)}
    {(' ' * WIDTH)}
    {('Following is your Madlib result:')}
    {(' ' * WIDTH)}
    {(' ' * WIDTH)}
    {(new)}
    {(' ' * WIDTH)}
    {(' ' * WIDTH)}
    {(' ' * WIDTH)}
    {(' * ' * (WIDTH//3) )}
    {(' ' * WIDTH)}
    {(' ' * WIDTH)}
    {(' ' * WIDTH)}
    {(' ' * WIDTH)}
    {('I hope you had fun. Thank you for playing.')}
    '''))
