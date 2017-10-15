# What are the total amount of sales contained in this data set?
#
# Which city had the highest sales in February?
#
# Out of the entire data set, what is the total amount of money
#  people have paid in cash?
#
# What is the most popular payment type in Oakland in March?
#
# How many sales were made on 4/20, and which city had the highest sales value?
#
# What is the average sales amount for credit card purchases?
#
# How many purchases were made by bartering with baseball cards?



def import_data():
    with open("sales_data.txt", 'r') as f:
        sales_data = list(f.readlines())
        f.close()

        cleaned_data = []

        for i in sales_data:
            cleaned_line = i.replace("\n",'').replace('$', '')
            cleaned_line = cleaned_line.split('\t')
            cleaned_line[3] = float(cleaned_line[3])
            cleaned_data.append(cleaned_line)
        return cleaned_data

cleaned_data = import_data()
all_phillie_sales = [i for i in cleaned_data if i[0] == 'Philadelphia']
total_sales = sum([i[3] for i in cleaned_data])

print total_sales

# def total_money():
#     # total_list = []
#     #
#     # for i in clean_data:
#     #     for j in i:
#     #         if '$' in j:
#     #             total_list.append(j.replace("$", ''))
#
#     total_money = 0
#
#     for i in clean_data:
#         total_money += float(i)
#
#     print(total_money)
#
#
#
#
#
# import_data()
# total_money()
