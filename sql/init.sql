CREATE TABLE public.users (
  user_id serial not null primary key,
  user_name VARCHAR(6) NULL,
  user_username VARCHAR(45) NULL,
  user_password VARCHAR(45) NULL);

CREATE TABLE IF NOT EXISTS public.holidays (
  id serial primary key,
  termin date,
  opis varchar(100),
  wariant varchar(2));

CREATE TABLE public.pociagi (
  plan varchar(4),
  obieg varchar(2),
  nr_poc varchar(7),
  termin date array[2],
  wyklucz date array,
  dolacz date array,
  wariant varchar(2),
  st_pocz varchar(40),
  st_konc varchar(40),
  godz_pocz time,
  godz_konc time,
  tabor varchar(10));

CREATE TABLE public.sluzby (
  id serial primary key not null,
  plan varchar(4),
  st_pocz varchar(40),
  godz_pocz time,
  godz_konc time,
  termin date array[2],
  wariant varchar(2));
