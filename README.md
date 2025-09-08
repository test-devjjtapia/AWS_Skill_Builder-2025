# AWS Skill Builder

## 1 AWS Certified Cloud Practitioner

### Fundamentos de la nube (Español de España).pdf
### Ramp-Up_Guide_CloudPractitioner.pdf

### Certificados

- 1 Job Roles in the Cloud (Español de España).pdf
- 2 AWS Cloud Practitioner Essentials (Español de España).pdf
- 3 Getting Started with Cloud Acquisition (Español de España).pdf
- 4 AWS Billing and Cost Management (Español de España).pdf

### Docs

- 10-considerations-for-a-cloud-procurement.pdf
- 2024-cloud-strategy-roadmap.pdf
- AWS Glosario-ESP.pdf
- AWS Glosario-Referencia.pdf
- AWS servicios por categoría-ESP.pdf
- AWS Sustainability FAQ.pdf
- aws-overview.pdf
- Cloud Acquisition FAQs.pdf
- MiniCustomerFAQ.pdf
- ntroducción a los aspectos básicos de la nube de AWS (Español de España).mp4
- Overview of Amazon Web Services-AWS Whitepaper.pdf
- Ramp-Up_Guide_Decision_Maker.pdf
- Spanish_CISPE-Buying-Cloud-Services-in-Public-Sector-Handbook-v2-FEB-2022_es.pdf
- unraveling-tomorrows-cloud-computing-landscape.pdf

#### Enlaces.txt
```
Conceptos básicos de la nube de AWS
https://aws.amazon.com/es/getting-started/cloud-essentials/

¿Qué es la computación en la nube?
https://aws.amazon.com/es/what-is-cloud-computing/

Tipos de cloud computing
https://aws.amazon.com/es/types-of-cloud-computing/

Computación en la nube con AWS
https://aws.amazon.com/es/what-is-aws/
```

## 2  AWS Certified Solutions Architect - Associate y AWS Certified Solutions Architect - Professional

### Ramp-Up_Guide_Architect.pdf

## 3 AWS Certified Security - Specialty

### Ramp-Up_Guide_Security.pdf

## 4 Developer Learning Plan (includes Labs) (Español LATAM)

### URL_Developer Learning Plan.txt
```
Developer Learning Plan (includes Labs) (Español LATAM)

https://skillbuilder.aws/learning-plan/2MB11RS27E/developer-learning-plan-includes-labs-espaol-latam/TRPKFBR4A1
```

### 1 Introduction to Containers

- Introduction to Containers (Español LATAM).pdf

### 2 Introduction to AWS Fargate (Español LATAM)

- Introduction to AWS Fargate (Español LATAM).pdf

### 3 Deep Dive on Container Security (Español LATAM)

### 4 Working with Amazon Elastic Container Service (Español LATAM)

### 5 Amazon EKS Primer (Español LATAM)

- Amazon EKS Primer (Español LATAM).pdf
- eksctl-main.zip
- Introducción a Amazon EKS-AWS Management Console y AWS CLI.pdf
- Qué es Amazon EKS.pdf

#### The official CLI for Amazon.txt
```
The official CLI for Amazon EKS
https://eksctl.io/
```

### 6 Introduction to Serverless Development (Español LATAM)

- Introduction to Serverless Development (Español LATAM).pdf

### 7 Getting into the Serverless Mindset (Español LATAM)

- Getting into the Serverless Mindset (Español LATAM).pdf

#### Herramientas para desarrolladores.txt
```
Herramientas para desarrolladores
https://aws.amazon.com/es/serverless/getting-started/?serverless.sort-by=item.additionalFields.createdDate&serverless.sort-order=desc#Documentation
```

### 8 AWS Lambda Foundations (Español LATAM)

- AWS Lambda Foundations (Español LATAM).pdf

### 9 Amazon API Gateway for Serverless Applications (Español LATAM)

- Amazon API Gateway for Serverless Applications (Español LATAM).pdf
- wellarchitected-serverless-applications-lens.pdf

#### Computación sin servidor.txt
```
Computación sin servidor - Sin servidor en AWS: Cree y ejecute aplicaciones sin preocuparse por los servidores
https://aws.amazon.com/es/serverless/

Welcome to Serverless Land
https://serverlessland.com/

Elección de un tutorial de integración de HTTP
https://docs.aws.amazon.com/es_es/apigateway/latest/developerguide/getting-started-http-integrations.html

Histórias de éxito de los clientes
https://aws.amazon.com/es/solutions/case-studies/?customer-references-cards.sort-by=item.additionalFields.sortDate&customer-references-cards.sort-order=desc&awsf.customer-references-location=*all&awsf.customer-references-industry=*all&awsf.customer-references-use-case=*all&awsf.language=language%23spanish

10 Things Serverless Architects Should Know
https://aws.amazon.com/es/blogs/architecture/ten-things-serverless-architects-should-know/

Category: Amazon API Gateway
https://aws.amazon.com/es/blogs/compute/category/application-services/amazon-api-gateway-application-services/
```

