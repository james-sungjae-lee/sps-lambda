import ast
import json
import boto3

ec2 = boto3.client('ec2')
print(boto3.__version__)

def handler(event, context):
    instance_types = ast.literal_eval(event['instance_types'])
    regions = ast.literal_eval(event['regions'])
    
    response = ec2.get_spot_placement_scores(InstanceTypes=instance_types,
    TargetCapacity=1, SingleAvailabilityZone=True, RegionNames=regions)
    scores = response['SpotPlacementScores']
    
    return {
        'statusCode': 200,
        'body': json.dumps(scores)
    }
