import ast
import json
import boto3

def lambda_handler(event, context):
    credential = event['credential']
    instance_types = ast.literal_eval(event['instance_types'])
    regions = ast.literal_eval(event['regions'])
    
    session = boto3.session.Session(
        aws_access_key_id=credential['aws_id'],
        aws_secret_access_key=credential['aws_pw'])
    ec2 = session.client('ec2', region_name='us-west-2')
    
    response = ec2.get_spot_placement_scores(
        InstanceTypes=instance_types,
        TargetCapacity=1,
        SingleAvailabilityZone=True,
        RegionNames=regions)
    scores = response['SpotPlacementScores']
    
    return {
        'statusCode': 200,
        'body': json.dumps(scores)
    }
