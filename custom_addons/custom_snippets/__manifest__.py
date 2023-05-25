{
    'name': 'Custom Snippets',
    'version': '1.0.0',
    'category': 'Website/Snippet',
    'summary': 'Custom Snippet',
    'author': 'Lim Tangmeng',
    'sequence': 0,
    'description': """Custom Snippet Description""",
    'depends': ["website", "website_sale", "sale"],
    'data': [
        # Security

        # Wizard

        # Views
        'views/snippets/s_dynamic_category.xml',
        'views/snippets/snippets.xml',
    ],
    'demo': [],
    'installable': True,
    'assets': {
        'web.assets_frontend': [
            'custom_snippets/static/src/snippets/s_dynamic_category/000.js'
        ]
    },
    'application': True,
    'license': 'LGPL-3',
}
