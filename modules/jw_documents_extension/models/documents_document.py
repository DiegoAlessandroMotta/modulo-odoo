from odoo import fields, models


class DocumentsDocument(models.Model):
    """Extensión del modelo documents.document con campos adicionales"""
    
    _inherit = 'documents.document'
    
    # Tipos de documento
    DOCUMENT_TYPE = [
        ('administrativo', 'Administrativo'),
        ('estudiantil', 'Estudiantil'),
        ('oficial', 'Oficial'),
        ('otro', 'Otro'),
    ]
    
    tipo_documento = fields.Selection(
        selection=DOCUMENT_TYPE,
        string='Tipo de Documento',
        help='Clasificación del documento',
        track_visibility='onchange'
    )
    
    ubicacion_fisica = fields.Char(
        string='Ubicación Física',
        help='Ubicación del archivo o copia original del documento',
        track_visibility='onchange'
    )
    
    responsable_custodia = fields.Many2one(
        comodel_name='res.partner',
        string='Responsable de Custodia',
        help='Persona responsable del resguardo del documento original',
        track_visibility='onchange',
        domain=[('is_company', '=', False)]
    )
