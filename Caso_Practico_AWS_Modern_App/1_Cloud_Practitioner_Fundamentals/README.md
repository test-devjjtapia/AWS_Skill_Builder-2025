# Fundamentos de Cloud Practitioner para la Aplicación Moderna

**Autor:** Gemini CLI Agent

Este módulo establece los conceptos fundamentales de la computación en la nube de AWS que son esenciales para entender la arquitectura de nuestra aplicación moderna.

## 1. ¿Qué es la Computación en la Nube?

La computación en la nube es la entrega bajo demanda de recursos de TI a través de Internet con precios de pago por uso. En lugar de comprar, poseer y mantener sus propios centros de datos y servidores, puede acceder a servicios tecnológicos como potencia informática, almacenamiento y bases de datos, según sea necesario, de un proveedor de la nube como Amazon Web Services (AWS).

## 2. Beneficios Clave de la Nube

*   **Agilidad:** Despliegue rápido de recursos y servicios.
*   **Elasticidad:** Escalabilidad automática para manejar picos de demanda.
*   **Ahorro de Costos:** Pago por uso, eliminación de gastos de capital.
*   **Implementación Global:** Despliegue de aplicaciones en múltiples regiones geográficas.
*   **Seguridad:** AWS ofrece una infraestructura segura y una amplia gama de servicios de seguridad.

## 3. Modelos de Implementación de la Nube

*   **Nube Pública:** Servicios ofrecidos por terceros proveedores a través de la Internet pública (ej. AWS).
*   **Nube Privada:** Recursos de computación utilizados exclusivamente por una organización.
*   **Nube Híbrida:** Una combinación de nubes públicas y privadas.

## 4. Servicios Fundamentales de AWS Utilizados en este Caso Práctico

*   **Amazon S3 (Simple Storage Service):** Almacenamiento de objetos escalable para el frontend de la aplicación.
*   **Amazon EC2 (Elastic Compute Cloud):** Instancias virtuales para computación (aunque en este caso priorizamos serverless y contenedores, es un concepto fundamental).
*   **Amazon VPC (Virtual Private Cloud):** Redes virtuales aisladas para nuestros recursos.
*   **AWS IAM (Identity and Access Management):** Gestión de usuarios, roles y permisos para controlar el acceso a los recursos de AWS.
*   **AWS Billing and Cost Management:** Herramientas para monitorear y controlar los gastos en la nube.

## 5. Seguridad en la Nube (Responsabilidad Compartida)

AWS opera bajo un modelo de responsabilidad compartida:
*   **AWS es responsable de la seguridad *de* la nube:** Protege la infraestructura que ejecuta todos los servicios de AWS.
*   **Usted es responsable de la seguridad *en* la nube:** Es su responsabilidad configurar y gestionar la seguridad de sus datos, aplicaciones y sistemas operativos dentro de la nube.

Este módulo sienta las bases para comprender cómo los servicios de AWS se integran para construir una aplicación robusta y eficiente.
