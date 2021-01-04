import pandas as pd
import numpy as np
import os.path

# Define a dictionary containing employee data
course_df = pd.DataFrame(
    columns=[
        'department',  # 0
        'code',  # 1
        'level',  # 2
        'name',  # 3
        'Credit Hours',  #
        'Prerequisites',  #
        'Description',  #
    ]
)


def check_string(many_lines, department, df):
    list_o_lines = list(many_lines[0])
    # print(type(list_o_lines))
    row_n = 0
    for i in range(0, len(list_o_lines)):
        line = list_o_lines[i]
        just_get_me_the_damn_description = 0
        df.at[row_n, 'department'] = department
        if line.startswith(department):
            df.at[row_n, 'code'] = line[:line.find('\t')].replace(' ', '_')
            df.at[row_n, 'level'] = line[str(df.iloc[row_n]['code']).find('_') + 1]
            df.at[row_n, 'name'] = line[line.find('\t'):].strip()
        elif line.startswith('Credit Hours'):
            df.at[row_n, 'Credit Hours'] = line[line.find('\t'):].strip()
        elif line.startswith('Prerequisite'):
            df.at[row_n, 'Prerequisites'] = line[line.find('\t'):].strip().replace(' ', '_')
            just_get_me_the_damn_description = 1
        elif line.startswith('Corequisite'):
            df.at[row_n, 'Corequisite'] = line[line.find('\t'):].strip().replace(' ', '_')
        elif line.startswith('Description'):
            line = list_o_lines[i + 1]
            df.at[row_n, 'Description'] = line.strip()
            row_n += 1
    generated_csv_filename = 'generated_csv/' + department + '.csv'
    course_df.to_csv(generated_csv_filename, index=True)


# constraint_info = '[constraint=false]'

def make_gv_file_bone(filename, LR_TB):
    f = open(filename, 'w+')
    f.write('digraph rank_same {\n')
    if LR_TB == 'LR':
        f.write('\trankdir=LR\n')
    elif LR_TB == 'TB':
        f.write('\trankdir=TB\n')
    for i in range(1, 8):
        f.write('\n\tsubgraph rank' + str(i) + ' {\n\t\trank=same\n\t\t#rank' + str(i) + 'area\n\n\t}')
    f.write('\n\t#edge_area\n\n}')


def line_num_for_phrase_in_file(phrase, filename):
    with open(filename, 'r') as f:
        for (i, line) in enumerate(f):
            if phrase in line:
                return i


def write_phrase_after_line_with_phrase(filename, existing_phrase, phrase_to_add):
    f = open(filename, "r")
    contents = f.readlines()
    f.close()
    contents.insert(line_num_for_phrase_in_file(existing_phrase, filename) + 1, phrase_to_add)
    f = open(filename, "w")
    contents = "".join(contents)
    f.write(contents)
    f.close()


def make_department_parent_nodes_edge(filename, department):
    write_phrase_after_line_with_phrase(filename, 'rankdir=LR', ('\n\t\t' + str(department) + '\n'))
    for i in range(1, 8):
        node_area_tracker = '#rank' + str(i) + 'area'
        edge_area_tracker = '#edge_area'
        write_phrase_after_line_with_phrase(
            filename,
            node_area_tracker,
            ('\n\t\t' + str(department) + str(i) + '\n')
        )
    write_phrase_after_line_with_phrase(
        filename,
        edge_area_tracker,
        (
                '\n\t\t' +
                str(department) + ' -> ' +
                str(department) + '1' + ' -> ' +
                str(department) + '2' + ' -> ' +
                str(department) + '3' + ' -> ' +
                str(department) + '4' + ' -> ' +
                str(department) + '5' + ' -> ' +
                str(department) + '6' + ' -> ' +
                str(department) + '7' + ' -> ' +
                str(department) + '8' +
                '\n'
        )
    )


