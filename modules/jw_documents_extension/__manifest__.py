{
    'name': 'JW Documents Extension',
    'version': '17.0.1.0.0',
    'category': 'Tools',
    'summary': 'Extensión del módulo de documentos con campos adicionales y tracking físico',
    'description': """
        Módulo que extiende la funcionalidad nativa de Odoo Documents
        con campos adicionales para gestión documentaria institucional:
        
        - Tipo de documento (administrativo, estudiantil, oficial, etc.)
        - Ubicación física del archivo original
        - Responsable de custodia
        - Búsqueda y filtrado avanzado
    """,
    'author': 'Colegio Jaime White',
    'license': 'LGPL-3',
    'depends': [
        'base',
        'documents',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/documents_document_views.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
