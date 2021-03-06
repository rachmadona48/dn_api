# -*- coding: utf-8 -*-
{
    'name': "Odoo 12 Rest Api",

    'summary': """
        This module to akses odoo via rest api""",

    'description': """
        1) Open odoo.conf
        2) Add 'dbfilter = dbname'.
        3) Restart odoo service.
    """,

    'author': "R4Y Jr",
    'website': "-",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Extra Tools',
    'price': 100,
    'currency': 'EUR',
    'version': '12.0.0.1',
    'support': 'rayci232@gmail.com',
    'images': ['images/login1.PNG'],

    # any module necessary for this one to work correctly
    'depends': ['base'],
    "data": [
            "data/ir_config_param.xml", 
            # "views/ir_model.xml", 
            # "views/res_users.xml", 
            # "security/ir.model.access.csv",
            ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
}