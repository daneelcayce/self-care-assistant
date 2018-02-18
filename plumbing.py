# self-care-assistant
# plumbing.py
# by Daniel Alexander <xandernaut@gmail.com>

# This is some of the stuff that makes this thing run.

from checkin import *

# have a fairly large list of acceptable responses
yes = set(["yes", "Yes", "YES", "y", "Y"])
no = set(["no", "No", "NO", "n", "N"])

# intro function
def begin():
    print("Hello!")
    print("I'm going to help you figure out why you don't feel quite right.")

# response parser
def parse(question):
    print(question)
    reply = input("> ")
    return reply
