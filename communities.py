user_community = input("Please enter the community: ")
communities = {'1':'internal flag',
              'X':{'0':'All','1':'Europe','2':'Russia','3':'North America','4':'Asia','5':'Africa','6':'Middle East','7':'South America'},
              'YY':{'0':{'00':'All','01':'All IX peers','99':'All transit peers'},
                    '1':{'00':'All','01':'AMS-IX','02':'LINX LON1','03':'DE-CIX Frankfurt','04':'DTEL-IX','07':'(was LINX/E)',
                         '09':'EE Paris','10':'MIX','11':'DE-CIX Madrid','12':'EE Zurich/ZH4','13':'NETNOD','14':'DE-CIX Marseille',
                         '15':'NL-IX','16':'BALCAN IX','85':'CenturyLink-LND-LD4','86':'CenturyLink-FRF-NTL','87':'CenturyLink-SOF',
                         '88':'CenturyLink-STK','89':'CenturyLink-MRS','90':'CenturyLink-MAD','91':'CenturyLink-ZUR-ZH4',
                         '92':'CenturyLink-MXP (Milan)','93':'CenturyLink-AMS-NKF','94':'CenturyLink-LND-LD5','95':'CenturyLink-ZUR-IXN',
                         '96':'CenturyLink-PAR','97':'CenturyLink-LND-T2','98':'CenturyLink-FRF-FR5','99':'CenturyLink-AMS-T1'},
                    '2':{'00':'All','01':'MSK-IX','02':'PITER-IX / SPB','03':'PITER-IX / MSK','04':'PITER-IX / ROV','99':'CenturyLink/RU/MSK'},
                    '3':{'00':'All','01':'EE Ashburn','02':'Telx NY','03':'NY-IX (PAIX)','04':'EE LA','05':'Any2 LA',
                         '06':'Telx ATL','07':'EE DAL','08':'TOR-IX','09':'SIX','10':'EE CHI','11':'NOTA MIA',
                         '12':'DE-CIX NY','13':'EE SJC','14':'DE-CIX Dallas','15':'EE PA','89':'CenturyLink/US/San Jose',
                         '90':'CenturyLink/US/Denver','91':'CenturyLink/US/Miami','92':'CenturyLink/US/Chicago',
                         '93':'CenturyLink/US/Seattle','94':'CenturyLink/CA/Toronto','95':'CenturyLink/US/Atlanta',
                         '96':'CenturyLink/US/Dallas','97':'CenturyLink/US/LA','98':'CenturyLink/US/NY','99':'CenturyLink/US/ASH'},
                    '4':{'00':'All','01':'EE/HK','02':'HKIX/HK','03':'EE/SG','04':'BBIX/HK','05':'BBIX/TY','06':'BBIX/SG','07':'SGIX',
                         '08':'JPNAP','09':'KINX','10':'JBIX','89':'PCCW IP Transit/KR','90':'China via Rostelecom/TY (CNRT vrf)',
                         '91':'China via Rostelecom/HK (CNRT vrf)','92':'CMC IP Transit/VN','93':'GSL IP Transit/AU','94':'PCCW China Transit/HK',
                         '95':'PCCW IP Transit/TW','96':'PCCW IP Transit/TY','97':'China Unicom Peering/HK','98':'PCCW IP Transit/SG','99':'PCCW IP Transit/HK'},
                    '5':{'00':'All','01':'NAP Africa','99':'CenturyLink/SA/Johannesburg'},
                    '6':{'00':'All','98':'Infonas AS35313/Bahrain (IPTP AS51601)','99':'CenturyLink/AE/Dubai'},
                    '7':{'00':'All','01':'IX.BR','05':'JumboIX Lima Peru','06':'PIT Chile Santiago','07':'EIE (Sao Paolo)',
                         '97':'Lumen Fortaleza','98':'Lumen San Paolo','99':'CenturyLink (Global Crossing)'}},
              'Z':{'0':'no prepend','1':'1 prepends','2':'2 prepends','4':'4 prepends','9':'Do Not Announce'}}

index_0 = user_community[0]
index_1 = user_community[1]
index_2 = user_community[2]
index_3 = user_community[3]
index_4 = user_community[4]

index_

filter1 = communities[index_1]
filter2 = communities['X']


#print(f"Your community {user_community}...")

print (user_community, index_0, index_1, index_2, index_3, index_4, filter1)