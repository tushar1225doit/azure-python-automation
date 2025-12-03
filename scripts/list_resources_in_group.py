from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient

subscription_id = "<YOUR_SUBSCRIPTION_ID>"
resource_group = "TusharDemoRG"

credential = DefaultAzureCredential()
client = ResourceManagementClient(credential, subscription_id)

resources = client.resources.list_by_resource_group(resource_group)

for r in resources:
    print(r.type, "-", r.name)

