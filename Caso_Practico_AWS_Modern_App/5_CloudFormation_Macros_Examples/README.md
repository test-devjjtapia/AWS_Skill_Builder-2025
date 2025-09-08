# Ejemplos de Macros de CloudFormation

**Autor:** Gemini CLI Agent

Las macros de AWS CloudFormation permiten extender las capacidades de CloudFormation, transformando las plantillas antes de que se procesen. Esto es útil para automatizar tareas repetitivas, aplicar estándares de gobernanza o generar recursos dinámicamente.

## 1. ¿Qué son las Macros de CloudFormation?

Una macro es una función AWS Lambda que CloudFormation invoca para procesar una plantilla. La macro recibe la plantilla como entrada, realiza transformaciones y devuelve la plantilla modificada. Esto permite una lógica de plantilla más compleja de lo que es posible con las funciones intrínsecas estándar de CloudFormation.

## 2. Casos de Uso Comunes

*   **Aplicación de Etiquetas (Tags):** Asegurar que todos los recursos tengan etiquetas específicas para la gestión de costos, identificación o cumplimiento.
*   **Generación de Recursos:** Crear múltiples recursos a partir de una definición simplificada.
*   **Validación de Plantillas:** Imponer reglas de negocio o seguridad antes del despliegue.
*   **Inyección de Código:** Añadir fragmentos de código o configuraciones a recursos existentes.

## 3. Ejemplo: Macro `AddTags`

La macro `AddTags` es un ejemplo práctico de cómo se pueden aplicar etiquetas automáticamente a todos los recursos dentro de una plantilla de CloudFormation. Esto es crucial para la gobernanza y la gestión de costos en entornos de AWS.

### Funcionamiento:

La macro `AddTags` (implementada como una función Lambda) itera sobre los recursos definidos en la plantilla de CloudFormation. Para cada recurso, verifica si tiene una propiedad `Tags` y, si no la tiene, la añade. Luego, inserta las etiquetas predefinidas o pasadas como parámetro a la macro.

### Archivos:

*   `add_tags_macro.yaml`: Plantilla de CloudFormation que define la macro y la función Lambda asociada.

