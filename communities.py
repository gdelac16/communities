import sys

COMMUNITIES = {'1': {'X': {'0': 'All', '1': 'Europe', '2': 'Russia', '3': 'North America', '4': 'Asia', '5': 'Africa', '6': 'Middle East', '7': 'South America'},
                     'YY': {'0': {'00': 'All', '01': 'All IX peers', '99': 'All transit peers'},
                            '1': {'00': 'All', '01': 'AMS-IX', '02': 'LINX LON1', '03': 'DE-CIX Frankfurt', '04': 'DTEL-IX', '07': '(was LINX/E)', '09': 'EE Paris', '10': 'MIX', '11': 'DE-CIX Madrid', 
                                  '12': 'EE Zurich/ZH4', '13': 'NETNOD', '14': 'DE-CIX Marseille', '15': 'NL-IX',  '16': 'BALCAN IX', '85': 'CenturyLink-LND-LD4', '86': 'CenturyLink-FRF-NTL', 
                                  '87': 'CenturyLink-SOF', '88': 'CenturyLink-STK', '89': 'CenturyLink-MRS', '90': 'CenturyLink-MAD', '91': 'CenturyLink-ZUR-ZH4', '92': 'CenturyLink-MXP (Milan)', 
                                  '93': 'CenturyLink-AMS-NKF', '94': 'CenturyLink-LND-LD5', '95': 'CenturyLink-ZUR-IXN', '96': 'CenturyLink-PAR', '97': 'CenturyLink-LND-T2', '98': 'CenturyLink-FRF-FR5',
                                  '99': 'CenturyLink-AMS-T1'},
                            '2': {'00': 'All', '01': 'MSK-IX', '02': 'PITER-IX / SPB', '03': 'PITER-IX / MSK', '04': 'PITER-IX / ROV', '99': 'CenturyLink/RU/MSK'},
                            '3': {'00': 'All', '01': 'EE Ashburn', '02': 'Telx NY', '03': 'NY-IX (PAIX)', '04': 'EE LA', '05': 'Any2 LA', '06': 'Telx ATL', '07': 'EE DAL', '08': 'TOR-IX', '09': 'SIX', 
                                  '10': 'EE CHI', '11': 'NOTA MIA', '12': 'DE-CIX NY', '13': 'EE SJC', '14': 'DE-CIX Dallas', '15': 'EE PA', '89': 'CenturyLink/US/San Jose', '90': 'CenturyLink/US/Denver', 
                                  '91': 'CenturyLink/US/Miami', '92': 'CenturyLink/US/Chicago', '93': 'CenturyLink/US/Seattle', '94': 'CenturyLink/CA/Toronto', '95': 'CenturyLink/US/Atlanta', '96': 'CenturyLink/US/Dallas', '97': 'CenturyLink/US/LA', '98': 'CenturyLink/US/NY', '99': 'CenturyLink/US/ASH'},
                            '4': {'00': 'All', '01': 'EE/HK', '02': 'HKIX/HK', '03': 'EE/SG', '04': 'BBIX/HK', '05': 'BBIX/TY', '06': 'BBIX/SG', '07': 'SGIX', '08': 'JPNAP', '09': 'KINX', '10': 'JBIX', 
                                  '89': 'PCCW IP Transit/KR', '90': 'China via Rostelecom/TY (CNRT vrf)', '91': 'China via Rostelecom/HK (CNRT vrf)', '92': 'CMC IP Transit/VN', '93': 'GSL IP Transit/AU', 
                                  '94': 'PCCW China Transit/HK', '95': 'PCCW IP Transit/TW', '96': 'PCCW IP Transit/TY', '97': 'China Unicom Peering/HK', '98': 'PCCW IP Transit/SG', '99': 'PCCW IP Transit/HK'},
                            '5': {'00': 'All', '01': 'NAP Africa', '99': 'CenturyLink/SA/Johannesburg'},
                            '6': {'00': 'All', '98': 'Infonas AS35313/Bahrain (IPTP AS51601)', '99': 'CenturyLink/AE/Dubai'},
                            '7': {'00': 'All', '01': 'IX.BR', '05': 'JumboIX Lima Peru', '06': 'PIT Chile Santiago', '07': 'EIE (Sao Paolo)', '97': 'Lumen Fortaleza', '98': 'Lumen San Paolo', 
                                  '99': 'CenturyLink (Global Crossing)'}},
                     'Z': {'0': 'announce with 0 prepends', '1': 'announce with 1 prepends', '2': 'announce with 2 prepends', '4': 'announce with 4 prepends', '9': 'does not announce'}},
               '2': {'X': {'0': 'All', '1': 'Europe', '2': 'Russia', '3': 'North America', '4': 'ASIA', '5': 'Africa', '6': 'Middle East (ME)', '7': 'South America'},
                     'YY': {'0': {'00': 'All', '01': 'All IX', '99': 'All IP transit'},
                            '1': {'00': 'All', '01': 'AMS-IX', '02': 'LINX LON1', '03': 'DE-CIX Frankfurt', '04': 'DTEL-IX', '07': '(was LINX/E)', '09': 'EE Paris', '10': 'MIX', '11': 'DE-CIX Madrid', '12': 'EE Zurich/ZH4', '13': 'NETNOD', '14': 'DE-CIX Marseille', '15': 'NL-IX', '16': 'BALCAN IX','85': 'CenturyLink-LND-LD4', '86': 'CenturyLink-FRF-NTL', '87': 'CenturyLink-SOF', '88': 'CenturyLink-STK', '89': 'CenturyLink-MRS', '90': 'CenturyLink-MAD', '91': 'CenturyLink-ZUR-ZH4', '92': 'CenturyLink-MXP (Milan)', '93': 'CenturyLink-AMS-NKF', '94': 'CenturyLink-LND-LD5', '95': 'CenturyLink-ZUR-IXN', '96': 'CenturyLink-PAR', '97': 'CenturyLink-LND-T2', '98': 'CenturyLink-FRF-FR5'}, '2': {'00': 'All', '01': 'MSK-IX', '02': 'PITER-IX / SPB < added by Slav', '03': 'PITER-IX / MSK < added by Slav', '04': 'PITER-IX / ROV < added by Slav (Rostov-on-Don)', '05': 'PITER-IX / VOZ', '06': 'PITER-IX / CHE', '97': 'TRT / TRANSROUTE < added by Slav', '98': 'RT / ROSTELECOM < added by Slav / IPT stopped.', '99': 'CenturyLink/RU/MSK'},
                            '3': {'00': 'All', '01': 'EE Ashburn', '02': 'Telx NY', '03': 'NY-IX (PAIX)', '04': 'EE LA', '05': 'Any2 LA', '06': 'Telx ATL', '07': 'EE DAL', '08': 'TOR-IX', '09': 'SIX', '10': 'EE CHI', '11': 'NOTA MIA', '12': 'DE-CIX NY', '13': 'EE SJC', '14': 'DE-CIX Dallas', '15': 'EE PA', '89': 'CenturyLink/US/San Jose', '90': 'CenturyLink/US/Denver', '91': 'CenturyLink/US/Miami', '92': 'CenturyLink/US/Chicago', '93': 'CenturyLink/US/Seattle', '94': 'CenturyLink/CA/Toronto', '95': 'CenturyLink/US/Atlanta', '96': 'CenturyLink/US/Dallas', '97': 'CenturyLink/US/LA', '98': 'CenturyLink/US/NY', '99': 'CenturyLink/US/ASH'},
                            '4': {'00': 'All', '01': 'EE/HK', '02': 'HKIX/HK', '03': 'EE/SG', '04': 'BBIX/HK', '05': 'BBIX/TY', '06': 'BBIX/SG', '07': 'SGIX', '08': 'JPNAP', '09': 'KINX', '10': 'JBIX', '11': 'AUIX', '89': 'PCCW IP Transit/KR', '90': 'China via Rostelecom/TY (CNRT vrf)', '91': 'China via Rostelecom/HK (CNRT vrf)', 
                                 '92': 'CMC IP Transit/VN', '93': 'GSL IP Transit/AU', '94': 'PCCW China Transit/HK', '95': 'PCCW IP Transit/TW', '96': 'PCCW IP Transit/TY', '97': 'China Unicom paid peering/HK', '98': 'PCCW IP Transit/SG', '99': 'PCCW IP Transit/HK'},
                            '5': {'00': 'All', '01': 'NAP Africa'},
                            '6': {'00': 'All', '98': 'Infonas AS35313/Bahrain (IPTP AS51601)', '99': 'CenturyLink/Dubai'},
                            '7': {'00': 'All', '01': 'IX.BR (Sao Paolo)', '02': 'IX.BR (Fortaleza)', '03': 'Lima/CTL', '04': 'Lima/AmTel', '05': 'Lima/JumboIX', '06': 'Santiago/Level3(Huecheraba)', '07': 'EIE (Sao Paolo)', '98': 'CenturyLink/Brazil/Fortaleza', '99': 'CenturyLink/Peru/Lima'}}},
               '3': {'3000 ': 'All direct customers', '3010': 'IX-Transit customers', '3020': 'All Anycast customers', '3100': 'EU direct customers', '3101': 'AMS direct customers additional community', '3120': 'EU Anycast customers', '3200': 'Russian direct customers', '3210': 'Russian IX-Transit customers', '3220': 'Russian Anycast customers', '3300': 'NA direct customers', '3320': 'NA Anycast customers', '3400': 'AP direct customers', '3401': 'HK direct customers additional community', '3402': 'SG direct customers additional community', '3403': 'TY direct customers additional community', '3404': 'VN direct customers additional community', '3405': 'MY direct customers additional community', '3406': 'TW direct customers additional community', '3407': 'ID direct customers additional community', '3408': 'KR direct customers additional community', '3410': 'AP IX-Transit customers', '3420': 'AP Anycast customers', '3500': 'Africa direct customers', '3520': 'Africa Anycast customers', '3600': 'ME direct customers', '3620': 'ME Anycast customers', '3700': 'South America direct customers', '3720': 'South America Anycast customers'},
               '4': {'0': 'All', '1': 'Europe', '2': 'Russia', '3': 'USA', '4': 'APAC', '5': 'Africa', '6': 'Middle East (ME)'},
               '5': {'X': {'0': 'All', '1': 'Europe', '2': 'Russia', '3': 'USA', '4': 'Asia', '5': 'Africa', '7': 'South America'},
                    'YY':{'0': {'00': 'All'},
                          '1':{'00': 'All', '01': 'AMS-NKF', '02': 'FRF-Ancotel', '03': 'FRF-NewTelco', '04': 'IXN-Zurich', '05': 'AMS-T1', '06': 'TH2-Paris', '07': 'Kiev-Newtelco', '08': 'London-LD5', '09': 'London-LD8 (Telecity 2)', '10': 'MRS-NetCenter', '11': 'Sofia Telepoint'},
                          '2': {'00': 'All'},
                          '3': {'00': 'All', '01': 'LA1 Equinix', '02': 'DC5 Equinix', '03': 'NY  TelX', '04': 'LA Coresite/1W', '05': 'MIA Terremark', '06': 'SV1 Equinix', '07': 'NY NY4'},
                          '4': {'00': 'All', '01': 'HK/Mega-i', '02': 'HK/Equinix', '03': 'SG/Equinix', '04': 'TY/Equinix', '05': 'SG/GlobalSwitch'}, 
                          '5': {'00': 'All'}, 
                          '6': {'00': 'All', '01': 'DX1/Equinix'}, 
                          '7': {'00': 'All', '01': 'Lima/CTL', '02': 'Lima/AmeTel', '03': 'SP/Equinix', '04': 'Fortaleza/Mob', '05': 'Santiago/Level3(Huecheraba)'}}},
               '6': {'X':{'0': 'BLOCKING toward peers, NOT USED FOR TAGGING', '1': 'Europe', '2': 'Russia', '3': 'Americas', '4': 'Asia', '5': 'Africa (535 max)', '6-9': 'N/A'}, 
                     'YYY': {'1': {'001': 'PI Telenor AS2119 Te1/12 @ sw2.r327.nkf.ams.nl', '002': 'PI Interoute AS8928 Te7/5 @ r0.r327.nkf', '003': 'PI Interoute AS8928 Te2/1 @ r0.r0.k3r8.anc.fra', '004': 'PI Vodafone AS1273 Po20 @ r0.r2116.ntl.kiev', '005': 'PI Vodafone AS1273 Te2/3 @ r0.610.ld5.lnd.uk', '006': 'PI Init7 AS13030 Te2/3 @ r0.r205.ixn.zrh.ch', '007': 'PI Ukrtelecom AS6849 Gi4/3 @ r0.r2116.ntl.kiev.ua', '008': 'PI Vodafone AS1273 Te4/2 @ r0.k3r8.anc.fra.de', '009': 'PI Fiord AS28917 Te1/15 @ sw2.r327.nkf.ams.nl (Vl1799@r0.r327.nkf.ams.nl)', '010': 'PI Liberty Global AS6830 Te0/0/0/8 @ r0.r328.nkf.ams.nl', '011': 'PI Liberty Global AS6830 BE20 (Te0/7/0/19) @ r0.k3r8.fr5.eq.fra.de', '012': 'PI Liberty Global AS6830 Te3/4 @ r1.1p19b.t2.lnd.uk', '013': 'PI KVANT AS43727 Vl1432 @ r0.911.ntl.fra', '014': 'PI Reliance Jio Infocomm AS64049 Po20 @ r0.b06.0a02.mrs.fr (Te8/5 @ r0.b06.0a02.mrs.fr)', '015': 'PI Reliance Jio Infocomm AS64049 Po21 @ r0.b06.0a02.mrs.fr (Te8/6 @ r0.b06.0a02.mrs.fr)', '016': 'PI Vodafone AS1273 Bundle-Ether7(Te0/0/0/11 Te0/0/0/12 Te0/1/0/11 Te0/1/0/12) @ r0.r328.nkf.ams.nl', '017': 'PI TopNet AS3326 Gi3/48 @ r0.k3r8.anc.fra.de <--- Slav', '018': 'PI Flag Telecom/ Reliance Globalcom AS15412 Gi1/2 @ r0.11a06.th2.par.fr <--- Slav', '019': 'PI ROMTELECOM AS9050 Gi3/5.512 @ r0.k3r8.anc.fra.de', '020': 'PI Vodafone AS1273 Vl4093 @ r0.2317.ntr.sof', '021': 'PI KVANT AS43727 Vl1433 @ r0.r2116.ntl.kiev.ua', '022': 'PI Etisalat AS8966 BE30.212 @ r0.r328.nkf.ams.nl (Eth1/12 @ sw0.r328.nkf.ams.nl)', '023': 'PI Reliance Jio Infocomm AS64049 nsw3.911.ntl.fra.de', '024': 'PI 1&1 Versatel Deutschland AS8881 TenGigE0/7/0/11 @ r0.k3r8.fr5.eq.fra.de', '025': 'PI Leaseweb AS16265 BE3 @ r0.r328.nkf.ams.nl (via AS51601 ; 51601:61025)', '026': 'PI Lucera AS63287 Vl1501 @ r0.402.ld4.lnd.uk Vl1502 @ r0.402.ld4.lnd.uk < added by YUK'},
                            '2': {'001': 'PI KVANT AS43727 Vl1442 @ r0.m5.m9', '002': '(PI) Filanco RS AS29076 @ r0.m5.m9'}, 
                            '3': {'001': 'PI Vodafone AS1273 BE5@r0.101.1ws.la.us', '002': 'PI Softbank AS17676 Te0/0/0/31 @ r0.101.1ws.la.us', '003': 'PI KT AS4766 Te0/1/0/27.2003 @ r0.101.1ws.la.us (Te0/3 @ sw0.111.la1.ca.us)', '004': 'PI Vodafone AS1273 Te5/4 @ r0.2cr164.ter.mia.us', '005': 'PI KDDI AS2516 Po20 (Te7/7 & Te9/5) @ r0.121.1270.sv1.sjc.us', '006': 'PI KDDI AS2516 BE20 (Te0/0/0/33 & Te0/1/0/33) @ r0.101.1ws.la.us', '007': 'PI TELIN AS7713 Te0/1/0/27.2005@r0.101.1ws.la.us (Te0/5 @ sw0.111.la1.ca.us)', '008': 'PI Vodafone AS1273 BE49@r0.107.dc5.ash.va.us', '009': 'PI Cox AS22773 Te0/1/0/28.2001 @r0.101.1ws.la.us  (Te0/2 @ sw0.111.la1.ca.us) <--- Slav', '010': 'PI Charter Communications AS20115 Te0/1/0/27.2002 @r0.101.1ws.la.us  (Te0/1 @ sw0.111.la1.ca.us)', '011': 'PI Charter Communications AS20115 Te0/7/0/7 @r0.107.dc5.ash.va.u', '012': 'PI Cox AS22773 Te0/0/0/15 @r0.107.dc5.ash.va.us', '013': 'PI PI Rogers Cable AS812 Te0/0/0/7 @r0.107.dc5.ash.va.us', '014': 'PI Google AS15169 Bundle-Ether40@r0.309.mi1.mia.us', '015': 'PI Netflix AS2906 Bundle-Ether41@r0.309.mi1.mia.us', '016': 'PI Facebook AS32934 Bundle-Ether42@r0.309.mi1.mia.us', '017': 'PI Facebook AS32934 BE10.1700@r0.f1k4-2.l3.lim.pe', '018': 'PI Facebook AS32934 BE10.1701@r0.f1k4-2.l3.lim.pe', '019': 'PI Google AS15169 @r0.l3.pit.scl.cl'}, 
                            '4': {'001': 'PI SingTel AS7473 Te3/3 @ r0.409.mi.hk', '002': 'PI Vodafone AS1273 Te3/1 @ r0.409.mi.hk', '003': 'FREE (WAS PI Pacnet AS10026 Vl731 @ r0.214.ty2.eq.jp (Eth1/31 @ sw5.214.ty2.eq.jp))', '004': 'PI Pacnet AS10026 Te5/4 @ r0.409.mi.hk', '005': 'PI Pacnet AS10026 Te1/5 @ r0.ib25.gs.sg', '006': 'PI Softbank AS17676 Vl727 @ r0.214.ty2.eq.jp (Eth1/27 @ sw5.214.ty2.eq.jp)', '007': 'PI Telstra AS4637 Te3/4 @ r0.616.eq.sg', '008': 'PI Telstra AS4637 Te3/6 @ r0.409.mi.hk', '009': 'PI Vodafone AS1273 Vl730 @ r0.214.ty2.eq.jp (Eth1/30 @ sw5.214.ty2.eq.jp)', '010': 'Pi Vodafone AS1273 Te1/4@ r0.616.eq.sg', '011': 'PI Softbank AS17676 Po100 @ sw0.bc04.bbt.ty.jp (Eth1/50 @ sw0.bc04.bbt.ty.jp)', '012': 'PI Telstra AS4637 Te4/6 @ r0.214.ty2.eq.jp', '013': 'PI SKB AS9318 Vl2100 @ r0.409.mi.hk', '014': 'PI KVANT AS43727 Vl1440 @ r0.409.mi.hk', '015': 'FREE (WAS PI TELIN AS7713 Te8/8 @ r0.101.eq.hk)', '016': 'PI KVANT AS43727 Vl1440 @ r1.102.e1.hk', '017': 'PI Reliance Jio Infocomm AS64049 Po20 @ r0.616.eq.sg (Te3/1 @ r0.616.eq.sg)', '018': 'PI Reliance Jio Infocomm AS64049 Po21 @ r0.616.eq.sg (Te3/2 @ r0.616.eq.sg)', '019': 'PI StarHub AS4657 Te2/3.145 @ r0.409.mi.hk', '020': 'PI StarHub AS38861 Te2/3.146 @ r0.409.mi.hk', '021': 'PI SKB AS9318 Te1/2.2930 @ r0.214.ty2.eq.jp', '022': 'PI Telstra AS4637 Po20 @ r0.bc05.bbt.ty.jp (Te3/6 @ r0.bc05.bbt.ty.jp)', '023': 'PI Softbank AS17676 Po101 @ sw0.bc04.bbt.ty.jp (Eth1/51 @ sw0.bc04.bbt.ty.jp)', '024': 'PI NTC AS9902 TenGigE0/0/0/1.3080@r0.f8.cmc.hcm.vn'}}}}


