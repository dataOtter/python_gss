import pandas as pd
import numpy as np
import csv
import bunch


def get_gss():
    gss_df = pd.read_csv('C:/Users/Maisha/Dropbox/MB_dev/Python/python_gss/Extract1_csv.csv')
    return gss_df


def get_gss_bunch1(target_column_name, target_names_list, description):
    data = get_gss()
    data_nd = data.as_matrix()
    target_labels = data[target_column_name]
    column_names = np.array(list(data))
    b = bunch.Bunch()

    b['data'] = data_nd
    b['target'] = target_labels
    b['target_names'] = target_names_list
    b['DESCR'] = description
    b['feature_names'] = column_names
    b['raw_pandas_frame'] = data

    return b


def print_bunch(the_bunch):
    print(the_bunch['data'])
    print(the_bunch['target'])
    print(the_bunch['target_names'])
    print(the_bunch['feature_names'])
    print(the_bunch['DESCR'])
    print(the_bunch['raw_pandas_frame'])

    #print(the_bunch)


def get_gss_happy():
    target_names = ['Not applicable', 'Very happy', 'Pretty happy', 'Not too happy', '', '', '', '', "Don't know", 'No answer']
    descr = "Whether or not the person was happy."
    the_bunch = get_gss_bunch1('happy', target_names, descr)

    return the_bunch



