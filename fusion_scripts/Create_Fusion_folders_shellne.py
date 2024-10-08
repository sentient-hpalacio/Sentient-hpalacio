# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 20:25:00 2023

@author: APandkar
"""

import os

import boto3

# User Inputs

customer = 'Shellne'

deployment_year_month = '2024-09'

crs_bucket_name = "central-results-storage-stg"

list_of_fusion_folders = ["Shellne_FUSION_Vestas-3000-90_GBX_",
                          "Shellne_FUSION_Vestas-3000-90_GEN_"
                          ]

# Create Boto3 S3 Client
s3 = boto3.client('s3')

customer_deployment_year_month_name = customer + '/' + deployment_year_month

for each_fusion_folder in list_of_fusion_folders:
    each_fusion_folder_yyyy_mm = each_fusion_folder + deployment_year_month

    print('Creating Fusion folder: ' + each_fusion_folder_yyyy_mm)

    fusion_folder_key = customer_deployment_year_month_name + "/" + each_fusion_folder_yyyy_mm + '/'

    s3.put_object(Bucket=crs_bucket_name, Body='', Key=fusion_folder_key)

    print(' Done!')
