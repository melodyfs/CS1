with open('sales_data.txt') as f:
    sales_data = list(f.readlines())
    no_space_data = []
    # list_to_strip = ['\n', '\t']
    # new_ = str(sales_data).strip(' \t\n\r')
    # new = map(str.strip, sales_data)

    for i in range(len(sales_data)):
        no_space_data.append(sales_data[i].strip('\n'))
    # for r in range(len(no_space_data)):
    #     no_tab_data.append(no_space_data[r].strip('\t'))



print new_
# print next_line
