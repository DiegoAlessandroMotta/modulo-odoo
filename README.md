# Módulos de Gestión Documentaria y Tracking Físico - Colegio Jaime White

## 📋 Descripción General

Sistema completo de gestión documentaria y tracking de objetos desarrollado para **Odoo 17 Community Edition**. Permite centralizar la información documentaria institucional y facilitar la trazabilidad de recursos del colegio.

## 🎯 Funcionalidades Principales

### 1. Gestión Documentaria (`jw_documents_extension`)

✅ **CRUD de Archivos Digitales**
- Almacenamiento de archivos binarios (PDF, DOCX, JPG, etc.)
- Metadatos: nombre, descripción, tipo, tamaño
- Cálculo automático de tipo de archivo y tamaño

✅ **Clasificación Documentaria**
- Tipos: Administrativo, Estudiantil, Oficial, Otro
- Ubicación física del original
- Responsable de custodia

✅ **Búsqueda y Filtrado**
- Búsqueda por nombre y descripción
- Filtros por tipo de documento
- Filtros por fecha de creación
- Agrupación por tipo, responsable

✅ **Auditoría y Seguridad**
- Registro de usuario que creó/modificó
- Registro de fechas
- Chatter integrado para comentarios
- Control de acceso por grupos

### 2. Tracking de Objetos (`jw_tracking_objetos`)

✅ **Gestión de Objetos Encontrados/Perdidos**
- Estados: Perdido, Encontrado, Reclamado, Entregado
- Descripción detallada y fotos
- Ubicación actual
- Persona que registra

✅ **Transiciones de Estado**
- Cambios de estado con registro automático en chatter
- Botones de acción rápida (Marcar como encontrado, etc.)

✅ **Integración Documentaria**
- Asociación con documentos (actas, comprobantes)
- Trazabilidad completa

✅ **Vistas Inteligentes**
- Tabla con colores por estado
- Kanban por estado
- Búsqueda avanzada y agrupación

---

## 📦 Instalación

### Requisitos
- Odoo 17 (Community Edition)
- Python 3.10+
- PostgreSQL 15+

### Pasos de Instalación

1. **Clonar el repositorio:**
```bash
git clone <repo-url>
cd modulos-odoo
```

2. **Instalar módulos en orden:**
```bash
# Primero: jw_documents_extension (sin dependencias, solo base y mail)
# Segundo: jw_tracking_objetos (depende de jw_documents_extension)
```

3. **En Odoo:**
   - Ir a `Aplicaciones` → `Actualizar lista de aplicaciones`
   - Buscar "JW Documents Extension"
   - Hacer clic en "Instalar"
   - Buscar "JW Tracking de Objetos"
   - Hacer clic en "Instalar"

---

## 🏗️ Estructura del Proyecto

```
modulos-odoo/
├── docs/
│   ├── REQUIREMENTS.md          # Especificación de requerimientos
│   └── PLAN_TRABAJO.md          # Plan de trabajo detallado
├── modules/
│   ├── jw_documents_extension/
│   │   ├── __init__.py
│   │   ├── __manifest__.py
│   │   ├── models/
│   │   │   ├── __init__.py
│   │   │   └── jw_documento.py          # Modelo principal
│   │   ├── views/
│   │   │   ├── jw_documento_views.xml   # Vistas (form, tree, search)
│   │   │   └── jw_documento_menus.xml   # Menús y acciones
│   │   ├── security/
│   │   │   ├── ir.model.access.csv      # Permisos ACL
│   │   │   └── jw_documents_groups.xml  # Definición de grupos
│   │   ├── tests/
│   │   │   ├── __init__.py
│   │   │   └── test_jw_documento.py     # 11 pruebas unitarias
│   │   ├── validate_module.py           # Script de validación
│   │   └── VALIDACION.md                # Reporte de validación
│   │
│   └── jw_tracking_objetos/
│       ├── __init__.py
│       ├── __manifest__.py
│       ├── models/
│       │   ├── __init__.py
│       │   └── jw_tracking_objeto.py    # Modelo de tracking
│       ├── views/
│       │   ├── jw_tracking_objeto_views.xml
│       │   └── jw_tracking_objeto_menus.xml
│       ├── security/
│       │   ├── ir.model.access.csv
│       │   └── jw_tracking_objetos_groups.xml
│       └── tests/
│           ├── __init__.py
│           └── test_jw_tracking_objeto.py
│
├── REFACTORIZACION.md           # Resumen de cambios
├── .gitignore
└── README.md                    # Este archivo
```

---

## 📚 Modelos de Datos

### jw.documento (Gestión Documentaria)

```python
class JWDocumento(models.Model):
    # Archivo y metadatos
    nombre              # Char (requerido)
    descripcion         # Text
    archivo             # Binary (requerido)
    nombre_archivo      # Char
    tipo_archivo        # Char (computed)
    tamaño_archivo      # Integer (computed)
    
    # Clasificación
    tipo_documento      # Selection: admin, estudiantil, oficial, otro
    ubicacion_fisica    # Char
    responsable_custodia # Many2one: res.partner
    
    # Auditoría
    fecha_creacion
    usuario_creacion
    fecha_modificacion
    usuario_modificacion
    message_ids         # Chatter
```

