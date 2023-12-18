create table variety_suitable_region
(
    id        int auto_increment
        primary key,
    region    varchar(255)               null,
    province  varchar(100)               null,
    corp_name varchar(10) default '水稻' null
);