### 10 Amazon DynamoDB for Serverless Architectures (Español LATAM)

- Amazon DynamoDB - Guía para desarrolladores.pdf
- Amazon DynamoDB for Serverless Architectures (Español LATAM).pdf

### 11 Introduction to AWS Lambda (Español LATAM)

### 12 Introduction to Amazon API Gateway (Español LATAM)

### 13 Getting Started with DevOps on AWS (Español LATAM)

- Getting Started with DevOps on AWS (Español LATAM).pdf

### 14 Build and Deploy APIs with a Serverless CI-CD (Español LATAM)

## Advanced CloudFormation-Macros (Español LATAM)

- Advanced CloudFormation-Macros (Español LATAM).pdf
- AWS CloudFormation - Guía del usuario.pdf

### AddTagsMacro.yml
```yaml
AWSTemplateFormatVersion: '2010-09-09'
Description: Macro that adds given tags
Resources:
  LambdaIamRole:
    Type: "AWS::IAM::Role"
    Properties: 
      AssumeRolePolicyDocument: 
        Version: "2012-10-17"
        Statement: 
          - Effect: "Allow"
            Principal: 
              Service: 
                - lambda.amazonaws.com
            Action: 
              - "sts:AssumeRole"
      Policies: 
        - 
          PolicyName: "LambdaPolicy"
          PolicyDocument: 
            Version: "2012-10-17"
            Statement: 
              - 
                Effect: "Allow"
                Action: 
                  - "logs:CreateLogGroup"
                  - "logs:CreateLogStream"
                  - "logs:PutLogEvents"
                Resource: "*"


  AddTagsLambdaFunction:
    Type: "AWS::Lambda::Function"
    Properties: 
      FunctionName: AddTags
      Handler: index.handler
      Role: !GetAtt LambdaIamRole.Arn
      Runtime: python3.6
      Code: 
        ZipFile: |
          def add_tags_to_resource(resource, tags):
            if('Properties' not in resource):
              resource['Properties']={}
            if('Tags' not in resource['Properties']):
                  resource['Properties']['Tags']=[]
            resource['Properties']['Tags'].extend( tags )
            return resource

          def transform_fragment(event):
            tag_list=event['params']['Tags']
            tag_tuples=map( lambda kv: kv.split("="), tag_list)
            tags=map( lambda t: {'Key':t[0],'Value':t[1]}, tag_tuples)
            new_fragment={k: add_tags_to_resource(v,tags) for k, v in event['fragment'].items()}
            return {
              "requestId": event['requestId'],
              "status": "success",
              "fragment": new_fragment
            }

          def handler(event, context):
            try:
              return transform_fragment(event)
            except BaseException as ex:
              print("Error - "+str(ex))
              return {
                "requestId": event['requestId'],
                "status": "ERROR - "+str(ex),
                "fragment": {}
              }

  AddTagsStringMacro:
    Type: AWS::CloudFormation::Macro
    Properties:
      Name: AddTags
      Description: Adds tags to every resource
      FunctionName: !Ref AddTagsLambdaFunction
```

### ErrorIfNotCostCenter.yml
```yaml
AWSTemplateFormatVersion: '2010-09-09'
Description: Macro that ensures every EBS volume is encrypted
Resources:
  LambdaIamRole:
    Type: "AWS::IAM::Role"
    Properties: 
      AssumeRolePolicyDocument: 
        Version: "2012-10-17"
        Statement: 
          - Effect: "Allow"
            Principal: 
              Service: 
                - lambda.amazonaws.com
            Action: 
              - "sts:AssumeRole"
      Policies: 
        - 
          PolicyName: "LambdaPolicy"
          PolicyDocument: 
            Version: "2012-10-17"
            Statement: 
              - 
                Effect: "Allow"
                Action: 
                  - "logs:CreateLogGroup"
                  - "logs:CreateLogStream"
                  - "logs:PutLogEvents"
                Resource: "*"


  LambdaFunction:
    Type: "AWS::Lambda::Function"
    Properties: 
      FunctionName: ErrorIfNotCostCenter
      Handler: index.handler
      Role: !GetAtt LambdaIamRole.Arn
      Runtime: python3.6
      Code: 
        ZipFile: |
          def fail_if_no_cost_center(name,resource):
            print('resource', resource)
            if 'Properties' not in resource:
              raise Exception(name+' does not have any Properties')  
            if 'Tags' not in resource['Properties']:
              raise Exception(name+' missing CostCenter tag')  
            if not list(filter(lambda x: x['Key']=='CostCenter', resource['Properties']['Tags'])):
              raise Exception(name+' missing CostCenter tag')  

          def transform_fragment(event):
            for name,resource in event['fragment']['Resources'].items():
              fail_if_no_cost_center(name,resource)            
            return {
              "requestId": event['requestId'],
              "status": "success",
              "fragment": event['fragment']
            }

          def handler(event, context):
            try:
              return transform_fragment(event)
            except BaseException as ex:
              print("Error - "+str(ex))
              return {
                "requestId": event['requestId'],
                "status": "ERROR - "+str(ex),
                "fragment": {}
              }

  Macro:
    Type: AWS::CloudFormation::Macro
    Properties:
      Name: ErrorIfNotCostCenter
      Description: Global macro. Ensure every resource is tagged with a cost center.
      FunctionName: !Ref LambdaFunction
```

