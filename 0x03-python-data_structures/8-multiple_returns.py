#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        return None, None
    else:
        my_tuple = ()
        sentence_len = len(sentence)
        first_char = sentence[0]
        return sentence_len, first_char
