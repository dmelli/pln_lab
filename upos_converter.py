#!/usr/bin/python
# -*- coding: utf-8 -*-
from trans_lineal import remaining_to_string

def upos_converter(tags):
#    print(tags[0])
    if tags[0] == 'A':
        #(A,type,degree,gender,num,possessorpers,possessornum)
        postype = tags[1]
        gen = tags[3]
        num = tags[4]
        posfunction = tags[5]
#        print(postype+'-'+gen+'-'+num)
        if postype == 'Q' and gen == 'M' and num == 'S' and posfunction == 'participle':
            return 'ADJ','Gender=Masc|Number=Sing|VerbForm=Part'
        elif postype == 'Q' and gen == 'M' and num == 'S':
            return 'ADJ','Gender=Masc|Number=Sing'
        elif postype == 'Q' and gen == 'M' and num == 'P' and posfunction == 'participle':
            return 'ADJ','Gender=Masc|Number=Plur|VerbForm=Part'
        elif postype == 'Q' and gen == 'M' and num == 'P':
            return 'ADJ','Gender=Masc|Number=Plur'
        elif postype == 'Q' and gen == 'F' and num == 'S' and posfunction == 'participle':
            return 'ADJ','Gender=Fem|Number=Sing|VerbForm=Part'
        elif postype == 'Q' and gen == 'F' and num == 'S':
            return 'ADJ','Gender=Fem|Number=Sing'
        elif postype == 'Q' and gen == 'F' and num == 'P' and posfunction == 'participle':
            return 'ADJ','Gender=Fem|Number=Plur|VerbForm=Part'
        elif postype == 'Q' and gen == 'F' and num == 'P':
            return 'ADJ','Gender=Fem|Number=Plur'
        elif postype == 'Q' and gen == 'C' and num == 'S':
            return 'ADJ','Number=Sing'
        elif postype == 'Q' and gen == 'C' and num == 'P':
            return 'ADJ','Number=Plur'
        elif postype == 'Q' and gen == 'C' and num == 'C':
            return 'ADJ',''
        elif postype == 'O' and gen == 'M' and num == 'S':
            return 'ADJ','Gender=Masc|NumType=Ord|Number=Sing'
        elif postype == 'O' and gen == 'M' and num == 'P':
            return 'ADJ','Gender=Masc|NumType=Ord|Number=Plur'
        elif postype == 'O' and gen == 'F' and num == 'S':
            return 'ADJ','Gender=Fem|NumType=Ord|Number=Sing'
        elif postype == 'O' and gen == 'F' and num == 'P':
            return 'ADJ','Gender=Fem|NumType=Ord|Number=Plur'
        elif postype == 'O' and gen == 'C' and num == 'S':
            return 'ADJ','NumType=Ord|Number=Sing'
        # Traducimos linealmente los remanentes a un String
        else:
            return 'ADJ', remaining_to_string(tags)
    elif tags[0] == 'C':
        #type/C:coordinating;S:subordinating
        postype = tags[1]
        if postype=='S':
            return 'SCONJ',''
        elif postype=='C':
            return 'CONJ',''
        else: #_
            return 'CONJ',''
    elif tags[0] == 'D':
        #type/A:article;D:demonstrative;I:indefinite;P:possessive;T:interrogative;E:exclamative 
        #person/1:1;2:2;3:3 
        #Gender/F:feminine;M:masculine;C:common 
        #num/S:singular;P:plural;N:invariable 
        #possessornum/S:singular;P:plural;N:invariable
        postype = tags[1]
        person = tags[2]
        gen = tags[3]
        num = tags[4]
        possessornum = tags[5]
        if postype=='R' and gen=='C' and num=='S':
            return 'DET','Number=Sing|PronType=Rel'
        elif postype=='R' and gen=='C' and num=='C':
            return 'DET','PronType=Rel'
        elif postype=='P' and gen=='M' and num=='S' and person=='3':
            return 'DET','Gender=Masc|Number=Sing|Person=3|Poss=Yes|PronType=Prs'
        elif postype=='P' and gen=='M' and num=='S' and person=='2' and possessornum=='S':
            return 'DET','Gender=Masc|Number=Sing|Number[psor]=Sing|Person=2|Poss=Yes|PronType=Prs'
        elif postype=='P' and gen=='M' and num=='S' and person=='1' and possessornum=='S':
            return 'DET','Gender=Masc|Number=Sing|Number[psor]=Sing|Person=1|Poss=Yes|PronType=Prs'
        elif postype=='P' and gen=='M' and num=='S' and person=='1' and possessornum=='P':
            return 'DET','Gender=Masc|Number=Sing|Number[psor]=Plur|Person=1|Poss=Yes|PronType=Prs'
        elif postype=='P' and gen=='M' and num=='P' and person=='3':
            return 'DET','Gender=Masc|Number=Plur|Person=3|Poss=Yes|PronType=Prs'
        elif postype=='P' and gen=='M' and num=='P' and person=='2' and possessornum=='S':
            return 'DET','Gender=Masc|Number=Plur|Number[psor]=Sing|Person=2|Poss=Yes|PronType=Prs'
        elif postype=='P' and gen=='M' and num=='P' and person=='1' and possessornum=='S':
            return 'DET','Gender=Masc|Number=Plur|Number[psor]=Sing|Person=1|Poss=Yes|PronType=Prs'
        elif postype=='P' and gen=='M' and num=='P' and person=='1' and possessornum=='P':
            return 'DET','Gender=Masc|Number=Plur|Number[psor]=Plur|Person=1|Poss=Yes|PronType=Prs'
        elif postype=='P' and gen=='F' and num=='S' and person=='3':
            return 'DET','Gender=Fem|Number=Sing|Person=3|Poss=Yes|PronType=Prs'
        elif postype=='P' and gen=='F' and num=='S' and person=='2' and possessornum=='S':
            return 'DET','Gender=Fem|Number=Sing|Number[psor]=Sing|Person=2|Poss=Yes|PronType=Prs'
        elif postype=='P' and gen=='F' and num=='S' and person=='1' and possessornum=='P':
            return 'DET','Gender=Fem|Number=Sing|Number[psor]=Sing|Person=1|Poss=Yes|PronType=Prs'
        elif postype=='P' and gen=='F' and num=='S' and person=='1' and possessornum=='S':
            return 'DET','Gender=Fem|Number=Sing|Number[psor]=Plur|Person=1|Poss=Yes|PronType=Prs'
        elif postype=='P' and gen=='F' and num=='P' and person=='3':
            return 'DET','Gender=Fem|Number=Plur|Person=3|Poss=Yes|PronType=Prs'
        elif postype=='P' and gen=='F' and num=='P' and person=='1' and possessornum=='S':
            return 'DET','Gender=Fem|Number=Plur|Number[psor]=Sing|Person=1|Poss=Yes|PronType=Prs'
        elif postype=='P' and gen=='F' and num=='P' and person=='1' and possessornum=='P':
            return 'DET','Gender=Fem|Number=Plur|Number[psor]=Plur|Person=1|Poss=Yes|PronType=Prs'
        elif postype=='P' and gen=='C' and num=='P' and person=='1' and possessornum=='P':
            return 'DET','Number=Plur|Number[psor]=Plur|Person=1|Poss=Yes|PronType=Prs'
        elif postype=='numeral' and gen=='M' and num=='S':
            return 'NUM','Gender=Masc|NumType=Card|Number=Sing'
        elif postype=='numeral' and gen=='M' and num=='P':
            return 'NUM','Gender=Masc|NumType=Card|Number=Plur'
        elif postype=='numeral' and gen=='F' and num=='S':
            return 'NUM','Gender=Fem|NumType=Card|Number=Sing'
        elif postype=='numeral' and gen=='F' and num=='P':
            return 'NUM','Gender=Fem|NumType=Card|Number=Plur'
        elif postype=='numeral' and gen=='C' and num=='S':
            return 'NUM','NumType=Card|Number=Sing'
        elif postype=='numeral' and gen=='C' and num=='P':
            return 'NUM','NumType=Card|Number=Plur'
        elif postype=='T' and gen=='M' and num=='S':
            return 'DET','Gender=Masc|Number=Sing|PronType=Int'
        elif postype=='T' and gen=='M' and num=='P':
            return 'DET','Gender=Masc|Number=Plur|PronType=Int'
        elif postype=='T' and gen=='F' and num=='S':
            return 'DET','Gender=Fem|Number=Sing|PronType=Int'
        elif postype=='T' and gen=='F' and num=='P':
            return 'DET','Gender=Fem|Number=Plur|PronType=Int'
        elif postype=='I' and gen=='M' and num=='S':
            return 'DET','Gender=Masc|Number=Sing|PronType=Ind'
        elif postype=='I' and gen=='M' and num=='P':
            return 'DET','Gender=Masc|Number=Plur|PronType=Ind'
        elif postype=='I' and gen=='F' and num=='S':
            return 'DET','Gender=Fem|Number=Sing|PronType=Ind'
        elif postype=='I' and gen=='F' and num=='P':
            return 'DET','Gender=Fem|Number=Plur|PronType=Ind'
        elif postype=='I' and gen=='C' and num=='S':
            return 'DET','Number=Sing|PronType=Ind'
        elif postype=='I' and gen=='C' and num=='P':
            return 'DET','Number=Plur|PronType=Ind'
        elif postype=='I' and gen=='C' and num=='C':
            return 'DET','PronType=Ind'
        elif postype=='exclamative' and gen=='C' and num=='C':
            return 'DET','PronType=Rel'
        elif postype=='D' and gen=='M' and num=='S':
            return 'DET','Gender=Masc|Number=Sing|PronType=Dem'
        elif postype=='D' and gen=='M' and num=='P':
            return 'DET','Gender=Masc|Number=Plur|PronType=Dem'
        elif postype=='D' and gen=='F' and num=='S':
            return 'DET','Gender=Fem|Number=Sing|PronType=Dem'
        elif postype=='D' and gen=='F' and num=='P':
            return 'DET','Gender=Fem|Number=Plur|PronType=Dem'
        elif postype=='D' and gen=='C' and num=='S':
            return 'DET','Number=Sing|PronType=Dem'
        elif postype=='D' and gen=='C' and num=='P':
            return 'DET','Number=Plur|PronType=Dem'
        elif postype=='A' and gen=='M' and num=='S':
            return 'DET','Gender=Masc|Number=Sing|PronType=Art'
        elif postype=='A' and gen=='M' and num=='P':
            return 'DET','Gender=Masc|Number=Plur|PronType=Art'
        elif postype=='A' and gen=='F' and num=='S':
            return 'DET','Gender=Fem|Number=Sing|PronType=Art'
        elif postype=='A' and gen=='F' and num=='P':
            return 'DET','Gender=Fem|Number=Plur|PronType=Art'
        elif postype=='A' and gen=='C' and num=='S':
            return 'DET','Number=Sing|PronType=Art'
        # Traducimos linealmente los remanentes a un String
        else:
            return 'DET', remaining_to_string(tags)

    elif tags[0] == 'N':	
        postype = tags[1]
        gen = tags[2]
        num = tags[3]
	#N 2 noun type/C:common;P:proper 
	#Gender/F:feminine;M:masculine;C:common 
	#num/S:singular;P:plural;N:invariable 
	#neclass/S:person;G:location;O:organization;V:other 
	#nesubclass/0:0;P:0 
	#degree/V:evaluative	
        if postype=='P' and gen=='M' and num=='S':
            return 'PROPN','Gender=Masc|Number=Sing'
        elif postype=='P' and gen=='C' and num=='C':
            return 'PROPN',''
        elif postype=='C' and gen=='M' and num=='S':
            return 'NOUN','Gender=Masc|Number=Sing'
        elif postype=='C' and gen=='M' and num=='P':
            return 'NOUN','Gender=Masc|Number=Plur'
        elif postype=='C' and gen=='M' and num=='C':
            return 'NOUN','Gender=Masc'
        elif postype=='C' and gen=='F' and num=='S':
            return 'NOUN','Gender=Fem|Number=Sing'
        elif postype=='C' and gen=='F' and num=='P':
            return 'NOUN','Gender=Fem|Number=Plur'
        elif postype=='C' and gen=='F' and num=='C':
            return 'NOUN','Gender=Fem'
        elif postype=='C' and gen=='C' and num=='S':
            return 'NOUN','Number=Sing'
        elif postype=='C' and gen=='C' and num=='P':
            return 'NOUN','Number=Plur'
        elif postype=='C' and gen=='C' and num=='C':
            return 'NOUN',''
        # Traducimos linealmente los remanentes a un String
        else:
            return 'NOUN', remaining_to_string(tags)

    elif tags[0] == 'P':
	#P 2 pronoun type/D:demonstrative;E:exclamative;I:indefinite;P:personal;R:relative;T:interrogative 
	#person/1:1;2:2;3:3 
	#Gender/F:feminine;M:masculine;C:common 
	#num/S:singular;P:plural;N:invariable 
	#case/N:nominative;A:accusative;D:dative;O:oblique 
	#polite/P:yes
        postype = tags[1]
        person = tags[2]
        gen = tags[3]
        num = tags[4]
        case = tags[5]
        polite = tags[5]
        if postype=='R' and gen=='M' and num=='S':
            return 'PRON','Gender=Masc|Number=Sing|PronType=Rel'
        elif postype=='R' and gen=='C' and num=='S':
            return 'PRON','Number=Sing|PronType=Rel'
        elif postype=='R' and gen=='C' and num=='P':
            return 'PRON','Number=Plur|PronType=Rel'
        elif postype=='R' and gen=='C' and num=='C':
            return 'PRON','PronType=Rel'
        elif postype=='possessive' and gen=='M' and num=='S' and person=='3':
            return 'PRON','Gender=Masc|Number=Sing|Person=3|Poss=Yes|PronType=Prs'
        elif postype=='possessive' and gen=='M' and num=='S' and person=='1' and possessornum=='P':
            return 'PRON','Gender=Masc|Number=Sing|Number[psor]=Plur|Person=1|Poss=Yes|PronType=Prs'
        elif postype=='possessive' and gen=='M' and num=='P' and person=='3':
            return 'PRON','Gender=Masc|Number=Plur|Person=3|Poss=Yes|PronType=Prs'
        elif postype=='possessive' and gen=='F' and num=='S' and person=='3' and possessornum=='S':
            return 'PRON','Gender=Fem|Number=Sing|Number[psor]=Sing|Person=3|Poss=Yes|PronType=Prs'
        elif postype=='possessive' and gen=='F' and num=='S' and person=='3':
            return 'PRON','Gender=Fem|Number=Sing|Person=3|Poss=Yes|PronType=Prs'
        elif postype=='possessive' and gen=='F' and num=='S' and person=='1' and possessornum=='P':
            return 'PRON','Gender=Fem|Number=Sing|Number[psor]=Plur|Person=1|Poss=Yes|PronType=Prs'
        elif postype=='possessive' and gen=='F' and num=='P' and person=='3' and possessornum=='S':
            return 'PRON','Gender=Fem|Number=Plur|Number[psor]=Sing|Person=3|Poss=Yes|PronType=Prs'
        elif postype=='possessive' and gen=='F' and num=='P' and person=='3':
            return 'PRON','Gender=Fem|Number=Plur|Person=3|Poss=Yes|PronType=Prs'
        elif postype=='possessive' and gen=='F' and num=='P' and person=='1' and possessornum=='P':
            return 'PRON','Gender=Fem|Number=Plur|Number[psor]=Plur|Person=1|Poss=Yes|PronType=Prs'
        elif postype=='possessive' and gen=='C' and num=='S' and person=='3' and possessornum=='P':
            return 'PRON','Number=Sing|Number[psor]=Plur|Person=3|Poss=Yes|PronType=Prs'
        elif postype=='possessive' and gen=='C' and num=='P' and person=='3' and possessornum=='P':
            return 'PRON','Number=Plur|Number[psor]=Plur|Person=3|Poss=Yes|PronType=Prs'
        elif postype=='P' and gen=='M' and num=='S' and person=='3' and case=='A':
            return 'PRON','Case=Acc|Gender=Masc|Number=Sing|Person=3|PronType=Prs'
        elif postype=='P' and gen=='M' and num=='S' and person=='3':
            return 'PRON','Gender=Masc|Number=Sing|Person=3|PronType=Prs'
        elif postype=='P' and gen=='M' and num=='P' and person=='3' and case=='A':
            return 'PRON','Case=Acc|Gender=Masc|Number=Plur|Person=3|PronType=Prs'
        elif postype=='P' and gen=='M' and num=='P' and person=='3':
            return 'PRON','Gender=Masc|Number=Plur|Person=3|PronType=Prs'
        elif postype=='P' and gen=='F' and num=='S' and person=='3' and case=='A':
            return 'PRON','Case=Acc|Gender=Fem|Number=Sing|Person=3|PronType=Prs'
        elif postype=='P' and gen=='F' and num=='S' and person=='3':
            return 'PRON','Gender=Fem|Number=Sing|Person=3|PronType=Prs'
        elif postype=='P' and gen=='F' and num=='P' and person=='3' and case=='A':
            return 'PRON','Case=Acc|Gender=Fem|Number=Plur|Person=3|PronType=Prs'
        elif postype=='P' and gen=='F' and num=='P' and person=='3':
            return 'PRON','Gender=Fem|Number=Plur|Person=3|PronType=Prs'
        elif postype=='P' and gen=='C' and num=='S' and person=='3' and case=='D':
            return 'PRON','Case=Dat|Number=Sing|Person=3|PronType=Prs'
        elif postype=='P' and gen=='C' and num=='S' and person=='3' and case=='A':
            return 'PRON','Case=Acc|Number=Sing|Person=3|PronType=Prs'
        elif postype=='P' and gen=='C' and num=='S' and person=='2' and polite=='P':
            return 'PRON','Number=Sing|Person=2|Polite=Pol|PronType=Prs'
        elif postype=='P' and gen=='C' and num=='S' and person=='2':
            return 'PRON','Number=Sing|Person=2|PronType=Prs'
        elif postype=='P' and gen=='C' and num=='S' and person=='1' and case=='O':
            return 'PRON','Number=Sing|Person=1|PrepCase=Pre|PronType=Prs'
        elif postype=='P' and gen=='C' and num=='S' and person=='1' and case=='N':
            return 'PRON','Case=Nom|Number=Sing|Person=1|PronType=Prs'
        elif postype=='P' and gen=='C' and num=='S' and person=='1':
            return 'PRON','Number=Sing|Person=1|PronType=Prs'
        elif postype=='P' and gen=='C' and num=='P' and person=='3':
            return 'PRON','Number=Plur|Person=3|PronType=Prs'
        elif postype=='P' and gen=='C' and num=='P' and person=='2' and polite=='P':
            return 'PRON','Number=Plur|Person=2|Polite=Pol|PronType=Prs'
        elif postype=='P' and gen=='C' and num=='P' and person=='2':
            return 'PRON','Number=Plur|Person=2|PronType=Prs'
        elif postype=='P' and gen=='C' and num=='P' and person=='1':
            return 'PRON','Number=Plur|Person=1|PronType=Prs'
        elif postype=='P' and gen=='C' and num=='C' and person=='3' and case=='O':
            return 'PRON','Person=3|PrepCase=Pre|PronType=Prs'
        elif postype=='P' and gen=='C' and num=='C' and person=='3':
            return 'PRON','Person=3|PronType=Prs'
        elif postype=='numeral' and gen=='M' and num=='S':
            return 'NUM','Gender=Masc|NumType=Card|Number=Sing'
        elif postype=='numeral' and gen=='M' and num=='P':
            return 'NUM','Gender=Masc|NumType=Card|Number=Plur'
        elif postype=='numeral' and gen=='F' and num=='S':
            return 'NUM','Gender=Fem|NumType=Card|Number=Sing'
        elif postype=='numeral' and gen=='F' and num=='P':
            return 'NUM','Gender=Fem|NumType=Card|Number=Plur'
        elif postype=='numeral' and gen=='C' and num=='S':
            return 'NUM','NumType=Card|Number=Sing'
        elif postype=='numeral' and gen=='C' and num=='P':
            return 'NUM','NumType=Card|Number=Plur'
        elif postype=='T' and gen=='M' and num=='S':
            return 'PRON','Gender=Masc|Number=Sing|PronType=Int'
        elif postype=='T' and gen=='M' and num=='P':
            return 'PRON','Gender=Masc|Number=Plur|PronType=Int'
        elif postype=='T' and gen=='F' and num=='S':
            return 'PRON','Gender=Fem|Number=Sing|PronType=Int'
        elif postype=='T' and gen=='F' and num=='P':
            return 'PRON','Gender=Fem|Number=Plur|PronType=Int'
        elif postype=='T' and gen=='C' and num=='S':
            return 'PRON','Number=Sing|PronType=Int'
        elif postype=='T' and gen=='C' and num=='C':
            return 'PRON','PronType=Int'
        elif postype=='I' and gen=='M' and num=='S':
            return 'PRON','Gender=Masc|Number=Sing|PronType=Ind'
        elif postype=='I' and gen=='M' and num=='P':
            return 'PRON','Gender=Masc|Number=Plur|PronType=Ind'
        elif postype=='I' and gen=='F' and num=='S':
            return 'PRON','Gender=Fem|Number=Sing|PronType=Ind'
        elif postype=='I' and gen=='F' and num=='P':
            return 'PRON','Gender=Fem|Number=Plur|PronType=Ind'
        elif postype=='I' and gen=='C' and num=='S':
            return 'PRON','Number=Sing|PronType=Ind'
        elif postype=='I' and gen=='C' and num=='P':
            return 'PRON','Number=Plur|PronType=Ind'
        elif postype=='I' and gen=='C' and num=='C':
            return 'PRON','PronType=Ind'
        elif postype=='D' and gen=='M' and num=='S':
            return 'PRON','Gender=Masc|Number=Sing|PronType=Dem'
        elif postype=='D' and gen=='M' and num=='P':
            return 'PRON','Gender=Masc|Number=Plur|PronType=Dem'
        elif postype=='D' and gen=='F' and num=='S':
            return 'PRON','Gender=Fem|Number=Sing|PronType=Dem'
        elif postype=='D' and gen=='F' and num=='P':
            return 'PRON','Gender=Fem|Number=Plur|PronType=Dem'
        elif postype=='D' and gen=='C' and num=='S':
            return 'PRON','Number=Sing|PronType=Dem'
        elif postype=='D' and gen=='C' and num=='P':
            return 'PRON','Number=Plur|PronType=Dem'
        elif gen=='C' and num=='S' and person=='2':
            return 'PRON','Number=Sing|Person=2'
        elif gen=='C' and num=='S' and person=='1':
            return 'PRON','Number=Sing|Person=1'
        elif gen=='C' and num=='P' and person=='2':
            return 'PRON','Number=Plur|Person=2'
        elif gen=='C' and num=='P' and person=='1':
            return 'PRON','Number=Plur|Person=1'
        elif gen=='C' and num=='C' and person=='3':
            return 'PRON','Person=3'
        elif gen=='C' and num=='C':
            return 'PRON',''
        # Traducimos linealmente los remanentes a un String
        else:
            return 'PRON', remaining_to_string(tags)
    elif tags[0] == 'V':
	#V 3 verb type/M:main;A:auxiliary;S:semiauxiliary 
	#mood/I:indicative;S:subjunctive;M:imperative;P:participle;G:gerund;N:infinitive 
	#tense/P:present;I:imperfect;F:future;S:past;C:conditional 
	#person/1:1;2:2;3:3 
	#num/S:singular;P:plural 
	#Gender/F:feminine;M:masculine;C:common
        postype = tags[1]
        mood = tags[2]
        tense = tags[3]
        person = tags[4]
        num = tags[5]
        gen = tags[6]
	#consistencia de tipos
        if gen=='0':
            gen=='C'
        if postype=='S' and gen=='M' and num=='S' and mood=='P' and tense=='S':
            return 'AUX','Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part'
        elif postype=='S' and gen=='C' and num=='S' and person=='3' and mood=='S' and tense=='P':
            return 'AUX','Mood=Sub|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin'
        elif postype=='S' and gen=='C' and num=='S' and person=='3' and mood=='S' and tense=='I':
            return 'AUX','Mood=Sub|Number=Sing|Person=3|Tense=Imp|VerbForm=Fin'
        elif postype=='S' and gen=='C' and num=='S' and person=='3' and mood=='I' and tense=='P':
            return 'AUX','Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin'
        elif postype=='S' and gen=='C' and num=='S' and person=='3' and mood=='I' and tense=='S':
            return 'AUX','Mood=Ind|Number=Sing|Person=3|Tense=Past|VerbForm=Fin'
        elif postype=='S' and gen=='C' and num=='S' and person=='3' and mood=='I' and tense=='I':
            return 'AUX','Mood=Ind|Number=Sing|Person=3|Tense=Imp|VerbForm=Fin'
        elif postype=='S' and gen=='C' and num=='S' and person=='3' and mood=='I' and tense=='F':
            return 'AUX','Mood=Ind|Number=Sing|Person=3|Tense=Fut|VerbForm=Fin'
        elif postype=='S' and gen=='C' and num=='S' and person=='3' and mood=='I' and tense=='C':
            return 'AUX','Mood=Cnd|Number=Sing|Person=3|VerbForm=Fin'
        elif postype=='S' and gen=='C' and num=='S' and person=='3' and mood=='M':
            return 'AUX','Mood=Imp|Number=Sing|Person=3|VerbForm=Fin'
        elif postype=='S' and gen=='C' and num=='S' and person=='2' and mood=='I' and tense=='P':
            return 'AUX','Mood=Ind|Number=Sing|Person=2|Tense=Pres|VerbForm=Fin'
        elif postype=='S' and gen=='C' and num=='S' and person=='1' and mood=='I' and tense=='P':
            return 'AUX','Mood=Ind|Number=Sing|Person=1|Tense=Pres|VerbForm=Fin'
        elif postype=='S' and gen=='C' and num=='S' and person=='1' and mood=='I' and tense=='I':
            return 'AUX','Mood=Ind|Number=Sing|Person=1|Tense=Imp|VerbForm=Fin'
        elif postype=='S' and gen=='C' and num=='P' and person=='3' and mood=='S' and tense=='P':
            return 'AUX','Mood=Sub|Number=Plur|Person=3|Tense=Pres|VerbForm=Fin'
        elif postype=='S' and gen=='C' and num=='P' and person=='3' and mood=='S' and tense=='I':
            return 'AUX','Mood=Sub|Number=Plur|Person=3|Tense=Imp|VerbForm=Fin'
        elif postype=='S' and gen=='C' and num=='P' and person=='3' and mood=='I' and tense=='P':
            return 'AUX','Mood=Ind|Number=Plur|Person=3|Tense=Pres|VerbForm=Fin'
        elif postype=='S' and gen=='C' and num=='P' and person=='3' and mood=='I' and tense=='S':
            return 'AUX','Mood=Ind|Number=Plur|Person=3|Tense=Past|VerbForm=Fin'
        elif postype=='S' and gen=='C' and num=='P' and person=='3' and mood=='I' and tense=='I':
            return 'AUX','Mood=Ind|Number=Plur|Person=3|Tense=Imp|VerbForm=Fin'
        elif postype=='S' and gen=='C' and num=='P' and person=='3' and mood=='I' and tense=='F':
            return 'AUX','Mood=Ind|Number=Plur|Person=3|Tense=Fut|VerbForm=Fin'
        elif postype=='S' and gen=='C' and num=='P' and person=='3' and mood=='I' and tense=='C':
            return 'AUX','Mood=Cnd|Number=Plur|Person=3|VerbForm=Fin'
        elif postype=='S' and gen=='C' and num=='P' and person=='3' and mood=='M':
            return 'AUX','Mood=Imp|Number=Plur|Person=3|VerbForm=Fin'
        elif postype=='S' and gen=='C' and num=='P' and person=='1' and mood=='S' and tense=='P':
            return 'AUX','Mood=Sub|Number=Plur|Person=1|Tense=Pres|VerbForm=Fin'
        elif postype=='S' and gen=='C' and num=='P' and person=='1' and mood=='I' and tense=='P':
            return 'AUX','Mood=Ind|Number=Plur|Person=1|Tense=Pres|VerbForm=Fin'
        elif postype=='S' and gen=='C' and num=='P' and person=='1' and mood=='I' and tense=='I':
            return 'AUX','Mood=Ind|Number=Plur|Person=1|Tense=Imp|VerbForm=Fin'
        elif postype=='S' and gen=='C' and num=='C' and mood=='N':
            return 'AUX','VerbForm=Inf'
        elif postype=='S' and gen=='C' and num=='C' and mood=='G':
            return 'AUX','VerbForm=Ger'
        
        elif postype=='M' and gen=='M' and num=='S' and mood=='P' and tense=='S':
            return 'VERB','Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part'
        elif postype=='M' and gen=='M' and num=='P' and mood=='P' and tense=='S':
            return 'VERB','Gender=Masc|Number=Plur|Tense=Past|VerbForm=Part'
        elif postype=='M' and gen=='F' and num=='S' and mood=='P' and tense=='S':
            return 'VERB','Gender=Fem|Number=Sing|Tense=Past|VerbForm=Part'
        elif postype=='M' and gen=='F' and num=='P' and mood=='P' and tense=='S':
            return 'VERB','Gender=Fem|Number=Plur|Tense=Past|VerbForm=Part'
        elif postype=='M' and gen=='C' and num=='S' and person=='3' and mood=='S' and tense=='P':
            return 'VERB','Mood=Sub|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin'
        elif postype=='M' and gen=='C' and num=='S' and person=='3' and mood=='S' and tense=='I':
            return 'VERB','Mood=Sub|Number=Sing|Person=3|Tense=Imp|VerbForm=Fin'
        elif postype=='M' and gen=='C' and num=='S' and person=='3' and mood=='I' and tense=='P':
            return 'VERB','Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin'
        elif postype=='M' and gen=='C' and num=='S' and person=='3' and mood=='I' and tense=='S':
            return 'VERB','Mood=Ind|Number=Sing|Person=3|Tense=Past|VerbForm=Fin'
        elif postype=='M' and gen=='C' and num=='S' and person=='3' and mood=='I' and tense=='I':
            return 'VERB','Mood=Ind|Number=Sing|Person=3|Tense=Imp|VerbForm=Fin'
        elif postype=='M' and gen=='C' and num=='S' and person=='3' and mood=='I' and tense=='F':
            return 'VERB','Mood=Ind|Number=Sing|Person=3|Tense=Fut|VerbForm=Fin'
        elif postype=='M' and gen=='C' and num=='S' and person=='3' and mood=='I' and tense=='C':
            return 'VERB','Mood=Cnd|Number=Sing|Person=3|VerbForm=Fin'
        elif postype=='M' and gen=='C' and num=='S' and person=='3' and mood=='M':
            return 'VERB','Mood=Imp|Number=Sing|Person=3|VerbForm=Fin'
        elif postype=='M' and gen=='C' and num=='S' and person=='2' and mood=='S' and tense=='P':
            return 'VERB','Mood=Sub|Number=Sing|Person=2|Tense=Pres|VerbForm=Fin'
        elif postype=='M' and gen=='C' and num=='S' and person=='2' and mood=='I' and tense=='P':
            return 'VERB','Mood=Ind|Number=Sing|Person=2|Tense=Pres|VerbForm=Fin'
        elif postype=='M' and gen=='C' and num=='S' and person=='2' and mood=='M':
            return 'VERB','Mood=Imp|Number=Sing|Person=2|VerbForm=Fin'
        elif postype=='M' and gen=='C' and num=='S' and person=='1' and mood=='S' and tense=='P':
            return 'VERB','Mood=Sub|Number=Sing|Person=1|Tense=Pres|VerbForm=Fin'
        elif postype=='M' and gen=='C' and num=='S' and person=='1' and mood=='S' and tense=='I':
            return 'VERB','Mood=Sub|Number=Sing|Person=1|Tense=Imp|VerbForm=Fin'
        elif postype=='M' and gen=='C' and num=='S' and person=='1' and mood=='I' and tense=='P':
            return 'VERB','Mood=Ind|Number=Sing|Person=1|Tense=Pres|VerbForm=Fin'
        elif postype=='M' and gen=='C' and num=='S' and person=='1' and mood=='I' and tense=='I':
            return 'VERB','Mood=Ind|Number=Sing|Person=1|Tense=Imp|VerbForm=Fin'
        elif postype=='M' and gen=='C' and num=='S' and person=='1' and mood=='I' and tense=='F':
            return 'VERB','Mood=Ind|Number=Sing|Person=1|Tense=Fut|VerbForm=Fin'
        elif postype=='M' and gen=='C' and num=='S' and person=='1' and mood=='I' and tense=='C':
            return 'VERB','Mood=Cnd|Number=Sing|Person=1|VerbForm=Fin'
        elif postype=='M' and gen=='C' and num=='P' and person=='3' and mood=='S' and tense=='P':
            return 'VERB','Mood=Sub|Number=Plur|Person=3|Tense=Pres|VerbForm=Fin'
        elif postype=='M' and gen=='C' and num=='P' and person=='3' and mood=='S' and tense=='I':
            return 'VERB','Mood=Sub|Number=Plur|Person=3|Tense=Imp|VerbForm=Fin'
        elif postype=='M' and gen=='C' and num=='P' and person=='3' and mood=='I' and tense=='P':
            return 'VERB','Mood=Ind|Number=Plur|Person=3|Tense=Pres|VerbForm=Fin'
        elif postype=='M' and gen=='C' and num=='P' and person=='3' and mood=='I' and tense=='S':
            return 'VERB','Mood=Ind|Number=Plur|Person=3|Tense=Past|VerbForm=Fin'
        elif postype=='M' and gen=='C' and num=='P' and person=='3' and mood=='I' and tense=='I':
            return 'VERB','Mood=Ind|Number=Plur|Person=3|Tense=Imp|VerbForm=Fin'
        elif postype=='M' and gen=='C' and num=='P' and person=='3' and mood=='I' and tense=='F':
            return 'VERB','Mood=Ind|Number=Plur|Person=3|Tense=Fut|VerbForm=Fin'
        elif postype=='M' and gen=='C' and num=='P' and person=='3' and mood=='I' and tense=='C':
            return 'VERB','Mood=Cnd|Number=Plur|Person=3|VerbForm=Fin'
        elif postype=='M' and gen=='C' and num=='P' and person=='3' and mood=='M':
            return 'VERB','Mood=Imp|Number=Plur|Person=3|VerbForm=Fin'
        elif postype=='M' and gen=='C' and num=='P' and person=='2' and mood=='S' and tense=='P':
            return 'VERB','Mood=Sub|Number=Plur|Person=2|Tense=Pres|VerbForm=Fin'
        elif postype=='M' and gen=='C' and num=='P' and person=='2' and mood=='I' and tense=='P':
            return 'VERB','Mood=Ind|Number=Plur|Person=2|Tense=Pres|VerbForm=Fin'
        elif postype=='M' and gen=='C' and num=='P' and person=='2' and mood=='I' and tense=='F':
            return 'VERB','Mood=Ind|Number=Plur|Person=2|Tense=Fut|VerbForm=Fin'
        elif postype=='M' and gen=='C' and num=='P' and person=='1' and mood=='S' and tense=='P':
            return 'VERB','Mood=Sub|Number=Plur|Person=1|Tense=Pres|VerbForm=Fin'
        elif postype=='M' and gen=='C' and num=='P' and person=='1' and mood=='S' and tense=='I':
            return 'VERB','Mood=Sub|Number=Plur|Person=1|Tense=Imp|VerbForm=Fin'
        elif postype=='M' and gen=='C' and num=='P' and person=='1' and mood=='I' and tense=='P':
            return 'VERB','Mood=Ind|Number=Plur|Person=1|Tense=Pres|VerbForm=Fin'
        elif postype=='M' and gen=='C' and num=='P' and person=='1' and mood=='I' and tense=='I':
            return 'VERB','Mood=Ind|Number=Plur|Person=1|Tense=Imp|VerbForm=Fin'
        elif postype=='M' and gen=='C' and num=='P' and person=='1' and mood=='I' and tense=='F':
            return 'VERB','Mood=Ind|Number=Plur|Person=1|Tense=Fut|VerbForm=Fin'
        elif postype=='M' and gen=='C' and num=='P' and person=='1' and mood=='I' and tense=='C':
            return 'VERB','Mood=Cnd|Number=Plur|Person=1|VerbForm=Fin'
        elif postype=='M' and gen=='C' and num=='P' and person=='1' and mood=='M':
            return 'VERB','Mood=Imp|Number=Plur|Person=1|VerbForm=Fin'
        elif postype=='M' and gen=='C' and num=='C' and mood=='P' and tense=='S':
            return 'VERB','Tense=Past|VerbForm=Part'
        elif postype=='M' and gen=='C' and num=='C' and mood=='N':
            return 'VERB','VerbForm=Inf'
        elif postype=='M' and gen=='C' and num=='C' and mood=='G':
            return 'VERB','VerbForm=Ger'
        elif postype=='M' and gen=='C' and num=='C':
            return 'VERB',''
        
        elif postype=='A' and gen=='M' and num=='S' and mood=='P' and tense=='S':
            return 'AUX','Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part'
        elif postype=='A' and gen=='C' and num=='S' and person=='3' and mood=='S' and tense=='P':
            return 'AUX','Mood=Sub|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin'
        elif postype=='A' and gen=='C' and num=='S' and person=='3' and mood=='S' and tense=='I':
            return 'AUX','Mood=Sub|Number=Sing|Person=3|Tense=Imp|VerbForm=Fin'
        elif postype=='A' and gen=='C' and num=='S' and person=='3' and mood=='I' and tense=='P':
            return 'AUX','Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin'
        elif postype=='A' and gen=='C' and num=='S' and person=='3' and mood=='I' and tense=='S':
            return 'AUX','Mood=Ind|Number=Sing|Person=3|Tense=Past|VerbForm=Fin'
        elif postype=='A' and gen=='C' and num=='S' and person=='3' and mood=='I' and tense=='I':
            return 'AUX','Mood=Ind|Number=Sing|Person=3|Tense=Imp|VerbForm=Fin'
        elif postype=='A' and gen=='C' and num=='S' and person=='3' and mood=='I' and tense=='F':
            return 'AUX','Mood=Ind|Number=Sing|Person=3|Tense=Fut|VerbForm=Fin'
        elif postype=='A' and gen=='C' and num=='S' and person=='3' and mood=='I' and tense=='C':
            return 'AUX','Mood=Cnd|Number=Sing|Person=3|VerbForm=Fin'
        elif postype=='A' and gen=='C' and num=='S' and person=='3' and mood=='M':
            return 'AUX','Mood=Imp|Number=Sing|Person=3|VerbForm=Fin'
        elif postype=='A' and gen=='C' and num=='S' and person=='2' and mood=='I' and tense=='P':
            return 'AUX','Mood=Ind|Number=Sing|Person=2|Tense=Pres|VerbForm=Fin'
        elif postype=='A' and gen=='C' and num=='S' and person=='1' and mood=='I' and tense=='P':
            return 'AUX','Mood=Ind|Number=Sing|Person=1|Tense=Pres|VerbForm=Fin'
        elif postype=='A' and gen=='C' and num=='S' and person=='1' and mood=='I' and tense=='I':
            return 'AUX','Mood=Ind|Number=Sing|Person=1|Tense=Imp|VerbForm=Fin'
        elif postype=='A' and gen=='C' and num=='S' and person=='1' and mood=='I' and tense=='F':
            return 'AUX','Mood=Ind|Number=Sing|Person=1|Tense=Fut|VerbForm=Fin'
        elif postype=='A' and gen=='C' and num=='P' and person=='3' and mood=='S' and tense=='P':
            return 'AUX','Mood=Sub|Number=Plur|Person=3|Tense=Pres|VerbForm=Fin'
        elif postype=='A' and gen=='C' and num=='P' and person=='3' and mood=='S' and tense=='I':
            return 'AUX','Mood=Sub|Number=Plur|Person=3|Tense=Imp|VerbForm=Fin'
        elif postype=='A' and gen=='C' and num=='P' and person=='3' and mood=='I' and tense=='P':
            return 'AUX','Mood=Ind|Number=Plur|Person=3|Tense=Pres|VerbForm=Fin'
        elif postype=='A' and gen=='C' and num=='P' and person=='3' and mood=='I' and tense=='S':
            return 'AUX','Mood=Ind|Number=Plur|Person=3|Tense=Past|VerbForm=Fin'
        elif postype=='A' and gen=='C' and num=='P' and person=='3' and mood=='I' and tense=='I':
            return 'AUX','Mood=Ind|Number=Plur|Person=3|Tense=Imp|VerbForm=Fin'
        elif postype=='A' and gen=='C' and num=='P' and person=='3' and mood=='I' and tense=='F':
            return 'AUX','Mood=Ind|Number=Plur|Person=3|Tense=Fut|VerbForm=Fin'
        elif postype=='A' and gen=='C' and num=='P' and person=='3' and mood=='I' and tense=='C':
            return 'AUX','Mood=Cnd|Number=Plur|Person=3|VerbForm=Fin'
        elif postype=='A' and gen=='C' and num=='P' and person=='3' and mood=='M':
            return 'AUX','Mood=Imp|Number=Plur|Person=3|VerbForm=Fin'
        elif postype=='A' and gen=='C' and num=='P' and person=='2' and mood=='I' and tense=='P':
            return 'AUX','Mood=Ind|Number=Plur|Person=2|Tense=Pres|VerbForm=Fin'
        elif postype=='A' and gen=='C' and num=='P' and person=='2' and mood=='I' and tense=='F':
            return 'AUX','Mood=Ind|Number=Plur|Person=2|Tense=Fut|VerbForm=Fin'
        elif postype=='A' and gen=='C' and num=='P' and person=='1' and mood=='S' and tense=='P':
            return 'AUX','Mood=Sub|Number=Plur|Person=1|Tense=Pres|VerbForm=Fin'
        elif postype=='A' and gen=='C' and num=='P' and person=='1' and mood=='S' and tense=='I':
            return 'AUX','Mood=Sub|Number=Plur|Person=1|Tense=Imp|VerbForm=Fin'
        elif postype=='A' and gen=='C' and num=='P' and person=='1' and mood=='I' and tense=='P':
            return 'AUX','Mood=Ind|Number=Plur|Person=1|Tense=Pres|VerbForm=Fin'
        elif postype=='A' and gen=='C' and num=='P' and person=='1' and mood=='I' and tense=='I':
            return 'AUX','Mood=Ind|Number=Plur|Person=1|Tense=Imp|VerbForm=Fin'
        elif postype=='A' and gen=='C' and num=='P' and person=='1' and mood=='I' and tense=='F':
            return 'AUX','Mood=Ind|Number=Plur|Person=1|Tense=Fut|VerbForm=Fin'
        elif postype=='A' and gen=='C' and num=='P' and person=='1' and mood=='I' and tense=='C':
            return 'AUX','Mood=Cnd|Number=Plur|Person=1|VerbForm=Fin'
        elif postype=='A' and gen=='C' and num=='C' and person=='1' and mood=='S' and tense=='I':
            return 'AUX','Mood=Sub|Person=1|Tense=Imp|VerbForm=Fin'
        elif postype=='A' and gen=='C' and num=='C' and mood=='N':
            return 'AUX','VerbForm=Inf'
        elif postype=='A' and gen=='C' and num=='C' and mood=='G':
            return 'AUX','VerbForm=Ger'
        # Traducimos linealmente los remanentes a un String
        else:
            return 'VERB', remaining_to_string(tags)

    elif tags[0] == 'Z':
	#2 number type/d:partitive;m:currency;p:percentage;u:unit
        if len(tags) > 1:
            postype = tags[1]
        else:
            postype = 'desconocido'
        if postype=='p':
            return 'NUM','NumForm=Digit|NumType=Frac'
        elif postype=='m':
            return 'NOUN','NumForm=Digit'
        else:
            return 'NUM','NumForm=Digit'

    elif tags[0] == 'W':
        return 'NOUN','AdvType=Tim'


    elif tags[0] == 'R':
	#R 2 adverb type/N:negative;G:general
        postype = tags[1]
        if postype=='N':
            return 'ADV','Negative=Neg'
        else:
            return 'ADV',''


    elif tags[0] == 'S':
	# 2 adposition type/P:preposition
            return 'ADP',''

    elif tags[0] == 'I':
	# 2 adposition type/P:preposition
            return 'INTJ',''

    elif tags[0] == 'F':
            return 'PUNCT',''
    print (tags)
    return 'OTRO'




			
