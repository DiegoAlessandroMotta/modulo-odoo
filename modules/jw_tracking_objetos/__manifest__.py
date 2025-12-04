{
    'name': 'JW Tracking de Objetos',
    'version': '17.0.1.0.0',
    'category': 'Tools',
    'summary': 'Módulo para el registro y tracking físico de objetos, materiales y pertenencias',
    'description': """
        Sistema completo para gestionar objetos perdidos, encontrados e institucionales
        dentro del colegio con las siguientes funcionalidades:
        
        - Registro de objetos con descripción y fotografías
        - Estados: perdido, encontrado, reclamado, entregado
        - Ubicación física de objetos
        - Asociación con documentos relacionados
        - Historial de cambios y auditoría
        - Búsqueda y filtrado avanzado
        - Reportes por estado y período
    """,
    'author': 'Colegio Jaime White',
    'license': 'LGPL-3',
    'depends': [
        'base',
        'jw_documents_extension',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/jw_tracking_objeto_views.xml',
        'views/jw_tracking_objeto_menus.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'jw_tracking_objetos/static/src/css/jw_tracking_objeto.css',
        ],
    },
    'installable': True,
    'auto_install': False,
    'application': True,
}
