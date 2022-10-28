# -*- coding: utf-8 -*-
{
    'name': "hr_hospital",

    'summary': """
        test 2.1 module""",

    'description': """
    """,

    'author': "George N",
    'website': "https://github.com/jiga23/odoo-school_2",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Castomization',
    'version': '15.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    'external_dependencies': {'python': [], },

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/hr_hospital_menu.xml',
        'views/hr_hospital_patient_views.xml',
        'views/hr_hospital_patient_profile_views.xml',
        'views/hr_hospital_diagnose_views.xml',
        'views/hr_hospital_doctor_views.xml',
    ],

    'installable': True,
    'auto_install': False,

    'images': [
        'static/description/icon.png',
    ],

    'price': 0,
    'currency': 'EUR',
}
