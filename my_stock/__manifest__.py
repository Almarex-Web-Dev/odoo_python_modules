# -*- coding: utf-8 -*-
{
    'name': "Gestion de Stock",
    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",
    'description': """
        Long description of module's purpose
    """,

    'author': "Lasisi Abdullahi",
    'website': "http://www.mystockcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sales/stock service',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/produit_categorie.xml',
        'views/produit_template.xml',
        'views/produit_fournisseur.xml',
        'views/stock_models.xml',
        'views/produit_vente.xml',
        'views/produit_client.xml',
        'reports/sales_report.xml',
        'reports/sales_report_template.xml',
        # 'views/views.xml',
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': True,
}
