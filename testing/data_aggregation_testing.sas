/* Connect to SQL database */
libname mydblib odbc dsn='your_dsn' user='your_username' password='your_password';

/* Read data from SQL database */
proc sql;
    create table work.mydata as 
    select *
    from mydblib.your_table;
quit;

/* Save data to CSV file */
proc export data=work.mydata
    outfile="mydata.csv"
    dbms=csv
    replace;
run;

/* Read data from CSV file */
proc import datafile="mydata.csv"
    out=work.mydata
    dbms=csv
    replace;
run;

/* Perform operations */
data work.mydata;
    set work.mydata;
    
    /* Column selection */
    column1 = column1;
    
    /* Row selection */
    if _N_ >= 10 and _N_ <= 20;
    
    /* Filtering */
    if column1 > 50;
    
    /* Sorting */
    proc sort data=work.mydata;
        by column1;
    run;
    
    /* Grouping */
    proc means data=work.mydata;
        by column1;
        var column2;
    run;
    
    /* Merging */
    data work.mydata_merged;
        merge work.mydata(in=a) work.mydata(in=b);
        by column1;
    run;
    
    /* Value counts */
    proc freq data=work.mydata;
        tables column1 / nocum nopercent;
    run;
    
    /* Duplicated */
    /* Drop duplicates */
    /* Missing values */
    /* Type casting */
    /* Applying functions */
    /* String operations */
    /* Date/Time operations */
    /* Binning data */
    /* Reshaping data */
    /* Descriptive statistics */
    /* Vectorized operations */
    
    /* Save final results */
    proc export data=work.mydata
        outfile="mydata_final.csv"
        dbms=csv
        replace;
run;

