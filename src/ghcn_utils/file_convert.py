import os

station_cols = [(0, 11), (12, 20), (21, 30), (31, 37), (38, 40), (41, 71), (72, 75), (76, 79), (80, 85)]
station_names = ['station_id', 'lat', 'lon', 'elev', 'state', 'name', 'gsn', 'network', 'wmo_id']

country_cols = [(0, 2), (3, 64)]
country_names = ['code', 'name']

state_cols = [(0, 2), (3, 50)]
state_names = ['code', 'name']

invent_cols = [(0, 11), (12, 20), (21, 30), (31, 35), (36, 40), (41, 45)]
invent_names = ['station_id', 'lat', 'lon', 'element', 'first_year', 'last_year']

dly_cols = [(0, 11), (11, 15), (15, 17), (17, 21),
            (21, 26), (26, 27), (27, 28), (28, 29),
            (29, 34), (34, 35), (35, 36), (36, 37),
            (37, 42), (42, 43), (43, 44), (44, 45),
            (45, 50), (50, 51), (51, 52), (52, 53),
            (53, 58), (58, 59), (59, 60), (60, 61),
            (61, 66), (66, 67), (67, 68), (68, 69),
            (69, 74), (74, 75), (75, 76), (76, 77),
            (77, 82), (82, 83), (83, 84), (84, 85),
            (85, 90), (90, 91), (91, 92), (92, 93),
            (93, 98), (98, 99), (99, 100), (100, 101),
            (101, 106), (106, 107), (107, 108), (108, 109),
            (109, 114), (114, 115), (115, 116), (116, 117),
            (117, 122), (122, 123), (123, 124), (124, 125),
            (125, 130), (130, 131), (131, 132), (132, 133),
            (133, 138), (138, 139), (139, 140), (140, 141),
            (141, 146), (146, 147), (147, 148), (148, 149),
            (149, 154), (154, 155), (155, 156), (156, 157),
            (157, 162), (162, 163), (163, 164), (164, 165),
            (165, 170), (170, 171), (171, 172), (172, 173),
            (173, 178), (178, 179), (179, 180), (180, 181),
            (181, 186), (186, 187), (187, 188), (188, 189),
            (189, 194), (194, 195), (195, 196), (196, 197),
            (197, 202), (202, 203), (203, 204), (204, 205),
            (205, 210), (210, 211), (211, 212), (212, 213),
            (213, 218), (218, 219), (219, 220), (220, 221),
            (221, 226), (226, 227), (227, 228), (228, 229),
            (229, 234), (234, 235), (235, 236), (236, 237),
            (237, 242), (242, 243), (243, 244), (244, 245),
            (245, 250), (250, 251), (251, 252), (252, 253),
            (253, 258), (258, 259), (259, 260), (260, 261),
            (261, 266), (266, 267), (267, 268), (268, 269)]
dly_names = ['station_id', 'year', 'month', 'element',
             'value1', 'mflag1', 'qflag1', 'sflag1',
             'value2', 'mflag2', 'qflag2', 'sflag2',
             'value3', 'mflag3', 'qflag3', 'sflag3',
             'value4', 'mflag4', 'qflag4', 'sflag4',
             'value5', 'mflag5', 'qflag5', 'sflag5',
             'value6', 'mflag6', 'qflag6', 'sflag6',
             'value7', 'mflag7', 'qflag7', 'sflag7',
             'value8', 'mflag8', 'qflag8', 'sflag8',
             'value9', 'mflag9', 'qflag9', 'sflag9',
             'value10', 'mflag10', 'qflag10', 'sflag10',
             'value11', 'mflag11', 'qflag11', 'sflag11',
             'value12', 'mflag12', 'qflag12', 'sflag12',
             'value13', 'mflag13', 'qflag13', 'sflag13',
             'value14', 'mflag14', 'qflag14', 'sflag14',
             'value15', 'mflag15', 'qflag15', 'sflag15',
             'value16', 'mflag16', 'qflag16', 'sflag16',
             'value17', 'mflag17', 'qflag17', 'sflag17',
             'value18', 'mflag18', 'qflag18', 'sflag18',
             'value19', 'mflag19', 'qflag19', 'sflag19',
             'value20', 'mflag20', 'qflag20', 'sflag20',
             'value21', 'mflag21', 'qflag21', 'sflag21',
             'value22', 'mflag22', 'qflag22', 'sflag22',
             'value23', 'mflag23', 'qflag23', 'sflag23',
             'value24', 'mflag24', 'qflag24', 'sflag24',
             'value25', 'mflag25', 'qflag25', 'sflag25',
             'value26', 'mflag26', 'qflag26', 'sflag26',
             'value27', 'mflag27', 'qflag27', 'sflag27',
             'value28', 'mflag28', 'qflag28', 'sflag28',
             'value29', 'mflag29', 'qflag29', 'sflag29',
             'value30', 'mflag30', 'qflag30', 'sflag30',
             'value31', 'mflag31', 'qflag31', 'sflag31']


