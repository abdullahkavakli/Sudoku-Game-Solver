import pyodbc 
import ast
import sudokusolver


def choose_random():

    cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=DESKTOP-1IRMV7Q;"
                      "Database=PythonList;"
                      "Trusted_Connection=yes;")


    cursor = cnxn.cursor()
    cursor.execute('SELECT top 1 List FROM tbl_main order by newid()')

    for row in cursor:
        a=ast.literal_eval(row[0] )

    return a

choose_random()
    
#to solve arbitrarily sudoku from DB
#print(sudokusolver.take_the_board_and_solve(a))


