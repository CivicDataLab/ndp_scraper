header_dict = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "keep-alive",
    "Content-Type": "application/json;charset=UTF-8",
    "Cookie": "_ga=GA1.3.1806082847.1658141362; _gid=GA1.3.961707762.1658141362",
    "Origin": "https://data.gov.in",
    "Referer": "https://data.gov.in/catalog/xyz",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.62",
    "sec-ch-ua": '" Not;A Brand";v="99", "Microsoft Edge";v="103", "Chromium";v="103"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
}

# Change this accordingly while site gets updated
PAGES_TO_TRAVERSE_IN_SITE = 523

NID_XPATH = "//*[@id='app']/div/div[3]/div[2]/div[1]/div/div/div[2]/div[2]"
RESOURCE_DETAIL_XPATH = "//div[@class='card-header']/span"

metadata_dict = {
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
}

k = {
    (
        "Preview of 'State/UTs-wise Unemployment Rate for Persons of Age 15 Years and above of Different General Education Level According to usual status Basis Approach during 2019-20 Periodic Labour Force Survey (PLFS)'",
        "7124777",
    ),
    (
        "Preview of 'Number and Type of vehicles registered in Mizoram (October to December 2020)'",
        "7144904",
    ),
    (
        "Preview of 'Wholesale Price Index - (Base Year 2004-05)- Upto October 2015'",
        "3731481",
    ),
    (
        "Preview of 'Wholesale Price Index - 1953-54 to 1961-62 (Base Year: 1952-53=100)'",
        "726941",
    ),
    (
        "Preview of 'Wholesale Price Index - 1962-63 to 1970-71 (Base Year: 1961-62=100)'",
        "726961",
    ),
    (
        "Preview of 'Wholesale Price Index for the base year 2004-05 - Upto February 2014'",
        "686561",
    ),
    ("Preview of 'City-wise list of Wellness Centres'", "4198001"),
    (
        "Preview of 'Wholesale Price Index - (Base Year 2004-05)- Upto April 2015'",
        "2918641",
    ),
    (
        "Preview of 'Wholesale Price Index - (Base Year 2004-05)- Upto July 2014'",
        "726961",
    ),
    ("Preview of 'Inner Line Permits (ILP) Regular 2017-2022'", "7139965"),
    (
        "Preview of 'Surat City Complaint Statistics from April 2015 onward (daily)'",
        "3786961",
    ),
    (
        "Preview of 'Estimated Maximum Viability Gap Funding (VGF) for PPP model of BharatNet (in reply to Unstarred Question on 10 December, 2021)'",
        "7124851",
    ),
    ("Preview of 'Flight Schedule'", "2970001"),
    ("Preview of 'List of Police Stations in Mizoram'", "7145520"),
    (
        "Preview of 'Wholesale Price Index - 1971-72 to 1981-82 (Base Year: 1970-71=100)'",
        "726981",
    ),
    ("Preview of 'Residential Certificate 2017-2022'", "7140093"),
    (
        "Preview of 'State/UTs-wise Regarding Registration of Unorganised Workers on e-SHRAM Portal (in reply to Unstarred Question on 9 December, 2021)'",
        "7124780",
    ),
    (
        "Preview of 'Water Charges Collection by Surat Municipal Corporation from April 2015 onward (daily)'",
        "3787201",
    ),
    (
        "Preview of 'Surat City Bus and BRTS Passenger Information from April 2015 (daily)'",
        "3787401",
    ),
    ("Preview of 'Self Printing of CGHS Card as on date'", "6629925"),
    ("Preview of 'Inner Line Permit (ILP) Renewal 2017-2022'", "7140070"),
    (
        "Preview of 'Number and Type of Vehicles registered in Mizoram (April to June 2019)'",
        "7144897",
    ),
    (
        "Preview of 'Wholesale Price Index - (Base Year 2004-05)- Upto May 2015'",
        "2918661",
    ),
    (
        "Preview of 'State/UTs-wise and Year-wise Sanctioned Projects under National Adaptation Fund for Climate Change (NAFCC) from 2015-16 to 2018-19'",
        "7124764",
    ),
    ("Preview of 'Enrollment in Employment Exchange 2017-2022'", "7140115"),
    (
        "Preview of 'Wholesale Price Index - (Base Year 2004-05)- Upto June 2016'",
        "786201",
    ),
    ("Preview of 'Scheduled Tribe Certificate 2017-2022'", "7140110"),
    (
        "Preview of 'Number and Type of vehicle registered in Mizoram (July to September 2021)'",
        "7144905",
    ),
    (
        "Preview of 'Number and Type of vehicle registered in Mizoram (October to December 2021)'",
        "7144906",
    ),
    (
        "Preview of 'Number and Type of vehicles registered in Mizoram (July to September 2020)'",
        "7144903",
    ),
    (
        "Preview of 'Wholesale Price Index (Base Year 2011-12) till last financial year'",
        "3731481",
    ),
    (
        "Preview of 'Number and Type of Vehicles registered in Mizoram (July to September 2019)'",
        "7144901",
    ),
    (
        "Preview of 'Wellness Centre-wise Beneficiaries registered under CGHS in different cities'",
        "6626709",
    ),
    ("Preview of 'Aviation Grievance - as on date'", "2970021"),
    (
        "Preview of 'Year-wise Achievements in Rajasthan Interest Subvention Scheme for Incremental Credit to MSMEs from 2018-19 to 2020-21'",
        "7027850",
    ),
    ("Preview of 'Members of 8th Mizoram Legislative Assembly'", "7145023"),
    (
        "Preview of 'State/UTs-wise Data for unorganised sector workers (in reply to Unstarred Question on 9 December, 2021)'",
        "7124775",
    ),
    (
        "Preview of 'Wholesale Price Index (Base Year 2004-05) Upto March 2017'",
        "2918661",
    ),
    (
        "Preview of 'Country-wise Disbursement of Financial Assistance Received by Government of India from 2019-20 to 2021-22'",
        "7028636",
    ),
    (
        "Preview of 'Sector-wise Projects Approved for Funding in Assam (in reply to Unstarred Question on 9 December, 2021)'",
        "7124870",
    ),
    (
        "Preview of 'Zone-wise Property tax Demand and Recovery in Surat city from 2002 to 2017'",
        "3787441",
    ),
    (
        "Preview of 'Wholesale Price Index (Base Year 2011-12) till last month'",
        "3390241",
    ),
    ("Preview of 'Common Service Center in Mizoram as on July 2022'", "7144995"),
    (
        "Preview of 'Wholesale Price Index - (Base Year 2004-05)- Upto January 2015'",
        "786201",
    ),
    (
        "Preview of 'Zone & Ward-wise Property tax Demand and Recovery in Surat city from 2002 to 2017'",
        "3787461",
    ),
    (
        "Preview of 'Project-wise Ongoing New Project in Rain Forest Research Institute (RFRI) at Jorhat, Assam (in reply to Unstarred Question on 9 December, 2021)'",
        "7124757",
    ),
    (
        "Preview of 'State/UTs-wise Job Seekers of Age 15 years and above of Different General Education Level Registered on National Career Service (NCS) Portal (in reply to Unstarred Question on 9 December, 2021)'",
        "7124778",
    ),
    (
        "Preview of 'State/UT-wise Connections released under PMUY, and Beneficiaries & Subsidy amount transferred under DBTL till last date'",
        "6690165",
    ),
    (
        "Preview of 'List of Diagnostics Centers empaneled under CGHS all over India'",
        "6626286",
    ),
    (
        "Preview of 'Project-wise NHs Presently under Construction in Assam (in reply to Unstarred Question on 02 August, 2021)'",
        "7028620",
    ),
    (
        "Preview of 'State/UT-wise Total Micro Enterprises Registered under Udyam Registration from 01-07-2020 to 29-07-2021'",
        "7028591",
    ),
    ("Preview of 'Permanent Residential Certificate 2017-2022'", "7140095"),
    ("Preview of 'List of Life Saving Drugs'", "4198021"),
    (
        "Preview of 'State/UTs-wise Automated Teller Machines (ATM) (in reply to Unstarred Question on 10 December, 2021)'",
        "7124856",
    ),
    (
        "Preview of 'State/UT-wise and Sector-wise Registration on Udyam Registration Portal during 2020 and 2021'",
        "7028595",
    ),
    (
        "Preview of 'District Wise Total MSME Registered Enterprises under UDYAM Registration till last date'",
        "6898754",
    ),
    (
        "Preview of 'District Level Manufacturing MSME Registered Enterprises under UDYAM Registration till last date'",
        "6898764",
    ),
    (
        "Preview of 'District wise Services MSME Registered Enterprises under UDYAM Registration till last date '",
        "6898767",
    ),
    (
        "Preview of 'Wholesale Price Index for the base year 2004-05 - Upto April 2014'",
        "726941",
    ),
    (
        "Preview of 'Scheme-wise Funds Allocated for Implementation of Various Schemes under the D/o Youth Affairs and D/o Sports during 2020-21 and 2021-2022'",
        "7028627",
    ),
    (
        "Preview of 'Year-wise Achievements in Rajasthan MSE-CDP from 2018-19 to 2020-21'",
        "7027851",
    ),
    ("Preview of 'Wholesale Price Index (Base Year 2011-12) Upto May 2017'", "2918641"),
    ("Preview of '20th Livestock Census, Mizoram'", "7145424"),
    (
        "Preview of 'Details of Vehicle Tax collected by Surat Municipal Corporation from Year 1989 onward'",
        "3787161",
    ),
    (
        "Preview of 'Current Daily Price of Various Commodities from Various Markets (Mandi)'",
        "86943",
    ),
    ("Preview of 'List of Hospitals empaneled under CGHS all over India'", "6626300"),
    (
        "Preview of 'Wholesale Price Index - (Base Year 2004-05)- Upto August 2015'",
        "3390241",
    ),
    (
        "Preview of 'Wholesale Price Index - (Base Year 2004-05)- Upto September 2014'",
        "726981",
    ),
    (
        "Preview of 'Year-wise Achievements in Rajasthan Credit Guarantee Scheme for Micro and Small Enterprises from 2018-19 to 2020-21'",
        "7027849",
    ),
    (
        "Preview of 'Agency-wise Disbursements by MSDCs (in reply to Unstarred Question on 02 August, 2021)'",
        "7028613",
    ),
    ("Preview of 'Real time Air Quality Index from various locations'", "804661"),
    (
        "Preview of 'Marriage Registration at Surat Municipal Corporation from January 2008 onward'",
        "3787001",
    ),
    (
        "Preview of 'Wholesale Price Index - (Base Year 2004-05)- Upto March 2016'",
        "686561",
    ),
    ("Preview of 'Income Certificate 2017-2022'", "7140079"),
    (
        "Preview of 'Geological Quadrangle Maps of India information from 1997 to 2014'",
        "7145816",
    ),
    (
        "Preview of 'District resource maps of India information from 1997 to 2022'",
        "7128400",
    ),
    (
        "Preview of 'Water Supplied in Surat city (in MLD) from April 2015 onward (daily)'",
        "3787181",
    ),
    ("Preview of 'AirSewa - Airport Services Data'", "2970061"),
    (
        "Preview of 'Garbage Collection in Surat City (in KG) from April 2015 onward (daily)'",
        "3786981",
    ),
    ("Preview of 'AirSewa - Aviation Frequently Asked Questions (FAQs)'", "2970041"),
}
print(len(k))
print(len(set(k)))
