import json
import boto3
from decimal import Decimal

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('DisneyAcceleratorTracker')

def lambda_handler(event, context):
    try:
        body = json.loads(event['body'])
        
        required = ['companyId', 'name', 'cohortYear', 'techCategory', 
                   'productionStage', 'disneyVertical', 'technologyMaturity']
        
        for field in required:
            if field not in body:
                return {
                    'statusCode': 400,
                    'headers': {'Access-Control-Allow-Origin': '*'},
                    'body': json.dumps({'error': f'Missing field: {field}'})
                }
        
        item = {
            'companyId': body['companyId'],
            'name': body['name'],
            'cohortYear': int(body['cohortYear']),
            'techCategory': body['techCategory'],
            'productionStage': body['productionStage'],
            'disneyVertical': body['disneyVertical'],
            'technologyMaturity': body['technologyMaturity'],
            'status': body.get('status', 'active cohort'),
            'notes': body.get('notes', '')
        }
        
        table.put_item(Item=item)
        
        return {
            'statusCode': 200,
            'headers': {'Access-Control-Allow-Origin': '*'},
            'body': json.dumps({'message': 'Company added successfully', 'company': item})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {'Access-Control-Allow-Origin': '*'},
            'body': json.dumps({'error': str(e)})
        }