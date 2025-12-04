# Corrección: Fotografías Many2many

## Problema Identificado
Las fotografías adjuntas no se guardaban ni visualizaban correctamente debido a una implementación incorrecta de la relación One2many con `ir.attachment`.

## Solución Implementada

### 1. Cambio de One2many a Many2many

**Antes (❌ No funcionaba):**
```python
fotografia_ids = fields.One2many(
    comodel_name='ir.attachment',
    inverse_name='res_id',
    string='Fotografías',
    domain=lambda self: [('res_model', '=', self._name)],
)
```

**Ahora (✅ Funciona):**
```python
fotografia_ids = fields.Many2many(
    comodel_name='ir.attachment',
    relation='jw_tracking_objeto_attachment_rel',
    column1='objeto_id',
    column2='attachment_id',
    string='Fotografías',
)
```

### 2. Widget Simplificado en la Vista

**Antes (❌ Complejo y no funcionaba):**
```xml
<field name="fotografia_ids" mode="kanban" context="...">
    <kanban>
        <!-- Plantilla kanban personalizada -->
    </kanban>
</field>
```

**Ahora (✅ Widget nativo de Odoo):**
```xml
<field name="fotografia_ids" widget="many2many_binary" 
       options="{'accepted_file_extensions': 'image/*'}"/>
```

### 3. Tests Actualizados

Los tests ahora usan la sintaxis correcta de Many2many:

```python
# Crear fotografías
foto1 = env['ir.attachment'].create({
    'name': 'foto1.jpg',
    'datas': base64.b64encode(b'imagen1'),
    'mimetype': 'image/jpeg',
})

# Vincular al objeto
objeto.write({
    'fotografia_ids': [(6, 0, [foto1.id, foto2.id])]  # Reemplazar todas
    # O para agregar: [(4, foto.id)]
    # O para quitar: [(3, foto.id)]
})
```

## Ventajas de Many2many

1. **✅ Guardado automático**: Odoo maneja la persistencia
2. **✅ Widget nativo**: `many2many_binary` es estándar
3. **✅ Vista previa**: Miniaturas automáticas
4. **✅ Descarga**: Funcionalidad integrada
5. **✅ Eliminación**: Confirmación automática
6. **✅ Múltiple upload**: Soportado nativamente

## Cómo Usar

### Desde la Interfaz

1. **Abrir objeto** → Pestaña "Fotografías"
2. **Clic en "Adjuntar archivos"** o ícono de clip
3. **Seleccionar una o múltiples imágenes**
4. **Las fotos aparecen inmediatamente** con miniaturas
5. **Hover sobre cada foto** para ver opciones (descargar, eliminar)

### Desde Código

```python
# Crear objeto con fotos
objeto = env['jw.tracking.objeto'].create({
    'nombre': 'Mochila',
    'fotografia_ids': [(0, 0, {
        'name': 'foto.jpg',
        'datas': imagen_base64,
        'mimetype': 'image/jpeg',
    })],
})

# Agregar foto existente
foto = env['ir.attachment'].create({...})
objeto.write({'fotografia_ids': [(4, foto.id)]})

# Agregar múltiples fotos
objeto.write({'fotografia_ids': [(6, 0, [id1, id2, id3])]})

# Quitar una foto
objeto.write({'fotografia_ids': [(3, foto_id)]})
```

## Actualización Requerida

**Importante**: Debes actualizar el módulo para aplicar estos cambios.

### Opción 1: Interfaz
```
Apps → JW Tracking de Objetos → Actualizar
```

### Opción 2: Terminal
```bash
python3 odoo-bin -u jw_tracking_objetos -d tu_base_datos
```

### Opción 3: Shell (desarrollo)
```python
env['ir.module.module'].search([
    ('name', '=', 'jw_tracking_objetos')
]).button_immediate_upgrade()
```

## Migración de Datos Existentes

Si tenías datos previos (aunque no funcionaban), no se perderán. Los attachments siguen en `ir.attachment`, solo necesitas re-vincularlos:

