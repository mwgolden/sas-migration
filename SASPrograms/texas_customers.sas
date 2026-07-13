libname sales "/data/sales";

data customers;
    set sales.customer;
    where state="TX";
    full_name = catx(" ", first_name, last_name);
run;