def filter_of_community(user_community):
    internal_flag_token = user_community[0]
    region_token = user_community[1]
    peer_number_token = user_community[2:4]
    prepends_token = user_community[4]

    region_dict = COMMUNITIES['1']['X']
    if region_token in region_dict.keys():
        region = region_dict[region_token]
    else:
        region = "The region is invalid"
        return region

    peer_location = COMMUNITIES['1']['YY'][region_token]

    if peer_number_token in peer_location.keys():
        peer = peer_location[peer_number_token]
    else:
        peer = "The peer is invalid"
        return peer

    prepends_number = COMMUNITIES['1']['Z']

    if prepends_token in prepends_number.keys():
        prepends = prepends_number[prepends_token]
    else:
        prepends = "The prepend is invalid"
        return prepends

    community_meaning = f"The prefix in the region of {region} to the {peer} peer, {prepends}."
    return community_meaning

def filter_of_community2(user_community):
    internal_flag_token = user_community[0]
    region_token = user_community[1]
    peer_number_token = user_community[2:4]
    
    region_dict = COMMUNITIES[internal_flag_token]['X']
    if region_token in region_dict.keys():
        region = region_dict[region_token]
    else:
        region = "The region is invalid"
        return region

    peer_location = COMMUNITIES[internal_flag_token]['YY'][region_token]

    if peer_number_token in peer_location.keys():
        peer = peer_location[peer_number_token]
    else:
        peer = "The community is invalid"
        return peer

    if internal_flag_token == '2':
        community_meaning = f"Community applied at ingress in {region} at {peer}"
    else:
        community_meaning = f"PI community in {region} region at {peer}"        
    return community_meaning

