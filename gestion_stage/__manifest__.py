# -*- coding: utf-8 -*-
{
    'name': "Gestion de Stage",
    'summary': "Gestion de Stage qui permettra a des eleve de fait leur stage dans une entreprise",
    'description': """
        Long description of module's purpose
    """,
    'author': "Lasisi Abdullahi M.",
    'website': "http://www.yourcompany.com",
    'category': 'Entreprise',
    'version': '0.1',
    'depends': ['base'],
    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/etablissment.xml',
        'views/encadreur.xml',
        'views/filiere.xml',
        'views/etudiant.xml',
        'views/stage.xml',
        'views/entreprise.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
