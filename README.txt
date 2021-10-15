DESCRIPTION
-----------
Ranking is an object performs various evaluation metrics
on a set of queries and their judgement scores. It's
constructor is given a judgement file with the format:
    'query' 'url' 'judgment score'
The column values are separated by a single space. The
query data used to perform the metrics on is a sample of
anonymized Yahoo search data.

HOW TO RUN
----------
Run the python command :
    python3 assignment3.py
Follow the prompts the program gives you. The script will
print out the scores of each metric. Ctrl + c will
terminate the program.