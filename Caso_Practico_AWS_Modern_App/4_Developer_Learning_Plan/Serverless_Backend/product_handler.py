# product_handler.py
# Autor: Gemini CLI Agent
# Descripción: Función AWS Lambda para gestionar operaciones CRUD en una tabla DynamoDB de productos.

import json
import os
import boto3

dynamodb = boto3.resource('dynamodb')
table_name = os.environ.get('TABLE_NAME', 'Products') # Nombre de la tabla DynamoDB
table = dynamodb.Table(table_name)

def lambda_handler(event, context):
    http_method = event['httpMethod']
    path = event['path']

    if http_method == 'POST' and path == '/products':
        return create_product(event)
    elif http_method == 'GET' and path == '/products':
        return get_all_products()
    elif http_method == 'GET' and path.startswith('/products/'):
        product_id = path.split('/')[-1]
        return get_product(product_id)
    elif http_method == 'PUT' and path.startswith('/products/'):
        product_id = path.split('/')[-1]
        return update_product(product_id, event)
    elif http_method == 'DELETE' and path.startswith('/products/'):
        product_id = path.split('/')[-1]
        return delete_product(product_id)
    else:
        return {
            'statusCode': 400,
            'body': json.dumps({'message': 'Método o ruta no soportada.'})
        }

def create_product(event):
    try:
        body = json.loads(event['body'])
        product = {
            'productId': body['productId'],
            'name': body['name'],
            'description': body.get('description'),
            'price': body.get('price'),
            'stock': body.get('stock', 0)
        }
        table.put_item(Item=product)
        return {
            'statusCode': 201,
            'body': json.dumps(product)
        }
    except KeyError as e:
        return {
            'statusCode': 400,
            'body': json.dumps({'message': f'Falta campo requerido: {e}'})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'message': str(e)})
        }

def get_all_products():
    try:
        response = table.scan()
        return {
            'statusCode': 200,
            'body': json.dumps(response['Items'])
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'message': str(e)})
        }

def get_product(product_id):
    try:
        response = table.get_item(Key={'productId': product_id})
        if 'Item' in response:
            return {
                'statusCode': 200,
                'body': json.dumps(response['Item'])
            }
        else:
            return {
                'statusCode': 404,
                'body': json.dumps({'message': 'Producto no encontrado.'})
            }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'message': str(e)})
        }

def update_product(product_id, event):
    try:
        body = json.loads(event['body'])
        update_expression = "SET "
        expression_attribute_values = {}
        for key, value in body.items():
            if key != 'productId':
                update_expression += f'{key} = :{key}, '
                expression_attribute_values[f':{key}'] = value
        
        update_expression = update_expression.rstrip(', ')

        response = table.update_item(
            Key={'productId': product_id},
            UpdateExpression=update_expression,
            ExpressionAttributeValues=expression_attribute_values,
            ReturnValues="UPDATED_NEW"
        )
        return {
            'statusCode': 200,
            'body': json.dumps(response['Attributes'])
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'message': str(e)})
        }

def delete_product(product_id):
    try:
        table.delete_item(Key={'productId': product_id})
        return {
            'statusCode': 204,
            'body': json.dumps({'message': 'Producto eliminado exitosamente.'})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'message': str(e)})
        }
