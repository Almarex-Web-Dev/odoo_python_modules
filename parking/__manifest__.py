# -*- coding: utf-8 -*-
{
    'name': "Gestion de Parking",
    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",
    'description': """
        Long description of module's purpose
    """,
    'author': "Parking Company",
    'website': "http://www.parkingcomapny.com",
    'category': 'parking Service',
    'version': '1.0',
    # any module necessary for this one to work correctly
    'depends': ['base'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/parking_terrain.xml',
        'views/parking_espace.xml',
        'views/parking_vehicule_propritaire.xml',
        'views/parking_vehicule.xml',
        'views/parking_vehicule_type.xml',
        'reports/parking_terrain_report.xml',
        'reports/reports.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': True
}
