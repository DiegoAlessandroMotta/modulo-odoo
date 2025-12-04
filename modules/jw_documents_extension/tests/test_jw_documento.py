from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError
import base64


class JWDocumentoTestCase(TransactionCase):
    """Pruebas unitarias para el modelo jw.documento"""

    def setUp(self):
        super().setUp()
        self.partner_model = self.env['res.partner']
        self.documento_model = self.env['jw.documento']
        
        # Crear un partner para usar como responsable
        self.responsable = self.partner_model.create({
            'name': 'Juan Responsable',
            'is_company': False,
        })
        
        # Crear contenido de ejemplo en base64
        self.contenido_prueba = base64.b64encode(b'Contenido de prueba del documento')
    
    def test_create_documento_basico(self):
        """Verificar que se puede crear un documento básico"""
        documento = self.documento_model.create({
            'nombre': 'Documento de Prueba',
            'archivo': self.contenido_prueba,
            'nombre_archivo': 'prueba.txt',
        })
        
        self.assertEqual(documento.nombre, 'Documento de Prueba')
        self.assertEqual(documento.nombre_archivo, 'prueba.txt')
        self.assertEqual(documento.tipo_archivo, 'txt')
    
    def test_create_documento_completo(self):
        """Verificar que se puede crear un documento con todos los campos"""
        documento = self.documento_model.create({
            'nombre': 'Acta de Consejo Académico',
            'descripcion': 'Acta de reunión del consejo académico de diciembre 2024',
            'tipo_documento': 'administrativo',
            'archivo': self.contenido_prueba,
            'nombre_archivo': 'acta_consejo.pdf',
            'ubicacion_fisica': 'Archivo General - Estante A1',
            'responsable_custodia': self.responsable.id,
        })
        
        self.assertEqual(documento.nombre, 'Acta de Consejo Académico')
        self.assertEqual(documento.tipo_documento, 'administrativo')
        self.assertEqual(documento.ubicacion_fisica, 'Archivo General - Estante A1')
        self.assertEqual(documento.responsable_custodia.id, self.responsable.id)
        self.assertEqual(documento.tipo_archivo, 'pdf')
    
    def test_documento_sin_archivo_falla(self):
        """Verificar que no se puede crear un documento sin archivo"""
        with self.assertRaises(ValidationError):
            self.documento_model.create({
                'nombre': 'Documento sin archivo',
                'nombre_archivo': 'vacio.pdf',
            })
    
    def test_tipos_documento_validos(self):
        """Verificar que todos los tipos de documento son válidos"""
        tipos = ['administrativo', 'estudiantil', 'oficial', 'otro']
        
        for tipo in tipos:
            documento = self.documento_model.create({
                'nombre': f'Doc {tipo}',
                'tipo_documento': tipo,
                'archivo': self.contenido_prueba,
                'nombre_archivo': f'{tipo}.pdf',
            })
            self.assertEqual(documento.tipo_documento, tipo)
    
    def test_search_by_tipo_documento(self):
        """Verificar búsqueda por tipo de documento"""
        self.documento_model.create({
            'nombre': 'Admin Doc 1',
            'tipo_documento': 'administrativo',
            'archivo': self.contenido_prueba,
            'nombre_archivo': 'admin1.pdf',
        })
        self.documento_model.create({
            'nombre': 'Admin Doc 2',
            'tipo_documento': 'administrativo',
            'archivo': self.contenido_prueba,
            'nombre_archivo': 'admin2.pdf',
        })
        self.documento_model.create({
            'nombre': 'Student Doc 1',
            'tipo_documento': 'estudiantil',
            'archivo': self.contenido_prueba,
            'nombre_archivo': 'student.pdf',
        })
        
        admin_docs = self.documento_model.search([
            ('tipo_documento', '=', 'administrativo')
        ])
        
        self.assertEqual(len(admin_docs), 2)
    
    def test_search_by_responsable(self):
        """Verificar búsqueda por responsable"""
        self.documento_model.create({
            'nombre': 'Doc con responsable',
            'responsable_custodia': self.responsable.id,
            'archivo': self.contenido_prueba,
            'nombre_archivo': 'responsable.pdf',
        })
        self.documento_model.create({
            'nombre': 'Doc sin responsable',
            'archivo': self.contenido_prueba,
            'nombre_archivo': 'sin_resp.pdf',
        })
        
        docs_con_responsable = self.documento_model.search([
            ('responsable_custodia', '!=', False)
        ])
        
        self.assertEqual(len(docs_con_responsable), 1)
    
    def test_get_documentos_por_tipo(self):
        """Verificar método get_documentos_por_tipo"""
        self.documento_model.create({
            'nombre': 'Oficial 1',
            'tipo_documento': 'oficial',
            'archivo': self.contenido_prueba,
            'nombre_archivo': 'oficial1.pdf',
        })
        self.documento_model.create({
            'nombre': 'Oficial 2',
            'tipo_documento': 'oficial',
            'archivo': self.contenido_prueba,
            'nombre_archivo': 'oficial2.pdf',
        })
        
        oficiales = self.documento_model.get_documentos_por_tipo('oficial')
        self.assertEqual(len(oficiales), 2)
    
    def test_get_documentos_por_responsable(self):
        """Verificar método get_documentos_por_responsable"""
        doc1 = self.documento_model.create({
            'nombre': 'Doc resp 1',
            'responsable_custodia': self.responsable.id,
            'archivo': self.contenido_prueba,
            'nombre_archivo': 'resp1.pdf',
        })
        doc2 = self.documento_model.create({
            'nombre': 'Doc resp 2',
            'responsable_custodia': self.responsable.id,
            'archivo': self.contenido_prueba,
            'nombre_archivo': 'resp2.pdf',
        })
        
        documentos = self.documento_model.get_documentos_por_responsable(self.responsable.id)
        self.assertEqual(len(documentos), 2)
    
    def test_auditoria_documento(self):
        """Verificar que los datos de auditoría se registran"""
        documento = self.documento_model.create({
            'nombre': 'Doc auditoría',
            'archivo': self.contenido_prueba,
            'nombre_archivo': 'audit.pdf',
        })
        
        self.assertIsNotNone(documento.fecha_creacion)
        self.assertEqual(documento.usuario_creacion.id, self.env.user.id)
        self.assertIsNotNone(documento.fecha_modificacion)
    
    def test_tipo_archivo_computed(self):
        """Verificar que el tipo de archivo se calcula correctamente"""
        extensiones = [
            ('documento.pdf', 'pdf'),
            ('hoja.xlsx', 'xlsx'),
            ('imagen.jpg', 'jpg'),
            ('archivo.docx', 'docx'),
        ]
        
        for nombre, tipo_esperado in extensiones:
            documento = self.documento_model.create({
                'nombre': f'Doc {tipo_esperado}',
                'archivo': self.contenido_prueba,
                'nombre_archivo': nombre,
            })
            self.assertEqual(documento.tipo_archivo, tipo_esperado)
    
    def test_tamaño_archivo_computed(self):
        """Verificar que el tamaño del archivo se calcula correctamente"""
        documento = self.documento_model.create({
            'nombre': 'Doc tamaño',
            'archivo': self.contenido_prueba,
            'nombre_archivo': 'tamaño.pdf',
        })
        
        # El contenido original es "Contenido de prueba del documento"
        contenido_original = b'Contenido de prueba del documento'
        self.assertEqual(documento.tamaño_archivo, len(contenido_original))

