DROP SCHEMA IF EXISTS 서울지하철;
DROP DATABASE IF EXISTS 서울지하철;

CREATE SCHEMA 서울지하철 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_bin;

use 서울지하철;

# jihaceolgonggijil TABLE COLUMN data type 수정
alter table jihaceolgonggijil
    modify column 호선명 varchar(30);
alter table jihaceolgonggijil
    modify column 시도명 varchar(30);
alter table jihaceolgonggijil
    modify column 시군구명 varchar(30);
alter table jihaceolgonggijil
    modify column 역명 varchar(30);
alter table jihaceolgonggijil
    add primary key (호선명, 역명);

# jihaceolseunghaca TABLE COLUMN data type 수정
alter table jihaceolseunghaca
    modify column 사용일자 DATE;
alter table jihaceolseunghaca
    modify column 호선명 varchar(30);
alter table jihaceolseunghaca
    modify column 역명 varchar(30);
alter table jihaceolseunghaca
    add primary key (사용일자, 호선명, 역명);

-- 요일별 승하차 승객수 합
SELECT MONTH(사용일자)           월
     , WEEKDAY(사용일자)         정수요일
     , CASE WEEKDAY(사용일자)
           WHEN 0 THEN '월요일'
           WHEN 1 THEN '화요일'
           WHEN 2 THEN '수요일'
           WHEN 3 THEN '목요일'
           WHEN 4 THEN '금요일'
           WHEN 5 THEN '토요일'
           WHEN 6 THEN '일요일'
    END                   AS 요일
     , SUM(승차승객수 + 하차승객수) AS 승하차승객수합
FROM jihaceolseunghaca
WHERE 호선명 = '2호선'
GROUP BY MONTH(사용일자), WEEKDAY(사용일자),
         CASE WEEKDAY(사용일자)
             WHEN 0 THEN '월요일'
             WHEN 1 THEN '화요일'
             WHEN 2 THEN '수요일'
             WHEN 3 THEN '목요일'
             WHEN 4 THEN '금요일'
             WHEN 5 THEN '토요일'
             WHEN 6 THEN '일요일'
             END;

create table 요일
(
    weekno int primary key,
    name   varchar(20),
    e_name varchar(20)
);
desc 요일;

insert into 요일
values (0, '월요일', 'Monday');
insert into 요일
values (1, '화요일', 'Tuesday');
insert into 요일
values (2, '수요일', 'Wednesday');
insert into 요일
values (3, '목요일', 'Thursday');
insert into 요일
values (4, '금요일', 'Friday');
insert into 요일
values (5, '토요일', 'Saturday');
insert into 요일
values (6, '일요일', 'Sunday');
commit;
select *
from 요일;


--

SELECT MONTH(사용일자)           월
     , WEEKDAY(사용일자)         정수요일
     , name               AS 요일
     , SUM(승차승객수 + 하차승객수) AS 승하차승객수합
FROM 서울지하철.jihaceolseunghaca,
     요일
WHERE weekday(사용일자) = weekno
  and 호선명 = '2호선'
GROUP BY MONTH(사용일자), WEEKDAY(사용일자), NAME
ORDER BY 1, 2;