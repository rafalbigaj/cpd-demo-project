CREATE TABLE input.trades
(
    account bigint,
    date text COLLATE pg_catalog."default",
    volume bigint,
    period text COLLATE pg_catalog."default",
    isin text COLLATE pg_catalog."default"
)


CREATE TABLE input.account_info
(
    account bigint,
    candidate boolean
)


CREATE TABLE output.scores
(
    account bigint,
    dbscan bigint,
    cpu_calculation numeric,
    gpu_calculation numeric,
    run_id text COLLATE pg_catalog."default",
    version text COLLATE pg_catalog."default",
    isin text COLLATE pg_catalog."default",
    start_date text COLLATE pg_catalog."default",
    end_date text COLLATE pg_catalog."default",
)
