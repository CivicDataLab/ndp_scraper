import csv


def write_catalog_data_to_csv(metadata, catalogdata):
    """ Writes metadata and catalog data to a csv file. """
    col_names = [
        "Catalog Name",
        "Catalog Info",
        "Released Under",
        "Contributor",
        "Keywords",
        "Group",
        "Sectors",
        "Catalog Published On",
        "Catalog Updated On",
        "Domain",
        "CDO Name",
        "CDO Post",
        "Ministry/State/Department",
        "Phone",
        "Email",
        "Address",
        "Resource",
        "NID",
        "File Size",
        "Downloads",
        "Granularity",
        "Resource Published On",
        "Resource Updated On",
        "Reference URL",
        "Sourced webservices/APIs",
        "Note"
    ]
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
