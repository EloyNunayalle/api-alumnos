import json
import boto3

def lambda_handler(event, context):
    body = event['body'] if isinstance(event['body'], dict) else json.loads(event['body'])

    tenant_id = body['tenant_id']
    alumno_id = body['alumno_id']

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('t_alumnos')

    response = table.delete_item(
        Key={
            'tenant_id': tenant_id,
            'alumno_id': alumno_id
        }
    )

    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Alumno eliminado', 'data': response})
    }

