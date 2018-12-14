from __future__ import print_function

import itertools
import sys
from nltk.grammar import Nonterminal


def generate(grammar, start=None, depth=None, n=None):
    """
    Generates an iterator of all sentences from a CFG.

    :param grammar: The Grammar used to generate sentences.
    :param start: The Nonterminal from which to start generate sentences.
    :param depth: The maximal depth of the generated tree.
    :param n: The maximum number of sentences to return.
    :return: An iterator of lists of terminal tokens.
    """
    if not start:
        start = grammar.start()
    if depth is None:
        depth = sys.maxsize

    iter = _generate_all(grammar, [start], depth)

    if n:
        iter = itertools.islice(iter, n)

    return iter



def _generate_all(grammar, items, depth):
    if items:
        try:
            for frag1 in _generate_one(grammar, items[0], depth):
                for frag2 in _generate_all(grammar, items[1:], depth):
                    yield frag1 + frag2
        except RuntimeError as _error:
            if _error.message == "maximum recursion depth exceeded":
                # Helpful error message while still showing the recursion stack.
                raise RuntimeError(
                    "The grammar has rule(s) that yield infinite recursion!!"
                )
            else:
                raise
    else:
        yield []


def _generate_one(grammar, item, depth):
    if depth > 0:
        if isinstance(item, Nonterminal):
            for prod in grammar.productions(lhs=item):
                for frag in _generate_all(grammar, prod.rhs(), depth - 1):
                    yield frag
        else:
            yield [item]


demo_grammar = """
  S -> NP VP
  NP -> Det N
  PP -> P NP
  VP -> 'a' | 'b' NP | 'c' PP
  Det -> 'd' | 'e'
  N -> 'f' | 'g' | 'h'
  P -> 'i' | 'j'
"""


def demo(N=26):
	from nltk.grammar import CFG
	senteneces = list()
	#print('Generating the first %d sentences for demo grammar:' % (N,))
	#print(demo_grammar)
	grammar = CFG.fromstring(demo_grammar)
	for n, sent in enumerate(generate(grammar, n=N), 1):
		print(' '.join(sent))
		#senteneces.append(sent)
	#print(senteneces)


if __name__ == '__main__':
    demo()