# **Requerimientos del Módulo de Gestión Documentaria y Tracking Físico – Colegio Jaime White**

## **1. Descripción general**

El objetivo del módulo es ofrecer una solución integrada dentro del entorno Odoo 17 para gestionar:

- La **documentación digital e institucional** del colegio (administrativa, oficial y estudiantil).  
- El **seguimiento físico de documentos** y su ubicación dentro del plantel.  
- El **registro y tracking de objetos encontrados o institucionales**, incluyendo fotografías y flujo de recuperación.

El sistema permitirá centralizar la información y facilitar la trazabilidad tanto documental como física de recursos del colegio.

---

## **2. Alcance funcional**

### **2.1. Gestión Documentaria (extensión de módulo existente)**

Basado en el módulo nativo `documents` de Odoo, se requiere ampliar sus capacidades con los siguientes elementos:

- **Metadatos adicionales** para cada documento:
  - Tipo de documento (administrativo, estudiantil, oficial, etc.).
  - Ubicación física o archivo donde se conserva la copia original.
  - Persona responsable de resguardo o custodia.  

- **Interfaz y vistas mejoradas**, manteniendo la estructura del módulo `documents`, que permitan visualizar y editar los nuevos campos.

- **Búsqueda y filtrado** por tipo de documento, ubicación o responsable.

- **Integración completa con Odoo Documents**, asegurando compatibilidad con la gestión de carpetas, versiones y permisos nativos.

---

### **2.2. Módulo de Tracking de Objetos**

Se debe incorporar un módulo nuevo, independiente pero integrable con el anterior, para el registro y control de objetos, materiales o pertenencias dentro del colegio.

**Funcionalidades esperadas:**

- Registro de **objetos perdidos, encontrados o institucionales**.  
- Posibilidad de **adjuntar una o más fotografías** del objeto.  
- Asignación de **estado del objeto**: perdido, encontrado, reclamado, entregado.  
- Campos de descripción, ubicación actual y persona que lo registró o encontró.  
- Capacidad de **asociar un documento** (por ejemplo, acta o comprobante de entrega).  
- Lista y formulario de gestión visualmente claros y accesibles desde el menú principal del sistema.  
- Opción de filtrar por estado, fecha de registro o responsable.

---

## **3. Requerimientos no funcionales**

- **Compatibilidad:** Odoo 17 (Enterprise o Community).  
- **Usabilidad:** Interfaz intuitiva, consistente con la apariencia nativa de Odoo.  
- **Seguridad y permisos:**  
  - Control de acceso por grupos de usuario (por ejemplo, docentes, administración).  
  - Solo personal autorizado podrá modificar o eliminar registros.  
- **Auditoría y trazabilidad:**  
  - Uso del *chatter* (seguimiento en Odoo) para registrar los cambios de estado.  
  - Registro automático de usuario y fecha de modificación.  
- **Mantenibilidad:** El código deberá seguir las convenciones estándar de desarrollo en Odoo (ORM, modularidad, herencia limpia).  
- **Localización:** Campos y etiquetas en idioma español, adaptable a futuro a otros idiomas.

---

## **4. Tecnologías y Herramientas Recomendadas**

| Categoría | Herramienta / Tecnología | Descripción |
|------------|--------------------------|--------------|
| **Framework principal** | **Odoo 17** | Plataforma base para el desarrollo modular |
| **Lenguaje** | **Python 3.10+** | Lógica de servidor y modelos ORM |
| **Motor de base de datos** | **PostgreSQL 15+** | Base de datos relacional compatible con Odoo |
| **Frontend** | **XML + QWeb (Odoo views)** | Definición de vistas y formularios |
| **Gestión UI / CSS** | Framework Core de Odoo (OWL, Bootstrap interno) | Interfaz de usuario coherente |
| **Versionado** | Git / GitHub / GitLab | Control de versiones y colaboración |
| **Testing** | Pruebas unitarias Odoo (`odoo.tests.common`) | Validación de integridad funcional |
| **Despliegue recomendado** | Servidor Ubuntu + entorno virtual (`odoo-bin`) | Entorno estándar de desarrollo y producción |
| **Extras opcionales** | Módulos `documents`, `mail`, `base` | Para funcionalidades nativas de archivos y mensajería interna |

---

## **5. Entregables previstos**

1. Módulo `jw_documents_extension` con campos adicionales y vistas personalizadas.  
2. Módulo `jw_tracking_objetos` con modelos, vistas, acciones y menús propios.  
3. Archivos de seguridad (`ir.model.access.csv`) con permisos definidos.  
4. Manual básico de uso y configuración inicial.  
5. Código versionado y documentado.
