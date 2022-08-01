import csv
import json
from collections import OrderedDict

import pandas as pd


def write_catalog_data_to_csv(metadata, catalogdata):
    col_names = ['Catalog Name', 'Catalog Info', 'Released Under', 'Contributor',
                 'Keywords', 'Group', 'Sectors', 'Catalog Published On', 'Catalog Updated On', 'Domain',
                 'CDO Name', 'CDO Post','Ministry/State/Department', 'Phone', 'Email', 'Address',
                 'Resource', 'NID', 'File Size', 'Downloads', 'Granularity', 'Resource Published On',
                 'Resource Updated On', 'Reference URL', 'Sourced webservices/APIs', 'Note']
    with open('data.csv', 'a', newline='') as out:
        csv_out = csv.writer(out)
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


def write_metadata_to_csv(data: dict):
    # print(data.keys)
    with open("data.csv", 'a', newline='') as f:
        # Using dictionary keys as fieldnames for the CSV file header
        writer = csv.DictWriter(f, data.keys())
        writer.writeheader()
        writer.writerow(data)


def write_data_to_csv(data: tuple):
    for i in data:
        print(i)
        # if(isinstance(i, dict)):
        #     write_metadata_to_csv(i)
        # else:
        #     write_catalog_data_to_csv(i)


metadata_dict = OrderedDict().update({
    "Catalog Name": "",
    "Catalog Info": "",
    "Released Under": "",
    "Contributor": "",
    "Keywords": "",
    "Group": "",
    "Sectors": "",
    "Published On": "",
    "Updated On": "",
    "Domain": "",
    "CDO Name": "",
    "CDO Post": "",
    "Ministry/State/Department": "",
    "Phone": "",
    "Email": "",
    "Address": "",
})

metadata_dict = {'Catalog Name': 'One Nation One Ration Card (ONORC) Plan',
            'Catalog Info': 'The catalog contains portability transactions data under One Nation One Ration Card (ONORC) plan.',
            'Released Under': 'National Data Sharing and Accessibility Policy (NDSAP)',
            'Contributor': ['Ministry of Consumer Affairs, Food and Public Distribution',
                            'Department of Food and Public Distribution'],
            'Keywords': ['ONORC', 'PDS'], 'Group': ['ONORC'],
            'Sectors': ['Food'],
            'Published On': ' 11-05-2022 ',
            'Updated On': ' 29/07/2022 ',
            'Domain': ' Open Government Data (OGD) Platform India ',
            'CDO Name': 'Shri S. Jagannathan', 'CDO Post': ('Joint Secretary',),
            'Ministry/State/Department': 'Ministry of Consumer Affairs, Food and Public Distribution ,Department of Food and Public Distribution',
            'Phone': ('23382956',), 'Email': ('jspd [dot] fpd [at] nic.in',),
            'Address': 'Room No. 183-A, Krishi Bhawan, New Delhi'}

