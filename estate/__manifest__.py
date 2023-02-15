# -*- coding: utf-8 -*-
{
    'name': "Estate Module",
    'summary': "New Estate module to keep track of all the records of Real Estates",
    'description': "This module was created by Abdullahi",
    'author': "Lasisi Abdullahi",
    'website': "http://www.yourcompany.com",
    'category': 'Real Estate/Brokerage',
    'sequence': -100,
    'version': '0.1',
    'depends': ['base', 'website', 'mail'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/estate_model.xml',
        'views/estate_property_type.xml',
        'views/estate_property_tags.xml',
        'views/estate_property_offer.xml',
        'views/res_user.xml',
        'views/assets.xml',
        'pages/service_page.xml',
        'pages/about.xml',
        'pages/contact.xml',
        'pages/available_properties.xml',
        'estates_templates/templates.xml',
        'estate_report/estate_property_reports.xml',
        'estate_report/offers_table_reports.xml',

    ],
    'demo': [
        # 'demo/demo_data.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': True
}
