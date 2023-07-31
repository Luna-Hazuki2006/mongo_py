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
        flash('Las notas mínimas de la materia son obligatorias')