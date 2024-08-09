/*복습*/
USE SCOTT;
SELECT ENAME
     , HIREDATE
     , YEAR(HIREDATE)  AS 입사년도
     , MONTH(HIREDATE) AS 입사월
FROM EMP
ORDER BY 입사월, 입사년도;

/*예제3-23*/
-- IF(조건1, 참일 경우 수식, 거짓일 경우 수식)
SELECT IF(12500 * 450 > 5000000, '초과달성', '미달성');

/*예제3-24*/
-- IFNULL(NULL이 아닐 경우 수식1, NULL일 경우 수식2)
SELECT IFNULL(1, 0)
     , IFNULL(NULL, 0)
     , IFNULL(1 / 0, 'OK');

/*예제3-25*/
-- NULLIF(수식1, 수식2)
-- 수식1==수식2, return NULL
-- 수식1!=수식2, return 수식1
SELECT NULLIF(12 * 10, 120)
     , NULLIF(12 * 10, 1200);

/*SCOTT에 응용*/
SELECT ENAME
     , HIREDATE
     , SAL
     , COMM
     , SAL + COMM   -- commision이 NULL일 경우 제대로 계산되지 않음
     , SAL + IFNULL(COMM, 0) 급여합 -- commision이 NULL일 경우 0으로 계산
FROM EMP
ORDER BY 급여합;


/*예제3-26*/
SELECT CASE
           WHEN 12500 * 450 > 5000000 THEN '초과달성'
           WHEN 2500 * 450 > 4000000 THEN '달성'
           ELSE '미달성'
           END;

/*한빛무역에 응용*/
use 한빛무역;
SELECT 고객회사명
     , 마일리지
     , CASE
           WHEN 마일리지 > 10000 then '골드'
           WHEN 마일리지 > 5000 then '실버'
    END AS 등급
FROM 고객
ORDER BY 등급;