/*Ch05 예제*/
/*예제5-1*/
/*ANSI SQL*/
SELECT 부서.부서번호
     , 부서명
     , 이름
     , 사원.부서번호
FROM 부서
         CROSS JOIN 사원
WHERE 이름 = '배재용';

/*SCOTT에 응용*/
USE SCOTT;
-- ANSI join, from 정의, -> join, join 조건 -> on
SELECT ENAME, EMP.DEPTNO, DNAME, LOC
FROM EMP
         JOIN DEPT
              ON EMP.DEPTNO = DEPT.DEPTNO;

/*Non-ANSI SQL*/
SELECT 부서.부서번호
     , 부서명
     , 이름
     , 사원.부서번호
FROM 부서
   , 사원
WHERE 이름 = '배재용';

/*SCOTT에 응용*/
USE SCOTT;
-- Non-ANSI join, from 정의, -> join, join 조건 -> WHERE
SELECT E.ENAME, E.DEPTNO, D.DNAME, D.LOC
FROM EMP E,
     DEPT D
WHERE E.DEPTNO = D.DEPTNO;

/*예제5-2*/
/*ANSI SQL*/
SELECT 사원번호
     , 직위
     , 사원.부서번호
     , 부서명
FROM 사원
         INNER JOIN 부서
                    ON 사원.부서번호 = 부서.부서번호
WHERE 이름 = '이소미';
/*SCOTT에 응용*/
USE SCOTT;
-- ANSI join, from 정의, -> join, join 조건 -> on
SELECT ENAME, EMP.DEPTNO, DNAME, LOC
FROM EMP
         INNER JOIN DEPT
                    ON EMP.DEPTNO = DEPT.DEPTNO
WHERE SAL > 3000;

/*Non-ANSI SQL*/
SELECT 사원번호
     , 직위
     , 사원.부서번호
     , 부서명
FROM 사원
   , 부서
WHERE 사원.부서번호 = 부서.부서번호
  AND 이름 = '이소미';
/*SCOTT에 응용*/
USE SCOTT;
-- Non-ANSI join, from 정의, -> join, join 조건 -> WHERE
SELECT E.ENAME, E.DEPTNO, D.DNAME, D.LOC
FROM EMP E,
     DEPT D
WHERE E.DEPTNO = D.DEPTNO
  and SAL > 3000;
