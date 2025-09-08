# Backend Serverless: API de Productos

**Autor:** Gemini CLI Agent

Este sub-módulo implementa un backend serverless para una API de productos utilizando AWS Lambda, Amazon API Gateway y Amazon DynamoDB. Esta arquitectura es ideal para microservicios que requieren alta escalabilidad y bajo costo operativo.

## 1. Arquitectura

*   **Amazon API Gateway:** Actúa como el punto de entrada para las solicitudes HTTP, enrutándolas a las funciones Lambda correspondientes.
*   **AWS Lambda:** Contiene la lógica de negocio para gestionar los productos (crear, leer, actualizar, eliminar).
*   **Amazon DynamoDB:** Base de datos NoSQL utilizada para almacenar la información de los productos.

## 2. Implementación

### a. Esquema de DynamoDB (Tabla `Products`)

La tabla `Products` en DynamoDB tendrá la siguiente estructura:

*   **Partition Key:** `productId` (String)
*   **Atributos:** `name` (String), `description` (String), `price` (Number), `stock` (Number)

No se incluye un archivo `.yaml` para la tabla de DynamoDB aquí, ya que su creación se gestionaría a través de CloudFormation en el módulo de Arquitectura de Soluciones, o directamente en la consola de DynamoDB para pruebas rápidas.

### b. Función Lambda (`product_handler.py`)

Esta función Python manejará las operaciones CRUD para los productos. Se activará mediante eventos de API Gateway.

### c. Definición de API Gateway (`api_gateway.yaml`)

Este archivo define los recursos y métodos de la API, y cómo se integran con la función Lambda.
