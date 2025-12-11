from odoo import fields, models, api
from odoo.exceptions import ValidationError


class JWTrackingObjeto(models.Model):
    _name = 'jw.tracking.objeto'
    _description = 'Tracking de Objetos'
    _order = 'fecha_registro desc'
    
    ESTADO_SELECTION = [
        ('perdido', 'Perdido'),
        ('encontrado', 'Encontrado'),
        ('reclamado', 'Reclamado'),
        ('entregado', 'Entregado'),
    ]
    
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
    
    documento_asociado = fields.Many2one(
        comodel_name='jw.documento',
        string='Documento Asociado',
        help='Documento relacionado (acta, comprobante de entrega, etc.)'
    )
    
    imagen = fields.Binary(
        string='Imagen Principal',
        help='Imagen principal del objeto',
        attachment=True
    )
    
    fotografia_ids = fields.Many2many(
        comodel_name='ir.attachment',
        relation='jw_tracking_objeto_attachment_rel',
        column1='objeto_id',
        column2='attachment_id',
        string='Fotografías',
        help='Fotografías del objeto'
    )
    
    num_fotografias = fields.Integer(
        string='Número de Fotografías',
        compute='_compute_num_fotografias',
        store=True
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
    
    @api.depends('fotografia_ids')
    def _compute_num_fotografias(self):
        for record in self:
            record.num_fotografias = len(record.fotografia_ids)
    
    @api.model
    def create(self, vals):
        record = super().create(vals)
        record.usuario_creacion = self.env.user.id
        record.fecha_creacion = fields.Datetime.now()
        return record
    
    def write(self, vals):
        vals['fecha_modificacion'] = fields.Datetime.now()
        vals['usuario_modificacion'] = self.env.user.id
        
        return super().write(vals)
    
    @api.constrains('estado')
    def _check_valid_state_transition(self):
        valid_transitions = {
            'perdido': ['encontrado', 'entregado'],
            'encontrado': ['reclamado', 'entregado'],
            'reclamado': ['entregado'],
            'entregado': [],
        }
        
        for record in self:
            if record.estado == 'entregado':
                pass
    
    @api.model
    def get_objetos_por_estado(self, estado):
        return self.search([('estado', '=', estado)])
    
    def action_marcar_encontrado(self):
        if self.estado == 'perdido':
            self.estado = 'encontrado'
    
    def action_marcar_reclamado(self):
        if self.estado == 'encontrado':
            self.estado = 'reclamado'
    
    def action_marcar_entregado(self):
        if self.estado in ['encontrado', 'reclamado']:
            self.estado = 'entregado'
