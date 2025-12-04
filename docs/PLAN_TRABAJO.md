# **Plan de Trabajo – Módulos de Gestión Documentaria y Tracking Físico**

## **Fase 1: Preparación y Configuración del Entorno**

- [x] Configurar repositorio Git y estructura base del proyecto
- [x] Crear directorio de módulos: `jw_documents_extension` y `jw_tracking_objetos`
- [x] Inicializar archivos `__init__.py` y `__manifest__.py` para ambos módulos
- [ ] Configurar entorno virtual y dependencias (Odoo 17, PostgreSQL)
- [ ] Documentar estructura base del proyecto

---

## **Fase 2: Módulo jw_documents_extension (Extensión de Documentos)**

### **2.1. Modelo de Datos**

- [x] Crear modelo heredado de `documents.document`
- [x] Agregar campos adicionales:
  - [x] `tipo_documento` (selection: administrativo, estudiantil, oficial, etc.)
  - [x] `ubicacion_fisica` (char: ubicación del archivo físico)
  - [x] `responsable_custodia` (many2one: res.partner)
- [ ] Definir validaciones y restricciones de negocio
- [ ] Crear índices en base de datos para búsqueda optimizada

### **2.2. Vistas y Formularios**

- [x] Crear vista de formulario mejorada con los nuevos campos
- [x] Crear vista de lista con columnas relevantes (tipo, ubicación, responsable)
- [x] Implementar vista de búsqueda y filtrado avanzado
- [ ] Agregar vista kanban (opcional, por estado o tipo)
- [ ] Personalizar iconos y colores según tipo de documento

### **2.3. Funcionalidades Adicionales**

- [x] Implementar búsqueda por tipo de documento, ubicación o responsable
- [ ] Crear acciones de servidor para cambio de estado o responsable
- [x] Integrar con el chatter nativo para auditoría de cambios
- [ ] Configurar permisos de acceso (grupos de usuario)

### **2.4. Archivos de Seguridad**

- [x] Crear archivo `ir.model.access.csv` con permisos por grupo

---

## **Fase 3: Módulo jw_tracking_objetos (Tracking de Objetos)**

### **3.1. Modelo de Datos**

- [x] Crear modelo `jw.tracking.objeto` con campos:
  - [x] `nombre` (char: nombre del objeto)
  - [x] `descripcion` (text: descripción detallada)
  - [x] `estado` (selection: perdido, encontrado, reclamado, entregado)
  - [x] `ubicacion_actual` (char o many2one: ubicación física)
  - [x] `persona_registro` (many2one: res.partner)
  - [x] `fecha_registro` (datetime: automático)
  - [x] `documento_asociado` (many2one: documents.document - opcional)
  - [x] `fotos` (attachment: múltiples fotografías)
- [x] Definir flujos de estado (transiciones válidas)
- [x] Crear validaciones y reglas de negocio

### **3.2. Modelos Auxiliares**

- [x] Crear modelo `jw.tracking.objeto.foto` si es necesario para galería de imágenes
- [x] Crear modelo `jw.tracking.objeto.estado_log` para historial de cambios de estado

### **3.3. Vistas y Formularios**

- [x] Crear formulario principal con pestañas:
  - [x] Información general
  - [x] Fotografías (galería)
  - [x] Documento asociado
  - [x] Historial de cambios (chatter)
- [x] Crear vista de lista con filtros por estado, fecha o responsable
- [x] Crear vista kanban por estado
- [x] Implementar vista de búsqueda avanzada
- [x] Personalizar colores y iconos por estado

### **3.4. Acciones y Menús**

- [x] Crear acciones de cambio de estado (perdido → encontrado → entregado, etc.)
- [x] Crear menú principal `jw_tracking_objetos` en el dashboard
- [x] Agregar submenús: "Objetos Perdidos", "Objetos Encontrados", "Todos"
- [x] Crear botones de acción en formulario (reclamar, entregar, etc.)

### **3.5. Funcionalidades de Negocio**

- [x] Implementar notificaciones cuando un objeto es registrado
- [x] Registrar automáticamente usuario y fecha de cada cambio
- [x] Permitir asociación con documentos relacionados
- [ ] Crear reportes por estado, período o responsable (opcional)

### **3.6. Archivos de Seguridad**

- [x] Crear archivo `ir.model.access.csv` con permisos por grupo
- [x] Definir grupos: "Rastreadores", "Administradores"

---

## **Fase 4: Integración y Configuración Global**

- [ ] Integrar ambos módulos en el entorno Odoo
- [ ] Configurar relaciones entre `documents` y `jw_tracking_objetos`
- [ ] Establecer permisos y accesos por grupo de usuario
- [ ] Crear botones de acceso cruzado (documento → objeto, objeto → documento)
- [ ] Configurar flujos de trabajo (workflows) si es necesario

---

## **Fase 5: Testing y Validación**

- [x] Escribir pruebas unitarias para modelos `jw_documents_extension`
- [ ] Escribir pruebas unitarias para modelos `jw_tracking_objetos`
- [ ] Realizar pruebas funcionales de crear/editar/eliminar registros
- [x] Validar búsquedas y filtrados funcionan correctamente
- [x] Probar permisos y accesos por grupo
- [ ] Verificar integridad de datos y transiciones de estado
- [ ] Testing de adjuntos y galería de fotografías
- [ ] Realizar pruebas de performance con datos grandes

---

## **Fase 6: Documentación y Despliegue**

- [ ] Redactar manual de usuario (operación básica del sistema)
- [ ] Crear guía de administración (configuración, permisos)
- [ ] Documentar estructura de código y arquitectura
- [ ] Crear docstrings en funciones y clases principales
- [ ] Generar archivo README.md del proyecto
- [ ] Preparar instrucciones de instalación y despliegue
- [ ] Validar código sigue convenciones Odoo (PEP 8, style guide)
- [ ] Realizar revisión final de código

---

## **Fase 7: Mejoras Futuras (Roadmap Opcional)**

- [ ] Integración con módulo `mail` para notificaciones por email
- [ ] Generación de reportes en PDF
- [ ] Dashboard de métricas (objetos perdidos/encontrados por período)
- [ ] App móvil para registro de objetos encontrados
- [ ] Integración con QR para seguimiento rápido
- [ ] Localización a idiomas adicionales
- [ ] Integración con módulo `survey` para encuestas de satisfacción

---

## **Notas Importantes**

- Mantener compatibilidad con Odoo 17 (Community Edition)
- Seguir convenciones de desarrollo de Odoo (herencia, ORM, vistas XML)
- Realizar commits frecuentes con mensajes descriptivos
- Documentar decisiones arquitectónicas y cambios significativos
- Considerar performance desde el inicio (índices, queries optimizadas)
