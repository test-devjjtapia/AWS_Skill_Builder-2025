# Plan de Aprendizaje para Desarrolladores: Backends Serverless y Contenedorizados

**Autor:** Javier J. Tapia - 2025

Este módulo explora dos enfoques modernos para el desarrollo de backends: serverless y contenedorizado. Ambos ofrecen ventajas significativas en términos de escalabilidad, eficiencia y gestión, y la elección entre ellos dependerá de los requisitos específicos de cada microservicio.

## 1. Backend Serverless con AWS Lambda y Amazon DynamoDB

El enfoque serverless nos permite construir y ejecutar aplicaciones y servicios sin tener que preocuparnos por la administración de servidores. AWS Lambda ejecuta nuestro código solo cuando es necesario y escala automáticamente, mientras que Amazon DynamoDB proporciona una base de datos NoSQL de alto rendimiento y sin servidor.

### Ventajas:
*   **Sin administración de servidores:** AWS se encarga de todo el aprovisionamiento, escalado y mantenimiento.
*   **Pago por valor:** Solo se paga por el tiempo de cómputo consumido.
*   **Escalado automático:** Se adapta instantáneamente a la demanda.

### Casos de Uso:
*   APIs RESTful de baja latencia.
*   Procesamiento de datos en tiempo real.
*   Backends para aplicaciones móviles y web.

## 2. Backend Contenedorizado con Amazon ECS/Fargate y Amazon Aurora

Los contenedores ofrecen una forma de empaquetar aplicaciones y sus dependencias en unidades aisladas, lo que garantiza la consistencia entre diferentes entornos. Amazon Elastic Container Service (ECS) es un servicio de orquestación de contenedores, y AWS Fargate nos permite ejecutar contenedores sin aprovisionar ni gestionar servidores.

### Ventajas:
*   **Portabilidad:** Los contenedores se ejecutan de manera consistente en cualquier entorno.
*   **Aislamiento:** Cada aplicación se ejecuta en su propio contenedor, evitando conflictos de dependencias.
*   **Eficiencia de recursos:** Los contenedores comparten el kernel del sistema operativo, lo que los hace más ligeros que las máquinas virtuales.

### Casos de Uso:
*   Microservicios complejos con dependencias específicas.
*   Aplicaciones que requieren un control más granular sobre el entorno de ejecución.
*   Migración de aplicaciones existentes a la nube.

## 3. Estructura de este Módulo

Este módulo se divide en dos subsecciones, cada una con ejemplos de código y configuraciones para implementar un backend utilizando el enfoque serverless o contenedorizado.

*   **Serverless_Backend:** Contiene ejemplos de funciones Lambda, definiciones de API Gateway y esquemas de DynamoDB.
*   **Containerized_Backend:** Incluye Dockerfiles, definiciones de tareas de ECS y configuraciones de base de datos Aurora.
