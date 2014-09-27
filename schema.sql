drop table if exists chain_freqs;
create table chain_freqs (
    id integer primary key autoincrement not null,
    prefix1 text not null,
    prefix2 text not null,
    suffix text not null,
    freq integer not null
);
