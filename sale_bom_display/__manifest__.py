{
    'name': 'Sale BOM Display',
    'version': '1.1',
    'depends': ['sale_management', 'mrp'],
    'data': [
        'data/ec210_products.xml', 
        'data/ec210_boms.xml',
        'data/ec210_routes.xml',
        'views/sale_order_view.xml',
        'reports/sale_order_report.xml',
    ],
    'installable': True,
}
