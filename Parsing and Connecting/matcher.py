__author__ = 'gerson64'
import csv
import fuzzywuzzy
import struct
import pandas as pd
import shutil
import glob

import numpy as np
import matplotlib.pyplot as plt

regexTrainedFellows= r'(\w*)\s([A-Z]\.\s|[A-Z]\.[A-Z]\.\s|)(\w*)?\W\s.*'

fieldNames = ['npi','nppes_provider_last_org_name','nppes_provider_first_name',
              'nppes_provider_mi','nppes_credentials','nppes_provider_gender','nppes_entity_code',
              'nppes_provider_street1','nppes_provider_street2','nppes_provider_city','nppes_provider_zip',
              'nppes_provider_state','nppes_provider_country','provider_type','medicare_participation_indicator',
              'place_of_Service','hcpcs_code','hcpcs_description','line_srvc_cnt','bene_unique_cnt','bene_day_srvc_cnt',
              'average_Medicare_allowed_amt','stdev_Medicate_allowed_amt','average_submitted_chrg_amt',
              'stdev_submitted_chrg_amt','average_Medicare_payment_amt','stdev_Medicare_payment_amt']

for i in range(0, 13):
    fileName='E://medicare/splitfile/medicare_records'+str(i)+'.txt'

    medicare_dat = pd.read_csv(fileName, delimiter='\t' , low_memory=False)
    medicare_dat.columns= fieldNames
    #print(medicare_dat)
    name_df = medicare_dat[['npi','nppes_provider_first_name','nppes_provider_mi','nppes_provider_last_org_name','nppes_credentials']]
    name_df=name_df.drop_duplicates()
    print(name_df)


    loc_df = medicare_dat[['npi','nppes_provider_city','nppes_provider_state','nppes_provider_zip','nppes_provider_country']]
    loc_df = loc_df.drop_duplicates()

    print(loc_df)
    tot_df = medicare_dat[['npi','nppes_provider_first_name','nppes_provider_mi','nppes_provider_last_org_name','nppes_credentials','nppes_provider_city','nppes_provider_state','nppes_provider_zip','nppes_provider_country']]
    tot_df = tot_df.drop_duplicates()

    tot_df.to_csv(path_or_buf='E://medicare/distinct_npi/medicare_npi'+str(i)+'.txt', mode = 'w' , sep = '\t')

tot_names=['npi','nppes_provider_first_name','nppes_provider_mi','nppes_provider_last_org_name','nppes_credentials','nppes_provider_city','nppes_provider_state','nppes_provider_zip','nppes_provider_country']

outfilename='E://medicare/medicare_npi_all.txt'

with open(outfilename, 'wb') as outfile:
    for filename in glob.glob('E://medicare/distinct_npi/*.txt'):
        with open(filename, 'rb') as readfile:
            shutil.copyfileobj(readfile, outfile)

nonFellowfileName = open("C:/Users/gerson64/Desktop/Dropbox Sync/Dropbox/Github/DirectoryScraper/Directory_Out/NonFellow.csv", 'r')
nonFellowfileName.columns = ['nppes_provider_first_name','nppes_provider_mi','nppes_provider_last_org_name','nppes_provider_city','nppes_provider_state']
Medicarefilename='E://medicare/medicare_npi_all.txt'
medicare_dat = pd.read_csv(Medicarefilename, delimiter='\t' , low_memory=False)
medicare_dat.columns= tot_names


concat(objs, axis=0, join='inner', join_axes=None, ignore_index=False,
       keys=None, levels=None, names=None, verify_integrity=False)