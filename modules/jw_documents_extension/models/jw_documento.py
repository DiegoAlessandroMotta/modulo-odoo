import base64
from odoo import fields, models, api
from odoo.exceptions import ValidationError


class JWDocumento(models.Model):
    """Modelo para gestión de documentos digitales institucionales"""
    
    _name = 'jw.documento'
    _description = 'Documento Digital'
    _order = 'fecha_creacion desc'
    
    # Tipos de documento
    DOCUMENTO_TYPE = [
        ('administrativo', 'Administrativo'),
        ('estudiantil', 'Estudiantil'),
        ('oficial', 'Oficial'),
        ('otro', 'Otro'),
    ]
    
    # Campos básicos
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
    
    # Archivo binario
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
    
    tamaño_archivo = fields.Integer(
        string='Tamaño (bytes)',
        compute='_compute_tamaño_archivo',
        store=True
    )
    
    # Ubicación y responsable
    ubicacion_fisica = fields.Char(
        string='Ubicación Física',
        help='Ubicación del archivo o copia original del documento'
    )
    
    responsable_custodia = fields.Many2one(
        comodel_name='res.partner',
        string='Responsable de Custodia',
        help='Persona responsable del resguardo del documento original',
        track_visibility='onchange',
        domain=[('is_company', '=', False)]
    )
    
    # Auditoría
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
    
    # Métodos computed
    @api.depends('nombre_archivo')
    def _compute_tipo_archivo(self):
        """Calcular tipo de archivo desde la extensión"""
        for record in self:
            if record.nombre_archivo:
                extensión = record.nombre_archivo.split('.')[-1] if '.' in record.nombre_archivo else 'desconocido'
                record.tipo_archivo = extensión.lower()
            else:
                record.tipo_archivo = ''
    
    @api.depends('archivo')
    def _compute_tamaño_archivo(self):
        """Calcular tamaño del archivo"""
        for record in self:
            if record.archivo:
                # El tamaño en bytes es la longitud del archivo en base64 decodificado
                try:
                    record.tamaño_archivo = len(base64.b64decode(record.archivo))
                except:
                    record.tamaño_archivo = 0
            else:
                record.tamaño_archivo = 0
    
    # Métodos de ciclo de vida
    def create(self, vals):
        """Sobrescribir create para auditoría"""
        record = super().create(vals)
        record.usuario_creacion = self.env.user.id
        record.fecha_creacion = fields.Datetime.now()
        return record
    
    def write(self, vals):
        """Sobrescribir write para auditoría"""
        vals['fecha_modificacion'] = fields.Datetime.now()
        vals['usuario_modificacion'] = self.env.user.id
        return super().write(vals)
    
    # Validaciones
    @api.constrains('archivo', 'nombre_archivo')
    def _check_archivo_valido(self):
        """Validar que el archivo no esté vacío"""
        for record in self:
            if not record.archivo:
                raise ValidationError('El documento debe incluir un archivo.')
    
    # Métodos de negocio
    def get_documento_tamaño_legible(self):
        """Obtener tamaño del archivo en formato legible (KB, MB, etc.)"""
        for record in self:
            tamaño = record.tamaño_archivo
            if tamaño < 1024:
                record.tamaño_legible = f'{tamaño} B'
            elif tamaño < 1024 * 1024:
                record.tamaño_legible = f'{tamaño / 1024:.2f} KB'
            elif tamaño < 1024 * 1024 * 1024:
                record.tamaño_legible = f'{tamaño / (1024 * 1024):.2f} MB'
            else:
                record.tamaño_legible = f'{tamaño / (1024 * 1024 * 1024):.2f} GB'
    
    @api.model
    def get_documentos_por_tipo(self, tipo):
        """Obtener documentos filtrados por tipo"""
        return self.search([('tipo_documento', '=', tipo)])
    
    @api.model
    def get_documentos_por_responsable(self, responsable_id):
        """Obtener documentos filtrados por responsable"""
        return self.search([('responsable_custodia', '=', responsable_id)])

