# JW Tracking de Objetos 📦📸

Módulo de Odoo 17 para el registro y seguimiento de objetos perdidos, encontrados e institucionales con soporte completo para fotografías.

## 🎯 Características Principales

### Gestión de Objetos
- ✅ Registro de objetos con información detallada
- ✅ Estados: perdido, encontrado, reclamado, entregado
- ✅ Seguimiento de ubicación física
- ✅ Asociación con documentos relacionados
- ✅ Historial de cambios y auditoría completa

### Sistema de Fotografías 📸
- ✅ **Imagen principal** como avatar del objeto
- ✅ **Galería de fotografías** con visualización en kanban
- ✅ **Contador automático** de fotografías
- ✅ **Descargar y eliminar** fotos individuales
- ✅ **Miniaturas** en listas y vistas kanban
- ✅ **Múltiples formatos** soportados (JPG, PNG, GIF, etc.)

### Vistas Avanzadas
- 📋 Vista de lista con filtros y búsqueda
- 🎴 Vista kanban organizada por estado
- 📝 Formulario completo con pestaña dedicada a fotos
- 🔍 Búsquedas y agrupaciones personalizadas

## 📦 Instalación

### Requisitos
- Odoo 17.0
- Módulo `jw_documents_extension`
- Python 3.8+
- PostgreSQL 12+

### Pasos de Instalación

1. **Copiar el módulo**
   ```bash
   cp -r jw_tracking_objetos /path/to/odoo/addons/
   ```

2. **Actualizar lista de aplicaciones**
   - Ir a Apps → Actualizar lista de aplicaciones
   - O ejecutar: `python3 odoo-bin -u all -d base_datos`

3. **Instalar el módulo**
   - Buscar "JW Tracking de Objetos"
   - Clic en "Instalar"

4. **Verificar instalación**
   - Debería aparecer menú "Tracking Objetos" en el menú principal

## 🚀 Inicio Rápido

### Crear un objeto con fotografía

1. **Ir al menú**: Tracking Objetos → Objetos → Crear

2. **Llenar información básica**:
   - Nombre: "Mochila azul"
   - Descripción: "Mochila deportiva con logo"
   - Estado: "Encontrado"

3. **Agregar imagen principal**:
   - Clic en el avatar (esquina superior izquierda)
   - Seleccionar imagen

4. **Agregar fotografías adicionales**:
   - Ir a pestaña "Fotografías"
   - Clic en "Agregar"
   - Seleccionar múltiples archivos

5. **Guardar**: El contador de fotos se actualiza automáticamente

## 📖 Uso del Sistema de Fotografías

### Imagen Principal
```
Ubicación: Avatar en formulario
Tamaño: 150x150 px
Uso: Identificación rápida del objeto
Visible en: Formulario, Lista, Kanban
```

### Galería de Fotografías
```
Ubicación: Pestaña "Fotografías"
Visualización: Kanban con miniaturas
Acciones: Ver, Descargar, Eliminar
Límite: Ilimitado (recomendado < 20)
```

### Contador de Fotografías
```
Campo: num_fotografias
Tipo: Calculado automáticamente
Visible en: Formulario y Lista
Actualización: Automática al agregar/eliminar
```

## 🎨 Capturas de Pantalla

### Vista de Formulario
```
┌────────────────────────────────────────────┐
│ [Avatar]  Mochila Azul          Estado: ✓  │
│ 150x150                                    │
│                                            │
│ Información General    │  Responsables     │
│ ─────────────────────  │  ───────────────  │
│ Descripción: ...       │  Persona: Juan    │
│ Ubicación: Patio       │  Documento: #123  │
│ Núm. Fotos: 3          │                   │
│                                            │
│ ┌─ Pestaña: Fotografías ──────────────┐   │
│ │  [+Agregar]                          │   │
│ │  ┌────┐ ┌────┐ ┌────┐               │   │
│ │  │ 📷 │ │ 📷 │ │ 📷 │               │   │
│ │  └────┘ └────┘ └────┘               │   │
│ └──────────────────────────────────────┘   │
└────────────────────────────────────────────┘
```

## 🔧 Configuración

### Permisos
El módulo incluye grupos de seguridad predefinidos:
- **Usuario**: Lectura y creación
- **Administrador**: Control total

### Personalización
Editar en `ir.model.access.csv` para ajustar permisos.

## 📊 Estructura de Datos

### Modelo Principal: `jw.tracking.objeto`

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `nombre` | Char | Nombre del objeto |
| `descripcion` | Text | Descripción detallada |
| `estado` | Selection | perdido/encontrado/reclamado/entregado |
| `ubicacion_actual` | Char | Ubicación física |
| `persona_registro` | Many2one | Persona que registra |
| `documento_asociado` | Many2one | Documento relacionado |
| `imagen` | Binary | Imagen principal |
| `fotografia_ids` | One2many | Galería de fotografías |
| `num_fotografias` | Integer | Contador (computed) |

