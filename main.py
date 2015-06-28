#!/usr/bin/python

from random import randint

pronouns={'1st_person_sing': 'Yo', '2nd_person_sing':'Tu', '3rd_person_sing_masc':'El', '3rd_person_sing_fem':'Ella'}

verbs=['hablar', 'opinar', 'terminar', 'llegar', 'ganar']

def verb_conjugation ( verb, person):
    verb = verb[:-2]
    if person == '1st_person_sing':
        verb = verb + 'o'
    if person == '2nd_person_sing':
        verb = verb + 'as'
    if person == '3rd_person_sing_masc' or person == '3rd_person_sing_fem':
         verb = verb + 'a'
    return verb 


random_person_num=randint(0,3)
pronoun_keys=pronouns.keys()
pronoun=pronoun_keys[random_person_num]


random_verb_num=randint(0,4)
verb=verbs[random_verb_num]
conjugated_verb = verb_conjugation(verb, pronoun)

#print pronoun_keys
#print random_person_num
#print pronoun
#print random_verb

print pronouns[pronoun] +' ' + conjugated_verb
