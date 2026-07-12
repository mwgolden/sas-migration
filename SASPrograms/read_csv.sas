/* Read a CSV file */
proc import
    datafile="C:\data\customers.csv"
    out=work.customers
    dbms=csv
    replace;
    guessingrows=max;
run;

/* Display first 10 rows */
proc print data=work.customers(obs=10);
run;