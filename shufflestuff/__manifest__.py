# -- coding: utf-8 -
{
    'name': "ShuffleStuff",
    'depends': ['base','sale_management'],
    'application': True,
    'license' : 'LGPL-3',
    'data' : [
        'security/ir.model.access.csv',
        'views/shufflestuff_customer_views.xml',
        'views/shufflestuff_tags_views.xml',
        'views/shufflestuff_categories_views.xml',
        'views/shufflestuff_pricelists_views.xml',
        'views/shufflestuff_products_views.xml',
        #'views/shufflestuff_orders_views.xml',
        'views/res_partner_views.xml',
        'views/shufflestuff_menus.xml'
        ]
    
}   