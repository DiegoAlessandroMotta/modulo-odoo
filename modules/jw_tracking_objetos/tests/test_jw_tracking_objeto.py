from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError
import base64


class JWTrackingObjetoTestCase(TransactionCase):
    """Pruebas unitarias para el módulo jw_tracking_objetos"""

    def setUp(self):
        super().setUp()
        self.partner_model = self.env['res.partner']
        self.objeto_model = self.env['jw.tracking.objeto']
        self.documento_model = self.env['jw.documento']
        
        # Crear partners para usar en los tests
        self.persona1 = self.partner_model.create({
            'name': 'Juan García',
            'is_company': False,
        })
        
        self.persona2 = self.partner_model.create({
            'name': 'María López',
            'is_company': False,
        })
        
        # Crear contenido para documentos en base64
        self.contenido_prueba = base64.b64encode(b'Contenido de prueba')
    
    def test_create_objeto_basico(self):
        """Verificar que se puede crear un objeto básico"""
        objeto = self.objeto_model.create({
            'nombre': 'Llave de salón',
            'estado': 'encontrado',
        })
        
        self.assertEqual(objeto.nombre, 'Llave de salón')
        self.assertEqual(objeto.estado, 'encontrado')
        self.assertFalse(objeto.documento_asociado)
    
    def test_create_objeto_completo(self):
        """Verificar que se puede crear un objeto con todos los campos"""
        objeto = self.objeto_model.create({
            'nombre': 'Mochila azul',
            'descripcion': 'Mochila azul con logo de marca X',
            'estado': 'perdido',
            'ubicacion_actual': 'Perdida en patio',
            'persona_registro': self.persona1.id,
        })
        
        self.assertEqual(objeto.nombre, 'Mochila azul')
        self.assertEqual(objeto.descripcion, 'Mochila azul con logo de marca X')
        self.assertEqual(objeto.estado, 'perdido')
        self.assertEqual(objeto.ubicacion_actual, 'Perdida en patio')
        self.assertEqual(objeto.persona_registro.id, self.persona1.id)
    
    def test_objeto_estado_default(self):
        """Verificar que el estado por defecto es 'encontrado'"""
        objeto = self.objeto_model.create({
            'nombre': 'Bolígrafo',
        })
        
        self.assertEqual(objeto.estado, 'encontrado')
    
    def test_objeto_cambio_estado(self):
        """Verificar que se puede cambiar el estado del objeto"""
        objeto = self.objeto_model.create({
            'nombre': 'Notebook',
            'estado': 'perdido',
        })
        
        self.assertEqual(objeto.estado, 'perdido')
        
        # Cambiar a encontrado
        objeto.action_marcar_encontrado()
        self.assertEqual(objeto.estado, 'encontrado')
        
        # Cambiar a reclamado
        objeto.action_marcar_reclamado()
        self.assertEqual(objeto.estado, 'reclamado')
        
        # Cambiar a entregado
        objeto.action_marcar_entregado()
        self.assertEqual(objeto.estado, 'entregado')
    
    def test_search_by_estado(self):
        """Verificar búsqueda por estado"""
        self.objeto_model.create({
            'nombre': 'Objeto 1',
            'estado': 'perdido',
        })
        self.objeto_model.create({
            'nombre': 'Objeto 2',
            'estado': 'perdido',
        })
        self.objeto_model.create({
            'nombre': 'Objeto 3',
            'estado': 'encontrado',
        })
        
        perdidos = self.objeto_model.search([('estado', '=', 'perdido')])
        self.assertEqual(len(perdidos), 2)
        
        encontrados = self.objeto_model.search([('estado', '=', 'encontrado')])
        self.assertEqual(len(encontrados), 1)
    
    def test_search_by_persona(self):
        """Verificar búsqueda por persona registradora"""
        self.objeto_model.create({
            'nombre': 'Obj persona 1',
            'persona_registro': self.persona1.id,
        })
        self.objeto_model.create({
            'nombre': 'Obj persona 2',
            'persona_registro': self.persona1.id,
        })
        self.objeto_model.create({
            'nombre': 'Obj persona 3',
            'persona_registro': self.persona2.id,
        })
        
        objetos_persona1 = self.objeto_model.search([
            ('persona_registro', '=', self.persona1.id)
        ])
        self.assertEqual(len(objetos_persona1), 2)
    
    def test_objeto_auditoria(self):
        """Verificar que los datos de auditoría se registran correctamente"""
        objeto = self.objeto_model.create({
            'nombre': 'Objeto auditoría',
        })
        
        self.assertIsNotNone(objeto.fecha_creacion)
        self.assertEqual(objeto.usuario_creacion.id, self.env.user.id)
        self.assertIsNotNone(objeto.fecha_registro)
    
    def test_objeto_con_documento(self):
        """Verificar que se puede asociar un documento jw.documento"""
        documento = self.documento_model.create({
            'nombre': 'Acta de entrega',
            'archivo': self.contenido_prueba,
            'nombre_archivo': 'acta.pdf',
        })
        
        objeto = self.objeto_model.create({
            'nombre': 'Objeto con documento',
            'documento_asociado': documento.id,
        })
        
        self.assertEqual(objeto.documento_asociado.id, documento.id)
    
    def test_get_objetos_por_estado(self):
        """Verificar método get_objetos_por_estado"""
        self.objeto_model.create({'nombre': 'Obj 1', 'estado': 'perdido'})
        self.objeto_model.create({'nombre': 'Obj 2', 'estado': 'perdido'})
        self.objeto_model.create({'nombre': 'Obj 3', 'estado': 'encontrado'})
        
        perdidos = self.objeto_model.get_objetos_por_estado('perdido')
        self.assertEqual(len(perdidos), 2)
    
    def test_objeto_con_imagen_principal(self):
        """Verificar que se puede agregar una imagen principal al objeto"""
        # Crear una imagen de prueba en base64 (1x1 pixel PNG)
        imagen_base64 = base64.b64encode(
            b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01'
            b'\x08\x02\x00\x00\x00\x90wS\xde\x00\x00\x00\x0cIDATx\x9cc\x00\x01'
            b'\x00\x00\x05\x00\x01\r\n-\xb4\x00\x00\x00\x00IEND\xaeB`\x82'
        )
        
        objeto = self.objeto_model.create({
            'nombre': 'Objeto con imagen',
            'imagen': imagen_base64,
        })
        
        self.assertIsNotNone(objeto.imagen)
        self.assertEqual(objeto.imagen, imagen_base64)
    
    def test_objeto_con_fotografias(self):
        """Verificar que se pueden agregar fotografías al objeto"""
        # Crear attachments primero
        attachment_model = self.env['ir.attachment']
        foto1 = attachment_model.create({
            'name': 'foto1.jpg',
            'datas': base64.b64encode(b'imagen1'),
            'mimetype': 'image/jpeg',
        })
        
        foto2 = attachment_model.create({
            'name': 'foto2.jpg',
            'datas': base64.b64encode(b'imagen2'),
            'mimetype': 'image/jpeg',
        })
        
        # Crear objeto con fotografías
        objeto = self.objeto_model.create({
            'nombre': 'Objeto con fotos',
            'fotografia_ids': [(6, 0, [foto1.id, foto2.id])],
        })
        
        # Verificar que el objeto tiene las fotografías
        self.assertEqual(len(objeto.fotografia_ids), 2)
        self.assertEqual(objeto.num_fotografias, 2)
        self.assertIn(foto1, objeto.fotografia_ids)
        self.assertIn(foto2, objeto.fotografia_ids)
    
    def test_contador_fotografias(self):
        """Verificar que el contador de fotografías se calcula correctamente"""
        objeto = self.objeto_model.create({
            'nombre': 'Objeto para contar fotos',
        })
        
        # Inicialmente sin fotos
        self.assertEqual(objeto.num_fotografias, 0)
        
        # Agregar una foto usando Many2many
        foto = self.env['ir.attachment'].create({
            'name': 'foto.jpg',
            'datas': base64.b64encode(b'imagen'),
            'mimetype': 'image/jpeg',
        })
        
        objeto.write({
            'fotografia_ids': [(4, foto.id)],
        })
        
        self.assertEqual(objeto.num_fotografias, 1)

