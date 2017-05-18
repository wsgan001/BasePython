#coding=utf8
#https://github.com/ictar/python-doc/blob/master/Testing/%E5%9C%A8Python%E4%B8%AD%E4%BD%BF%E7%94%A8Behave%E6%9D%A5%E5%BC%80%E5%A7%8B%E8%A1%8C%E4%B8%BA%E6%B5%8B%E8%AF%95.md

from behave import *
from twentyone import *

@given('a dealer')
def step_impl(context):
    context.dealer = Dealer()

@when('the round starts')
def step_impl(context):
    context.dealer.new_round()

@then('the dealer gives itself two cards')
def step_impl(context):
    assert(len(context.dealer.hand) == 2)


@when('the dealer sums the cards')
def step_impl(context):
    context.dealer_total = context.dealer.get_hand_total()

@then('the {total:d} is correct')
def step_impl(context, total):
    assert (context.dealer_total == total)

## NEW STEP
@given('a hand {total:d}')
def step_impl(context, total):
    context.dealer = Dealer()
    context.total = total

@when('the dealer determines a play')
def step_impl(context):
    context.dealer_play = context.dealer.determine_play(context.total)

## NEW STEP
@then('the {play} is correct')
def step_impl(context, play):
    assert (context.dealer_play == play)
