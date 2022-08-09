# %%
import requests
import PyPDF2
import io
import os
import pandas as pd
from sodapy import Socrata

# %%
def ll37_pdf_scraper():
    month_name_dict = {
        'January': '01',
        'February': '02',
        'March': '03',
        'April': '04',
        'May': '05',
        'June': '06',
        'July': '07',
        'August': '08',
        'September': '09',
        'October': '10',
        'November': '11',
        'December': '12'
    }

    r = requests.get('https://www1.nyc.gov/assets/operations/downloads/pdf/temporary_housing_report.pdf', stream=True)
    pdf_bytes = io.BytesIO(r.content)
    pdf_content = PyPDF2.PdfReader(pdf_bytes)

    for i in range(pdf_content.numPages):
        pageObj = pdf_content.getPage(i)
        text_to_find = 'DHSLocalLaw37reportfortheMonthof'
        lines = pageObj.extract_text()
        lines = lines.split('\n')
        for line in lines:
            line = line.replace(' ', '')
            if text_to_find in line:
                month_year = line[len(text_to_find):].strip()


    month, year = month_year[:len(month_year)-4], month_year[len(month_year)-4:]
    month = month_name_dict[month]


    file_name = f'../Data/LL37 PDFs/PDFs/{year}.{month} Local Law 37 Report.pdf'
    if not os.path.exists(file_name):
        with open(file_name, 'wb') as f:
            f.write(r.content)


ll37_pdf_scraper()


# %%

def ll37_get_open_data():
    pass

dhs_api_endpoint = 'https://data.cityofnewyork.us/resource/2mqz-v5im.json'
dhs_api_code = dhs_api_endpoint[-14:-5]

hra_api_endpoint = 'https://data.cityofnewyork.us/resource/e4ty-r26d.json'
hra_api_code = hra_api_endpoint[-14:-5]

hpd_api_endpoint = 'https://data.cityofnewyork.us/resource/mdht-5s6e.json'
hpd_api_code = hpd_api_endpoint[-14:-5]

dycd_api_endpoint = 'https://data.cityofnewyork.us/resource/2232-dj5q.json'
dycd_api_code = dycd_api_endpoint[-14:-5]

# %%
client = Socrata("data.cityofnewyork.us", None)


# %%
dhs_results = client.get(dhs_api_code, where="ll37_report_row_name LIKE '%Number of unduplicated persons%'")
hra_results = client.get(hra_api_code, where="category LIKE '%Number of unduplicated persons%'")
hpd_results = client.get(hpd_api_code, where="facility_indicator LIKE '%%'") # HPD doesn't report unduplicated persons
dycd_results = client.get(dycd_api_code, where="category LIKE '%unduplicated%DYCD-administered facilities'")


# %%
dhs_results_df = pd.DataFrame.from_records(dhs_results)

dhs_to_num_list = [
    'single_men',
    'single_women',
    'total_single_adults',
    'families_with_children',
    'adult_families',
    'total_families',
    'total_adults_in_families',
    'total_children',
    'data_period'
    ]

dhs_shelter_list = [
    'dhs-administered', 
    'safe', 
    'cj', 
    'veteran', 
    'stabilization'
    ]

dhs_shelter_rows = dhs_results_df['ll37_report_row_name'].str.lower().str.contains('|'.join(dhs_shelter_list))
dhs_results_df = dhs_results_df[dhs_shelter_rows]

dhs_singles_only = [item for item in dhs_shelter_list if item != 'dhs-administered']
dhs_nan_rows = dhs_results_df['ll37_report_row_name'].str.lower().str.contains('|'.join(dhs_singles_only))
dhs_nan_cols = ['families_with_children', 'adult_families', 'total_families', 'total_adults_in_families', 'total_children']
dhs_results_df.loc[dhs_nan_rows, dhs_nan_cols] = dhs_results_df.loc[dhs_nan_rows, dhs_nan_cols].fillna(0)

dhs_results_df[dhs_to_num_list] = dhs_results_df[dhs_to_num_list].astype('float')

dhs_results_df['data_period'] = pd.to_datetime(dhs_results_df['data_period'], format='%Y%m')

dhs_results_df = dhs_results_df.groupby('data_period').sum()

# Adding column suffixes
# dhs_suff_df = dhs_results_df.rename({col: col+'_dhs' for col in dhs_results_df.columns}, axis=1)

# %%
hra_results_df = pd.DataFrame.from_records(hra_results)

hra_to_num_list = [
    'adult_families',
    'families_children',
    'single_men',
    'single_women',
    'adults_families',
    'total_children',
    'total_families',
    'total_single_adults',
    # 'data_period'
    ]

