def relation_to_luke(person: str) -> str:
    relation = ''
    if person == 'Darth Vader':
        relation = "Luke, I am your father."
    elif person == 'Leia':
        relation = "Luke, I am your sister."
    elif person == 'Han':
        relation = "Luke, I am your brother in law."
    elif person == 'R2D2':
        relation = "Luke, I am your droid."
    return relation

name = input()
print(relation_to_luke(name))