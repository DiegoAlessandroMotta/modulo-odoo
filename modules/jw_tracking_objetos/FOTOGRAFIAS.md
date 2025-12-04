# Guía para Usar Fotografías en el Módulo de Tracking de Objetos

## Cambios Implementados

Se han realizado las siguientes mejoras para permitir la visualización completa de fotografías en el módulo:

### 1. **Imagen Principal**
- Se agregó un campo `imagen` que muestra una foto principal del objeto
- Aparece como un avatar en la esquina superior izquierda del formulario
- Dimensiones: 150x150 píxeles
- Es visible en la vista de lista y kanban

### 2. **Galería de Fotografías**
- El campo `fotografia_ids` reemplaza al anterior `attachment_ids`
- Usa una relación One2many con `ir.attachment`
- Las fotografías se visualizan en formato kanban dentro de una pestaña dedicada
- Cada foto muestra:
  - Miniatura de la imagen
  - Nombre del archivo
  - Botón para eliminar
  - Botón para descargar

### 3. **Contador de Fotografías**
- Campo calculado `num_fotografias` que muestra el total de fotos
- Visible en el formulario y en la vista de lista
- Se actualiza automáticamente

### 4. **Vistas Mejoradas**
- **Vista de formulario**: Avatar + galería en pestaña
- **Vista de lista**: Columna opcional con miniatura
- **Vista kanban**: Miniatura + contador de fotos

## Cómo Usar

### Agregar una Imagen Principal
1. Abre el registro del objeto
2. Haz clic en el avatar (esquina superior izquierda)
3. Selecciona una imagen desde tu computadora
4. La imagen se mostrará inmediatamente

### Agregar Fotografías Adicionales
1. Abre el registro del objeto
2. Ve a la pestaña "Fotografías"
3. Haz clic en el botón "Agregar" o "Crear"
4. Selecciona o arrastra las imágenes
5. Las fotos aparecerán en formato galería

### Ver las Fotografías
- **En el formulario**: Pestaña "Fotografías"
- **En la lista**: Columna "Imagen" (actívala desde el menú de columnas)
- **En kanban**: Miniatura en cada tarjeta

### Descargar una Fotografía
1. Abre la pestaña "Fotografías"
2. Haz clic en el ícono de descarga (flecha hacia abajo) de la foto deseada

### Eliminar una Fotografía
1. Abre la pestaña "Fotografías"
2. Haz clic en el ícono de papelera de la foto que deseas eliminar

## Formatos Soportados

El sistema acepta cualquier formato de imagen estándar:
- JPEG/JPG
- PNG
- GIF
- BMP
- WEBP
- SVG

## Consideraciones Técnicas

### Almacenamiento
- Las imágenes se guardan como attachments en Odoo
- Se almacenan en la base de datos por defecto
- La imagen principal usa el campo Binary con `attachment=True`

### Rendimiento
- Las miniaturas se generan automáticamente
- El campo `num_fotografias` está almacenado para consultas rápidas
- Las imágenes se cargan bajo demanda

### Seguridad
- Los permisos de acceso se heredan del modelo principal
- Solo usuarios con permisos sobre `jw.tracking.objeto` pueden ver/editar fotos

## Actualización del Módulo

Para aplicar estos cambios en una instalación existente:

```bash
# 1. Actualizar el módulo
python3 odoo-bin -u jw_tracking_objetos -d nombre_base_datos

# O desde la interfaz:
# Apps > JW Tracking de Objetos > Actualizar
```

### Migración de Datos Existentes

Si tenías datos en el campo anterior `attachment_ids`, deberás migrarlos manualmente:

```python
# Ejecutar en el shell de Odoo o en un script de migración
tracking_objects = env['jw.tracking.objeto'].search([])
for obj in tracking_objects:
    # Los attachments anteriores seguirán existiendo en ir.attachment
    # Solo necesitas asegurar que res_model y res_id estén correctos
    pass
```

## Estilos Personalizados

Se ha incluido un archivo CSS (`static/src/css/jw_tracking_objeto.css`) que mejora la presentación visual de las fotografías con:
- Bordes y sombras suaves
- Hover effects
- Layout responsive
- Botones de acción estilizados

## Resolución de Problemas

### Las imágenes no se muestran
1. Verifica que el módulo esté actualizado
2. Limpia la caché del navegador (Ctrl+Shift+R)
3. Revisa los permisos del usuario

### Error al subir imágenes
1. Verifica el tamaño del archivo (límite por defecto: 25MB)
2. Asegúrate de que el formato sea compatible
3. Revisa los logs de Odoo para errores específicos

### La galería aparece vacía
1. Confirma que las imágenes se hayan guardado correctamente
2. Verifica que `res_model` sea 'jw.tracking.objeto'
3. Confirma que `res_id` coincida con el ID del registro

## Próximas Mejoras

Posibles mejoras futuras:
- Visor de imágenes en pantalla completa (lightbox)
- Edición de imágenes (recortar, rotar)
- Reconocimiento de texto en imágenes (OCR)
- Organización de fotos por categorías
- Comparación lado a lado de fotos
