
Download the csv of exam results from gradescope into the same director as the .py script.  Also make a csv file of the maximum points by question.  The first row should be the names of the questions, exactly matching the names in the gradescope csv.  The second row should be the maximum points for each question (see example mt2_maxes.csv).  You also need a roster file which should be a csv with the names of the students for your section, one on each line. Change the variable at the top of exam_csv_processor.py to match the name of your roster file.

run the script with:
```
python exam_csv_processor.py <gradescope_csv_file> <maximum_points_file>
```
Right now it just prints class mean/median for each problem and the total score, and the same information for your section, as well as the differences between your section and the class.  It should be fairly easy to extend the functionality
