import argparse

from helpers import list_utilities


def initialize_current(women):
    return [None] * len(women)


def initialize_ranking(woman_pref):
    ranking = []
    for woman in woman_pref:
        number_of_women = len(woman)
        highest_rank = number_of_women - 1
        rank_indexed_by_man = [None] * number_of_women
        for pref in woman:
            rank_indexed_by_man[pref] = highest_rank
            highest_rank -= 1
        ranking.append(rank_indexed_by_man)
    return ranking


def initialize_next(men):
    return [0] * len(men)


def match_genders(men, man_pref, current, next, ranking):
    while men.node:
        m = men.node.value
        w = man_pref[m][next[m]]
        m_prime = current[w]
        if not m_prime:
            current[w] = m
            men.remove(m)
        else:
            if ranking[w][m] > ranking[w][m_prime]:
                current[w] = m
                men.remove(m)
                men.add(m_prime)
                next[m_prime] += 1
            else:
                next[m] += 1
    return current


def extract_pref_for_gender(filename):
    n = []
    prefs = []
    with open(filename, 'r') as f:
        lines = f.readlines()
        for line in lines:
            pref = line.split(':')
            n.append(int(pref[0]))
            int_pref = [int(p) for p in pref[1].split(' ')]
            prefs.append(int_pref)
    return n, prefs

if __name__ == 'main':
    parser = argparse.ArgumentParser(description='Inputs for stable matching algorithm for genders')
    parser.add_argument('--men', required=True)
    parser.add_argument('--women', required=True)
    arguments = parser.parse_args()
    m, man_pref = extract_pref_for_gender(arguments.men)
    w, woman_pref = extract_pref_for_gender(arguments.women)

    current = initialize_current(w)
    next = initialize_next(m)
    ranking = initialize_ranking(woman_pref)
    men = list_utilities.to_linked_list(m)
    match_genders(men, man_pref, current, next, ranking)
    print(current)
