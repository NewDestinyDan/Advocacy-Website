# %%
import pandas as pd
import tabula
from pathlib import Path


# %%
def get_dhs_data(dhs_df: pd.DataFrame) -> int:
    dhs_col_map = {
        'Category': 'category',
        'SINGLE_MEN':  'single_men',
        'SINGLE_WOMEN':  'single_women',
        'TOTAL_SINGLE_\rADULTS':  'total_single_adults',
        'FAMILIES\rWITH\rCHILDREN':  'families_with_children',
        'ADULT\rFAMILIES':  'adult_families',
        'TOTAL\rFAMILIES':  'total_families',
        'TOTAL_ADULT\rS IN FAMILIES':  'total_adults_in_families',
        'TOTAL\rCHILDREN':  'total_children',
        'DATA_PERIOD':  'data_period',
        }


    dhs_cols_to_keep = [
        'total_single_adults',
        'total_adults_in_families',
        'total_children',
        ]

    dhs_df = dhs_df.rename(dhs_col_map, axis=1)

    dhs_df = dhs_df.set_index('category')

    dhs_df = dhs_df.loc[dhs_df.index.str.contains('unduplicated persons'), dhs_cols_to_keep]

    result = int(dhs_df.sum().sum())

    return result


def get_hpd_data(hpd_df: pd.DataFrame) -> int:
    hpd_col_map = {
        'facility': 'facility',
        'Unnamed: 0': 'category',
        'Single Men': 'single_men',
        'Single\rWomen': 'single_women',
        'Total\rSingle\rAdults': 'total_single_adults',
        'Families\rwith\rChildren': 'families_with_children',
        'Adult\rFamilies': 'adult_families',
        'Total\rFamilies': 'total_families',
        'Total\rAdults': 'total_adults',
        'Total\rChildren': 'total_children',
        'Data_ Period': 'data_period',
    }

    hpd_df.columns = hpd_col_map.values()

    hpd_cols_to_keep = [
        'total_single_adults',
        'total_adults',
        'total_children',
    ]

    hpd_df = hpd_df.rename(hpd_col_map, axis=1)

    hpd_df = hpd_df.set_index('category')

    hpd_df = hpd_df.loc[hpd_df.index == 'Census Total', hpd_cols_to_keep]

    hpd_df.head()

    return round(hpd_df.sum().sum() * 1.05)



def get_hra_data(hra_df: pd.DataFrame) -> tuple[int, int]:
    hra_df.iloc[0, 0] = 'category'

    hra_df.columns = hra_df.iloc[0]
    hra_df = hra_df.drop(0)

    hra_col_map = {
        float('nan'): 'category',
        'single\rmen': 'single_men',
        'single\rwomen': 'single_women',
        'total single\radults': 'total_single_adults',
        'families with\rchildren': 'families_with_children',
        'adult families': 'adult_families',
        'total families': 'total_families',
        'total adults in\rfamilies': 'total_adults_in_families',
        'total\rchildren': 'total_children',
        'data_period': 'data_period',
    }

    hra_cols_to_keep = [
        'total_single_adults',
        'total_adults_in_families',
        'total_children',
    ]


    hra_df = hra_df.rename(hra_col_map, axis=1)

    hra_df = hra_df.set_index('category')

    hra_df = hra_df.loc[hra_df.index.str.contains('unduplicated persons'), hra_cols_to_keep]

    hra_df = hra_df.astype(int)

    hasa_result = hra_df[hra_df.index.str.contains('HASA')].sum().sum()

    dv_result = hra_df[hra_df.index.str.contains('domestic violence')].sum().sum()

    return hasa_result, dv_result



def get_dycd_data(dycd_df: pd.DataFrame) -> int:
    dycd_df.columns = [
        'category',
        'single_men',
        'single_men',
        'single_women',
        'total_single_adults',
        'total_single_adults',
        'families_with_children',
        'families_with_children',
        'adult_families',
        'total_families',
        'total_families',
        'total_adults_in_families',
        'total_adults_in_families',
        'total_children',
        'data_period',
        ]

    dycd_df = dycd_df.loc[:,~dycd_df.columns.duplicated(keep='last')]

    dycd_rows_to_keep = [3]

    dycd_cols_to_keep = [
        'total_single_adults',
        'total_adults_in_families',
        'total_children',
    ]

    dycd_df = dycd_df.loc[dycd_rows_to_keep, dycd_cols_to_keep]


    dycd_df = dycd_df.astype(int)

    result = dycd_df.sum().sum()

    return result



# %%

def get_data_from_pdf(path_to_pdf):
    dfs = tabula.read_pdf(path_to_pdf, pages='all') # The order of the tables in the PDF is DHS, HPD, HRA, DYCD

    dhs = get_dhs_data(dhs_df = dfs[0])
    hpd = get_hpd_data(hpd_df = dfs[1])
    hasa, dv = get_hra_data(hra_df = dfs[2])
    dycd = get_dycd_data(dycd_df = dfs[3])

    data_row = (dhs, dv, hasa, hpd, dycd)

    return data_row


get_data_from_pdf('../Data/LL37 PDFs/PDFs/2022.06 Local Law 37 Report.pdf')


# %%
path_to_pdfs = '../Data/LL37 PDFs/PDFs/'
pdf_path_list = Path(path_to_pdfs).glob('*.pdf')

rows = []

for pdf_path in pdf_path_list:
    year_dot_month = pdf_path.stem.split(' ')[0]
    year, month = year_dot_month.split('.')
    index_val = f'{year}-{month}-01'
    data_row = get_data_from_pdf(pdf_path)

    new_row = []
    new_row.append(index_val)
    new_row.extend(data_row)

    rows.append(new_row)


# df = pd.DataFrame(columns=[
#     'data_period',
#     'DHS Total Unique Count',
#     'HRA DV Total Unique Count',
#     'HRA HASA Total Unique Count',
#     'HPD Total Unique Count (105% Est.)',
#     'DYCD Total Unique Count'
#     ])

# %%
