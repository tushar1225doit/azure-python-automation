from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient

subscription_id = "9c68c679-faa8-48d6-bc11-1b65925a2fb4"

credential = DefaultAzureCredential()
client = ResourceManagementClient(credential, subscription_id)

for rg in client.resource_groups.list():
    print(rg.name, "-", rg.location)