def filter_of_community3(user_community):
    community_token = user_community[:4]
    
    community_3_dict = COMMUNITIES['3']
    if community_token in community_3_dict.keys():
        community_3 = community_3_dict[community_token]
    else:
        community_3 = "The community is invalid"
        return community_3
    
    community_meaning = f"Community applied at ingress {community_3}"
    return community_meaning

def filter_of_community4(user_community):
    region_of_origin_token = user_community[1]
    region_of_processing_token = user_community[2]
    processing_token = user_community[3]
    
    community_4_dict = COMMUNITIES['4']
    if region_of_origin_token in community_4_dict.keys():
        origin_region = community_4_dict[region_of_origin_token]
    else:
        origin_region = "The region of origin is invalid"
        return origin_region
    
    if region_of_processing_token in community_4_dict.keys():
        processing_region = community_4_dict[region_of_processing_token]
    else:
        processing_region = "The region of processing is invalid"
        return processing_region

    if region_of_origin_token == region_of_processing_token:
        show_this_result = f"{processing_region}\'s the route is not imported by regional RR in {origin_region} region"
        return show_this_result  
        
    if processing_token <= '8':
        processing = 'it\'s reserved'
    else:
        processing = 'Don\'t import in {processing_region} region'
        return processing
    
    community_meaning = f"The prefix in {origin_region} (region of origin) to {processing_region} (region of processing), {processing} "
    return community_meaning

