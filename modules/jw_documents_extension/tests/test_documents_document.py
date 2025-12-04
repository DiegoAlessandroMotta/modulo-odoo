from odoo.tests.common import TransactionCase


class DocumentsDocumentTestCase(TransactionCase):
    """Pruebas unitarias para la extensión de documents.document"""

    def setUp(self):
        super().setUp()
        self.partner_model = self.env['res.partner']
        self.document_model = self.env['documents.document']
        
        # Crear un partner para usar como responsable
        self.responsable = self.partner_model.create({
            'name': 'Juan Responsable',
            'is_company': False,
        })
    
    def test_create_document_with_extension_fields(self):
        """Verificar que se pueden crear documentos con los campos extendidos"""
        document = self.document_model.create({
            'name': 'Documento de Prueba',
            'tipo_documento': 'administrativo',
            'ubicacion_fisica': 'Archivo General - Estante A1',
            'responsable_custodia': self.responsable.id,
        })
        
        self.assertEqual(document.tipo_documento, 'administrativo')
        self.assertEqual(document.ubicacion_fisica, 'Archivo General - Estante A1')
        self.assertEqual(document.responsable_custodia.id, self.responsable.id)
    
    def test_document_type_selection(self):
        """Verificar que los tipos de documento son válidos"""
        valid_types = ['administrativo', 'estudiantil', 'oficial', 'otro']
        
        for doc_type in valid_types:
            document = self.document_model.create({
                'name': f'Documento {doc_type}',
                'tipo_documento': doc_type,
            })
            self.assertEqual(document.tipo_documento, doc_type)
    
    def test_document_search_by_type(self):
        """Verificar que se pueden buscar documentos por tipo"""
        self.document_model.create({
            'name': 'Admin Doc 1',
            'tipo_documento': 'administrativo',
        })
        self.document_model.create({
            'name': 'Admin Doc 2',
            'tipo_documento': 'administrativo',
        })
        self.document_model.create({
            'name': 'Student Doc 1',
            'tipo_documento': 'estudiantil',
        })
        
        admin_docs = self.document_model.search([
            ('tipo_documento', '=', 'administrativo')
        ])
        
        self.assertEqual(len(admin_docs), 2)
    
    def test_document_search_by_responsible(self):
        """Verificar que se pueden buscar documentos por responsable"""
        self.document_model.create({
            'name': 'Doc with responsible',
            'responsable_custodia': self.responsable.id,
        })
        self.document_model.create({
            'name': 'Doc without responsible',
        })
        
        docs_with_responsible = self.document_model.search([
            ('responsable_custodia', '!=', False)
        ])
        
        self.assertEqual(len(docs_with_responsible), 1)
