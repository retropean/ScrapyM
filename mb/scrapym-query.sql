SELECT fares.*, ca.amtrakcity as amtrakorig, cd.amtrakcity as amtrakdest FROM fares
LEFT JOIN cities ca ON fares.orig = ca.mbcity
LEFT JOIN cities cd ON fares.dest = cd.mbcity
order by id

select * from fares

select * from cities

where dest = 'Montgomery, AL'