### Relaciones
- `res.partner`: Personas involucradas
- `jw.documento`: Documentos asociados
- `ir.attachment`: Fotografías adjuntas

## 🧪 Testing

### Tests Unitarios
El módulo incluye tests completos:

```bash
# Ejecutar tests
python3 odoo-bin -d test_db --test-enable --stop-after-init -u jw_tracking_objetos
```

### Tests de Fotografías
```python
# Desde el shell de Odoo
python3 odoo-bin shell -d mi_base_datos

# Ejecutar script de prueba
>>> execfile('modules/jw_tracking_objetos/tests/test_fotografias_manual.py')
>>> ejecutar_todos_los_tests(env)
```

### Coverage
```bash
pytest --cov=modules/jw_tracking_objetos tests/
```

## 📚 Documentación Adicional

- [FOTOGRAFIAS.md](FOTOGRAFIAS.md) - Guía completa sobre fotografías
- [GUIA_VISUAL_FOTOGRAFIAS.md](GUIA_VISUAL_FOTOGRAFIAS.md) - Guía visual paso a paso
- [CAMBIOS_FOTOGRAFIAS.md](CAMBIOS_FOTOGRAFIAS.md) - Log de cambios recientes

## 🛠️ Desarrollo

### Estructura del Módulo
```
jw_tracking_objetos/
├── __init__.py
├── __manifest__.py
├── README.md
├── FOTOGRAFIAS.md
├── GUIA_VISUAL_FOTOGRAFIAS.md
├── CAMBIOS_FOTOGRAFIAS.md
├── models/
│   ├── __init__.py
│   └── jw_tracking_objeto.py
├── views/
│   ├── jw_tracking_objeto_views.xml
│   └── jw_tracking_objeto_menus.xml
├── security/
│   └── ir.model.access.csv
├── static/
│   └── src/
│       └── css/
│           └── jw_tracking_objeto.css
└── tests/
    ├── __init__.py
    ├── test_jw_tracking_objeto.py
    └── test_fotografias_manual.py
```

### Contribuir

1. Fork el repositorio
2. Crear rama feature: `git checkout -b feature/nueva-funcionalidad`
3. Commit cambios: `git commit -am 'Agregar nueva funcionalidad'`
4. Push a la rama: `git push origin feature/nueva-funcionalidad`
5. Crear Pull Request

### Coding Style
- Seguir [OCA guidelines](https://github.com/OCA/odoo-community.org/blob/master/website/Contribution/CONTRIBUTING.rst)
- PEP 8 para Python
- Usar pylint-odoo para validación

## 🐛 Resolución de Problemas

### Las fotos no se muestran
```bash
# 1. Actualizar módulo
python3 odoo-bin -u jw_tracking_objetos -d mi_base_datos

# 2. Limpiar caché del navegador
Ctrl + Shift + R

# 3. Verificar permisos
Revisar ir.model.access.csv
```

### Error al subir imágenes grandes
```python
# Aumentar límite en configuración de Odoo
--limit-memory-hard = 2684354560  # 2.5GB
--limit-memory-soft = 2147483648  # 2GB
```

### Performance con muchas fotos
```python
# Optimizar consultas
# Usar límites en búsquedas
objetos = env['jw.tracking.objeto'].search([], limit=50)
```

## 📝 Changelog

### v1.0.0 (2025-12-04)
- ✨ Sistema completo de fotografías
- ✨ Imagen principal como avatar
- ✨ Galería de fotos con kanban
- ✨ Contador automático de fotos
- ✨ Estilos CSS personalizados
- ✨ Tests unitarios ampliados
- 📚 Documentación completa

### v0.1.0 (inicial)
- Modelo básico de tracking
- Estados de objeto
- Auditoría básica

## 📄 Licencia

LGPL-3 - Ver archivo LICENSE para más detalles

## 👥 Autores

- **Colegio Jaime White** - *Desarrollo inicial*

## 🙏 Agradecimientos

- Comunidad Odoo
- OCA (Odoo Community Association)
- Contribuidores del proyecto

## 📞 Soporte

- Issues: [GitHub Issues](https://github.com/tu-repo/issues)
- Email: soporte@colegiojaimewhite.edu
- Documentación: [Wiki del proyecto](https://github.com/tu-repo/wiki)

## 🔗 Enlaces Útiles

- [Odoo Documentation](https://www.odoo.com/documentation/17.0/)
- [OCA Guidelines](https://github.com/OCA/odoo-community.org)
- [Python Odoo Guide](https://www.odoo.com/documentation/17.0/developer/howtos/backend.html)

---

Hecho con ❤️ para la gestión eficiente de objetos
