SELECT fares.*, ca.amtrakcity as amtrakorig, cd.amtrakcity as amtrakdest FROM fares
LEFT JOIN cities ca ON fares.orig = ca.mbcity
LEFT JOIN cities cd ON fares.dest = cd.mbcity
where datescraped = '4/21/2016'
order by id
limit 10

select * from fares

select * from cities

where dest = 'Montgomery, AL'

/*Check number of rows per datescraped in database*/
select datescraped, count(fare) from fares
group by datescraped
order by datescraped

/*Check number of rows in database*/
select count(*) from fares