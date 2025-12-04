# Guía Rápida: Fotografías Corregidas ✅

## 🎉 ¡Problema Resuelto!

Las fotografías ahora **funcionan correctamente** usando Many2many con el widget nativo de Odoo.

---

## 📸 Cómo Agregar Fotografías

### Paso 1: Abrir el Objeto
```
Menú → Tracking Objetos → Objetos → [Seleccionar objeto]
```

### Paso 2: Ir a la Pestaña Fotografías
```
┌─────────────────────────────────────┐
│ [Avatar] Nombre del Objeto          │
│ ├─ General  ├─ Responsables         │
│ ├─ Fotografías ✓ (AQUÍ)             │
│ └─ Auditoría                        │
└─────────────────────────────────────┘
```

### Paso 3: Adjuntar Archivos
Verás una de estas dos interfaces:

**Opción A: Sin fotos previas**
```
┌──────────────────────────────────────┐
│  📎 Adjuntar archivos                │
│                                      │
│  Arrastra archivos aquí o haz clic  │
└──────────────────────────────────────┘
```

**Opción B: Con fotos previas**
```
┌──────────────────────────────────────┐
│  📎 + Adjuntar                       │
│                                      │
│  ┌────────┐  ┌────────┐             │
│  │ [img]  │  │ [img]  │             │
│  │foto1   │  │foto2   │             │
│  │ 🗑️ ⬇️  │  │ 🗑️ ⬇️  │             │
│  └────────┘  └────────┘             │
└──────────────────────────────────────┘
```

### Paso 4: Seleccionar Imágenes
- **Un archivo**: Click en "Adjuntar" → Seleccionar imagen
- **Múltiples**: Ctrl+Click o Shift+Click para seleccionar varias
- **Drag & Drop**: Arrastra desde tu explorador de archivos

### Paso 5: ¡Listo! ✅
Las fotos aparecen **inmediatamente** con:
- ✅ Miniatura de la imagen
- ✅ Nombre del archivo
- ✅ Tamaño del archivo
- ✅ Botones de acción (eliminar, descargar)

---

## 🖼️ Visualización de Fotografías

### En el Formulario
```
┌─────────────────────────────────────────┐
│ [Avatar]  Mochila Azul      [Estado]    │
│ 150x150                                 │
│                                         │
│ Pestaña: Fotografías                    │
│ ┌───────────────────────────────────┐   │
│ │ 📎 + Adjuntar                     │   │
│ │                                   │   │
│ │ ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐  │   │
│ │ │ 📷  │ │ 📷  │ │ 📷  │ │ 📷  │  │   │
│ │ │img1 │ │img2 │ │img3 │ │img4 │  │   │
│ │ └─────┘ └─────┘ └─────┘ └─────┘  │   │
│ │ foto1.jpg  foto2.jpg  ...         │   │
│ │ 125 KB     98 KB                  │   │
│ │ [🗑️] [⬇️]  [🗑️] [⬇️]              │   │
│ └───────────────────────────────────┘   │
│                                         │
│ Núm. Fotografías: 4                     │
└─────────────────────────────────────────┘
```

### Vista Previa (Click en miniatura)
```
┌──────────────────────────────┐
│          [IMAGEN GRANDE]      │
│                              │
│   foto1.jpg                  │
│   125 KB                     │
│                              │
│   [< Anterior]  [Siguiente >]│
│   [Cerrar]                   │
└──────────────────────────────┘
```

### En la Lista
```
┌────────┬─────────────┬─────────┬──────┐
│ Imagen │ Nombre      │ Estado  │ Fotos│
├────────┼─────────────┼─────────┼──────┤
│ [📷]   │ Mochila     │ Perdido │  4   │
│ [📷]   │ Llave       │ Encontr.│  2   │
└────────┴─────────────┴─────────┴──────┘
```

### En Kanban
```
┌────────────────┐
│ [📷 imagen]    │
│ Mochila Azul   │
│                │
│ Juan García    │
│ 04/12/2025     │
│ 📷 4 fotos     │
└────────────────┘
```

---

## ⚡ Acciones Disponibles

### 🖼️ Ver Foto en Tamaño Completo
```
1. Hover sobre la miniatura
2. Click en la imagen
3. Se abre visor de imágenes
4. Usar flechas para navegar
```

### ⬇️ Descargar Foto
```
1. Hover sobre la foto
2. Click en ícono de descarga (⬇️)
3. Archivo se descarga automáticamente
```

### 🗑️ Eliminar Foto
```
1. Hover sobre la foto
2. Click en ícono de papelera (🗑️)
3. Confirmar eliminación
4. Contador se actualiza automáticamente
```

### ➕ Agregar Más Fotos
```
1. Click en "📎 Adjuntar archivos"
2. Seleccionar imágenes
3. Se agregan a las existentes
```

---

## 🎯 Ejemplos de Uso

### Caso 1: Objeto Perdido con Múltiples Ángulos
```
Nombre: Mochila deportiva roja
Estado: Perdido
Fotografías:
  - mochila_frente.jpg (vista frontal)
  - mochila_logo.jpg (detalle del logo)
  - mochila_etiqueta.jpg (etiqueta con nombre)
  - mochila_interior.jpg (contenido)
```