```python
# Script de migración (ejecutar desde shell)
objetos = env['jw.tracking.objeto'].search([])
for objeto in objetos:
    # Buscar attachments antiguos por res_model y res_id
    attachments = env['ir.attachment'].search([
        ('res_model', '=', 'jw.tracking.objeto'),
        ('res_id', '=', objeto.id),
    ])
    
    if attachments:
        # Re-vincular usando Many2many
        objeto.write({'fotografia_ids': [(6, 0, attachments.ids)]})
        print(f"Migradas {len(attachments)} fotos para {objeto.nombre}")

env.cr.commit()
```

## Verificación Post-Actualización

### 1. Verificar Campo
```python
objeto = env['jw.tracking.objeto'].search([], limit=1)
print(type(objeto.fotografia_ids))  # Debe ser: ir.attachment()
print(objeto._fields['fotografia_ids'].type)  # Debe ser: 'many2many'
```

### 2. Probar Agregar Foto
1. Abrir cualquier objeto
2. Ir a pestaña "Fotografías"
3. Clic en "Adjuntar archivos"
4. Seleccionar imagen
5. **Debe aparecer miniatura inmediatamente**

### 3. Verificar Contador
```python
objeto = env['jw.tracking.objeto'].browse(ID)
print(f"Fotos: {objeto.num_fotografias}")  # Debe coincidir con fotografia_ids
```

## Características del Widget many2many_binary

### Vista de Fotografías
- **Miniaturas**: Automáticas para imágenes
- **Nombres**: Muestra nombre del archivo
- **Tamaño**: Muestra tamaño del archivo
- **Hover**: Opciones de descarga/eliminación
- **Click**: Vista previa en tamaño completo

### Upload
- **Drag & drop**: Arrastrar archivos
- **Múltiple**: Seleccionar varios a la vez
- **Filtro**: Solo imágenes por defecto
- **Progreso**: Barra de carga automática

### Descarga
- **Individual**: Click derecho → Guardar
- **Múltiple**: (requiere personalización)

## Troubleshooting

### "No veo el botón para agregar fotos"
**Solución**: 
- Asegúrate de que el objeto esté guardado (debe tener ID)
- Verifica permisos de escritura en el modelo
- Actualiza el módulo

### "Las fotos se suben pero no aparecen"
**Solución**:
- Refresca la página (F5)
- Verifica que `num_fotografias` se actualice
- Revisa logs de Odoo para errores

### "Error al actualizar el módulo"
**Solución**:
```bash
# Modo debug
python3 odoo-bin -u jw_tracking_objetos -d tu_db --log-level=debug

# Si hay error de relación, eliminar tabla antigua
psql tu_db -c "DROP TABLE IF EXISTS jw_tracking_objeto_attachment_rel CASCADE;"

# Re-intentar actualización
python3 odoo-bin -u jw_tracking_objetos -d tu_db
```

### "Las fotos antiguas no aparecen"
**Solución**: Ejecutar script de migración arriba

## Comparación: Antes vs Ahora

| Aspecto | Antes (One2many) | Ahora (Many2many) |
|---------|------------------|-------------------|
| Guardado | ❌ No funcionaba | ✅ Automático |
| Visualización | ❌ No aparecían | ✅ Miniaturas |
| Widget | ❌ Personalizado | ✅ Nativo Odoo |
| Descarga | ❌ No disponible | ✅ Integrada |
| Upload múltiple | ❌ No | ✅ Sí |
| Drag & drop | ❌ No | ✅ Sí |
| Mantenimiento | ❌ Complejo | ✅ Simple |

## Conclusión

La implementación con **Many2many + widget nativo** es la forma correcta y estándar en Odoo para manejar múltiples archivos adjuntos. Proporciona:

- ✅ Funcionalidad completa out-of-the-box
- ✅ Interfaz consistente con el resto de Odoo
- ✅ Mantenimiento mínimo
- ✅ Mejor experiencia de usuario

**Estado**: ✅ FUNCIONANDO CORRECTAMENTE

Fecha de corrección: 4 de diciembre de 2025
