from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
    aws_lambda as _lambda,
    aws_apigateway as apigateway,
)
from constructs import Construct

class AwsServerlessPythonStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        hello_world_function = _lambda.Function(
            self,
            "AwsServerlessPythonFunction",
            runtime = _lambda.Runtime.PYTHON_3_8, # Choose any supported Node.js runtime
            code = _lambda.Code.from_asset("lambda"), # Points to the lambda directory
            handler = "deploy.handler", # Points to the 'hello' file in the lambda directory
        )

        # Define the API Gateway resource
        api = apigateway.LambdaRestApi(
            self,
            "AwsServerlessPythonApi",
            handler = hello_world_function,
            proxy = False,
        )
        
        # Define the '/hello' resource with a GET method
        hello_resource = api.root.add_resource("page")
        hello_resource.add_method("GET")
