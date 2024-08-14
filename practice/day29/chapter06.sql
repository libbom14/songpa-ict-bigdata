/*Ch06 예제*/
/*예제6-1*/
-- 최고 마일리지 정보
SELECT MAX(마일리지)
FROM 고객;
-- 최고 마일리지를 보유한 고객의 정보
SELECT 고객번호
     , 고객회사명
     , 담당자명
     , 마일리지
FROM 고객
WHERE 마일리지 = (SELECT MAX(마일리지)
              FROM 고객);

/*예제6-2*/
-- 주문번호 = 'H0250'을 주문한 고객에 대해 고객회사명과 담당자명 조회
SELECT 고객회사명
     , 담당자명
FROM 고객
WHERE 고객번호 = (SELECT 고객번호
              FROM 주문
              WHERE 주문번호 = 'H0250');

SELECT 고객회사명
     , 담당자명
FROM 고객
         INNER JOIN 주문
                    ON 고객.고객번호 = 주문.고객번호
WHERE 주문번호 = 'H0250';

/*예제6-3*/
SELECT 담당자명
     , 고객회사명
     , 마일리지
FROM 고객
WHERE 마일리지 > (SELECT MIN(마일리지)
              FROM 고객
              WHERE 도시 = '부산광역시');

/*예제6-4*/
SELECT COUNT(*) AS 주문건수
FROM 주문
WHERE 고객번호 IN (SELECT 고객번호
               FROM 고객
               WHERE 도시 = '부산광역시');

/*SCOTT에 응용*/
SELECT *
FROM scott.EMP E
WHERE (DEPTNO, SAL) IN (SELECT DEPTNO, MAX(SAL) FROM scott.EMP GROUP BY DEPTNO);
;

/*예제6-5*/
-- ANY : 다중 행 연산자. 조건을 만족하는 값이 하나라도 있다면 결과를 리턴
-- 즉 부산광역시 데이터중 가장 작은 마일리지 806 보다 큰 데이터가 리턴
SELECT 마일리지
FROM 고객
WHERE 도시 = '부산광역시';

SELECT 담당자명
     , 고객회사명
     , 마일리지
FROM 고객
WHERE 마일리지 > ANY (SELECT 마일리지
                  FROM 고객
                  WHERE 도시 = '부산광역시');
-- ANY -> WHERE 마일리지 > 2819 or 마일리지 > 806 or 마일리지 > 7795 or 마일리지 > 1177 or 마일리지 > 7329
-- 결국 ANY는 나올 수 있는 모든 조건에 OR 연산을 수행한것과 동일한 결과를 얻는다.
-- ALL -> WHERE 마일리지 > 2819 and 마일리지 > 806 and 마일리지 > 7795 and 마일리지 > 1177 and 마일리지 > 7329
-- 결국 ALL은  나올 수 있는 모든 조건에 AND 연산을 수행한것과 동일한 결과를 얻는다.

/*예제6-6*/
-- ALL : 다중 행 연산자. 모든조건을 만족하는 결과를 리턴
-- 즉 부산광역시 데이터중 가장 작은 마일리지 806 보다 큰 데이터가 리턴
-- > 와 같이 쓰면 MAX
SELECT 담당자명
     , 고객회사명
     , 마일리지
FROM 고객
WHERE 마일리지 > ALL (SELECT AVG(마일리지)
                  FROM 고객
                  GROUP BY 지역);


/*예제6-7*/
SELECT 고객번호
     , 고객회사명
FROM 고객
WHERE EXISTS (SELECT *
              FROM 주문
              WHERE 고객번호 = 고객.고객번호);

SELECT 고객번호
     , 고객회사명
FROM 고객
WHERE 고객번호 IN (SELECT DISTINCT 고객번호
               FROM 주문);

SELECT DISTINCT 고객.고객번호
              , 고객회사명
FROM 고객
         INNER JOIN 주문
                    ON 고객.고객번호 = 주문.고객번호;

/*예제6-8*/
SELECT 도시
     , AVG(마일리지) AS 평균마일리지
FROM 고객
GROUP BY 도시
HAVING AVG(마일리지) > (SELECT AVG(마일리지)
                    FROM 고객);

/*예제6-9*/
SELECT 담당자명
     , 고객회사명
     , 마일리지
     , 고객.도시
     , 도시_평균마일리지
     , 도시_평균마일리지 - 마일리지 AS 차이
FROM 고객
   , (SELECT 도시
           , AVG(마일리지) AS 도시_평균마일리지
      FROM 고객
      GROUP BY 도시) AS 도시별요약
WHERE 고객.도시 = 도시별요약.도시;

/*예제6-10*/
SELECT 고객번호
     , 담당자명
     , (SELECT MAX(주문일)
        FROM 주문
        WHERE 주문.고객번호 = 고객.고객번호) AS 최종주문일
FROM 고객;

/*예제6-11*/
WITH 도시별요약 AS
         (SELECT 도시
               , AVG(마일리지) AS 도시_평균마일리지
          FROM 고객
          GROUP BY 도시)

SELECT 담당자명
     , 고객회사명
     , 마일리지
     , 고객.도시
     , 도시_평균마일리지
     , 도시_평균마일리지 - 마일리지 AS 차이
FROM 고객
   , 도시별요약
WHERE 고객.도시 = 도시별요약.도시;

/*예제6-12*/
SELECT 사원번호
     , 이름
     , 상사번호
     , (SELECT 이름
        FROM 사원 AS 상사
        WHERE 상사.사원번호 = 사원.상사번호) AS 상사이름
FROM 사원;

/*예제6-13*/
SELECT 도시
     , 담당자명
     , 고객회사명
     , 마일리지
FROM 고객
WHERE (도시, 마일리지) IN (SELECT 도시, MAX(마일리지)
                     FROM 고객
                     GROUP BY 도시);