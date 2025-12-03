from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient

subscription_id = "<YOUR_SUBSCRIPTION_ID>"

credential = DefaultAzureCredential()
resource_client = ResourceManagementClient(credential, subscription_id)

resource_group_params = {
    "location": "eastus"
}

resource_group_name = "TusharDemoRG"

result = resource_client.resource_groups.create_or_update(
    resource_group_name,
    resource_group_params
)

print(f"Resource Group created: {result.name}")
