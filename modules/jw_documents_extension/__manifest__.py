{
    'name': 'JW Documents Extension',
    'version': '17.0.1.0.0',
    'category': 'Tools',
    'summary': 'Módulo para la gestión de documentos y tracking físico',
    'description': """
        Módulo de gestión documentaria institucional con funcionalidades:

        - Gestión de archivos digitales con metadatos
        - Tipo de documento (administrativo, estudiantil, oficial, etc.)
        - Ubicación física del archivo original
        - Responsable de custodia
        - Control de acceso y auditoría
        - Búsqueda y filtrado
    """,
    'author': 'Colegio Jaime White',
    'license': 'LGPL-3',
    'depends': [
        'base',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/jw_documento_views.xml',
        'views/jw_documento_menus.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
