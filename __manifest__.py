# -*- coding: utf-8 -*-
{
    'name': "Journal Partner",

    'summary': """
        Agregar campos al clientes
        """,

    'description': """
        Nuevo campos de Diarios a clientes y sea heredados en la factura
    """,

    'author': "Merlin Alvarez Amador",
    'website': "http://www.mer.plus",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Accounting',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','account'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'views/openacademy.xml',
        # 'views/templates.xml',
        'views/partner.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        #'demo/demo.xml',
    ],
}