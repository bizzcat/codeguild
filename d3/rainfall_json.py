import final_rainfall as big_data

monthly_averages = big_data.monthly_averages

def get_monthly_avg_JSON(monthly_averages):
    JSON_text_list = []
    JSON_full_text = ''
    for month in monthly_averages:
        month_text = "\"" + str(month) + "\":\"" + str(monthly_averages[month]) + "\""
        JSON_text_list.append(month_text)
    JSON_full_text = "\'{\'" + '\',\''.join(JSON_text_list) + "\'}\'"
    return JSON_full_text


JSON_full_text = get_monthly_avg_JSON(monthly_averages)
print(JSON_full_text)

print(str(monthly_averages))


# clean_data_dict (day to day total)
# day_averages
# monthly_averages
# specific_monthly_totals
# specific_monthly_averages
# year_totals
# year_daily_averages
