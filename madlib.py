"""Madlib program that replace user's inputs in the template text string."""



def trypytest():
    """To test pytest setup."""
    pass


def welcome(new):
    """Explain the game to the user and invoke check_string()."""
    print('Welcome to Madlib!')
    print('Make me a video game!')
    print('Please follow the promps to enter your choices of words.')
    return(new)


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
    question_1(ques, new)
    return (ques, new)    ############


def question_1(ques, new):
    """Prompt the user to enter their word and pass the word to the next function."""
    print('Please enter a(n) ' + ques + ' of your choice.')
    user_input = input()
    update_newlist(ques, new, user_input)
    return (ques, new, user_input) ###########


def update_newlist(ques, new, user_input):
    """Update the 'new' string with user's input and decide the next step."""
    new = new.replace(ques, user_input, 1)
    if '{' in new:
        check_string(new)
        return(new)
    else:
        with open('outfile.txt', 'w') as wf:
            wf.write(new)
        print('Following is your Madlib result:')
        print(new)
        print('I hope you had fun.')
        print('Thank you for playing.')
        exit()
        return(new)

if __name__ == '__main__':
    with open('infile.txt') as f:
        new = f.read()
    welcome(new)
    check_string(new)
