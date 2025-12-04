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
        'documents',
        'mail',
    ],
    'data': [
        'security/ir.model.access.csv',
        'security/jw_tracking_objetos_groups.xml',
        'views/jw_tracking_objeto_views.xml',
        'views/jw_tracking_objeto_menus.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
