# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': "Inherits Concept",
    'version': '16.0.1.0.0',
    'summary': 'AryanSir Task',
    'author': 'Ramiz Belim',
    'sequence': 10,
    'website': 'https://www.odoo.com/app/invoicing',
    'depends': ['sale_management'],
    'description': """ Understand concept of Inherits and Inherit """,
    'data': [
        'security/ir.model.access.csv',
        'views/car_views.xml'
    ],

    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
