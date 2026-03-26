{
    'name': 'Sale BOM Display',
    'version': '1.0',
    'depends': ['sale', 'mrp'],
    'data': [
        'views/sale_order_view.xml',
        'reports/sale_order_report.xml',
    ],
    'installable': True,
}