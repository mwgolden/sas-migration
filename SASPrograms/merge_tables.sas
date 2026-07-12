proc sort data=customers;
    by customer_id;
run;

proc sort data=orders;
    by customer_id;
run;

data customer_orders;
    merge customers(in=a)
          orders(in=b);
    by customer_id;

    if a and b;
run;