create table users(
user_id int primary key,
name varchar(50),
location varchar(50),
city varchar(50),
state_province varchar(50),
country_name varchar(50),
country_code varchar(10),
user_url varchar(300));

create table organizations(
organization_id int primary key,
name varchar(50),
location varchar(50),
address varchar(50),
city varchar(50),
state_province varchar(50),
postal_code varchar(50),
country_name varchar(50),
country_code varchar(50),
website varchar(300),
mission text,
organization_url varchar(300));

create table target(
ID int auto_increment primary key,
name varchar(50),
title text,
type varchar(50),
target_area varchar(50));






create table petitions(
petition_id int primary key,
title text,
status_petition varchar(30),
url varchar(300),
target_id int,
letter_body text,
signature_count int,
imager_url varchar(300),
category varchar(50),
goal int,
created_at datetime,
end_at datetime,
user_id int,
organization_id int,
foreign key(user_id) references users(user_id),
foreign key(organization_id) references organizations(organization_id));

create table signatures(
ID int auto_increment primary key,
name varchar(50),
city varchar(50),
state varchar(50),
country varchar(50),
country_code varchar(10),
signed_on datetime,
phone varchar(10),
reason text,
petition_id int,
user_id int,
foreign key(petition_id) references petitions(petition_id),
foreign key(user_id) references users(user_id));

create table target_petition(
ID int auto_increment primary key,
petition_id int,
target_id int,
foreign key(petition_id)  references petitions(petition_id),
foreign key(target_id) references target(ID));

create table reasons (
ID int auto_increment primary key,
created_on datetime,
content text,
like_count int,
author_name varchar(50),
author_url varchar(300),
petition_id int,
foreign key (petition_id) references petitions(petition_id));

create table updates (
ID int auto_increment primary key,
created_on datetime,
content text,
author_name varchar(50),
author_url varchar(300),
petition_id int,
foreign key (petition_id) references petitions(petition_id));



