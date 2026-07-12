proc freq data=customers;
    tables state
           gender
           account_type;
run;