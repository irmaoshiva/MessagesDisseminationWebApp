drop table if exists messages;
drop table if exists users;
drop table if exists building;


create table building(
  id integer,
  name varchar(255),
  lat numeric(8,6),
  longit numeric(8,6),
  primary key(id)
);

create table messages(
  id integer,
  message varchar(255), 
  building_id integer,
  creation date, 
  primary key(id),
  foreign key(building_id) references building(id)
);

create table users(
  name varchar(255),
  istid varchar(255),
  build_id integer,
  range_user integer,
  lat numeric(8,6),
  longit numeric(8,6),
  primary key(istid),
  foreign key(build_id) references building(id)

);