### ExtractVarsMacro.yml
```yaml
AWSTemplateFormatVersion: '2010-09-09'
Description: Macro that ensures every EBS volume is encrypted
Resources:
  LambdaIamRole:
    Type: "AWS::IAM::Role"
    Properties: 
      AssumeRolePolicyDocument: 
        Version: "2012-10-17"
        Statement: 
          - Effect: "Allow"
            Principal: 
              Service: 
                - lambda.amazonaws.com
            Action: 
              - "sts:AssumeRole"
      Policies: 
        - 
          PolicyName: "LambdaPolicy"
          PolicyDocument: 
            Version: "2012-10-17"
            Statement: 
              - 
                Effect: "Allow"
                Action: 
                  - "logs:CreateLogGroup"
                  - "logs:CreateLogStream"
                  - "logs:PutLogEvents"
                Resource: "*"


  LambdaFunction:
    Type: "AWS::Lambda::Function"
    Properties: 
      FunctionName: ExtractVarsMacro
      Handler: index.handler
      Role: !GetAtt LambdaIamRole.Arn
      Runtime: python3.6
      Code: 
        ZipFile: |
          def transform_fragment(event):
              expr=event['params']['Expression']
              var_name=event['params']['Variable']

              var=list(filter( lambda v: v[0]== var_name,
                  map( lambda kv: kv.split("="), expr.split(',') )
              ))
              print('var',var)
              return {
                  "requestId": event['requestId'],
                  "status": "success",
                  "fragment": var[0][1]
              }

          def handler(event, context):
              try:
                  return transform_fragment(event)
              except BaseException as ex:
                  print("Error - "+str(ex))
                  return {
                      "requestId": event['requestId'],
                      "status": "ERROR - "+str(ex),
                      "fragment": {}
                  }
  Macro:
    Type: AWS::CloudFormation::Macro
    Properties:
      Name: ExtractVarsMacro
      Description: Makes sure the Encrypted property is true for any EBS Volume
      FunctionName: !Ref LambdaFunction
```

### Recursos.txt
```
Advanced CloudFormation-Macros (Español LATAM)

Página de inicio de AWS CloudFormation
https://aws.amazon.com/es/cloudformation/

Guía del usuario de AWS CloudFormation
https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html
```

## Advanced Testing Practices Using AWS DevOps Tools (Español LATAM)

- Advanced Testing Practices Using AWS DevOps Tools (Español LATAM).pdf
- AWS_DevOps.pdf
- practicing-continuous-integration-continuous-delivery-on-AWS.pdf

### Resources.txt
```
Resources:

Introduction to DevOps on AWS
https://d0.awsstatic.com/whitepapers/AWS_DevOps.pdf

Practicing Continuous Integration and Continuous Delivery on AWS
https://d0.awsstatic.com/whitepapers/DevOps/practicing-continuous-integration-continuous-delivery-on-AWS.pdf

UI Testing at Scale with AWS Lambda
https://aws.amazon.com/blogs/devops/ui-testing-at-scale-with-aws-lambda/

Crear una solicitud de extracción en AWS CodeCommit
https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-create-pull-request.html

Automating your API testing with AWS CodeBuild, AWS CodePipeline and Postman
https://aws.amazon.com/blogs/devops/automating-your-api-testing-with-aws-codebuild-aws-codepipeline-and-postman/

Identifying and resolving security code vulnerabilities using Snyk in AWS CI/CD Pipeline
https://aws.amazon.com/blogs/devops/identifying-and-resolving-vulnerabilities-in-your-code/

Uso del monitoreo de Amazon CloudWatch Synthetics
https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.html

Pruebas de rendimiento en entrega continua con AWS CodePipeline y BlazeMeter
https://aws.amazon.com/blogs/apn/performance-testing-in-continuous-delivery-using-aws-codepipeline-and-blazemeter/

Probar aplicaciones iOS en AWS Device Farm con Appium
https://aws.amazon.com/blogs/mobile/test-ios-apps-on-aws-device-farm-using-appium-part-1-prerequisities-environment-set-up-and-test-creation/

Configuraciones de implementación
https://docs.aws.amazon.com/codedeploy/latest/userguide/deployment-configurations.html

Uso de configuraciones de implementación en CodeDeploy
https://docs.aws.amazon.com/codedeploy/latest/userguide/deployment-configurations.html
```