# hra_results_df = hra_results_df.fillna(0)

hra_results_df[hra_to_num_list] = hra_results_df[hra_to_num_list].astype('float') # float to handle null values

hra_results_df['data_period'] = pd.to_datetime(hra_results_df['data_period'], format='%Y%m')

hra_results_df = hra_results_df.rename(
    {
    'families_children': 'families_with_children',
    'adults_families': 'total_adults_in_families'
    }, axis=1
)

hra_results_df['data_period'] = pd.to_datetime(hra_results_df['data_period'], format='%Y%m')

hra_dv_df = hra_results_df[hra_results_df['category'].str.contains('domestic violence')]
hra_hasa_df = hra_results_df[hra_results_df['category'].str.contains('HASA')]

hra_dv_df = hra_dv_df.dropna().groupby('data_period').sum()
hra_hasa_df = hra_hasa_df.dropna().groupby('data_period').sum()

# %%
hpd_results_df = pd.DataFrame.from_records(hpd_results)

hpd_to_num_list = [
    'single_men',
    'single_women',
    'total_single_adults',
    'families_with_children',
    'adult_families',
    'total_families',
    'total_adults',
    'total_children',
    # 'data_period'
]

# hpd_results_df = hpd_results_df.dropna()
hpd_results_df = hpd_results_df[~hpd_results_df['data_period'].isna()]

hpd_results_df[hpd_to_num_list] = hpd_results_df[hpd_to_num_list].astype('float')

hpd_results_df['data_period'] = pd.to_datetime(hpd_results_df['data_period'], format='%Y%m')

hpd_results_df = hpd_results_df.set_index('data_period')

hpd_results_df = hpd_results_df[hpd_results_df['facility_type'] == 'HPD Facilities Combined (Census Total)']

hpd_results_df = hpd_results_df.drop(['facility_type', 'facility_indicator'], axis=1)

# This needs to be verified
hpd_results_df = hpd_results_df.rename(
    {
    'total_adults': 'total_adults_in_families'
    }, axis=1
)

# Adding column suffixes
# hpd_suff_df = hpd_results_df.rename({col: col+'_hpd' for col in hpd_results_df.columns}, axis=1)


# %%
dycd_results_df = pd.DataFrame.from_records(dycd_results)

dycd_to_num_list = [
    # 'adult_families',
    'families_with_children',
    'single_men',
    'single_women',
    'total_adults_in_families',
    'total_children',
    'total_families',
    'total_single_adults',
    'data_period'
    ]

dycd_results_df[dycd_to_num_list] = dycd_results_df[dycd_to_num_list].astype('float')

dycd_results_df['data_period'] = pd.to_datetime(dycd_results_df['data_period'], format='%Y%m')

dycd_results_df = dycd_results_df.groupby('data_period').sum()



# %%

dhs_total = dhs_results_df[['total_single_adults', 'total_adults_in_families', 'total_children']].dropna().sum(axis=1)
hra_dv_total = hra_dv_df[['total_single_adults', 'total_adults_in_families', 'total_children']].dropna().sum(axis=1)
hra_hasa_total = hra_hasa_df[['total_single_adults', 'total_adults_in_families', 'total_children']].dropna().sum(axis=1)
hpd_total = hpd_results_df[['total_single_adults', 'total_adults_in_families', 'total_children']].dropna().sum(axis=1)
dycd_total = dycd_results_df[['total_single_adults', 'total_adults_in_families', 'total_children']].dropna().sum(axis=1)

dhs_total = dhs_total.rename('DHS Total Unique Count')
hra_dv_total = hra_dv_total.rename('HRA DV Total Unique Count')
hra_hasa_total = hra_hasa_total.rename('HRA HASA Total Unique Count')
hpd_total = hpd_total.rename('HPD Total Unique Count (105% Est.)')
dycd_total = dycd_total.rename('DYCD Total Unique Count')

hpd_total = round(hpd_total*1.05)



# %%
# shared_indices = set(dhs_results_df.index).intersection(
#     set(hra_dv_df.index).intersection(
#     set(hra_hasa_df.index).intersection(
#     set(hpd_results_df.index).intersection(
#     set(dycd_results_df.index)
#     ))))

df = pd.concat([dhs_total, hra_dv_total, hra_hasa_total, hpd_total, dycd_total], axis=1)
df = df.dropna()

df = df.astype('int')

# df.index = df.index.strftime('%Y/%m')

# df.index = df.index.rename('Data Period')


# %%
df.to_csv('../Data/Five System Total.csv')



# %%
