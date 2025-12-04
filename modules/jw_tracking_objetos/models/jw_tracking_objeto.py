from odoo import fields, models, api
from odoo.exceptions import ValidationError


class JWTrackingObjeto(models.Model):
    """Modelo para el registro y tracking de objetos, materiales y pertenencias"""
    
    _name = 'jw.tracking.objeto'
    _description = 'Tracking de Objetos'
    _order = 'fecha_registro desc'
    
    # Estados
    ESTADO_SELECTION = [
        ('perdido', 'Perdido'),
        ('encontrado', 'Encontrado'),
        ('reclamado', 'Reclamado'),
        ('entregado', 'Entregado'),
    ]
    
    # Campos básicos
    nombre = fields.Char(
        string='Nombre del Objeto',
        required=True,
        help='Descripción breve del objeto'
    )
    
    descripcion = fields.Text(
        string='Descripción Detallada',
        help='Descripción completa del objeto, características distintivas, etc.'
    )
    
    estado = fields.Selection(
        selection=ESTADO_SELECTION,
        string='Estado',
        default='encontrado',
        required=True
    )
    
    # Ubicación y contacto
    ubicacion_actual = fields.Char(
        string='Ubicación Actual',
        help='Donde se encuentra actualmente el objeto'
    )
    
    persona_registro = fields.Many2one(
        comodel_name='res.partner',
        string='Persona que Registra',
        default=lambda self: self.env.user.partner_id,
        help='Persona que registró el objeto',
        domain=[('is_company', '=', False)]
    )
    
    fecha_registro = fields.Datetime(
        string='Fecha de Registro',
        default=fields.Datetime.now,
        readonly=True
    )
    
    # Documento asociado
    documento_asociado = fields.Many2one(
        comodel_name='jw.documento',
        string='Documento Asociado',
        help='Documento relacionado (acta, comprobante de entrega, etc.)'
    )
    
    # Imagen principal
    imagen = fields.Binary(
        string='Imagen Principal',
        help='Imagen principal del objeto',
        attachment=True
    )
    
    # Fotografías adicionales
    fotografia_ids = fields.Many2many(
        comodel_name='ir.attachment',
        relation='jw_tracking_objeto_attachment_rel',
        column1='objeto_id',
        column2='attachment_id',
        string='Fotografías',
        help='Fotografías del objeto'
    )
    
    # Contador de fotos
    num_fotografias = fields.Integer(
        string='Número de Fotografías',
        compute='_compute_num_fotografias',
        store=True
    )
    
    # Campos de auditoría
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
    
    # Métodos computados
    @api.depends('fotografia_ids')
    def _compute_num_fotografias(self):
        """Calcular el número de fotografías"""
        for record in self:
            record.num_fotografias = len(record.fotografia_ids)
    
    # Métodos
    @api.model
    def create(self, vals):
        """Sobrescribir create para auditoría"""
        record = super().create(vals)
        record.usuario_creacion = self.env.user.id
        record.fecha_creacion = fields.Datetime.now()
        return record
    
    def write(self, vals):
        """Sobrescribir write para auditoría"""
        # Actualizar auditoría
        vals['fecha_modificacion'] = fields.Datetime.now()
        vals['usuario_modificacion'] = self.env.user.id
        
        return super().write(vals)
    
    @api.constrains('estado')
    def _check_valid_state_transition(self):
        """Validar transiciones de estado válidas"""
        valid_transitions = {
            'perdido': ['encontrado', 'entregado'],
            'encontrado': ['reclamado', 'entregado'],
            'reclamado': ['entregado'],
            'entregado': [],
        }
        
        for record in self:
            if record.estado == 'entregado':
                # Verificar que no se puede cambiar de entregado
                pass  # Se valida solo al hacer transiciones desde otros estados
    
    @api.model
    def get_objetos_por_estado(self, estado):
        """Obtener objetos filtrados por estado"""
        return self.search([('estado', '=', estado)])
    
    def action_marcar_encontrado(self):
        """Acción para marcar objeto como encontrado"""
        if self.estado == 'perdido':
            self.estado = 'encontrado'
    
    def action_marcar_reclamado(self):
        """Acción para marcar objeto como reclamado"""
        if self.estado == 'encontrado':
            self.estado = 'reclamado'
    
    def action_marcar_entregado(self):
        """Acción para marcar objeto como entregado"""
        if self.estado in ['encontrado', 'reclamado']:
            self.estado = 'entregado'