### Caso 2: Objeto Encontrado con Características
```
Nombre: Celular Samsung
Estado: Encontrado
Fotografías:
  - celular_pantalla.jpg (pantalla)
  - celular_trasera.jpg (parte trasera)
  - celular_imei.jpg (número IMEI)
```

### Caso 3: Material Institucional Inventariado
```
Nombre: Proyector Epson
Estado: Reclamado
Fotografías:
  - proyector_general.jpg
  - proyector_serial.jpg (número de serie)
  - proyector_estado.jpg (condición física)
```

---

## 🔧 Configuración del Widget

El widget `many2many_binary` soporta estas opciones:

```xml
<field name="fotografia_ids" 
       widget="many2many_binary"
       options="{
           'accepted_file_extensions': 'image/*',
           'max_file_size': 10485760,  # 10 MB (opcional)
       }"/>
```

### Opciones Disponibles
- `accepted_file_extensions`: Filtro de archivos (`'image/*'`, `'.jpg,.png'`)
- `max_file_size`: Tamaño máximo en bytes (default: 25 MB)

---

## 📊 Datos Técnicos

### Tabla de Relación
```sql
jw_tracking_objeto_attachment_rel
├── objeto_id      (int) → jw_tracking_objeto.id
└── attachment_id  (int) → ir_attachment.id
```

### Tipos de Archivo Soportados
| Extensión | MIME Type | Soportado |
|-----------|-----------|-----------|
| .jpg/.jpeg| image/jpeg | ✅ |
| .png | image/png | ✅ |
| .gif | image/gif | ✅ |
| .bmp | image/bmp | ✅ |
| .webp | image/webp | ✅ |
| .svg | image/svg+xml | ✅ |
| .tiff | image/tiff | ✅ |

### Límites por Defecto
- **Tamaño máximo por archivo**: 25 MB
- **Número de archivos**: Ilimitado
- **Formatos permitidos**: Todos los de imagen

---

## ✅ Checklist Post-Actualización

Después de actualizar el módulo, verifica:

- [ ] Puedes abrir un objeto existente
- [ ] Ves la pestaña "Fotografías"
- [ ] Puedes hacer click en "Adjuntar archivos"
- [ ] Puedes seleccionar una imagen
- [ ] La imagen aparece como miniatura
- [ ] El contador `num_fotografias` se actualiza
- [ ] Puedes ver la imagen en tamaño completo
- [ ] Puedes descargar la imagen
- [ ] Puedes eliminar la imagen
- [ ] Puedes agregar múltiples imágenes a la vez

### Si alguno falla:
1. Actualiza el módulo nuevamente
2. Limpia caché del navegador (Ctrl+Shift+R)
3. Revisa permisos del usuario
4. Consulta logs de Odoo: `/var/log/odoo/odoo.log`

---

## 🚀 Actualizar el Módulo

### Método 1: Interfaz Web (Recomendado)
```
1. Apps
2. Buscar "JW Tracking"
3. Menú (⋮) → Actualizar
4. Esperar confirmación
5. Refrescar página (Ctrl+Shift+R)
```

### Método 2: Terminal
```bash
cd /ruta/a/odoo
python3 odoo-bin -u jw_tracking_objetos -d tu_base_datos
```

### Método 3: Shell de Odoo
```python
env['ir.module.module'].search([
    ('name', '=', 'jw_tracking_objetos')
]).button_immediate_upgrade()
```

---

## 💡 Tips Profesionales

### 📷 Para Mejores Fotos
- Usar buena iluminación natural
- Enfocar detalles distintivos
- Incluir referencia de tamaño si es relevante
- Tomar desde múltiples ángulos

### 📝 Para Nombrar Archivos
- Usar nombres descriptivos: `mochila_frente.jpg`
- Incluir ángulo o detalle: `celular_pantalla.jpg`
- Evitar espacios: `objeto-azul.jpg` mejor que `objeto azul.jpg`

### 🎯 Para Organización
- Subir foto principal primero (avatar)
- Luego agregar fotos de detalles
- Eliminar duplicadas o borrosas
- Mantener < 10 fotos por objeto (recomendado)

### ⚡ Para Rendimiento
- Optimizar imágenes antes de subir (max 2 MB)
- Usar JPG para fotos, PNG para capturas
- Evitar imágenes de más de 4000x3000 px

---

## 🆘 Soporte

**¿Problemas?** Revisa:
1. [CORRECCION_FOTOGRAFIAS.md](CORRECCION_FOTOGRAFIAS.md) - Troubleshooting detallado
2. [FOTOGRAFIAS.md](FOTOGRAFIAS.md) - Documentación técnica completa
3. Logs de Odoo para errores específicos

**¿Sugerencias?** Contacta al equipo de desarrollo.

---

**Estado**: ✅ COMPLETAMENTE FUNCIONAL  
**Última actualización**: 4 de diciembre de 2025  
**Versión del módulo**: 17.0.1.0.0
