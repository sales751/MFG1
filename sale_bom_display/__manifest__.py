{
    'name': 'Sale BOM Display',
    'version': '1.0',
    'depends': ['sale_management', 'mrp'],
    'data': [
        'data/ec210_products.xml', 
        'views/sale_order_view.xml',
        'reports/sale_order_report.xml',
    ],
    'installable': True,
}