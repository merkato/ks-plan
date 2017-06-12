CREATE SCHEMA grafik;

CREATE TABLE grafik.holidays (termin date, opis varchar, wariant varchar(2));
INSERT INTO grafik.holidays VALUES ('2017-06-17','Boże Ciało', 'C')

CREATE TABLE grafik.pociagi(plan varchar, 
obieg varchar, nr_poc varchar, termin array, wyklucz array, dolacz array, wariant varchar, 
st_pocz varchar, st_konc varchar, godz_pocz time, godz_konc, tabor enum);

INSERT INTO grafik.pociagi VALUES
('K65', '49712', '2017-06-12,2017-07-07','2017-06-16', '', 'D', 'Żywiec', 'Katowice', '5:45','7:40','EN76'),
('K65', '40919', '2017-06-12,2017-07-07','2017-06-16', '', 'D', 'Katowice', 'Tychy Lodowisko', '8:16','8:47','57AKS'),
('K65', '44004', '2017-06-12,2017-07-07','2017-06-16', '', 'D', 'Tychy Lodowisko', 'Katowice', '9:41','10:08','EN76')
