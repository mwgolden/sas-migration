data work.employee_clean;
    set work.employee_raw;

    full_name = catx(' ', first_name, last_name);

    annual_salary = monthly_salary * 12;

    if annual_salary >= 100000 then salary_band = "High";
    else if annual_salary >= 50000 then salary_band = "Medium";
    else salary_band = "Low";

    hire_year = year(hire_date);

    keep employee_id full_name annual_salary salary_band hire_year;
run;