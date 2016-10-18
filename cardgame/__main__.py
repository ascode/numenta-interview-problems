#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
The engineers at Numenta have invented a simple card game with the following
rules:

Every player is dealt some number of cards.  Each player's hand is scored
according to some simple heuristic.  The winner in each round is determined by
the hand with the highest score.  There can be at most one winner per round.
"""

import random

ranks = u"A23456789TJQK"
suits = u"♠♥♦♣"


def compare_hands(leftHand, rightHand):
  return score(leftHand) - score(rightHand)


def deal_cards(hands=1, size=7):
  samples = random.sample([x+y for x in ranks for y in suits], hands*size)

  return zip(*[iter(samples)]*size)


def render_hand(hand):
  return ", ".join(card for card in hand)


def score(hand):
  """ Calculate cumulative score for hand according to the following rules:

  1 point for each 3-sequence, ranked pair, or suited pair
  2 points for each 4-sequence, ranked three-of-a-kind, or suited three-of-a-kind
  3 points for each 5-sequence, ranked four-of-a-kind, or suited four-of-a-kind
  4 points for each 6-sequence
  5 points for each 7-sequence

  An n-sequence is a set of n contiguous ranks, independent of suit e.g. 2, 3, 4
  Two cards of equal rank comprise a "ranked pair"
  Two cards of equal suite comprise a "suited pair"

  Note: a 4-sequence does not also count as a 3-sequence, a three-of-a-kind does
  not also count as a pair, etc.

  :param hand: sequence of cards
  :return: Score for hand
  """
  return random.randint(0, 100)


if __name__ == "__main__":
  (leftHand, rightHand) = deal_cards(2, 7)

  result = compare_hands(leftHand, rightHand)

  print render_hand(leftHand), "Win" if result > 0 else ""
  print render_hand(rightHand), "Win" if result < 0 else ""