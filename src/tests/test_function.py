import pytest
import sys
sys.path.append("..")
from main.app import search


def toArray(string):
    sentence = []
    sentence.append(string)
    return sentence


def test_sentiment_positive():
    assert "positive" == search(toArray("Trump"))

