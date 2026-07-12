libname src oracle
    user=user
    password=pwd
    path=PROD;

libname tgt oracle
    user=user
    password=pwd
    path=DW;

/* Read source */
data policy;
    set src.policy_master;

    where status='ACTIVE';

    premium_amt = premium * 12;

    if missing(agent_id) then
        agent_id = 0;
run;

/* Aggregate */
proc sql;
create table premium_summary as
select
    state,
    count(*) as policies,
    sum(premium_amt) as total_premium
from policy
group by state;
quit;

/* Load target */
data tgt.policy_summary;
    set premium_summary;
run;