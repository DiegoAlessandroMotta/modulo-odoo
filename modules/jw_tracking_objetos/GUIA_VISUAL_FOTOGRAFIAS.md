# Guía Visual: Uso de Fotografías en Tracking de Objetos

## 🎯 Vista General del Sistema

El módulo ahora soporta tres formas de trabajar con imágenes:

1. **Imagen Principal** (Avatar)
2. **Galería de Fotografías** (Múltiples fotos)
3. **Visualización en Listas/Kanban** (Miniaturas)

---

## 📸 1. Imagen Principal

### Ubicación
Esquina superior izquierda del formulario, junto al título

### Cómo se ve
```
┌─────────────────────────────────────────┐
│ [Foto]  Nombre del Objeto               │
│ 150x150                                 │
│                                         │
│ ┌─ Información General ───────────┐   │
│ │ Descripción: ...                 │   │
│ │ Ubicación: ...                   │   │
│ │ Núm. Fotografías: 3              │   │
│ └──────────────────────────────────┘   │
└─────────────────────────────────────────┘
```

### Cómo agregar
1. Clic en el espacio de la imagen
2. Seleccionar archivo desde tu computadora
3. La imagen aparece inmediatamente

### Formatos soportados
- JPG/JPEG
- PNG
- GIF
- BMP
- WEBP

---

## 🖼️ 2. Galería de Fotografías

### Ubicación
Pestaña "Fotografías" en el formulario

### Cómo se ve
```
┌─────────────────────────────────────────────────┐
│  [Agregar]                                      │
│                                                 │
│  ┌────────┐  ┌────────┐  ┌────────┐           │
│  │        │  │        │  │        │           │
│  │ Foto 1 │  │ Foto 2 │  │ Foto 3 │           │
│  │        │  │        │  │        │           │
│  └────────┘  └────────┘  └────────┘           │
│  foto1.jpg   foto2.jpg   foto3.jpg            │
│  [🗑️] [⬇️]   [🗑️] [⬇️]   [🗑️] [⬇️]            │
└─────────────────────────────────────────────────┘
```

### Acciones disponibles
- **Agregar**: Botón para subir nuevas fotos
- **Ver**: Clic en la miniatura para ver tamaño completo
- **Descargar**: Icono de flecha hacia abajo
- **Eliminar**: Icono de papelera

### Cómo agregar múltiples fotos
1. Ir a la pestaña "Fotografías"
2. Clic en "Agregar" o "Crear"
3. Seleccionar uno o varios archivos
4. Las fotos se muestran automáticamente

---

## 📋 3. Vista de Lista

### Cómo se ve
```
┌────────┬───────────────┬──────────┬──────┐
│ Imagen │ Nombre        │ Estado   │ Fotos│
├────────┼───────────────┼──────────┼──────┤
│ [📷]   │ Mochila azul  │ Perdido  │  2   │
│ [📷]   │ Llave salón   │ Encontr. │  1   │
│ [📷]   │ Celular       │ Reclamad.│  5   │
└────────┴───────────────┴──────────┴──────┘
```

### Características
- Miniatura de 50x50 píxeles
- Columna opcional (puede ocultarse)
- Contador de fotografías visible

### Activar/Desactivar columna Imagen
1. Clic en el icono de engranaje (⚙️) en la vista de lista
2. Marcar o desmarcar "Imagen"
3. Guardar vista

---

## 🎴 4. Vista Kanban

### Cómo se ve
```
Perdidos          │ Encontrados       │ Reclamados
──────────────────┼───────────────────┼──────────────
┌────────────┐    │ ┌────────────┐   │ ┌──────────┐
│ [📷]       │    │ │ [📷]       │   │ │ [📷]     │
│ Mochila    │    │ │ Llave      │   │ │ Celular  │
│            │    │ │            │   │ │          │
│ Por: Juan  │    │ │ Por: María │   │ │ Por: Ana │
│ 04/12/2025 │    │ │ 03/12/2025 │   │ │ 02/12/25 │
│ 📷 2 fotos │    │ │ 📷 1 foto  │   │ │ 📷 5 fot │
└────────────┘    │ └────────────┘   │ └──────────┘
```

### Características
- Imagen de 64x64 píxeles
- Información condensada
- Contador de fotos con icono
- Arrastrar y soltar entre estados

---

