import sys
import csv
# import numpy as np
# import statistics

#######################################
# Make sure these match the csv file #
#######################################
roster_file_name = "myroster.csv"
name_column_title = "Name"
total_column = "Total Score"
#######################################
    
def read_max_points(exam_max_points_csv):
    points_available = {}
    with open(exam_max_points_csv, 'r') as csvfile:
        csv_scan = csv.reader(csvfile)
        header = next(csv_scan)
        point_vals = next(csv_scan)
        for i in range(len(header)):
            points_available[header[i]] = float(point_vals[i])
    return points_available, header
    
def get_general_data(exam_results_csv, max_dict):
    data = {}
    question_to_index = {}
    with open(exam_results_csv, 'r') as csvfile:
        csv_scan = csv.reader(csvfile)
        header = next(csv_scan)
        for question_name in max_dict.keys():
            data[question_name] = []
            question_to_index[question_name] = header.index(question_name)
        # name_column_index = header.index(name_column_title)
        for student_entry in csv_scan:
            # name = student_entry[name_column_index]
            for question_name in data.keys():
                data[question_name].append(float(student_entry[question_to_index[question_name]]))
    return data
    
def get_section_data(exam_results_csv, max_dict, roster_file):
    data = {}
    question_to_index = {}
    section_roster = set()
    with open(roster_file, 'r') as csvfile:
        csv_scan = csv.reader(csvfile)
        for student_entry in csv_scan:
            section_roster.add(student_entry[0].strip(' '))
    with open(exam_results_csv, 'r') as csvfile:
        csv_scan = csv.reader(csvfile)
        header = next(csv_scan)
        for question_name in max_dict.keys():
            data[question_name] = []
            question_to_index[question_name] = header.index(question_name)
            name_column_index = header.index(name_column_title)
        for student_entry in csv_scan:
            name = student_entry[name_column_index]
            if name in section_roster:
                for question_name in data.keys():
                    data[question_name].append(float(student_entry[question_to_index[question_name]]))
    return data
    
def print_class_stats(data, question_titles):
    for title in question_titles:
        print(title)
        d = data[title]
        print("Median: {}\nMean: {}".format(median(d), mean(d)))
        # print("Median: {}\nMean: {}\nStandard deviation: {}".format(statistics.median(d), statistics.mean(d), statistics.stdev(d)))
        # d = np.array(data[title])
        # print("Median: {}\nMean: {}\nStandard deviation: {}".format(np.median(d), np.mean(d), np.stdev(d)))
       
def mean(lst):
    total = 0.0
    count = 0.0
    for n in lst:
        total += n
        count += 1.0
    return total / count
        
def median(lst):
    #slow
    lst.sort()
    return lst[len(lst)//2]
    
def print_diff(data1, data2, question_titles):
    for title in question_titles:
        print(title)
        d1 = data1[title]
        d2 = data2[title]
        print("Median difference: {}\nMean difference: {}".format(median(d2)-median(d1), mean(d2)-mean(d1)))
        # print("Median: {}\nMean: {}\nStandard deviation: {}".format(statistics.median(d), statistics.mean(d), statistics.stdev(d)))
        # d = np.array(data[title])
        # print("Median: {}\nMean: {}\nStandard deviation: {}".format(np.median(d), np.mean(d), np.stdev(d)))
    
if __name__ == "__main__":
    exam_results_csv = sys.argv[1]
    exam_max_points_csv = sys.argv[2]
    max_dict, question_titles = read_max_points(exam_max_points_csv)
    class_data = get_general_data(exam_results_csv, max_dict)
    section_data = get_section_data(exam_results_csv, max_dict, roster_file_name)
    print("\nClasswide: ")
    print_class_stats(class_data, question_titles)
    print("\nMy section: ")
    print_class_stats(section_data, question_titles)
    print("\nDifference between my section and class: ")
    print_diff(class_data, section_data, question_titles)
    