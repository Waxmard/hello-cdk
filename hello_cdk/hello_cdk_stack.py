import aws_cdk as cdk
from aws_cdk import Stack
from aws_cdk import aws_s3 as s3
# aws_sqs as sqs,
from constructs import Construct


class HelloCdkStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        bucket = s3.Bucket(self, "MyFirstBucket", versioned=True, removal_policy=cdk.RemovalPolicy.DESTROY, auto_delete_objects=True)
        # example resource
        # queue = sqs.Queue(
        #     self, "HelloCdkQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )
