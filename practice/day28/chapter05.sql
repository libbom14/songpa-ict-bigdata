/*예제5-3*/
/*ANSI SQL*/
SELECT 고객.고객번호
     , 담당자명
     , 고객회사명
     , COUNT(*) AS 주문건수
FROM 고객
         INNER JOIN 주문
                    ON 고객.고객번호 = 주문.고객번호
GROUP BY 고객.고객번호
       , 담당자명
       , 고객회사명
ORDER BY COUNT(*) DESC;

/*Non-ANSI SQL*/
SELECT 고객.고객번호
     , 담당자명
     , 고객회사명
     , COUNT(*) AS 주문건수
FROM 고객
   , 주문
WHERE 고객.고객번호 = 주문.고객번호
GROUP BY 고객.고객번호
       , 담당자명
       , 고객회사명
ORDER BY COUNT(*) DESC;

/*예제5-4*/
/*ANSI SQL*/
SELECT 고객.고객번호
     , 담당자명
     , 고객회사명
     , SUM(주문수량 * 단가) AS 주문금액합
FROM 고객
         INNER JOIN 주문
                    ON 고객.고객번호 = 주문.고객번호
         INNER JOIN 주문세부
                    ON 주문.주문번호 = 주문세부.주문번호
GROUP BY 고객.고객번호
       , 담당자명
       , 고객회사명
ORDER BY 4 DESC;

/*Non-ANSI SQL*/
SELECT 고객.고객번호
     , 담당자명
     , 고객회사명
     , SUM(주문수량 * 단가) AS 주문금액합
FROM 고객
   , 주문
   , 주문세부
WHERE 고객.고객번호 = 주문.고객번호
  AND 주문.주문번호 = 주문세부.주문번호
GROUP BY 고객.고객번호
       , 담당자명
       , 고객회사명
ORDER BY 4 DESC;

/*예제5-5*/
/*ANSI SQL*/
SELECT 고객번호
     , 담당자명
     , 마일리지
     , 등급.*
FROM 고객
         CROSS JOIN 마일리지등급 AS 등급
WHERE 담당자명 = '이은광';

/*Non-ANSI SQL*/
SELECT 고객번호
     , 담당자명
     , 마일리지
     , 등급.*
FROM 고객
   , 마일리지등급 AS 등급
WHERE 담당자명 = '이은광';

/*예제5-6*/
/*ANSI SQL*/
SELECT 고객번호
     , 고객회사명
     , 담당자명
     , 마일리지
     , 등급명
FROM 고객
         INNER JOIN 마일리지등급
                    ON 마일리지 >= 하한마일리지
                        AND 마일리지 <= 상한마일리지
WHERE 담당자명 = '이은광';

/*Non-ANSI SQL*/
SELECT 고객번호
     , 고객회사명
     , 담당자명
     , 마일리지
     , 등급명
FROM 고객
   , 마일리지등급
WHERE 마일리지 BETWEEN 하한마일리지 AND 상한마일리지
  AND 담당자명 = '이은광';

/*예제5-7*/
SELECT 사원번호
     , 이름
     , 부서명
FROM 사원
         LEFT OUTER JOIN 부서
                         ON 사원.부서번호 = 부서.부서번호
WHERE 성별 = '여';

/*예제5-8*/
SELECT 부서명
     , 사원.*
FROM 사원
         RIGHT OUTER JOIN 부서
                          ON 사원.부서번호 = 부서.부서번호;

/*예제5-9*/
SELECT 부서명
     , 사원.*
FROM 사원
         RIGHT OUTER JOIN 부서
                          ON 사원.부서번호 = 부서.부서번호
WHERE 사원.부서번호 IS NULL;

/*예제5-10*/
SELECT 이름
     , 부서.*
FROM 사원
         LEFT OUTER JOIN 부서
                         ON 사원.부서번호 = 부서.부서번호
WHERE 부서.부서번호 IS NULL;


-- Self Join
/*예제5-11*/
/*ANSI SQL*/
SELECT 사원.사원번호
     , 사원.이름
     , 상사.사원번호 AS '상사의 사원번호'
     , 상사.이름   AS '상사의 이름'
FROM 사원
         INNER JOIN 사원 AS 상사
                    ON 사원.상사번호 = 상사.사원번호;

/*Non-ANSI SQL*/
SELECT 사원.사원번호
     , 사원.이름
     , 상사.사원번호 AS '상사의 사원번호'
     , 상사.이름   AS '상사의 이름'
FROM 사원
   , 사원 AS 상사
WHERE 사원.상사번호 = 상사.사원번호;


/*SCOTT에 응용 - 상사가 없는 사원은 제외*/
-- Non-ANSI join, from 정의, -> join
SELECT E.EMPNO 사원번호, E.ENAME 사원명, M.EMPNO 상사사번, M.ENAME 상사이름
FROM scott.EMP E,
     scott.EMP M
WHERE E.EMPNO = M.DEPTNO;
-- ANSI join, from 정의, -> join
SELECT E.EMPNO 사원번호, E.ENAME 사원명, M.EMPNO 상사사번, M.ENAME 상사이름
FROM scott.EMP E
         JOIN scott.EMP M
              ON E.EMPNO = M.DEPTNO;


/*예제5-12*/
SELECT 사원.이름 AS 이름
     , 사원.직위
     , 상사.이름 AS 상사이름
FROM 사원 AS 상사
         RIGHT OUTER JOIN 사원
                          ON 사원.상사번호 = 상사.사원번호
ORDER BY 상사이름;


/*SCOTT에 응용 - 상사가 없는 사원은 제외*/
SELECT E.EMPNO 사원번호, E.ENAME 사원명, M.EMPNO 상사사번, M.ENAME 상사이름
FROM scott.EMP E
         LEFT OUTER JOIN scott.EMP M
                         ON E.MGR = M.EMPNO;
-- 상사보다 급여가 더 많은 사원 조회
SELECT E.EMPNO 사원번호, E.ENAME 사원명, M.EMPNO 상사사번, M.ENAME 상사이름, E.SAL
FROM scott.EMP E
         LEFT OUTER JOIN scott.EMP M
                         ON E.MGR = M.EMPNO
WHERE E.SAL > M.SAL;


-- 테이블 3개 조인
SELECT E.ENAME, D.DNAME, D.LOC, E.SAL, S.GRADE
FROM scott.EMP E
         JOIN scott.DEPT D ON E.DEPTNO = D.DEPTNO
         JOIN scott.SALGRADE S ON E.SAL BETWEEN S.LOSAL AND S.HISAL
WHERE E.SAL > 2000;