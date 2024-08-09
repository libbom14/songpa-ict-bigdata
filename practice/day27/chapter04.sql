/*Ch04 예제*/
/*예제4-1*/
USE 한빛무역;
SELECT COUNT(*)
     , COUNT(고객번호)
     , COUNT(도시)
     , COUNT(지역)
FROM 고객;

/*예제4-2*/
SELECT SUM(마일리지)
     , AVG(마일리지)
     , MIN(마일리지)
     , MAX(마일리지)
FROM 고객;

/*예제4-3*/
SELECT SUM(마일리지)
     , AVG(마일리지)
     , MIN(마일리지)
     , MAX(마일리지)
FROM 고객
WHERE 도시 = '서울특별시';

-- 아래 쿼리는 [42000][1140] 에러가 발생한다.
-- Group By 절에 포함되지 않는 Column (nonaggregated column)을 select 할 경우, 컬럼의 어느 부분에 표시해야 할 지 애매하여 발생하는 에러입니다. (Exception)
SELECT *, SUM(마일리지)
from 고객
where 도시 = '서울특별시';

/*예제4-4*/
SELECT 도시
     , COUNT(*)  AS 고객수
     , AVG(마일리지) AS 평균마일리지
FROM 고객
GROUP BY 도시;

SELECT 도시
     , COUNT(*)  AS 고객수
     , AVG(마일리지) AS 평균마일리지
FROM 고객
GROUP BY 1;

-- 도시별 마일리지 합계와 평균 마일리지
SELECT 도시
     , SUM(마일리지)
     , ROUND(AVG(마일리지)) AS 평균마일리지
FROM 고객
GROUP BY 도시;


/*예제4-5*/
SELECT 담당자직위
     , 도시
     , COUNT(*)  AS 고객수
     , AVG(마일리지) AS 평균마일리지
FROM 고객
GROUP BY 담당자직위
       , 도시
ORDER BY 1, 2;

-- 담당자직위와 광역도시별로 합계, MAX, MIN, 평균 조회
SELECT 담당자직위
     , 도시
     , SUM(마일리지) SUM
     , MAX(마일리지) MAX
     , MIN(마일리지) MIN
     , AVG(마일리지) AVG
FROM 고객
WHERE 도시 LIKE '%광역시'
GROUP BY 담당자직위
       , 도시
ORDER BY 담당자직위
       , 도시;


/*예제4-6*/
SELECT 도시
     , COUNT(*)  AS 고객수
     , AVG(마일리지) AS 평균마일리지
FROM 고객
GROUP BY 도시
HAVING COUNT(*) >= 10;

-- 담당자직위와 광역도시별로 합계, MAX, MIN, 평균 조회
-- GROUP BY의 결과에 대하여 추가 조건 HAVING절 사용
-- SELECT 절에 있는 컬럼과 함수에 대한 조건만 넣을 수 있다.
SELECT 담당자직위
     , 도시
     , SUM(마일리지) SUM
     , MAX(마일리지) MAX
     , MIN(마일리지) MIN
     , AVG(마일리지) AVG
FROM 고객
WHERE 도시 LIKE '%광역시'
GROUP BY 담당자직위
       , 도시
HAVING AVG(마일리지) > 5000
ORDER BY 담당자직위
       , 도시;

/*예제4-7*/
SELECT 도시
     , SUM(마일리지)
FROM 고객
WHERE 고객번호 LIKE 'T%'
GROUP BY 도시
HAVING SUM(마일리지) >= 1000;

/*예제4-8*/
-- WITH ROLLUP: 그룹별 소계와 전체 총계를 한번에 확인하고 싶을때 사용
SELECT 도시
     , COUNT(*)  AS 고객수
     , AVG(마일리지) AS 평균마일리지
FROM 고객
WHERE 지역 IS NULL
GROUP BY 도시
WITH ROLLUP;

SELECT IFNULL(도시, '총계') AS 도시
     , COUNT(*)         AS 고객수
     , AVG(마일리지)        AS 평균마일리지
FROM 고객
WHERE 지역 IS NULL
GROUP BY 도시
WITH ROLLUP;

/*예제4-9*/
SELECT 담당자직위
     , 도시
     , COUNT(*) AS 고객수
FROM 고객
WHERE 담당자직위 LIKE '%마케팅%'
GROUP BY 담당자직위
       , 도시
WITH ROLLUP;

/*예제4-10*/
SELECT 지역
     , COUNT(*) AS 고객수
FROM 고객
WHERE 담당자직위 = '대표 이사'
GROUP BY 지역
WITH ROLLUP;

SELECT 지역
     , COUNT(*)     AS 고객수
     , GROUPING(지역) AS 구분
FROM 고객
WHERE 담당자직위 = '대표 이사'
GROUP BY 지역
WITH ROLLUP;

/* 응용 */
SELECT ifnull(if(grouping(지역) != 1, 지역, '총계'), '--') as 지역
     , COUNT(*)                                      as 고객수
FROM 고객
WHERE 담당자직위 in ('대표 이사')
GROUP BY 지역
WITH ROLLUP;


/*예제4-11*/
SELECT GROUP_CONCAT(이름)
FROM 사원;

/*예제4-12*/
SELECT GROUP_CONCAT(DISTINCT 지역)
FROM 고객;

/*예제4-13*/
SELECT 도시
     , GROUP_CONCAT(고객회사명) AS 고객회사명목록
FROM 고객
GROUP BY 도시;