catalog_data = {('Variety-wise Daily Market Prices Data of Ashgourd for 2015', '209583', '3.9 MB',
                 '199', 'NA', '26/02/2015', '10/06/2015', 'There is no Reference URL for this resource.', (
                     'Variety-wise Daily Market Price',
                     'https://data.gov.in/datasets_webservices/datasets/3670701'),
                 'Note for this resource is not available.'), (
                    'Variety-wise Daily Market Prices Data of Barley (Jau) for 2017', '4253381', '4.5 MB', '23',
                    'NA', '09/02/2018', '20/02/2018', 'There is no Reference URL for this resource.', (
                        'Variety-wise Daily Market Price',
                        'https://data.gov.in/datasets_webservices/datasets/3670701'),
                    'Note for this resource is not available.'), (
                    'Variety-wise Daily Market Prices Data of Ashgourd for 2007', '92330', '354 KB', '63',
                    'Daily', '24/05/2013', '17/04/2014', 'There is no Reference URL for this resource.', (
                        'Variety-wise Daily Market Price',
                        'https://data.gov.in/datasets_webservices/datasets/3670701'),
                    'This dataset is published in the Data Portal India by consuming Web Services exposed by AGMARKNET.'),
                ('Variety-wise Daily Market Prices of Banana - Green 2019', '6673492', '2.0 MB', '47',
                 'Daily', '08/08/2019', '08/08/2019', 'There is no Reference URL for this resource.', (
                     'Variety-wise Daily Market Price',
                     'https://data.gov.in/datasets_webservices/datasets/3670701'),
                 'Note for this resource is not available.'), (
                    'Financial progress under Jal Jeevan Mission (JJM) - block Siddipet Rural for district Siddipet, Telangana as on date',
                    '7112619', 'NA', '1', 'Daily', '31/05/2022', '31/05/2022',
                    'There is no Reference URL for this resource.', (
                        'Financial progress under Jal Jeevan Mission (JJM)',
                        'https://data.gov.in/datasets_webservices/datasets/7078830'),
                    'Note for this resource is not available.'), (
                    'Building Plan Applications at Surat Municipal Corporation from April 2015 onward (daily)',
                    '3786941', '23 KB', '133', 'Daily', '21/09/2017', '29/07/2022',
                    'There is no Reference URL for this resource.', (
                        'Building Plan Applications at Surat Municipal Corporation from April 2015 onward (daily)',
                        'https://data.gov.in/datasets_webservices/datasets/4206721'),
                    'The resource contains data set for Building Plan Approval and Building Usage permission data from April 2015 onward at Surat Municipal Corporation'),
                ('Variety-wise Daily Market Prices Data of Banana - Green for 2011', '92380', '3.1 MB', '75',
                 'Daily', '24/05/2013', '17/04/2014', 'There is no Reference URL for this resource.', (
                     'Variety-wise Daily Market Price',
                     'https://data.gov.in/datasets_webservices/datasets/3670701'),
                 'This dataset is published in the Data Portal India by consuming Web Services exposed by AGMARKNET.'),
                ('Variety-wise Daily Market Prices Data of Banana - Green for 2003', '92372', '672 KB', '88',
                 'Daily', '24/05/2013', '17/04/2014', 'There is no Reference URL for this resource.', (
                     'Variety-wise Daily Market Price',
                     'https://data.gov.in/datasets_webservices/datasets/3670701'),
                 'This dataset is published in the Data Portal India by consuming Web Services exposed by AGMARKNET.'),
                ('Variety-wise Daily Market Prices Data of Banana - Green for 2007', '92376', '1.9 MB', '94',
                 'Daily', '24/05/2013', '17/04/2014', 'There is no Reference URL for this resource.', (
                     'Variety-wise Daily Market Price',
                     'https://data.gov.in/datasets_webservices/datasets/3670701'),
                 'This dataset is published in the Data Portal India by consuming Web Services exposed by AGMARKNET.'),
                ('Garbage Collection in Surat City (in KG) from April 2015 onward (daily)', '3786981',
                 '20 KB', '195', 'Daily', '21/09/2017', '29/07/2022',
                 'There is no Reference URL for this resource.', (
                     'Garbage Collection in Surat City (in KG) from April 2015 onward (daily)',
                     'https://data.gov.in/datasets_webservices/datasets/4206761'),
                 'The catalog contains data set of Garbage Collection in Surat City from April 2015 onward.'),
                (
                    'Financial progress under Jal Jeevan Mission (JJM) - block Chinthlapalem for district Suryapet, Telangana as on date',
                    '7112622', 'NA', '1', 'Daily', '31/05/2022', '31/05/2022',
                    'There is no Reference URL for this resource.', (
                        'Financial progress under Jal Jeevan Mission (JJM)',
                        'https://data.gov.in/datasets_webservices/datasets/7078830'),
                    'Note for this resource is not available.'), (
                    'Variety-wise Daily Market Prices Data of Banana - Green for 2016', '962001', '7.8 MB', '79',
                    'NA', '16/08/2016', '16/08/2016', 'There is no Reference URL for this resource.', (
                        'Variety-wise Daily Market Price',
                        'https://data.gov.in/datasets_webservices/datasets/3670701'),
                    'Note for this resource is not available.'), (
                    'Variety-wise Daily Market Prices Data of Cluster beans for 2016', '963021', '2.8 MB', '52',
                    'NA', '16/08/2016', '16/08/2016', 'There is no Reference URL for this resource.', (
                        'Variety-wise Daily Market Price',
                        'https://data.gov.in/datasets_webservices/datasets/3670701'),
                    'Note for this resource is not available.'), (
                    'Financial progress under Jal Jeevan Mission (JJM) - block Nyoma for district Leh (ladakh), Ladakh as on date',
                    '7112626', 'NA', '1', 'Daily', '31/05/2022', '31/05/2022',
                    'There is no Reference URL for this resource.', (
                        'Financial progress under Jal Jeevan Mission (JJM)',
                        'https://data.gov.in/datasets_webservices/datasets/7078830'),
                    'Note for this resource is not available.'), (
                    'Variety-wise Daily Market Prices Data of Cluster beans for 2010', '92700', '936 KB', '50',
                    'Daily', '24/05/2013', '17/04/2014', 'There is no Reference URL for this resource.', (
                        'Variety-wise Daily Market Price',
                        'https://data.gov.in/datasets_webservices/datasets/3670701'),
                    'This dataset is published in the Data Portal India by consuming Web Services exposed by AGMARKNET.'),
                (
                    'Financial progress under Jal Jeevan Mission (JJM) - block Garidepally for district Suryapet, Telangana as on date',
                    '7112620', 'NA', '3', 'Daily', '31/05/2022', '31/05/2022',
                    'There is no Reference URL for this resource.', (
                        'Financial progress under Jal Jeevan Mission (JJM)',
                        'https://data.gov.in/datasets_webservices/datasets/7078830'),
                    'Note for this resource is not available.'), (
                    'Variety-wise Daily Market Prices Data of Barley (Jau) for 2004', '92386', '2.2 MB', '142',
                    'Daily', '24/05/2013', '17/04/2014', 'There is no Reference URL for this resource.', (
                        'Variety-wise Daily Market Price',
                        'https://data.gov.in/datasets_webservices/datasets/3670701'),
                    'This dataset is published in the Data Portal India by consuming Web Services exposed by AGMARKNET.'),
                (
                    'Financial progress under Jal Jeevan Mission (JJM) - block Srirampoor for district Peddapalli, Telangana as on date',
                    '7112615', 'NA', '1', 'Daily', '31/05/2022', '31/05/2022',
                    'There is no Reference URL for this resource.', (
                        'Financial progress under Jal Jeevan Mission (JJM)',
                        'https://data.gov.in/datasets_webservices/datasets/7078830'),
                    'Note for this resource is not available.'), (
                    'Variety-wise Daily Market Prices Data of Barley (Jau) for 2014', '97051', '6.0 MB', '251',
                    'Daily', '21/03/2014', '17/04/2014', 'There is no Reference URL for this resource.', (
                        'Variety-wise Daily Market Price',
                        'https://data.gov.in/datasets_webservices/datasets/3670701'),
                    'Note for this resource is not available.'), (
                    'Variety-wise Daily Market Prices Data of Apple for 2009', '92291', 'NA', '121', 'Daily',
                    '24/05/2013', '17/04/2014', 'There is no Reference URL for this resource.', (
                        'Variety-wise Daily Market Price',
                        'https://data.gov.in/datasets_webservices/datasets/3670701'),
                    'This dataset is published in the Data Portal India by consuming Web Services exposed by AGMARKNET.'),
                (
                    'Variety-wise Daily Market Prices of Cluster beans 2019', '6673533', '368 KB', '22', 'Daily',
                    '08/08/2019', '08/08/2019', 'There is no Reference URL for this resource.', (
                        'Variety-wise Daily Market Price',
                        'https://data.gov.in/datasets_webservices/datasets/3670701'),
                    'Note for this resource is not available.'), (
                    'Birth Registration & Birth Certificate Issuance at Surat Municipal Corporation from Year 2005 onwards',
                    '3786781', '68 KB', '116', 'Monthly', '20/09/2017', '29/07/2022',
                    'There is no Reference URL for this resource.', (
                        'Birth Registration & Birth Certificate Issuance at Surat Municipal Corporation from Year 2005 onwards',
                        'https://data.gov.in/datasets_webservices/datasets/4206621'),
                    'This data set provides count of male and female birth registration and birth certificate issued at Surat Municipal Corporation. The data is available from Year 2005.'),
                (
                    'Financial progress under Jal Jeevan Mission (JJM) - block Bhimbat Drass for district Kargil, Ladakh as on date',
                    '7112628', 'NA', '6', 'Daily', '31/05/2022', '31/05/2022',
                    'There is no Reference URL for this resource.', (
                        'Financial progress under Jal Jeevan Mission (JJM)',
                        'https://data.gov.in/datasets_webservices/datasets/7078830'),
                    'Note for this resource is not available.'), (
                    'Variety-wise Daily Market Prices Data of Apple for 2011', '92293', 'NA', '137', 'Daily',
                    '24/05/2013', '17/04/2014', 'There is no Reference URL for this resource.', (
                        'Variety-wise Daily Market Price',
                        'https://data.gov.in/datasets_webservices/datasets/3670701'),
                    'This dataset is published in the Data Portal India by consuming Web Services exposed by AGMARKNET.'),
                ('Zone & Ward-wise Property tax Demand and Recovery in Surat city from 2002 to 2017',
                 '3787461', '59 KB', '120', 'Annual', '21/09/2017', '21/09/2017',
                 'There is no Reference URL for this resource.', ('NA', 'No link available'),
                 'The resource contains data set related to Zone wise Ward wise Property Tax Demand and Recovery at Surat Municipal Corporation since Year 2002.'),
                ('Variety-wise Daily Market Prices Data of Apple for 2016', '961781', 'NA', '128', 'NA',
                 '16/08/2016', '16/08/2016', 'There is no Reference URL for this resource.', (
                     'Variety-wise Daily Market Price',
                     'https://data.gov.in/datasets_webservices/datasets/3670701'),
                 'Note for this resource is not available.'), (
                    'Water Charges Collection by Surat Municipal Corporation from April 2015 onward (daily)',
                    '3787201', '23 KB', '97', 'Daily', '21/09/2017', '29/07/2022',
                    'There is no Reference URL for this resource.', (
                        'Water Charges Collection by Surat Municipal Corporation from April 2015 onward (daily)',
                        'https://data.gov.in/datasets_webservices/datasets/4206781'),
                    'The resource contains data set contains details of Water Meter Charges collection by Surat Municipal Corporation from April 2015 onward.'),
                (
                    'Financial progress under Jal Jeevan Mission (JJM) - block Telkapally for district Nagarkurnool, Telangana as on date',
                    '7112613', 'NA', '1', 'Daily', '31/05/2022', '31/05/2022',
                    'There is no Reference URL for this resource.', (
                        'Financial progress under Jal Jeevan Mission (JJM)',
                        'https://data.gov.in/datasets_webservices/datasets/7078830'),
                    'Note for this resource is not available.'), (
                    'Variety-wise Daily Market Prices Data of Apple for 2006', '92288', 'NA', '181', 'Daily',
                    '24/05/2013', '17/04/2014', 'There is no Reference URL for this resource.', (
                        'Variety-wise Daily Market Price',
                        'https://data.gov.in/datasets_webservices/datasets/3670701'),
                    'This dataset is published in the Data Portal India by consuming Web Services exposed by AGMARKNET.'),
                ('Variety-wise Daily Market Prices of Ashgourd 2020', '6720073', '34 KB', '25', 'Daily',
                 '17/01/2020', '17/01/2020', 'There is no Reference URL for this resource.', (
                     'Variety-wise Daily Market Price',
                     'https://data.gov.in/datasets_webservices/datasets/3670701'),
                 'Note for this resource is not available.'), (
                    'Variety-wise Daily Market Prices Data of Barley (Jau) for 2001-2002', '92383', '715 KB',
                    '139', 'Daily', '29/05/2013', '17/04/2014', 'There is no Reference URL for this resource.', (
                        'Variety-wise Daily Market Price',
                        'https://data.gov.in/datasets_webservices/datasets/3670701'),
                    'This dataset is published in the Data Portal India by consuming Web Services exposed by AGMARKNET.'),
                ('Variety-wise Daily Market Prices Data of Cluster beans for 2011', '92701', '1.1 MB', '61',
                 'Daily', '24/05/2013', '17/04/2014', 'There is no Reference URL for this resource.', (
                     'Variety-wise Daily Market Price',
                     'https://data.gov.in/datasets_webservices/datasets/3670701'),
                 'This dataset is published in the Data Portal India by consuming Web Services exposed by AGMARKNET.'),
                ('Variety-wise Daily Market Prices of Barley (Jau) 2022', '6910040', '16 KB', '101', 'NA',
                 '07/01/2022', '29/07/2022', 'There is no Reference URL for this resource.',
                 ('NA', 'No link available'), 'Note for this resource is not available.'), (
                    'Variety-wise Daily Market Prices of Ashgourd 2019', '6673486', '619 KB', '28', 'Daily',
                    '08/08/2019', '08/08/2019', 'There is no Reference URL for this resource.', (
                        'Variety-wise Daily Market Price',
                        'https://data.gov.in/datasets_webservices/datasets/3670701'),
                    'Note for this resource is not available.'), (
                    'Variety-wise Daily Market Prices of Banana - Green 2022', '6910039', '53 KB', '199', 'NA',
                    '07/01/2022', '29/07/2022', 'There is no Reference URL for this resource.',
                    ('NA', 'No link available'), 'Note for this resource is not available.'), (
                    'Variety-wise Daily Market Prices Data of Ashgourd for 2006', '92329', '351 KB', '77',
                    'Daily', '24/05/2013', '17/04/2014', 'There is no Reference URL for this resource.', (
                        'Variety-wise Daily Market Price',
                        'https://data.gov.in/datasets_webservices/datasets/3670701'),
                    'This dataset is published in the Data Portal India by consuming Web Services exposed by AGMARKNET.'),
                ('Variety-wise Daily Market Prices of Cluster beans 2021', '6854006', '82 KB', '18', 'Daily',
                 '25/02/2021', '25/02/2021', 'There is no Reference URL for this resource.', (
                     'Variety-wise Daily Market Price',
                     'https://data.gov.in/datasets_webservices/datasets/3670701'),
                 'Note for this resource is not available.'), (
                    'Variety-wise Daily Market Prices Data of Ashgourd for 2001-2002', '92324', '114 KB', '113',
                    'Daily', '29/05/2013', '17/04/2014', 'There is no Reference URL for this resource.', (
                        'Variety-wise Daily Market Price',
                        'https://data.gov.in/datasets_webservices/datasets/3670701'),
                    'This dataset is published in the Data Portal India by consuming Web Services exposed by AGMARKNET.'),
                ('Variety-wise Daily Market Prices Data of Ashgourd for 2014', '97046', '3.9 MB', '273',
                 'Daily', '21/03/2014', '17/04/2014', 'There is no Reference URL for this resource.', (
                     'Variety-wise Daily Market Price',
                     'https://data.gov.in/datasets_webservices/datasets/3670701'),
                 'Note for this resource is not available.'), (
                    'Surat City Complaint Statistics from April 2015 onward (daily)', '3786961', '27 KB', '130',
                    'Daily', '21/09/2017', '29/07/2022', 'There is no Reference URL for this resource.', (
                        'Surat City Complaint Statistics from April 2015 onward (daily)',
                        'https://data.gov.in/datasets_webservices/datasets/4206821'),
                    'The catalog contains data set for Complaint statistics covering number of complaints received, resolved and pending on a particular day. The data is made available from April 2015 onward.'),
                (
                    'Financial progress under Jal Jeevan Mission (JJM) - block Bhiknoor for district Kamareddy, Telangana as on date',
                    '7112610', 'NA', '0', 'Daily', '31/05/2022', '31/05/2022',
                    'There is no Reference URL for this resource.', (
                        'Financial progress under Jal Jeevan Mission (JJM)',
                        'https://data.gov.in/datasets_webservices/datasets/7078830'),
                    'Note for this resource is not available.'), (
                    'Auditorium-Party Plot-Community Hall Booking data owed by Surat Municipal Corporation from 1st April 2015 (Daily)',
                    '3786801', '35 KB', '49', 'Daily', '20/09/2017', '29/07/2022',
                    'There is no Reference URL for this resource.', (
                        'Auditorium-Party Plot-Community Hall Booking data owed by Surat Municipal Corporation from 1st April 2015 (Daily)',
                        'https://data.gov.in/datasets_webservices/datasets/4206741'),
                    'The Data set contains details of bookings done for Community Halls, Party Plots and Auditoriums owed by Surat Municipal Corporation. Daily booking count and booking amount is provided from 01.04.2015 onward.'),
                ('Variety-wise Daily Market Prices of Barley (Jau) 2021', '6853973', '178 KB', '22', 'Daily',
                 '25/02/2021', '25/02/2021', 'There is no Reference URL for this resource.', (
                     'Variety-wise Daily Market Price',
                     'https://data.gov.in/datasets_webservices/datasets/3670701'),
                 'Note for this resource is not available.'), (
                    'Financial progress under Jal Jeevan Mission (JJM) - block Utkoor for district Narayanpet, Telangana as on date',
                    '7112624', 'NA', '0', 'Daily', '31/05/2022', '31/05/2022',
                    'There is no Reference URL for this resource.', (
                        'Financial progress under Jal Jeevan Mission (JJM)',
                        'https://data.gov.in/datasets_webservices/datasets/7078830'),
                    'Note for this resource is not available.'), (
                    'Zone-wise Property tax Demand and Recovery in Surat city from 2002 to 2017', '3787441',
                    '5.4 KB', '42', 'Annual', '21/09/2017', '21/09/2017',
                    'There is no Reference URL for this resource.', ('NA', 'No link available'),
                    'The resource contains data set of Property tax demand and recovery at Surat Municipal Corporation since Year 2002.'),
                ('Variety-wise Daily Market Prices Data of Ashgourd for 2008', '92331', '560 KB', '65',
                 'Daily', '24/05/2013', '17/04/2014', 'There is no Reference URL for this resource.', (
                     'Variety-wise Daily Market Price',
                     'https://data.gov.in/datasets_webservices/datasets/3670701'),
                 'This dataset is published in the Data Portal India by consuming Web Services exposed by AGMARKNET.'),
                (
                    'Financial progress under Jal Jeevan Mission (JJM) - block Narva for district Narayanpet, Telangana as on date',
                    '7112625', 'NA', '2', 'Daily', '31/05/2022', '31/05/2022',
                    'There is no Reference URL for this resource.', (
                        'Financial progress under Jal Jeevan Mission (JJM)',
                        'https://data.gov.in/datasets_webservices/datasets/7078830'),
                    'Note for this resource is not available.'), (
                    'Variety-wise Daily Market Prices Data of Ashgourd for 2016', '961861', '4.4 MB', '83', 'NA',
                    '16/08/2016', '16/08/2016', 'There is no Reference URL for this resource.', (
                        'Variety-wise Daily Market Price',
                        'https://data.gov.in/datasets_webservices/datasets/3670701'),
                    'Note for this resource is not available.'), (
                    'Variety-wise Daily Market Prices of Apple 2020', '6720070', '200 KB', '100', 'Daily',
                    '17/01/2020', '17/01/2020', 'There is no Reference URL for this resource.', (
                        'Variety-wise Daily Market Price',
                        'https://data.gov.in/datasets_webservices/datasets/3670701'),
                    'Note for this resource is not available.'), (
                    'Variety-wise Daily Market Prices Data of Apple for 2003', '92285', '4.6 MB', '153', 'Daily',
                    '24/05/2013', '17/04/2014', 'There is no Reference URL for this resource.', (
                        'Variety-wise Daily Market Price',
                        'https://data.gov.in/datasets_webservices/datasets/3670701'),
                    'This dataset is published in the Data Portal India by consuming Web Services exposed by AGMARKNET.'),
                (
                    'Financial progress under Jal Jeevan Mission (JJM) - block Undavelli for district Jogulamba Gadwal, Telangana as on date',
                    '7112609', 'NA', '0', 'Daily', '31/05/2022', '31/05/2022',
                    'There is no Reference URL for this resource.', (
                        'Financial progress under Jal Jeevan Mission (JJM)',
                        'https://data.gov.in/datasets_webservices/datasets/7078830'),
                    'Note for this resource is not available.'), (
                    'Variety-wise Daily Market Prices Data of Banana - Green for 2008', '92377', '2.0 MB', '90',
                    'Daily', '24/05/2013', '17/04/2014', 'There is no Reference URL for this resource.', (
                        'Variety-wise Daily Market Price',
                        'https://data.gov.in/datasets_webservices/datasets/3670701'),
                    'This dataset is published in the Data Portal India by consuming Web Services exposed by AGMARKNET.'),
                ('Variety-wise Daily Market Prices Data of Ashgourd for 2018', '6621842', '4.7 MB', '36',
                 'NA', '28/03/2019', '28/03/2019', 'There is no Reference URL for this resource.', (
                     'Variety-wise Daily Market Price',
                     'https://data.gov.in/datasets_webservices/datasets/3670701'),
                 'Note for this resource is not available.'), (
                    'Variety-wise Daily Market Prices of Apple 2019', '6673483', '3.0 MB', '69', 'Daily',
                    '08/08/2019', '08/08/2019', 'There is no Reference URL for this resource.', (
                        'Variety-wise Daily Market Price',
                        'https://data.gov.in/datasets_webservices/datasets/3670701'),
                    'Note for this resource is not available.'), (
                    'Variety-wise Daily Market Prices Data of Cluster beans for 2008', '92698', '1.9 MB', '52',
                    'Daily', '24/05/2013', '17/04/2014', 'There is no Reference URL for this resource.', (
                        'Variety-wise Daily Market Price',
                        'https://data.gov.in/datasets_webservices/datasets/3670701'),
                    'This dataset is published in the Data Portal India by consuming Web Services exposed by AGMARKNET.'),
                ('Details of Vehicle Tax collected by Surat Municipal Corporation from Year 1989 onward',
                 '3787161', '11 KB', '555', 'Monthly', '21/09/2017', '29/07/2022',
                 'There is no Reference URL for this resource.', (
                     'Details of Vehicle Tax collected by Surat Municipal Corporation from Year 1989 onward',
                     'https://data.gov.in/datasets_webservices/datasets/4206681'),
                 'The resource contains data set for summary of Vehicle Tax collected by Surat Municipal Corporation from year 1989 onward.'),
                (
                    'Financial progress under Jal Jeevan Mission (JJM) - block Jarasangam for district Sangareddy, Telangana as on date',
                    '7112618', 'NA', '1', 'Daily', '31/05/2022', '31/05/2022',
                    'There is no Reference URL for this resource.', (
                        'Financial progress under Jal Jeevan Mission (JJM)',
                        'https://data.gov.in/datasets_webservices/datasets/7078830'),
                    'Note for this resource is not available.'), (
                    'Variety-wise Daily Market Prices Data of Barley (Jau) for 2005', '92387', '2.4 MB', '84',
                    'Daily', '24/05/2013', '17/04/2014', 'There is no Reference URL for this resource.', (
                        'Variety-wise Daily Market Price',
                        'https://data.gov.in/datasets_webservices/datasets/3670701'),
                    'This dataset is published in the Data Portal India by consuming Web Services exposed by AGMARKNET.'),
                ('Variety-wise Daily Market Prices Data of Cluster beans for 2006', '92696', '1.3 MB', '60',
                 'Daily', '24/05/2013', '17/04/2014', 'There is no Reference URL for this resource.', (
                     'Variety-wise Daily Market Price',
                     'https://data.gov.in/datasets_webservices/datasets/3670701'),
                 'This dataset is published in the Data Portal India by consuming Web Services exposed by AGMARKNET.'),
                (
                    'Current Daily Price of Various Commodities from Various Markets (Mandi)', '86943', '951 KB',
                    '26,544', 'Daily', '23/05/2013', '29/07/2022',
                    'There is no Reference URL for this resource.', (
                        'Current Daily Price of Various Commodities from Various Markets (Mandis)',
                        'https://data.gov.in/datasets_webservices/datasets/6622308'),
                    'Note for this resource is not available.'), (
                    'Variety-wise Daily Market Prices Data of Ashgourd for 2004', '92327', '121 KB', '117',
                    'Daily', '24/05/2013', '17/04/2014', 'There is no Reference URL for this resource.', (
                        'Variety-wise Daily Market Price',
                        'https://data.gov.in/datasets_webservices/datasets/3670701'),
                    'This dataset is published in the Data Portal India by consuming Web Services exposed by AGMARKNET.'),
                ('Variety-wise Daily Market Prices Data of Barley (Jau) for 2007', '92389', 'NA', '77',
                 'Daily', '24/05/2013', '17/04/2014', 'There is no Reference URL for this resource.', (
                     'Variety-wise Daily Market Price',
                     'https://data.gov.in/datasets_webservices/datasets/3670701'),
                 'This dataset is published in the Data Portal India by consuming Web Services exposed by AGMARKNET.'),
                ('Variety-wise Daily Market Prices Data of Ashgourd for 2005', '92328', '244 KB', '101',
                 'Daily', '24/05/2013', '17/04/2014', 'There is no Reference URL for this resource.', (
                     'Variety-wise Daily Market Price',
                     'https://data.gov.in/datasets_webservices/datasets/3670701'),
                 'This dataset is published in the Data Portal India by consuming Web Services exposed by AGMARKNET.'),
                (
                    'Financial progress under Jal Jeevan Mission (JJM) - block Addagudur for district Yadadri Bhongiri, Telangana as on date',
                    '7112623', 'NA', '1', 'Daily', '31/05/2022', '31/05/2022',
                    'There is no Reference URL for this resource.', (
                        'Financial progress under Jal Jeevan Mission (JJM)',
                        'https://data.gov.in/datasets_webservices/datasets/7078830'),
                    'Note for this resource is not available.'), (
                    'Variety-wise Daily Market Prices Data of Barley (Jau) for 2003', '92385', '2.6 MB', '88',
                    'Daily', '24/05/2013', '17/04/2014', 'There is no Reference URL for this resource.', (
                        'Variety-wise Daily Market Price',
                        'https://data.gov.in/datasets_webservices/datasets/3670701'),
                    'This dataset is published in the Data Portal India by consuming Web Services exposed by AGMARKNET.'),
                (
                    'Variety-wise Daily Market Prices Data of Banana - Green for 2014', '97050', '6.9 MB', '158',
                    'Daily', '21/03/2014', '17/04/2014', 'There is no Reference URL for this resource.', (
                        'Variety-wise Daily Market Price',
                        'https://data.gov.in/datasets_webservices/datasets/3670701'),
                    'Note for this resource is not available.'), (
                    'Variety-wise Daily Market Prices Data of Apple for 2008', '92290', 'NA', '134', 'Daily',
                    '24/05/2013', '17/04/2014', 'There is no Reference URL for this resource.', (
                        'Variety-wise Daily Market Price',
                        'https://data.gov.in/datasets_webservices/datasets/3670701'),
                    'This dataset is published in the Data Portal India by consuming Web Services exposed by AGMARKNET.'),
                ('Variety-wise Daily Market Prices Data of Banana - Green for 2009', '92378', '2.2 MB', '96',
                 'Daily', '24/05/2013', '17/04/2014', 'There is no Reference URL for this resource.', (
                     'Variety-wise Daily Market Price',
                     'https://data.gov.in/datasets_webservices/datasets/3670701'),
                 'This dataset is published in the Data Portal India by consuming Web Services exposed by AGMARKNET.'),
                ('Variety-wise Daily Market Prices Data of Apple for 2012', '92294', 'NA', '87', 'Daily',
                 '24/05/2013', '17/04/2014', 'There is no Reference URL for this resource.', (
                     'Variety-wise Daily Market Price',
                     'https://data.gov.in/datasets_webservices/datasets/3670701'),
                 'This dataset is published in the Data Portal India by consuming Web Services exposed by AGMARKNET.'),
                ('Variety-wise Daily Market Prices Data of Ashgourd for 2017', '4253241', '3.4 MB', '31',
                 'NA', '09/02/2018', '20/02/2018', 'There is no Reference URL for this resource.', (
                     'Variety-wise Daily Market Price',
                     'https://data.gov.in/datasets_webservices/datasets/3670701'),
                 'Note for this resource is not available.'), (
                    'Variety-wise Daily Market Prices Data of Cluster beans for 2003', '92693', '193 KB', '71',
                    'Daily', '24/05/2013', '17/04/2014', 'There is no Reference URL for this resource.', (
                        'Variety-wise Daily Market Price',
                        'https://data.gov.in/datasets_webservices/datasets/3670701'),
                    'This dataset is published in the Data Portal India by consuming Web Services exposed by AGMARKNET.'),
                (
                    'Variety-wise Daily Market Prices Data of Cluster beans for 2017', '4254181', '2.1 MB', '23',
                    'NA', '09/02/2018', '20/02/2018', 'There is no Reference URL for this resource.', (
                        'Variety-wise Daily Market Price',
                        'https://data.gov.in/datasets_webservices/datasets/3670701'),
                    'Note for this resource is not available.'), (
                    'Variety-wise Daily Market Prices of Banana - Green 2020', '6720079', '126 KB', '48',
                    'Daily', '17/01/2020', '17/01/2020', 'There is no Reference URL for this resource.', (
                        'Variety-wise Daily Market Price',
                        'https://data.gov.in/datasets_webservices/datasets/3670701'),
                    'Note for this resource is not available.'), (
                    'Variety-wise Daily Market Prices Data of Cluster beans for 2015', '210543', '297 KB', '110',
                    'NA', '26/02/2015', '09/06/2015', 'There is no Reference URL for this resource.', (
                        'Variety-wise Daily Market Price',
                        'https://data.gov.in/datasets_webservices/datasets/3670701'),
                    'Note for this resource is not available.'), (
                    'Variety-wise Daily Market Prices Data of Cluster beans for 2009', '92699', '1.2 MB', '87',
                    'Daily', '24/05/2013', '17/04/2014', 'There is no Reference URL for this resource.', (
                        'Variety-wise Daily Market Price',
                        'https://data.gov.in/datasets_webservices/datasets/3670701'),
                    'This dataset is published in the Data Portal India by consuming Web Services exposed by AGMARKNET.'),
                ('Variety-wise Daily Market Prices of Ashgourd 2021', '6853967', '145 KB', '24', 'Daily',
                 '25/02/2021', '25/02/2021', 'There is no Reference URL for this resource.', (
                     'Variety-wise Daily Market Price',
                     'https://data.gov.in/datasets_webservices/datasets/3670701'),
                 'Note for this resource is not available.'), (
                    'Financial progress under Jal Jeevan Mission (JJM) - block Odela for district Peddapalli, Telangana as on date',
                    '7112616', 'NA', '1', 'Daily', '31/05/2022', '31/05/2022',
                    'There is no Reference URL for this resource.', (
                        'Financial progress under Jal Jeevan Mission (JJM)',
                        'https://data.gov.in/datasets_webservices/datasets/7078830'),
                    'Note for this resource is not available.'), (
                    'Variety-wise Daily Market Prices Data of Apple for 2014', '97043', 'NA', '292', 'Daily',
                    '21/03/2014', '17/04/2014', 'There is no Reference URL for this resource.', (
                        'Variety-wise Daily Market Price',
                        'https://data.gov.in/datasets_webservices/datasets/3670701'),
                    'Note for this resource is not available.'), (
                    'Variety-wise Daily Market Prices Data of Banana - Green for 2018', '6621848', 'NA', '31',
                    'NA', '28/03/2019', '28/03/2019', 'There is no Reference URL for this resource.', (
                        'Variety-wise Daily Market Price',
                        'https://data.gov.in/datasets_webservices/datasets/3670701'),
                    'Note for this resource is not available.'), (
                    'Variety-wise Daily Market Prices Data of Apple for 2010', '92292', 'NA', '128', 'Daily',
                    '24/05/2013', '17/04/2014', 'There is no Reference URL for this resource.', (
                        'Variety-wise Daily Market Price',
                        'https://data.gov.in/datasets_webservices/datasets/3670701'),
                    'This dataset is published in the Data Portal India by consuming Web Services exposed by AGMARKNET.'),
                ('Variety-wise Daily Market Prices Data of Apple for 2007', '92289', 'NA', '131', 'Daily',
                 '24/05/2013', '17/04/2014', 'There is no Reference URL for this resource.', (
                     'Variety-wise Daily Market Price',
                     'https://data.gov.in/datasets_webservices/datasets/3670701'),
                 'This dataset is published in the Data Portal India by consuming Web Services exposed by AGMARKNET.'),
                ('Variety-wise Daily Market Prices of Barley (Jau) 2019', '6673493', '1.2 MB', '32', 'Daily',
                 '08/08/2019', '08/08/2019', 'There is no Reference URL for this resource.', (
                     'Variety-wise Daily Market Price',
                     'https://data.gov.in/datasets_webservices/datasets/3670701'),
                 'Note for this resource is not available.'), (
                    'Variety-wise Daily Market Prices Data of Cluster beans for 2018', '6621890', '2.9 MB', '18',
                    'NA', '28/03/2019', '28/03/2019', 'There is no Reference URL for this resource.', (
                        'Variety-wise Daily Market Price',
                        'https://data.gov.in/datasets_webservices/datasets/3670701'),
                    'Note for this resource is not available.'), (
                    'Variety-wise Daily Market Prices of Apple 2021', '6853965', '733 KB', '102', 'Daily',
                    '25/02/2021', '25/02/2021', 'There is no Reference URL for this resource.', (
                        'Variety-wise Daily Market Price',
                        'https://data.gov.in/datasets_webservices/datasets/3670701'),
                    'Note for this resource is not available.'), (
                    'Financial progress under Jal Jeevan Mission (JJM) - block Achampet for district Nagarkurnool, Telangana as on date',
                    '7112614', 'NA', '1', 'Daily', '31/05/2022', '31/05/2022',
                    'There is no Reference URL for this resource.', (
                        'Financial progress under Jal Jeevan Mission (JJM)',
                        'https://data.gov.in/datasets_webservices/datasets/7078830'),
                    'Note for this resource is not available.'), (
                    'Financial progress under Jal Jeevan Mission (JJM) - block Chuchot for district Leh (ladakh), Ladakh as on date',
                    '7112627', 'NA', '26', 'Daily', '31/05/2022', '31/05/2022',
                    'There is no Reference URL for this resource.', (
                        'Financial progress under Jal Jeevan Mission (JJM)',
                        'https://data.gov.in/datasets_webservices/datasets/7078830'),
                    'Note for this resource is not available.'), (
                    'Variety-wise Daily Market Prices Data of Banana - Green for 2012', '92381', '5.4 MB', '101',
                    'Daily', '24/05/2013', '17/04/2014', 'There is no Reference URL for this resource.', (
                        'Variety-wise Daily Market Price',
                        'https://data.gov.in/datasets_webservices/datasets/3670701'),
                    'This dataset is published in the Data Portal India by consuming Web Services exposed by AGMARKNET.'),
                ('Variety-wise Daily Market Prices of Cluster beans 2022', '6910068', '15 KB', '68', 'NA',
                 '07/01/2022', '29/07/2022', 'There is no Reference URL for this resource.',
                 ('NA', 'No link available'), 'Note for this resource is not available.'), (
                    'Variety-wise Daily Market Prices Data of Cluster beans for 2001-2002', '92691', '114 KB',
                    '78', 'Daily', '29/05/2013', '17/04/2014', 'There is no Reference URL for this resource.', (
                        'Variety-wise Daily Market Price',
                        'https://data.gov.in/datasets_webservices/datasets/3670701'),
                    'This dataset is published in the Data Portal India by consuming Web Services exposed by AGMARKNET.'),
                ('Marriage Registration at Surat Municipal Corporation from January 2008 onward', '3787001',
                 '26 KB', '268', 'Monthly', '21/09/2017', '29/07/2022',
                 'There is no Reference URL for this resource.', (
                     'Marriage Registration at Surat Municipal Corporation from January 2008 onward',
                     'https://data.gov.in/datasets_webservices/datasets/4206661'),
                 'The catalog contains data sets of Marriage Registration at Surat Municipal Corporation from January 2008 onward.'),
                ('Variety-wise Daily Market Prices Data of Ashgourd for 2010', '92333', '1.1 MB', '63',
                 'Daily', '24/05/2013', '17/04/2014', 'There is no Reference URL for this resource.', (
                     'Variety-wise Daily Market Price',
                     'https://data.gov.in/datasets_webservices/datasets/3670701'),
                 'This dataset is published in the Data Portal India by consuming Web Services exposed by AGMARKNET.'),
                ('Variety-wise Daily Market Prices Data of Apple for 2017', '4253181', 'NA', '50', 'NA',
                 '09/02/2018', '20/02/2018', 'There is no Reference URL for this resource.', (
                     'Variety-wise Daily Market Price',
                     'https://data.gov.in/datasets_webservices/datasets/3670701'),
                 'Note for this resource is not available.'), (
                    'Financial progress under Jal Jeevan Mission (JJM) - block Palakurthy for district Peddapalli, Telangana as on date',
                    '7112617', 'NA', '2', 'Daily', '31/05/2022', '31/05/2022',
                    'There is no Reference URL for this resource.', (
                        'Financial progress under Jal Jeevan Mission (JJM)',
                        'https://data.gov.in/datasets_webservices/datasets/7078830'),
                    'Note for this resource is not available.'), (
                    'Variety-wise Daily Market Prices Data of Apple for 2015', '209523', 'NA', '185', 'NA',
                    '26/02/2015', '10/06/2015', 'There is no Reference URL for this resource.', (
                        'Variety-wise Daily Market Price',
                        'https://data.gov.in/datasets_webservices/datasets/3670701'),
                    'Note for this resource is not available.'), (
                    'Financial progress under Jal Jeevan Mission (JJM) - block Mellacheruvu for district Suryapet, Telangana as on date',
                    '7112621', 'NA', '1', 'Daily', '31/05/2022', '31/05/2022',
                    'There is no Reference URL for this resource.', (
                        'Financial progress under Jal Jeevan Mission (JJM)',
                        'https://data.gov.in/datasets_webservices/datasets/7078830'),
                    'Note for this resource is not available.'), (
                    'Death Registration & Death Certificate Issuance at Surat Municipal Corporation from Year 1989 onward',
                    '3786921', '267 KB', '108', 'Monthly', '21/09/2017', '29/07/2022',
                    'There is no Reference URL for this resource.', (
                        'Death Registration & Death Certificate Issuance at Surat Municipal Corporation from Year 1989 onward',
                        'https://data.gov.in/datasets_webservices/datasets/4206641'),
                    'The resource contains data set of number of death registration death certificate issued at Surat Municipal Corporation from year 1989 onward.'),
                ('Water Supplied in Surat city (in MLD) from April 2015 onward (daily)', '3787181', '17 KB',
                 '175', 'Daily', '21/09/2017', '22/09/2017', 'There is no Reference URL for this resource.',
                 ('Water Supplied in Surat city (in MLD) from April 2015 onward (daily)',
                  'https://data.gov.in/datasets_webservices/datasets/4206801'),
                 'The resource contains data set for Water Supplied in Surat City (in MLD) from April 2015 onward.'),
                ('Variety-wise Daily Market Prices Data of Apple for 2018', '6621839', 'NA', '55', 'NA',
                 '28/03/2019', '28/03/2019', 'There is no Reference URL for this resource.', (
                     'Variety-wise Daily Market Price',
                     'https://data.gov.in/datasets_webservices/datasets/3670701'),
                 'Note for this resource is not available.'), (
                    'Surat City Bus and BRTS Passenger Information from April 2015 (daily)', '3787401', '18 KB',
                    '461', 'Daily', '21/09/2017', '29/07/2022', 'There is no Reference URL for this resource.', (
                        'Surat City Bus and BRTS Passenger Information from April 2015 (daily)',
                        'https://data.gov.in/datasets_webservices/datasets/4206701'),
                    'The resource contains the data set of passengers of BRTS and City Bus on a particular day with number of buses in operation at Surat.'),
                ('Variety-wise Daily Market Prices Data of Barley (Jau) for 2018', '6621849', '7.9 MB', '16',
                 'NA', '28/03/2019', '28/03/2019', 'There is no Reference URL for this resource.', (
                     'Variety-wise Daily Market Price',
                     'https://data.gov.in/datasets_webservices/datasets/3670701'),
                 'Note for this resource is not available.'), (
                    'Variety-wise Daily Market Prices Data of Banana - Green for 2001-2002', '92370', '153 KB',
                    '104', 'Daily', '29/05/2013', '17/04/2014', 'There is no Reference URL for this resource.', (
                        'Variety-wise Daily Market Price',
                        'https://data.gov.in/datasets_webservices/datasets/3670701'),
                    'This dataset is published in the Data Portal India by consuming Web Services exposed by AGMARKNET.'),
                ('Variety-wise Daily Market Prices of Apple 2022', '6910033', '94 KB', '282', 'NA',
                 '07/01/2022', '29/07/2022', 'There is no Reference URL for this resource.',
                 ('NA', 'No link available'), 'Note for this resource is not available.'), (
                    'Variety-wise Daily Market Prices Data of Cluster beans for 2005', '92695', '186 KB', '51',
                    'Daily', '24/05/2013', '17/04/2014', 'There is no Reference URL for this resource.', (
                        'Variety-wise Daily Market Price',
                        'https://data.gov.in/datasets_webservices/datasets/3670701'),
                    'This dataset is published in the Data Portal India by consuming Web Services exposed by AGMARKNET.'),
                ('Variety-wise Daily Market Prices Data of Banana - Green for 2004', '92373', '730 KB', '95',
                 'Daily', '24/05/2013', '17/04/2014', 'There is no Reference URL for this resource.', (
                     'Variety-wise Daily Market Price',
                     'https://data.gov.in/datasets_webservices/datasets/3670701'),
                 'This dataset is published in the Data Portal India by consuming Web Services exposed by AGMARKNET.'),
                ('Variety-wise Daily Market Prices Data of Ashgourd for 2003', '92326', '201 KB', '105',
                 'Daily', '24/05/2013', '17/04/2014', 'There is no Reference URL for this resource.', (
                     'Variety-wise Daily Market Price',
                     'https://data.gov.in/datasets_webservices/datasets/3670701'),
                 'This dataset is published in the Data Portal India by consuming Web Services exposed by AGMARKNET.'),
                ('Variety-wise Daily Market Prices Data of Banana - Green for 2017', '4253361', '6.2 MB',
                 '31', 'NA', '09/02/2018', '20/02/2018', 'There is no Reference URL for this resource.', (
                     'Variety-wise Daily Market Price',
                     'https://data.gov.in/datasets_webservices/datasets/3670701'),
                 'Note for this resource is not available.'), (
                    'Variety-wise Daily Market Prices of Barley (Jau) 2020', '6720080', '45 KB', '19', 'Daily',
                    '17/01/2020', '17/01/2020', 'There is no Reference URL for this resource.', (
                        'Variety-wise Daily Market Price',
                        'https://data.gov.in/datasets_webservices/datasets/3670701'),
                    'Note for this resource is not available.'), (
                    'Variety-wise Daily Market Prices Data of Banana - Green for 2015', '209663', '8.0 MB',
                    '137', 'NA', '26/02/2015', '10/06/2015', 'There is no Reference URL for this resource.', (
                        'Variety-wise Daily Market Price',
                        'https://data.gov.in/datasets_webservices/datasets/3670701'),
                    'Note for this resource is not available.'), (
                    'Variety-wise Daily Market Prices Data of Barley (Jau) for 2011', '92393', '6.3 MB', '74',
                    'Daily', '24/05/2013', '17/04/2014', 'There is no Reference URL for this resource.', (
                        'Variety-wise Daily Market Price',
                        'https://data.gov.in/datasets_webservices/datasets/3670701'),
                    'This dataset is published in the Data Portal India by consuming Web Services exposed by AGMARKNET.'),
                ('Variety-wise Daily Market Prices Data of Barley (Jau) for 2010', '92392', '5.8 MB', '80',
                 'Daily', '24/05/2013', '17/04/2014', 'There is no Reference URL for this resource.', (
                     'Variety-wise Daily Market Price',
                     'https://data.gov.in/datasets_webservices/datasets/3670701'),
                 'This dataset is published in the Data Portal India by consuming Web Services exposed by AGMARKNET.'),
                ('Variety-wise Daily Market Prices Data of Barley (Jau) for 2016', '962021', '4.2 MB', '106',
                 'NA', '16/08/2016', '16/08/2016', 'There is no Reference URL for this resource.', (
                     'Variety-wise Daily Market Price',
                     'https://data.gov.in/datasets_webservices/datasets/3670701'),
                 'Note for this resource is not available.'), (
                    'Variety-wise Daily Market Prices of Cluster beans 2020', '6720121', '16 KB', '23', 'Daily',
                    '17/01/2020', '17/01/2020', 'There is no Reference URL for this resource.', (
                        'Variety-wise Daily Market Price',
                        'https://data.gov.in/datasets_webservices/datasets/3670701'),
                    'Note for this resource is not available.'), (
                    'Variety-wise Daily Market Prices Data of Ashgourd for 2012', '92335', '2.9 MB', '80',
                    'Daily', '24/05/2013', '17/04/2014', 'There is no Reference URL for this resource.', (
                        'Variety-wise Daily Market Price',
                        'https://data.gov.in/datasets_webservices/datasets/3670701'),
                    'This dataset is published in the Data Portal India by consuming Web Services exposed by AGMARKNET.'),
                ('Variety-wise Daily Market Prices of Banana - Green 2021', '6853972', '499 KB', '82',
                 'Daily', '25/02/2021', '25/02/2021', 'There is no Reference URL for this resource.', (
                     'Variety-wise Daily Market Price',
                     'https://data.gov.in/datasets_webservices/datasets/3670701'),
                 'Note for this resource is not available.'), (
                    'Variety-wise Daily Market Prices of Ashgourd 2022', '6910035', '17 KB', '70', 'NA',
                    '07/01/2022', '29/07/2022', 'There is no Reference URL for this resource.',
                    ('NA', 'No link available'), 'Note for this resource is not available.'), (
                    'Variety-wise Daily Market Prices Data of Cluster beans for 2004', '92694', '143 KB', '74',
                    'Daily', '24/05/2013', '17/04/2014', 'There is no Reference URL for this resource.', (
                        'Variety-wise Daily Market Price',
                        'https://data.gov.in/datasets_webservices/datasets/3670701'),
                    'This dataset is published in the Data Portal India by consuming Web Services exposed by AGMARKNET.'),
                ('Variety-wise Daily Market Prices Data of Barley (Jau) for 2009', '92391', '6.6 MB', '69',
                 'Daily', '24/05/2013', '17/04/2014', 'There is no Reference URL for this resource.', (
                     'Variety-wise Daily Market Price',
                     'https://data.gov.in/datasets_webservices/datasets/3670701'),
                 'This dataset is published in the Data Portal India by consuming Web Services exposed by AGMARKNET.'),
                ('Variety-wise Daily Market Prices Data of Cluster beans for 2014', '97094', '2.6 MB', '146',
                 'Daily', '21/03/2014', '17/04/2014', 'There is no Reference URL for this resource.', (
                     'Variety-wise Daily Market Price',
                     'https://data.gov.in/datasets_webservices/datasets/3670701'),
                 'Note for this resource is not available.'), (
                    'Real time Air Quality Index from various locations', '804661', '17 KB', '12,361', 'Hourly',
                    '04/08/2016', '29/07/2022', 'https://cpcb.gov.in/', (
                        'Real time Air Quality Index from various locations',
                        'https://data.gov.in/datasets_webservices/datasets/3630781'),
                    'The real-time data as collected from the field instruments is displayed live without human intervention from CPCB. It is likely that the live data may display some errors or abnormal values. Any abnormal value may be due to any episode or instrumental error at any particular time.'),
                (
                    'Variety-wise Daily Market Prices Data of Banana - Green for 2010', '92379', '3.2 MB', '103',
                    'Daily', '24/05/2013', '17/04/2014', 'There is no Reference URL for this resource.', (
                        'Variety-wise Daily Market Price',
                        'https://data.gov.in/datasets_webservices/datasets/3670701'),
                    'This dataset is published in the Data Portal India by consuming Web Services exposed by AGMARKNET.'),
                ('Variety-wise Daily Market Prices Data of Apple for 2001-2002', '92283', '1.5 MB', '149',
                 'Daily', '29/05/2013', '17/04/2014', 'There is no Reference URL for this resource.', (
                     'Variety-wise Daily Market Price',
                     'https://data.gov.in/datasets_webservices/datasets/3670701'),
                 'This dataset is published in the Data Portal India by consuming Web Services exposed by AGMARKNET.'),
                ('Variety-wise Daily Market Prices Data of Barley (Jau) for 2015', '209683', '137 KB', '3',
                 'NA', '26/02/2015', '10/12/2021', 'There is no Reference URL for this resource.', (
                     'Variety-wise Daily Market Price',
                     'https://data.gov.in/datasets_webservices/datasets/3670701'),
                 'Note for this resource is not available.'), (
                    'Variety-wise Daily Market Prices Data of Barley (Jau) for 2006', '92388', '7.1 MB', '107',
                    'Daily', '24/05/2013', '17/04/2014', 'There is no Reference URL for this resource.', (
                        'Variety-wise Daily Market Price',
                        'https://data.gov.in/datasets_webservices/datasets/3670701'),
                    'This dataset is published in the Data Portal India by consuming Web Services exposed by AGMARKNET.')}

write_catalog_data_to_csv(metadata_dict, catalog_data)

# write_metadata_to_csv(metadata)
json_obj = json.dumps(metadata_dict)
print(json_obj)
print("#######", type(json_obj))

# write_data_to_csv({
#                    ('Variety-wise Daily Market Prices Data of Ashgourd for 2015',
#                     '209583', '3.9 MB', '199', 'NA', '26/02/2015',
#                     '10/06/2015', 'There is no Reference URL for this resource.')
#                     })
