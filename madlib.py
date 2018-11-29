"""Madlib program that replace user's inputs in the template text string."""

template = """
Make Me A Video Game!

I the {Adjective} and {Adjective} {A First Name} have {Past Tense Verb} {A First Name}'s {Adjective} sister and plan to steal her {Adjective} {Plural Noun}!

What are a {Large Animal} and backpacking {Small Animal} to do? Before you can help {A Girl's Name}, you'll have to collect the {Adjective} {Plural Noun} and {Adjective} {Plural Noun} that open up the {Number 1-50} worlds connected to A {First Name's} Lair. There are {Number} {Plural Noun} and {Number} {Plural Noun} in the game, along with hundreds of other goodies for you to find."
"""
status = True
new = template


def welcome():
    """Here."""
    print('Welcome to Madlib! Please follow the promps to enter your choices of words.')
    check_string()


def check_string():
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
    question_1(ques)


def question_1(ques):
    print('Please enter a(n) ' + ques + ' of your choice.')
    user_input=input()
    print('you have chosen:' + user_input)



welcome()


while status is True:
    pass
