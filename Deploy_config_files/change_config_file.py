import json
import boto3
from botocore.exceptions import NoCredentialsError
import pandas as pd

filepath = "device_level_plot_config.json"
with open(file=filepath, mode='r') as file:
    config_data = json.load(file)

assets_df = pd.read_excel(io="New_assets.xlsx", sheet_name='Vestas-6000-162')

# # modifying and saving the config_file
# config_data['customer'] = 'liberty'
# config_data['plant'] = assets_df['Site'][0]
# config_data['device'] = assets_df['Device'][0]

# with open(file="modified_config_files/device_level_config.json", mode='w') as f:
#     json.dump(config_data, f, indent=4)
#
# #s3_bucket = "technicaldashboardstacks-technicaldashboardbucket-1uglybpy4q8fa" #stg
# s3_bucket = "technicaldashboardstackp-technicaldashboardbucket-1frt3g7ydvmv3"  #prod
#
# s3_key = config_data['customer'] + "/" + config_data['plant'] + "/" + config_data[
#     'device'] + "/device_level_plot_config.json"
# s3_client = boto3.Session(profile_name='prod').client('s3')
# #s3_client = boto3.client('s3')
#
# s3_client.upload_file("modified_config_files/device_level_config.json", s3_bucket, s3_key)

for i in range(assets_df.shape[0]):
    config_data['customer'] = 'liberty'
    config_data['plant'] = assets_df.loc[i, 'Site']
    config_data['device'] = assets_df.loc[i, 'Device']

    with open(file="modified_config_files/device_level_config.json", mode='w') as f:
        json.dump(config_data, f, indent=4)

    s3_bucket = "technicaldashboardstackp-technicaldashboardbucket-1frt3g7ydvmv3"
    s3_key = config_data['customer'] + "/" + config_data['plant'] + "/" + config_data[
        'device'] + "/device_level_plot_config.json"

    s3_client = boto3.Session(profile_name='prod').client('s3')
    #s3_client = boto3.client('s3')
    s3_client.upload_file("modified_config_files/device_level_config.json", s3_bucket, s3_key)
