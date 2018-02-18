# self-care-assistant
## README
Daniel Alexander <xandernaut@gmail.com>
*(Updated February 2018)*

This program is meant to help me manage my executive functioning issues. It currently runs through a questionnaire inspired by ["You Feel Like Shit: An Interactive Self-Care Guide"](http://philome.la/jace_harr/you-feel-like-shit-an-interactive-self-care-guide), tailored to focus on the most common causes of me feeling _bad_ and not being sure why.

It's also a very good excuse for me to finally learn Python. :)

### Current Status
Things I'm currently working on:
  * repeating question if the answer given't isn't in the yes or no sets
  * introduce granularity re: which functions run; ask user whether they'd like to go through each set of questions

### Project To-Do
In `begin()`:
  * incorporate user's name
  * remember it across sessions? (potentially, profiles for mood tracking/etc)

In `checkin.py`:
  * alphabetize functions
  * is there a way to clean up/reduce duplicate code?

### Future Plans
In the future, I'd like to extend it to be a more comprehensive helper program. Some of the features I'm playing with are:
  * adding a mood indicator and tracking mood over time
  * warning when there are long periods of low mood or rapid fluctuation