### jw.tracking.objeto (Tracking de Objetos)

```python
class JWTrackingObjeto(models.Model):
    # Información básica
    nombre              # Char (requerido)
    descripcion         # Text
    estado              # Selection: perdido, encontrado, reclamado, entregado
    
    # Ubicación
    ubicacion_actual    # Char
    persona_registro    # Many2one: res.partner
    fecha_registro      # Datetime
    
    # Relaciones
    documento_asociado  # Many2one: jw.documento
    attachment_ids      # One2many: ir.attachment (fotos)
    
    # Auditoría
    fecha_creacion
    usuario_creacion
    fecha_modificacion
    usuario_modificacion
    message_ids         # Chatter
```

---

## 🔐 Seguridad y Permisos

### jw_documents_extension

**Grupos:**
- `Usuarios de Documentos` - Lectura, creación, modificación
- `Administrador de Documentos` - Acceso completo

### jw_tracking_objetos

**Grupos:**
- `Rastreadores` - Lectura, creación, modificación
- `Administradores de Tracking` - Acceso completo

---

## 🧪 Testing

### Ejecutar Pruebas

```bash
# Pruebas de jw_documents_extension
python -m pytest modules/jw_documents_extension/tests/test_jw_documento.py -v

# Pruebas de jw_tracking_objetos
python -m pytest modules/jw_tracking_objetos/tests/test_jw_tracking_objeto.py -v
```

### Cobertura de Pruebas

✅ **jw_documents_extension:** 11 pruebas
- Crear documentos (básico y completo)
- Validación de archivo requerido
- Búsqueda por tipo
- Búsqueda por responsable
- Cálculo de tipo y tamaño de archivo
- Auditoría

✅ **jw_tracking_objetos:** 10 pruebas
- Crear objetos
- Cambios de estado
- Búsqueda y filtrado
- Asociación con documentos
- Auditoría

---

## 📖 Documentación

- **REQUIREMENTS.md** - Especificación completa de requerimientos
- **PLAN_TRABAJO.md** - Plan detallado con checklist
- **REFACTORIZACION.md** - Detalles de cambios realizados
- **VALIDACION.md** - Reporte de validación del módulo

---

## 🔄 Workflow de Estados (Tracking de Objetos)

```
[Perdido] ──→ [Encontrado] ──→ [Reclamado] ──→ [Entregado]
                    ↓
                [Entregado]
```

**Estados:**
- **Perdido** - Objeto reportado como perdido
- **Encontrado** - Objeto encontrado y registrado
- **Reclamado** - Persona reclama el objeto
- **Entregado** - Objeto entregado a su propietario

---

## 💡 Casos de Uso

### Gestión Documentaria

1. **Secretaría carga acta de consejo académico**
   - Tipo: Administrativo
   - Ubicación: Archivo General - Estante A1
   - Responsable: Director Administrativo

2. **Docente busca documentos de estudiante**
   - Filtra por: Tipo = Estudiantil
   - Busca: Nombre del estudiante
   - Accede a: Certificados, constancias

### Tracking de Objetos

1. **Estudiante reporta pérdida de lentes**
   - Crea registro: "Lentes negros"
   - Estado: Perdido
   - Descripción: "Montura rectangular, marca..."

2. **Se encuentran los lentes**
   - Actualiza estado: Encontrado
   - Ubicación: Dirección
   - El sistema notifica al propietario (vía chatter)

3. **Estudiante reclama**
   - Estado: Reclamado
   - Se prepara comprobante de entrega

4. **Se entregan los lentes**
   - Estado: Entregado
   - Documento asociado: Acta de entrega

---

## 🚀 Próximas Mejoras (Roadmap)

- [ ] Notificaciones por email
- [ ] Reportes PDF
- [ ] Dashboard de métricas
- [ ] Integración con QR
- [ ] Aplicación móvil
- [ ] Localización a otros idiomas

---

## 📝 Notas Importantes

1. **Independencia:** Los módulos son completamente independientes del módulo `documents` de Enterprise
2. **Community Edition:** Compatible con Odoo 17 Community Edition
3. **Extensible:** Fácil de extender con nuevos tipos de documentos o estados
4. **Auditoría:** Todo cambio queda registrado con usuario y fecha

---

## 📧 Contacto y Soporte

Para preguntas o soporte, contactar a:
- **Proyecto:** Módulos de Gestión Documentaria - Colegio Jaime White
- **Versión:** 17.0.1.0.0

---

## 📄 Licencia

LGPL-3

---

## 🎓 Referencia Rápida

### Menús Principales

**Gestión Documentaria**
- Todos los Documentos
- Documentos Administrativos
- Documentos Estudiantiles
- Documentos Oficiales

**Tracking de Objetos**
- Todos los Objetos
- Objetos Perdidos
- Objetos Encontrados
- Objetos Reclamados
- Objetos Entregados

### Atajos Útiles

| Acción | Descripción |
|--------|-------------|
| Crear Documento | Menú → Gestión Documentaria → Nuevo |
| Buscar Documento | Usar buscador rápido + Filtros |
| Crear Objeto | Menú → Tracking de Objetos → Nuevo |
| Cambiar Estado | Botón de acción en formulario |

