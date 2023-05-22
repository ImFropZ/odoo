{
    'name': 'Time Off',
    'version': '1.0.0',
    'category': 'Services/Time Off',
    'summary': 'Time Off',
    'author': 'Lim Tangmeng',
    'sequence': 0,
    'description': """Time Off Description""",
    'depends': ["mail"],
    'data': [
        # Security
        'security/ir.model.access.csv',

        # Wizard


        # Views
        # 'views/dashboard_view.xml',
        'views/request_view.xml',
        'views/menu.xml'
    ],
    'demo': [],
    'installable': True,
    'assets': {},
    'application': True,
    'license': 'LGPL-3',
}