def add_node_from_df(filename, df):
    for index, row in df.iterrows():
        if (row['level']) == '1':
            write_phrase_after_line_with_phrase(filename, '#rank1area', '\n\t\t' + str(row['code']))
            write_phrase_after_line_with_phrase(filename, '#edge_area',
                                                '\n\t\t' + str(row['department']) + ' -> ' + str(row['code']))
        elif (row['level']) == '2':
            write_phrase_after_line_with_phrase(filename, '#rank2area', '\n\t\t' + str(row['code']))
        # write_phrase_after_line_with_phrase(filename, '#edge_area', '\n\t\t' + str(row['department']) + '1 -> ' + str(row['code']))
        elif (row['level']) == '3':
            write_phrase_after_line_with_phrase(filename, '#rank3area', '\n\t\t' + str(row['code']))
        elif (row['level']) == '4':
            write_phrase_after_line_with_phrase(filename, '#rank4area', '\n\t\t' + str(row['code']))
        elif (row['level']) == '5':
            write_phrase_after_line_with_phrase(filename, '#rank5area', '\n\t\t' + str(row['code']))
        elif (row['level']) == '6':
            write_phrase_after_line_with_phrase(filename, '#rank6area', '\n\t\t' + str(row['code']))
        elif (row['level']) == '7':
            write_phrase_after_line_with_phrase(filename, '#rank7area', '\n\t\t' + str(row['code']))
        elif (row['level']) == '8':
            write_phrase_after_line_with_phrase(filename, '#rank8area', '\n\t\t' + str(row['code']))


def make_prerequisite_edge_from_df(filename, df):
    for every_code in df['code']:
        for index2, row2 in df.iterrows():
            if str(every_code) in str(row2['Prerequisites']) and \
                    str(every_code) != str(row2['code']) and \
                    str(row2['Prerequisites']) != None:
                print(
                    str(every_code), '\t',
                    str(row2['code']), '\t',
                    str(row2['Prerequisites']), '\t'
                )
                write_phrase_after_line_with_phrase(
                    filename,
                    '#edge_area',
                    ('\n\t\t' + str(every_code) + ' -> ' + str(row2['code']) + '\n')
                )
'''
            else:
                write_phrase_after_line_with_phrase(filename,
                                                    '#edge_area',
                                                    '\n\t\t' +
                                                    str(row2['department']) +
                                                    str(row2['code'])[ len(str(row2['department']))+1 : len(str(row2['department']))+2 ] +
                                                    ' -> ' +
                                                    str(row2['code'])
                                                    )
'''


print(course_df)

# make_gv_file_bone(filename='generated.gv', LR_TB='LR')

# data = pd.read_csv('course_txt_from_html/holder.txt', sep="\n", header=None)
# data = pd.read_csv('course_txt_from_html/ARBC.txt', sep="\n", header=None)
# print(data)

'''
data = pd.read_csv('course_txt_from_html/BIOL.txt', sep="\n", header=None)
check_string(data, 'BIOL', course_df)
make_department_parent_nodes_edge('generated.gv', 'BIOL')
add_node_from_df('generated.gv', course_df)
make_prerequisite_edge_from_df('generated.gv', course_df)

data = pd.read_csv('course_txt_from_html/CSC.txt', sep="\n", header=None)
check_string(data, 'CSC', course_df)
make_department_parent_nodes_edge('generated.gv', 'CSC')
add_node_from_df('generated.gv', course_df)
make_prerequisite_edge_from_df('generated.gv', course_df)
'''

# global??
default_gv_filename = 'generated.gv'


def iniate_gv_file_from_txt_import_data_write_to_dataset_then_add_node_n_edge(department):
    default_gv_filename = 'generated.gv'
    make_gv_file_bone(filename=default_gv_filename, LR_TB='LR')
    append_gv_file_from_txt_import_data_write_to_dataset_then_add_node_n_edge(department)


def append_gv_file_from_txt_import_data_write_to_dataset_then_add_node_n_edge(department):
    default_gv_filename = 'generated.gv'
    data = pd.read_csv(
        'course_txt_from_html/' +
        str(department) +
        '.txt', sep="\n", header=None)
    check_string(data, str(department), course_df)
    make_department_parent_nodes_edge(default_gv_filename, str(department))
    add_node_from_df(default_gv_filename, course_df)
    make_prerequisite_edge_from_df(default_gv_filename, course_df)

print(course_df)

iniate_gv_file_from_txt_import_data_write_to_dataset_then_add_node_n_edge('CSC')
#append_gv_file_from_txt_import_data_write_to_dataset_then_add_node_n_edge('MATH')
#append_gv_file_from_txt_import_data_write_to_dataset_then_add_node_n_edge('BIOL')
