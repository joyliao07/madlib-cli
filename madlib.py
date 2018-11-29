"""Madlib program that replace user's inputs in the template text string."""
template = """
Make Me A Video Game!

I the {Adjective} and {Adjective} {A First Name} have {Past Tense Verb} {A First Name}'s {Adjective} sister and plan to steal her {Adjective} {Plural Noun}!

What are a {Large Animal} and backpacking {Small Animal} to do? Before you can help {A Girl's Name}, you'll have to collect the {Adjective} {Plural Noun} and {Adjective} {Plural Noun} that open up the {Number 1-50} worlds connected to A {First Name's} Lair. There are {Number} {Plural Noun} and {Number} {Plural Noun} in the game, along with hundreds of other goodies for you to find.
"""
new = template


def welcome(new):
    """Explain the game to the user and invoke check_string()."""
    print('Welcome to Madlib!')
    print('Make me a video game!')
    print('Please follow the promps to enter your choices of words.')
    check_string(new)


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


def question_1(ques, new):
    """Prompt the user to enter their word and pass the word to the next function."""
    print('Please enter a(n) ' + ques + ' of your choice.')
    user_input = input()
    update_newlist(ques, new, user_input)


def update_newlist(ques, new, user_input):
    """Update the 'new' string with user's input and decide the next step."""
    new = new.replace(ques, user_input, 1)
    if '{' in new:
        check_string(new)
    else:
        print('Following is your Madlib result:')
        print(new)
        print('I hope you had fun.')
        print('Thank you for playing.')
        exit()


welcome(new)
