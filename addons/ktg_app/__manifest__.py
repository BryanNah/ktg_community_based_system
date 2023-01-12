# -*- coding: utf-8 -*-
{
    'name': "KTG Management Application",
    'summary': "KTG Management Application",
    'description': "KTG Management Application",
    'author': "KTG",
    'sequence': 1,
    'website': "",
    'category': 'Other',
    'version': '14.0.0.2',
    'depends': ['base'],
    'license': "LGPL-3",
    # always loaded
    'data': [
        'security/ktg_security.xml',
        'security/ir.model.access.csv',
        'data/generating_ktg_member_number.xml',
        'views/member_view.xml',
        'views/financial_year_view.xml',
        'views/drive_setup_view.xml',
        'views/drive_participation_view.xml',
        'views/annual_subscription.xml',
        'menu/ktg_menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
}
