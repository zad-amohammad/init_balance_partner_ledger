# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Init Balance Partner Ledger',
    'version' : '1.0',
    'depends' : ['account_reports'],
    'data': [
        'views/template.xml',
    ],
    'assets':{
        'web.assets_backend': [
            'init_balance_partner_ledger/static/src/js/initial_balance.js',
        ],
    }
}
