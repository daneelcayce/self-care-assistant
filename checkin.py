# self-care-assistant
# checkin.py
# by Daniel Alexander <xandernaut@gmail.com>

# The check-in questionnaire

import plumbing

# Functions:
# check()
# basic, hygiene, stress, sleep, cleanup

def check():
    basic()
    hygiene()
    stress()
    sleep()
    cleanup()

def basic():
    question = "Have you eaten in the past few hours?"
    reply = plumbing.parse(question)
    if reply in plumbing.yes:
        print("Glad to hear it!")
    elif reply in plumbing.no:
        print("Let's find something to eat.")
        print("(to be added later)")
    else:
        print("Sorry, I didn't catch that.")
    # ask about water
    question = "Have you had something to drink lately?"
    reply = plumbing.parse(question)
    if reply in plumbing.yes:
        print("Good!")
    elif reply in plumbing.no:
        print("Go get a glass of water.")
        print("Press [ENTER] when you're ready to go forward.")
        input()
    else:
        print("Sorry, I didn't catch that.")
    # ask about meds
    question = "Have you taken your meds today?"
    reply = plumbing.parse(question)
    if reply in plumbing.yes:
        print("Excellent!")
    elif reply in plumbing.no:
        print("How about you go take those?")
        print("It's okay if it's too late for your Vyvanse.")
        input("Press [ENTER] when you're ready to keep going.")
    else:
        print("Sorry, I didn't catch that.")


def hygiene():
    question = "Have you taken a shower yet today?"
    reply = plumbing.parse(question)
    if reply in plumbing.yes:
        print("Good!")
    elif reply in plumbing.no:
        print("Go take one (or a bath, if that would be better).")
        print("It'll help, I promise.")
        input("Press [ENTER] when you get back.")
    else:
        print("Sorry, I didn't catch that.")

    # teeth brushed
    question = "Have you brushed your teeth and/or washed your face lately?"
    reply = plumbing.parse(question)
    if reply in plumbing.yes:
        print("Good to hear!")
    elif reply in plumbing.no:
        print("Okay.")
        print("Go brush your teeth, and scrub your face.")
        print("Press [ENTER] when you're done.")
    else:
        print("Sorry, I didn't catch that.")


def sleep():
    question = "Do you feel well-rested?"
    reply = plumbing.parse(question)
    if reply in plumbing.yes:
        print("Okay!")
    elif reply in plumbing.no:
        print("All right.")
        question = "Do you need to take a nap?"
        if reply in plumbing.yes:
            print("Go take a nap for a little while.")
            input("I'll be here when you get back.")
        elif reply in plumbing.no:
            print("Go rest for a little bit.")
            print("You don't need to take a nap, but just relax for a while.")
            input("I'll be here when you're back.")
        else:
            print("Sorry, didn't catch that.")
    else:
        print("Sorry, I didn't catch that.")


def stress():
    question = "Have you been under a lot of stress lately?"
    reply = plumbing.parse(question)
    if reply in plumbing.yes:
        print("Okay. Let's see if we can figure out how to help you deal with it.")
        question = "Would listening to music help?"
        reply = plumbing.parse(question)
        if reply in plumbing.yes:
            print("Go listen to some music for a little while.")
        elif reply in plumbing.no:
            print("Okay.")
            print("Go write some things out for about fifteen minutes.")
            print("You'll feel a lot better afterward.")
        else:
            print("Sorry, I didn't catch that.")
    elif reply in plumbing.no:
        print("That's good to hear.")
    else:
        print("Sorry, I didn't catch that.")


def cleanup():
    question = "Is there anywhere in your space that needs to be cleaned up?"
    reply = plumbing.parse(question)
    if reply in plumbing.yes:
        print("Got it.")
        print("Pick a small area and take five minutes to tidy it up.")
        input("I'll be here when you're done.")
    elif reply in plumbing.no:
        print("I'm glad to hear that you're on top of that!")
        tally += 1
    else:
        print("Sorry, I didn't catch that.")
