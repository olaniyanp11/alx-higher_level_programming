#!/usr/bin/bash
def multiple_returns(sentence):
    if not sentence:
        return len(sentence), None
    else:
        length = len(sentence), sentence[0]
        return length
