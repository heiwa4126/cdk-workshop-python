from aws_cdk import (
    core,
    aws_lambda as _lambda,
    aws_apigateway as apigw,
)

from cdk_workshop.hitcounter import HitCounter


class CdkWorkshopStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Defines an AWS Lambda resource
        hello = _lambda.Function(
            self, 'HelloHandler',
            runtime=_lambda.Runtime.PYTHON_3_8,
            code=_lambda.Code.asset('lambda'),
            handler="hello.handler",
        )

        hello_with_counter = HitCounter(
            self, 'HelloHitCounter',
            downstream=hello,
        )

        apigw.LambdaRestApi(
            self, 'Endpoint',
            handler=hello_with_counter.handler,
        )
