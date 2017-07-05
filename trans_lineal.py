def remaining_to_string(tags):
# Hacemos una traduccion lineal de los parametros de entrada en salida
    retorno = []
    if tags[0] == 'A':
        #(A,type,degree,gender,num,possessorpers,possessornum)
        postype = tags[1]
        gen = tags[3] #
        num = tags[4] #
        posfunction = tags[5]
        if gen == 'M':
            retorno.append('Gender=Masc')
        if gen == 'F':
            retorno.append('Gender=Fem')
        if num == 'P':
            retorno.append('Number=Plur')
        if num == 'S':
            retorno.append('Number=Sing')
        if posfunction == 'participle':
            retorno.append('VerbForm=Part')
        return "|".join(retorno)
#--------------------------------------------------
    if tags[0] == 'D':
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

        if gen == 'M':
            retorno.append('Gender=Masc')
        if gen == 'F':
            retorno.append('Gender=Fem')
        if num == 'P':
            retorno.append('Number=Plur')
        if num == 'S':
            retorno.append('Number=Sing')
        if person == '3':
            retorno.append('Person=3')
        if person == '2':
            retorno.append('Person=2')
        if person == '1':
            retorno.append('Person=1')
        return "|".join(retorno)
#--------------------------------------------------
    if tags[0] == 'N':	
        postype = tags[1]
        gen = tags[2]
        num = tags[3]
	#N 2 noun type/C:common;P:proper 
	#Gender/F:feminine;M:masculine;C:common 
	#num/S:singular;P:plural;N:invariable 
	#neclass/S:person;G:location;O:organization;V:other 
	#nesubclass/0:0;P:0 
	#degree/V:evaluative	
        if gen == 'M':
            retorno.append('Gender=Masc')
        if gen == 'F':
            retorno.append('Gender=Fem')
        if num == 'P':
            retorno.append('Number=Plur')
        if num == 'S':
            retorno.append('Number=Sing')
        return "|".join(retorno)
#--------------------------------------------------
    if tags[0] == 'P':
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
        if gen == 'M':
            retorno.append('Gender=Masc')
        if gen == 'F':
            retorno.append('Gender=Fem')
        if num == 'P':
            retorno.append('Number=Plur')
        if num == 'S':
            retorno.append('Number=Sing')
        if person == '3':
            retorno.append('Person=3')
        if person == '2':
            retorno.append('Person=2')
        if person == '1':
            retorno.append('Person=1')
        return "|".join(retorno)
#--------------------------------------------------
    if tags[0] == 'V':
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
        if mood == 'I':
            retorno.append('Mood=Ind')
        if mood == 'S':
            retorno.append('Mood=Sub')
        if mood == 'M':
            retorno.append('Mood=Imp')

        if gen == 'M':
            retorno.append('Gender=Masc')
        if gen == 'F':
            retorno.append('Gender=Fem')
        if num == 'P':
            retorno.append('Number=Plur')
        if num == 'S':
            retorno.append('Number=Sing')
        if person == '3':
            retorno.append('Person=3')
        if person == '2':
            retorno.append('Person=2')
        if person == '1':
            retorno.append('Person=1')
        if tense == 'S':
            retorno.append('Tense=Past')
        if tense == 'P':
            retorno.append('Tense=Pres')
        if tense == 'I':
            retorno.append('Tense=Imp')
        if tense == 'F':
            retorno.append('Tense=Fut')
        return "|".join(retorno)
#--------------------------------------------------
        














