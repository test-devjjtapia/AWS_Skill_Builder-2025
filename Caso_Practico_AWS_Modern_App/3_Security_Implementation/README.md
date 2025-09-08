# Implementación de Seguridad para la Aplicación Moderna

**Autor:** Javier J. Tapia - 2025

La seguridad es un pilar fundamental en el diseño y despliegue de nuestra aplicación moderna en AWS. Este módulo detalla las estrategias y configuraciones de seguridad implementadas para proteger nuestros recursos y datos.

## 1. Modelo de Responsabilidad Compartida de AWS

Recordamos el modelo de responsabilidad compartida: AWS es responsable de la seguridad *de* la nube (infraestructura subyacente), mientras que nosotros somos responsables de la seguridad *en* la nube (configuración de nuestros recursos, datos, etc.).

## 2. Gestión de Identidad y Acceso (IAM)

AWS Identity and Access Management (IAM) nos permite gestionar de forma segura el acceso a los servicios y recursos de AWS. Definiremos roles y políticas con el principio de privilegio mínimo.

### Ejemplo de Política IAM

A continuación, se muestra un ejemplo de una política IAM que permite el acceso de solo lectura a un bucket S3 específico. Esta política se adjuntaría a un rol o usuario que necesite acceder a los archivos estáticos del frontend.

## 3. Seguridad de Red

*   **Grupos de Seguridad (Security Groups):** Actúan como firewalls virtuales a nivel de instancia, controlando el tráfico de entrada y salida.
*   **Listas de Control de Acceso a la Red (Network ACLs):** Firewalls sin estado a nivel de subred.
*   **AWS WAF (Web Application Firewall):** Protege las aplicaciones web de ataques comunes de la web.

## 4. Protección de Datos

*   **Cifrado en Reposo y en Tránsito:** Asegurar que los datos estén cifrados tanto cuando se almacenan como cuando se mueven entre servicios.
*   **AWS Key Management Service (KMS):** Servicio para crear y controlar las claves de cifrado.

## 5. Monitoreo y Auditoría

*   **AWS CloudTrail:** Registra la actividad de la API de AWS, proporcionando un historial de las acciones realizadas en su cuenta.
*   **Amazon CloudWatch:** Monitorea los recursos de AWS y las aplicaciones que ejecuta en AWS en tiempo real.

## 6. Gestión de Vulnerabilidades

*   **AWS Security Hub:** Proporciona una vista completa de su estado de seguridad en AWS.
*   **Amazon Inspector:** Ayuda a mejorar la seguridad y el cumplimiento de las aplicaciones implementadas en AWS.