## Building Generative AI Applications Using Amazon Bedrock (Español LATAM)

### Module 1 - Introduction to Amazon Bedrock (LATAM Spanish)

### Module 2 - Application Components (LATAM Spanish)

### Module 3 - Foundation Models (LATAM Spanish)

### Module 4 - Using LangChain (LATAM Spanish)

### Module 5 - Architecture Patterns (LATAM Spanish)

### Module 6 - Hands-on Labs (LATAM Spanish)

## Getting Started with AWS CloudFormation (Español LATAM)

- Getting Started with AWS CloudFormation (Español LATAM).pdf
- Ramp-Up_Guide_Operations.pdf

### BudgetWithParams.yaml
```yaml
---
AWSTemplateFormatVersion: "2010-09-09"
Description: "Simple budget example"
Parameters:
  Email:
    Type: String
    Default: email@example.com
    Description: Please enter the email address to which budget notifications should be addressed.
Resources:
  BudgetExample:
    Type: "AWS::Budgets::Budget"
    Properties:
      Budget:
        BudgetLimit:
          Amount: 10
          Unit: USD
        TimeUnit: MONTHLY
        BudgetType: COST
      NotificationsWithSubscribers:
        - Notification:
            NotificationType: ACTUAL
            ComparisonOperator: GREATER_THAN
            Threshold: 99
          Subscribers:
            - SubscriptionType: EMAIL
              Address: !Ref Email
        - Notification:
            NotificationType: ACTUAL
            ComparisonOperator: GREATER_THAN
            Threshold: 80
          Subscribers:
          - SubscriptionType: EMAIL
            Address: !Ref Email
Outputs:
  BudgetId:
    Value: !Ref BudgetExample
```

### Recursos.txt
```
AWS CloudFormation
https://aws.amazon.com/es/cloudformation/

Preguntas frecuentes de AWS
https://aws.amazon.com/es/faqs/#Management_Tools

Referencia de la CLI de CloudFormation
https://docs.aws.amazon.com/cli/latest/reference/cloudformation/index.html#cli-aws-cloudformation

Guía del usuario de CloudFormation
https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html

Curso: Solución de problemas: Pilas de AWS CloudFormation (30 min)
https://www.aws.training/Details/eLearning?id=71220

Referencia de la política JSON de IAM
https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements.html

La sección de CloudFormation en el Knowledge Center
https://aws.amazon.com/premiumsupport/knowledge-center/#AWS_CloudFormation

Guía de aprendizaje de AWS: Operaciones 
```

## Temarios

- AWS-Certified-Developer-Associate_Exam-Guide.pdf
- AWS-DEVOPS DevOps Engineering on AWS.pdf
- Fast Lane - AW-SEC-ESS.pdf

## Caso Práctico: Desarrollo y Despliegue de una Aplicación Web Moderna y Segura en AWS

Este caso práctico demuestra la aplicación de los conocimientos adquiridos en los diferentes módulos del curso para construir y desplegar una aplicación web moderna y segura en AWS, utilizando enfoques serverless y contenedorizados, así como prácticas de DevOps y seguridad.

**Directorio del Caso Práctico:** `Caso_Practico_AWS_Modern_App`

**Contenido:**

*   **1_Cloud_Practitioner_Fundamentals:** Documentación conceptual sobre los fundamentos de la nube aplicados al caso.
*   **2_Solutions_Architecture_Design:** Plantillas de CloudFormation para la infraestructura base (VPC, subredes).
*   **3_Security_Implementation:** Ejemplos de políticas IAM y consideraciones de seguridad.
*   **4_Developer_Learning_Plan:** Implementaciones de backends serverless (Lambda, API Gateway, DynamoDB) y contenedorizados (Docker, ECS, Fargate, Aurora).
*   **5_CloudFormation_Macros_Examples:** Ejemplos de macros de CloudFormation para automatización.
*   **6_DevOps_CI_CD:** Ejemplos de pipelines de CI/CD con AWS CodePipeline, CodeBuild y CodeDeploy.
