def read_csv(file_name):
    f = open(file_name)
    data = f.read()
    string_list = data.split("\n")[1:]
    string_fields = []
    final_list = []

    for row in string_list:
        string_fields = row.split(',')
        int_fields = []
        for item in string_fields:
            int_fields.append(int(item))

        final_list.append(int_fields)
        #print(final_list)

    return final_list

#US_births_1994-2003_CDC_NCHS.csv
cdc_list = read_csv("births.csv")
for item in range(0,10):
    print(cdc_list[item])