def stations_copy_to_csv(source_path, target_path=None, headers_first_row=True):
    if target_path is None:
        target_path = source_path.with_suffix('.csv')

    with source_path.open("r", encoding="utf-8") as file:
        lines = file.readlines()

    file_append = open(target_path, 'a')
    if headers_first_row:
        header = "\"" + "\",\"".join(station_names) + "\"\n"
        file_append.write(header)
    for line in lines:
        csv_line1 = (f'"{line[station_cols[0][0]:station_cols[0][1]].strip()}",' +
                     f'"{line[station_cols[1][0]:station_cols[1][1]].strip()}",' +  # keep precision for lat
                     f'"{line[station_cols[2][0]:station_cols[2][1]].strip()}",' +  # keep precision for lon
                     f'"{line[station_cols[3][0]:station_cols[3][1]].strip()}",' +
                     f'"{line[station_cols[4][0]:station_cols[4][1]].strip()}",' +
                     f'"{line[station_cols[5][0]:station_cols[5][1]].strip()}",' +
                     f'"{line[station_cols[6][0]:station_cols[6][1]].strip()}",' +
                     f'"{line[station_cols[7][0]:station_cols[7][1]].strip()}",' +
                     f'"{line[station_cols[8][0]:station_cols[8][1]].strip()}"\n')
        file_append.write(csv_line1)


def countries_copy_to_csv(source_path, target_path=None, headers_first_row=True):
    if target_path is None:
        target_path = source_path.with_suffix('.csv')

    with source_path.open("r", encoding="utf-8") as file:
        lines = file.readlines()

    file_append = open(target_path, 'a')
    if headers_first_row:
        header = "\"" + "\",\"".join(country_names) + "\"\n"
        file_append.write(header)
    for line in lines:
        csv_line1 = (f'"{line[country_cols[0][0]:country_cols[0][1]].strip()}",' +
                     f'"{line[country_cols[1][0]:country_cols[1][1]].strip()}"\n')
        file_append.write(csv_line1)


def states_copy_to_csv(source_path, target_path=None, headers_first_row=True):
    if target_path is None:
        target_path = source_path.with_suffix('.csv')

    with source_path.open("r", encoding="utf-8") as file:
        lines = file.readlines()

    file_append = open(target_path, 'a')
    if headers_first_row:
        header = "\"" + "\",\"".join(state_names) + "\"\n"
        file_append.write(header)
    for line in lines:
        csv_line1 = (f'"{line[state_cols[0][0]:state_cols[0][1]].strip()}",' +
                     f'"{line[state_cols[1][0]:state_cols[1][1]].strip()}"\n')
        file_append.write(csv_line1)


def inventory_copy_to_csv(source_path, target_path=None, headers_first_row=True):
    if target_path is None:
        target_path = source_path.with_suffix('.csv')

    with source_path.open("r", encoding="utf-8") as file:
        lines = file.readlines()

    file_append = open(target_path, 'a')
    if headers_first_row:
        header = "\"" + "\",\"".join(invent_names) + "\"\n"
        file_append.write(header)
    for line in lines:
        csv_line1 = (f'"{line[invent_cols[0][0]:invent_cols[0][1]].strip()}",' +
                     f'"{line[invent_cols[1][0]:invent_cols[1][1]].strip()}",' +  # keep precision for lat
                     f'"{line[invent_cols[2][0]:invent_cols[2][1]].strip()}",' +  # keep precision for lon
                     f'"{line[invent_cols[3][0]:invent_cols[3][1]].strip()}",' +
                     f'"{line[invent_cols[4][0]:invent_cols[4][1]].strip()}",' +
                     f'"{line[invent_cols[5][0]:invent_cols[5][1]].strip()}"\n')
        file_append.write(csv_line1)


