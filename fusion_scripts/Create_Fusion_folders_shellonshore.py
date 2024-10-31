# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 20:25:00 2023

@author: APandkar
"""

import os

import boto3

# User Inputs

customer = 'Shellonshore'

deployment_year_month = '2024-11'

crs_bucket_name = "central-results-storage-stg"


list_of_fusion_folders = ["Shellonshore_FUSION_Nordex-3600-131_GBX_",
                          "Shellonshore_FUSION_Nordex-3600-131_GEN_",
                          "Shellonshore_FUSION_Nordex-3600-131_MS-BRG-RS_",
                          "Shellonshore_FUSION_Nordex-4800-155_GBX_",
                          "Shellonshore_FUSION_Nordex-4800-155_GEN_",
                          "Shellonshore_FUSION_Nordex-4800-155_MS-BRG-RS_",
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
