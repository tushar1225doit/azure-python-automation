from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient

subscription_id = "9c68c679-faa8-48d6-bc11-1b65925a2fb4"
resource_group = "TusharDemoRG"

credential = DefaultAzureCredential()
client = ResourceManagementClient(credential, subscription_id)

resources = client.resources.list_by_resource_group(resource_group)

for r in resources:
    print(r.type, "-", r.name)

