data high_value_orders;
    set orders;

    where amount > 1000
          and order_date >= '01JAN2025'd;
run;