## 🔧 Casos de Uso Comunes

### Caso 1: Registrar objeto perdido con foto
```
1. Crear nuevo registro → Objetos
2. Nombre: "Mochila deportiva roja"
3. Estado: Perdido
4. Clic en avatar → subir foto principal
5. Guardar
```

### Caso 2: Agregar evidencias fotográficas
```
1. Abrir objeto existente
2. Ir a pestaña "Fotografías"
3. Clic en "Agregar"
4. Seleccionar múltiples fotos (Ctrl+clic)
5. Confirmar
```

### Caso 3: Ver todas las fotos de un objeto
```
1. Abrir objeto
2. Pestaña "Fotografías"
3. Clic en cualquier miniatura → vista completa
4. Usar flechas para navegar entre fotos
```

### Caso 4: Descargar foto para enviar por email
```
1. Abrir objeto
2. Pestaña "Fotografías"
3. Clic en icono de descarga (⬇️)
4. Archivo se descarga automáticamente
```

### Caso 5: Eliminar foto duplicada
```
1. Abrir objeto
2. Pestaña "Fotografías"
3. Buscar foto a eliminar
4. Clic en icono papelera (🗑️)
5. Confirmar eliminación
```

---

## 💡 Consejos y Mejores Prácticas

### Para Fotos de Calidad
- ✅ Usar buena iluminación
- ✅ Tomar desde múltiples ángulos
- ✅ Incluir detalles distintivos
- ✅ Fondo neutro preferiblemente
- ❌ Evitar fotos borrosas
- ❌ No usar flash directo

### Para Organización
- Usar nombres descriptivos: "mochila_frente.jpg", "mochila_etiqueta.jpg"
- Subir foto principal primero
- Agregar fotos adicionales de detalles
- Eliminar fotos duplicadas

### Para Rendimiento
- Tamaño recomendado: 1-2 MB por foto
- Resolución óptima: 1920x1080 px
- Formato preferido: JPG para fotos reales
- Formato PNG para capturas de pantalla

---

## 🐛 Solución de Problemas

### "No veo la imagen que subí"
**Solución**:
1. Actualizar página (F5)
2. Limpiar caché del navegador (Ctrl+Shift+R)
3. Verificar que se guardó el registro

### "El botón Agregar no funciona"
**Solución**:
1. Verificar permisos de usuario
2. Confirmar que el registro está guardado
3. Revisar espacio disponible en servidor

### "Las fotos se ven pixeladas"
**Solución**:
1. Usar imágenes de mayor resolución
2. Evitar agrandar fotos muy pequeñas
3. Subir versión de mejor calidad

### "No puedo eliminar una foto"
**Solución**:
1. Verificar permisos de escritura
2. Confirmar que no está referenciada en otros lugares
3. Contactar administrador si persiste

---

## 📱 Compatibilidad Móvil

El diseño es responsive y funciona en:
- ✅ Tablets (iPad, Android)
- ✅ Smartphones (iOS, Android)
- ✅ Desktop (Windows, Mac, Linux)

### En móviles
- Tocar avatar para subir desde cámara o galería
- Pellizcar para zoom en miniaturas
- Deslizar para navegar fotos

---

## 📊 Información Técnica

### Almacenamiento
- Base de datos: Odoo PostgreSQL
- Tabla: `ir_attachment`
- Campo Binary con `attachment=True`

### Límites
- Tamaño máximo por archivo: 25 MB (configurable)
- Número de fotos: ilimitado (recomendado < 20)
- Formatos: todos los de imagen estándar

### Seguridad
- Permisos heredados del modelo principal
- Solo usuarios autorizados pueden ver/editar
- Registro de auditoría en cada cambio

---

## ✨ Resumen de Funcionalidades

| Característica | Estado | Vista |
|----------------|--------|-------|
| Imagen Principal | ✅ | Formulario, Lista, Kanban |
| Galería de Fotos | ✅ | Formulario (pestaña) |
| Contador de Fotos | ✅ | Todas las vistas |
| Descargar Foto | ✅ | Galería |
| Eliminar Foto | ✅ | Galería |
| Vista Previa | ✅ | Clic en miniatura |
| Múltiple Upload | ✅ | Galería |
| Drag & Drop | ⏳ | Próximamente |

**Leyenda**: ✅ Implementado | ⏳ En desarrollo | ❌ No disponible