def dly_copy_to_csv(source_path, target_path=None, headers_first_row=True):
    if target_path is None:
        target_path = source_path.with_suffix('.csv')

    with source_path.open("r", encoding="utf-8") as infile, target_path.open("x", encoding="utf-8") as outfile:
        if headers_first_row:
            header = "\"" + "\",\"".join(dly_names) + "\"\n"
            outfile.write(header)

        for line in infile:
            csv_line1 = (f'{line[dly_cols[0][0]:dly_cols[0][1]].strip()},' +
                         f'{line[dly_cols[1][0]:dly_cols[1][1]].strip()},' +
                         f'{line[dly_cols[2][0]:dly_cols[2][1]].strip()},' +
                         f'{line[dly_cols[3][0]:dly_cols[3][1]].strip()},' +
                         f'{line[dly_cols[4][0]:dly_cols[4][1]].strip()},' +
                         f'{line[dly_cols[5][0]:dly_cols[5][1]].strip()},' +
                         f'{line[dly_cols[6][0]:dly_cols[6][1]].strip()},' +
                         f'{line[dly_cols[7][0]:dly_cols[7][1]].strip()},' +
                         f'{line[dly_cols[8][0]:dly_cols[8][1]].strip()},' +
                         f'{line[dly_cols[9][0]:dly_cols[9][1]].strip()},' +
                         f'{line[dly_cols[10][0]:dly_cols[10][1]].strip()},' +
                         f'{line[dly_cols[11][0]:dly_cols[11][1]].strip()},' +
                         f'{line[dly_cols[12][0]:dly_cols[12][1]].strip()},' +
                         f'{line[dly_cols[13][0]:dly_cols[13][1]].strip()},' +
                         f'{line[dly_cols[14][0]:dly_cols[14][1]].strip()},' +
                         f'{line[dly_cols[15][0]:dly_cols[15][1]].strip()},' +
                         f'{line[dly_cols[16][0]:dly_cols[16][1]].strip()},' +
                         f'{line[dly_cols[17][0]:dly_cols[17][1]].strip()},' +
                         f'{line[dly_cols[18][0]:dly_cols[18][1]].strip()},' +
                         f'{line[dly_cols[19][0]:dly_cols[19][1]].strip()},' +
                         f'{line[dly_cols[20][0]:dly_cols[20][1]].strip()},' +
                         f'{line[dly_cols[21][0]:dly_cols[21][1]].strip()},' +
                         f'{line[dly_cols[22][0]:dly_cols[22][1]].strip()},' +
                         f'{line[dly_cols[23][0]:dly_cols[23][1]].strip()},' +
                         f'{line[dly_cols[24][0]:dly_cols[24][1]].strip()},' +
                         f'{line[dly_cols[25][0]:dly_cols[25][1]].strip()},' +
                         f'{line[dly_cols[26][0]:dly_cols[26][1]].strip()},' +
                         f'{line[dly_cols[27][0]:dly_cols[27][1]].strip()},' +
                         f'{line[dly_cols[28][0]:dly_cols[28][1]].strip()},' +
                         f'{line[dly_cols[29][0]:dly_cols[29][1]].strip()},' +
                         f'{line[dly_cols[30][0]:dly_cols[30][1]].strip()},' +
                         f'{line[dly_cols[31][0]:dly_cols[31][1]].strip()},' +
                         f'{line[dly_cols[32][0]:dly_cols[32][1]].strip()},' +
                         f'{line[dly_cols[33][0]:dly_cols[33][1]].strip()},' +
                         f'{line[dly_cols[34][0]:dly_cols[34][1]].strip()},' +
                         f'{line[dly_cols[35][0]:dly_cols[35][1]].strip()},' +
                         f'{line[dly_cols[36][0]:dly_cols[36][1]].strip()},' +
                         f'{line[dly_cols[37][0]:dly_cols[37][1]].strip()},' +
                         f'{line[dly_cols[38][0]:dly_cols[38][1]].strip()},' +
                         f'{line[dly_cols[39][0]:dly_cols[39][1]].strip()},' +
                         f'{line[dly_cols[40][0]:dly_cols[40][1]].strip()},' +
                         f'{line[dly_cols[41][0]:dly_cols[41][1]].strip()},' +
                         f'{line[dly_cols[42][0]:dly_cols[42][1]].strip()},' +
                         f'{line[dly_cols[43][0]:dly_cols[43][1]].strip()},' +
                         f'{line[dly_cols[44][0]:dly_cols[44][1]].strip()},' +
                         f'{line[dly_cols[45][0]:dly_cols[45][1]].strip()},' +
                         f'{line[dly_cols[46][0]:dly_cols[46][1]].strip()},' +
                         f'{line[dly_cols[47][0]:dly_cols[47][1]].strip()},' +
                         f'{line[dly_cols[48][0]:dly_cols[48][1]].strip()},' +
                         f'{line[dly_cols[49][0]:dly_cols[49][1]].strip()},' +
                         f'{line[dly_cols[50][0]:dly_cols[50][1]].strip()},' +
                         f'{line[dly_cols[51][0]:dly_cols[51][1]].strip()},' +
                         f'{line[dly_cols[52][0]:dly_cols[52][1]].strip()},' +
                         f'{line[dly_cols[53][0]:dly_cols[53][1]].strip()},' +
                         f'{line[dly_cols[54][0]:dly_cols[54][1]].strip()},' +
                         f'{line[dly_cols[55][0]:dly_cols[55][1]].strip()},' +
                         f'{line[dly_cols[56][0]:dly_cols[56][1]].strip()},' +
                         f'{line[dly_cols[57][0]:dly_cols[57][1]].strip()},' +
                         f'{line[dly_cols[58][0]:dly_cols[58][1]].strip()},' +
                         f'{line[dly_cols[59][0]:dly_cols[59][1]].strip()},' +
                         f'{line[dly_cols[60][0]:dly_cols[60][1]].strip()},' +
                         f'{line[dly_cols[61][0]:dly_cols[61][1]].strip()},' +
                         f'{line[dly_cols[62][0]:dly_cols[62][1]].strip()},' +
                         f'{line[dly_cols[63][0]:dly_cols[63][1]].strip()},' +
                         f'{line[dly_cols[64][0]:dly_cols[64][1]].strip()},' +
                         f'{line[dly_cols[65][0]:dly_cols[65][1]].strip()},' +
                         f'{line[dly_cols[66][0]:dly_cols[66][1]].strip()},' +
                         f'{line[dly_cols[67][0]:dly_cols[67][1]].strip()},' +
                         f'{line[dly_cols[68][0]:dly_cols[68][1]].strip()},' +
                         f'{line[dly_cols[69][0]:dly_cols[69][1]].strip()},' +
                         f'{line[dly_cols[70][0]:dly_cols[70][1]].strip()},' +
                         f'{line[dly_cols[71][0]:dly_cols[71][1]].strip()},' +
                         f'{line[dly_cols[72][0]:dly_cols[72][1]].strip()},' +
                         f'{line[dly_cols[73][0]:dly_cols[73][1]].strip()},' +
                         f'{line[dly_cols[74][0]:dly_cols[74][1]].strip()},' +
                         f'{line[dly_cols[75][0]:dly_cols[75][1]].strip()},' +
                         f'{line[dly_cols[76][0]:dly_cols[76][1]].strip()},' +
                         f'{line[dly_cols[77][0]:dly_cols[77][1]].strip()},' +
                         f'{line[dly_cols[78][0]:dly_cols[78][1]].strip()},' +
                         f'{line[dly_cols[79][0]:dly_cols[79][1]].strip()},' +
                         f'{line[dly_cols[80][0]:dly_cols[80][1]].strip()},' +
                         f'{line[dly_cols[81][0]:dly_cols[81][1]].strip()},' +
                         f'{line[dly_cols[82][0]:dly_cols[82][1]].strip()},' +
                         f'{line[dly_cols[83][0]:dly_cols[83][1]].strip()},' +
                         f'{line[dly_cols[84][0]:dly_cols[84][1]].strip()},' +
                         f'{line[dly_cols[85][0]:dly_cols[85][1]].strip()},' +
                         f'{line[dly_cols[86][0]:dly_cols[86][1]].strip()},' +
                         f'{line[dly_cols[87][0]:dly_cols[87][1]].strip()},' +
                         f'{line[dly_cols[88][0]:dly_cols[88][1]].strip()},' +
                         f'{line[dly_cols[89][0]:dly_cols[89][1]].strip()},' +
                         f'{line[dly_cols[90][0]:dly_cols[90][1]].strip()},' +
                         f'{line[dly_cols[91][0]:dly_cols[91][1]].strip()},' +
                         f'{line[dly_cols[92][0]:dly_cols[92][1]].strip()},' +
                         f'{line[dly_cols[93][0]:dly_cols[93][1]].strip()},' +
                         f'{line[dly_cols[94][0]:dly_cols[94][1]].strip()},' +
                         f'{line[dly_cols[95][0]:dly_cols[95][1]].strip()},' +
                         f'{line[dly_cols[96][0]:dly_cols[96][1]].strip()},' +
                         f'{line[dly_cols[97][0]:dly_cols[97][1]].strip()},' +
                         f'{line[dly_cols[98][0]:dly_cols[98][1]].strip()},' +
                         f'{line[dly_cols[99][0]:dly_cols[99][1]].strip()},' +
                         f'{line[dly_cols[100][0]:dly_cols[100][1]].strip()},' +
                         f'{line[dly_cols[101][0]:dly_cols[101][1]].strip()},' +
                         f'{line[dly_cols[102][0]:dly_cols[102][1]].strip()},' +
                         f'{line[dly_cols[103][0]:dly_cols[103][1]].strip()},' +
                         f'{line[dly_cols[104][0]:dly_cols[104][1]].strip()},' +
                         f'{line[dly_cols[105][0]:dly_cols[105][1]].strip()},' +
                         f'{line[dly_cols[106][0]:dly_cols[106][1]].strip()},' +
                         f'{line[dly_cols[107][0]:dly_cols[107][1]].strip()},' +
                         f'{line[dly_cols[108][0]:dly_cols[108][1]].strip()},' +
                         f'{line[dly_cols[109][0]:dly_cols[109][1]].strip()},' +
                         f'{line[dly_cols[110][0]:dly_cols[110][1]].strip()},' +
                         f'{line[dly_cols[111][0]:dly_cols[111][1]].strip()},' +
                         f'{line[dly_cols[112][0]:dly_cols[112][1]].strip()},' +
                         f'{line[dly_cols[113][0]:dly_cols[113][1]].strip()},' +
                         f'{line[dly_cols[114][0]:dly_cols[114][1]].strip()},' +
                         f'{line[dly_cols[115][0]:dly_cols[115][1]].strip()},' +
                         f'{line[dly_cols[116][0]:dly_cols[116][1]].strip()},' +
                         f'{line[dly_cols[117][0]:dly_cols[117][1]].strip()},' +
                         f'{line[dly_cols[118][0]:dly_cols[118][1]].strip()},' +
                         f'{line[dly_cols[119][0]:dly_cols[119][1]].strip()},' +
                         f'{line[dly_cols[120][0]:dly_cols[120][1]].strip()},' +
                         f'{line[dly_cols[121][0]:dly_cols[121][1]].strip()},' +
                         f'{line[dly_cols[122][0]:dly_cols[122][1]].strip()},' +
                         f'{line[dly_cols[123][0]:dly_cols[123][1]].strip()},' +
                         f'{line[dly_cols[124][0]:dly_cols[124][1]].strip()},' +
                         f'{line[dly_cols[125][0]:dly_cols[125][1]].strip()},' +
                         f'{line[dly_cols[126][0]:dly_cols[126][1]].strip()},' +
                         f'{line[dly_cols[127][0]:dly_cols[127][1]].strip()}\n')
            outfile.write(csv_line1)


def dly_combine(source_dir, target_path, delete_source_files=False):
    dly_files = list(source_dir.glob("*.dly"))  # only return files - not recursive

    with open(target_path, 'w') as outfile:
        for file in dly_files:
            with file.open("r", encoding="utf-8") as infile:
                for line in infile:
                    outfile.write(line)

    if delete_source_files:
        for file in dly_files:
            os.remove(file)


def dly_combine_us(source_dir, target_path, delete_source_files=False):
    dly_files = list(source_dir.glob("US1*.dly"))  # only return files - not recursive

    with open(target_path, 'w') as outfile:
        for file in dly_files:
            with file.open("r", encoding="utf-8") as infile:
                for line in infile:
                    outfile.write(line)

    if delete_source_files:
        for file in dly_files:
            os.remove(file)


def dly_combine_state(source_dir, target_path, state, delete_source_files=False):
    search = f"US1{state}*.dly"    #US1OKHN0001.dly
    dly_files = list(source_dir.glob(search))  # only return files - not recursive

    with open(target_path, 'w') as outfile:
        for file in dly_files:
            with file.open("r", encoding="utf-8") as infile:
                for line in infile:
                    outfile.write(line)

    if delete_source_files:
        for file in dly_files:
            os.remove(file)