import csv


def write_catalog_data_to_csv(metadata, catalogdata, col_names:list):
    """ Writes metadata and catalog data to a csv file. """
    with open("data.csv", "a+", newline="") as out:
        csv_out = csv.writer(out)
        file_content = out.read()
        print(file_content)
        if out.tell() == 0:
            csv_out.writerow(col_names)
        data = []
        for tuple_data in catalogdata:
            flat_list = []
            for value in list(metadata.values()):
                flat_list.append(value)
            for elem in tuple_data:
                flat_list.append(elem)
            data.append(flat_list)
        for row in data:
            csv_out.writerow(row)
