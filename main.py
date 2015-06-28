#!/usr/bin/python

pronouns={'1st_person_sing': 'yo', '2nd_person_sing':'tu', '3rd_person_sing_masc':'el', '3rd_person_sing_fem':'ella'}

verbs=['hablar', 'opinar', 'terminar', 'llegar', 'ganar']

def verb_conjugation ( verb, person):
    verb = verb[:-2]
    if person == '1st_person_sing':
        verb = verb + 'o'
    if person == '2nd_person_sing':
        verb = verb + 'as'
    if person == '3rd_person_sing_masc' || person == '3rd_person_sing_fem':
         verb = verb + 'a'
    return verb 

random_verb = verb_conjugation (verbs[0], '1st_person_sing')

print random_verb
