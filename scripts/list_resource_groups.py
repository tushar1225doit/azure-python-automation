from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient

subscription_id = "<YOUR_SUBSCRIPTION_ID>"

credential = DefaultAzureCredential()
client = ResourceManagementClient(credential, subscription_id)

for rg in client.resource_groups.list():
    print(rg.name, "-", rg.location)
