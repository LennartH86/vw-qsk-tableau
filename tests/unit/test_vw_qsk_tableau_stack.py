import aws_cdk as core
import aws_cdk.assertions as assertions

from vw_qsk_tableau.vw_qsk_tableau_stack import VwQskTableauStack

# example tests. To run these tests, uncomment this file along with the example
# resource in vw_qsk_tableau/vw_qsk_tableau_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = VwQskTableauStack(app, "vw-qsk-tableau")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