def filter_of_community6(user_community):
    internal_flag_token = user_community[0]
    region_of_6_token = user_community[1]
    pi_port_tag_token = user_community[2:5]

    region_6_dict = COMMUNITIES['6']['X']
    if region_of_6_token in region_6_dict.keys():
        region_6 = region_6_dict[region_of_6_token]
    else:
        region_6 = "The region is invalid"
        return region_6

    pi_port_location = COMMUNITIES['6']['YYY'][region_of_6_token]

    if pi_port_tag_token in pi_port_location.keys():
        pi_port = pi_port_location[pi_port_tag_token]
    else:
        pi_port = "The PI is invalid"
        return pi_port

    community_meaning = f"Private peering in the region of {region_6} with {pi_port}"
    return community_meaning
    
def filter_internal(user_community):
    internal_flag_token = user_community[0]
            
    if internal_flag_token == '1':
        return filter_of_community(user_community)
    elif internal_flag_token == '2' or internal_flag_token == '5':
        return filter_of_community2(user_community)
    elif internal_flag_token == '3':
        return filter_of_community3(user_community)
    elif internal_flag_token == '4':
        return filter_of_community4(user_community)
    elif internal_flag_token == '6':
        return filter_of_community4(user_community)
    else:
        return 'The community is invalid'
        

def run_script():
    if len(sys.argv) != 2:
        print("Error, Execute: communities community_number")
        sys.exit(1)

    user_community = sys.argv[1]

    community = filter_internal(user_community)
    print(community)


if __name__ == "__main__":
    run_script()
