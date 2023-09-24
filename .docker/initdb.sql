create table products (
    id int not null,
    name varchar(50) not null,
    space float not null,
    value float not null,
    quantity int not null
);

alter table products add constraint pk_products primary key (id);
create sequence seq_product_id increment 1 start 1;

insert into products (id, name, space, value, quantity) 
values (nextval('seq_product_id'), 'Geladeira Dako', 0.751, 999.90, 1);

insert into products (id, name, space, value, quantity) 
values (nextval('seq_product_id'), 'Iphone 6', 0.0000899, 2911.12, 5);

insert into products (id, name, space, value, quantity) 
values (nextval('seq_product_id'), 'TV 55', 0.400, 4346.99, 2);

insert into products (id, name, space, value, quantity) 
values (nextval('seq_product_id'), 'TV 50', 0.290, 3999.90, 3);

insert into products (id, name, space, value, quantity) 
values (nextval('seq_product_id'), 'TV 42', 0.200, 2999.00, 4);

insert into products (id, name, space, value, quantity) 
values (nextval('seq_product_id'), 'Notebook Dell', 0.00350, 2499.90, 1);

insert into products (id, name, space, value, quantity) 
values (nextval('seq_product_id'), 'Ventilador Panasonic', 0.496, 199.90, 10);

insert into products (id, name, space, value, quantity) 
values (nextval('seq_product_id'), 'Microondas Electrolux', 0.0424, 308.66, 3);

insert into products (id, name, space, value, quantity) 
values (nextval('seq_product_id'), 'Microondas LG', 0.0544, 429.90, 3);

insert into products (id, name, space, value, quantity) 
values (nextval('seq_product_id'), 'Microondas Panasonic', 0.0319, 299.29, 2);

insert into products (id, name, space, value, quantity) 
values (nextval('seq_product_id'), 'Geladeira Brastemp', 0.635, 849.00, 1);

insert into products (id, name, space, value, quantity) 
values (nextval('seq_product_id'), 'Geladeira Consul', 0.870, 1199.89, 2);

insert into products (id, name, space, value, quantity) 
values (nextval('seq_product_id'), 'Notebook Lenovo', 0.498, 1999.90, 10);

insert into products (id, name, space, value, quantity) 
values (nextval('seq_product_id'), 'Notebook Asus', 0.527, 3999.00, 15);
