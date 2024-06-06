# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 20:25:00 2023

@author: APandkar
"""

import os

import boto3

# User Inputs

customer = 'Liberty'

deployment_year_month = '2024-06'

crs_bucket_name = "central-results-storage-stg"


list_of_fusion_folders = ["Liberty_FUSION_SGRE-4700-145_GBX_",
                          "Liberty_FUSION_SGRE-4700-145_GEN_",
                          "Liberty_FUSION_SGRE-4700-145_MS-BRG-RS_",
                          "Liberty_FUSION_SGRE-4700-145_MS-BRG-GS_",
                          "Liberty_FUSION_SGRE-4800-145_GBX_",
                          "Liberty_FUSION_SGRE-4800-145_GEN_",
                          "Liberty_FUSION_SGRE-4800-145_MS-BRG-RS_",
                          "Liberty_FUSION_SGRE-4800-145_MS-BRG-GS_",
                          "Liberty_FUSION_SGRE-5000-145_GBX_",
                          "Liberty_FUSION_SGRE-5000-145_GEN_",
                          "Liberty_FUSION_SGRE-5000-145_MS-BRG-RS_",
                          "Liberty_FUSION_SGRE-5000-145_MS-BRG-GS_",
                          "Liberty_FUSION_Gamesa-2000-90_GBX_",
                          "Liberty_FUSION_Gamesa-2000-90_GEN_",
                          "Liberty_FUSION_Gamesa-2000-90_MS-BRG-RS_",
                          "Liberty_FUSION_Gamesa-2000-90_MS-BRG-GS_",
                          "Liberty_FUSION_Vestas-1650-82_GBX_",
                          "Liberty_FUSION_Vestas-1650-82_GEN_",
                          "Liberty_FUSION_Vestas-1650-82_MS-BRG-RS_",
                          "Liberty_FUSION_Vestas-2000-110_GBX_",
                          "Liberty_FUSION_Vestas-2000-110_GEN_",
                          "Liberty_FUSION_Vestas-2000-110_MS-BRG-RS_",
                          "Liberty_FUSION_Vestas-2050-110_GBX_",
                          "Liberty_FUSION_Vestas-2050-110_GEN_",
                          "Liberty_FUSION_Vestas-2050-110_MS-BRG-RS_",
                          "Liberty_FUSION_Vestas-2100-110_GBX_",
                          "Liberty_FUSION_Vestas-2100-110_GEN_",
                          "Liberty_FUSION_Vestas-2100-110_MS-BRG-RS_",
                          "Liberty_FUSION_Vestas-2200-120_GBX_",
                          "Liberty_FUSION_Vestas-2200-120_GEN_",
                          "Liberty_FUSION_Vestas-3700-136_MS-BRG-RS_",
                          "Liberty_FUSION_Vestas-4200-150_GBX_",
                          "Liberty_FUSION_Vestas-4200-150_GEN_",
                          "Liberty_FUSION_Vestas-4200-150_MS-BRG-RS_",
                          "Liberty_FUSION_Goldwind-1500-82_GEN_",
                          "Liberty_FUSION_Goldwind-2500-100_GEN_",
                          "Liberty_FUSION_Siemens-2300-113_GEN_",
                          "Liberty_FUSION_Siemens-2772-113_GEN_",
                          "Liberty_FUSION_Siemens-2942-113_GEN_",
                          "Liberty_FUSION_Enercon-2300-92_GEN_",
                          "Liberty_FUSION_Enercon-2300-92_MS-BRG-RS_",
                          "Liberty_FUSION_Enercon-2300-92_MS-BRG-GS_",
                          "Liberty_FUSION_Enercon-4000-126_GEN_",
                          "Liberty_FUSION_Enercon-4000-126_MS-BRG-RS_",
                          "Liberty_FUSION_Enercon-4000-126_MS-BRG-GS_"
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
