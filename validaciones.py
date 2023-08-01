from flask import flash

def validar_clase(forma):
    es_valido = True
    if not forma['teacher']['id']:
        es_valido = False
        flash('La cédula del profesor es obligatoria')

    if not forma['teacher']['firstname']:
        es_valido = False
        flash('El nombre del profesor es obligatorio')

    if not forma['teacher']['lastname']:
        es_valido = False
        flash('El apellido del profesor es obligatorio')

    if not forma['name']:
        es_valido = False
        flash('El nombre de la materia es obligatorio')

    if not forma['objetive']: 
        es_valido = False
        flash('El obejtivo de la materia es obligatorio')

    if not forma['duration']:
        es_valido = False
        flash('La duración de la materia es obligatoria')

    if not forma['minimum_grades']:
        es_valido = False
        flash('Las notas mínimas aprobatorias de la materia son obligatorias')

    if forma['duration'] and forma['duration'].isdigit():
        forma['duration'] = int(forma['duration'])
    else: 
        es_valido = False
        flash('Duración inválida')

    if forma['minimum_grades'] and forma['minimum_grades'].replace('.', '', 1).isdigit():
        minimum_grades = float(forma['minimum_grades'])
        if minimum_grades > 100:
            flash('Nota mínima aprobatoria inválida')
            es_valido = False
        else: 
            forma['minimum_grades'] = float(forma['minimum_grades'])
    else: 
        es_valido = False
        flash('Nota mínima aprobatoria inválida')
    
    return es_valido