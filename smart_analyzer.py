#!/usr/bin/python

import sys
from bs4 import BeautifulSoup


if __name__ == '__main__':
    print('Number of arguments:', len(sys.argv), 'arguments.')
    print('Argument List:', str(sys.argv))
    origin_file = sys.argv[1]
    other_file = sys.argv[2]

    text_pattern = 'make-everything-ok-button'

    with open(origin_file, 'r') as origin_html, open(other_file, 'r') as other_html:
        soup = BeautifulSoup(origin_html, "html.parser")
        # Can apply different possibilities to find a resource
        container = soup.find(id=text_pattern)
        comparators = [
            ('id', text_pattern),
            ('content', container.string.strip()),
            ('href',container.get('href')),
            ('class', container.get('class')),
            ('title', container.get('title')),
            ('onclick', container.get('onclick')),
        ]

        soup = BeautifulSoup(other_html, "html.parser")
        # tagname should be another comparator
        candidates = soup.find_all('a')
        best_score = 0
        for candidate in candidates:
            if candidate:
                score = 0
                for c in comparators:
                    if c[0] == 'content':
                        score += 1 if candidate.string and c[1] == candidate.string.strip() else 0
                    else:
                        score += 1 if candidate.get(c[0]) and c[1] == candidate.get(c[0]) else 0
                if score > best_score:
                    best_score = score
                    best_candidate = candidate

        print(best_candidate)



