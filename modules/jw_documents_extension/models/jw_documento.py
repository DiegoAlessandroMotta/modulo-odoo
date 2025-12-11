import base64
from odoo import fields, models, api
from odoo.exceptions import ValidationError


class JWDocumento(models.Model):
    _name = 'jw.documento'
    _description = 'Documento Digital'
    _order = 'fecha_creacion desc'
    
    DOCUMENTO_TYPE = [
        ('administrativo', 'Administrativo'),
        ('estudiantil', 'Estudiantil'),
        ('oficial', 'Oficial'),
        ('otro', 'Otro'),
    ]
    
    nombre = fields.Char(
        string='Nombre del Documento',
        required=True,
        help='Nombre o descripción breve del documento'
    )
    
    descripcion = fields.Text(
        string='Descripción',
        help='Descripción detallada del contenido del documento'
    )
    
    tipo_documento = fields.Selection(
        selection=DOCUMENTO_TYPE,
        string='Tipo de Documento',
        help='Clasificación del documento'
    )
    
    archivo = fields.Binary(
        string='Archivo',
        required=True,
        help='Archivo digital del documento'
    )
    
    nombre_archivo = fields.Char(
        string='Nombre del Archivo',
        help='Nombre original del archivo'
    )
    
    tipo_archivo = fields.Char(
        string='Tipo de Archivo',
        compute='_compute_tipo_archivo',
        store=True,
        help='Extensión del archivo (pdf, docx, jpg, etc.)'
    )
    
    tamano_archivo = fields.Integer(
        string='Tamaño (bytes)',
        compute='_compute_tamano_archivo',
        store=True
    )
    
    ubicacion_fisica = fields.Char(
        string='Ubicación Física',
        help='Ubicación del archivo o copia original del documento'
    )
    
    responsable_custodia = fields.Many2one(
        comodel_name='res.partner',
        string='Responsable de Custodia',
        help='Persona responsable del resguardo del documento original',
        domain=[('is_company', '=', False)]
    )
    
    fecha_creacion = fields.Datetime(
        string='Fecha de Creación',
        default=fields.Datetime.now,
        readonly=True
    )
    
    usuario_creacion = fields.Many2one(
        comodel_name='res.users',
        string='Usuario que Creó',
        default=lambda self: self.env.user,
        readonly=True
    )
    
    fecha_modificacion = fields.Datetime(
        string='Última Modificación',
        readonly=True
    )
    
    usuario_modificacion = fields.Many2one(
        comodel_name='res.users',
        string='Último Usuario que Modificó',
        readonly=True
    )
    
    @api.depends('nombre_archivo')
    def _compute_tipo_archivo(self):
        for record in self:
            if record.nombre_archivo:
                extensión = record.nombre_archivo.split('.')[-1] if '.' in record.nombre_archivo else 'desconocido'
                record.tipo_archivo = extensión.lower()
            else:
                record.tipo_archivo = ''
    
    @api.depends('archivo')
    def _compute_tamano_archivo(self):
        for record in self:
            if record.archivo:
                try:
                    record.tamano_archivo = len(base64.b64decode(record.archivo))
                except:
                    record.tamano_archivo = 0
            else:
                record.tamano_archivo = 0
    
    def create(self, vals):
        record = super().create(vals)
        record.usuario_creacion = self.env.user.id
        record.fecha_creacion = fields.Datetime.now()
        if 'archivo' in vals:
            record._compute_tamano_archivo()
        if 'nombre_archivo' in vals:
            record._compute_tipo_archivo()
        return record
    
    def write(self, vals):
        vals['fecha_modificacion'] = fields.Datetime.now()
        vals['usuario_modificacion'] = self.env.user.id
        result = super().write(vals)
        if 'archivo' in vals:
            self._compute_tamano_archivo()
        if 'nombre_archivo' in vals:
            self._compute_tipo_archivo()
        return result
    
    @api.constrains('archivo', 'nombre_archivo')
    def _check_archivo_valido(self):
        for record in self:
            if not record.archivo:
                raise ValidationError('El documento debe incluir un archivo.')
    
    def get_documento_tamano_legible(self):
        for record in self:
            tamano = record.tamano_archivo
            if tamano < 1024:
                record.tamano_legible = f'{tamano} B'
            elif tamano < 1024 * 1024:
                record.tamano_legible = f'{tamano / 1024:.2f} KB'
            elif tamano < 1024 * 1024 * 1024:
                record.tamano_legible = f'{tamano / (1024 * 1024):.2f} MB'
            else:
                record.tamano_legible = f'{tamano / (1024 * 1024 * 1024):.2f} GB'
    
    @api.model
    def get_documentos_por_tipo(self, tipo):
        return self.search([('tipo_documento', '=', tipo)])
    
    @api.model
    def get_documentos_por_responsable(self, responsable_id):
        return self.search([('responsable_custodia', '=', responsable_id)])
