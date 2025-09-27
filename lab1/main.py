from cpd_statistics import loan_statistics
from statistics_view import view_statistics_by_data

FILE_PATH = './resource/indicators_cpd.xlsx'
KEYS = ['Непродовольственные товары', 'Услуги']
GROWTH_RATE_LABLE = 'Темпы прироста (%)'
DATE_LABLE = 'Дата'

data = loan_statistics(FILE_PATH, KEYS)
view_statistics_by_data(data, KEYS, GROWTH_RATE_LABLE, DATE_LABLE, GROWTH_RATE_LABLE)
