{
    'name': 'School Management',
    'version': '1.0.0',
    'category': 'Services/School',
    'summary': 'School Management',
    'author': 'Lim Tangmeng',
    'sequence': 0,
    'description': """School Management Description""",
    'depends': ["mail"],
    'data': [
        # Security
        'security/school_security.xml',
        'security/ir.model.access.csv',

        # Wizard
        'wizard/remove_classroom_view.xml',

        # Views
        'views/student_view.xml',
        'views/teacher_view.xml',
        'views/classroom_view.xml',
        'views/appointment_view.xml',
        'views/menu.xml',
        'views/template.xml'
    ],
    'demo': [],
    'installable': True,
    'assets': {},
    'application': True,
    'license': 'LGPL-3',
}
