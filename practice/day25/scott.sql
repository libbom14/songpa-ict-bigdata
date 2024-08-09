DROP DATABASE IF EXISTS scott;

CREATE DATABASE scott ;

USE scott;

drop table if exists DEPT ;
CREATE TABLE DEPT
       (DEPTNO int PRIMARY KEY,
	DNAME VARCHAR(14) ,
	LOC VARCHAR(13) ) ;

drop table if exists EMP ;
CREATE TABLE EMP
       (EMPNO int PRIMARY KEY,
	ENAME VARCHAR(10),
	JOB VARCHAR(9),
	MGR int,
	HIREDATE DATE,
	SAL int,
	COMM int,
	DEPTNO int ,
	FOREIGN KEY (DEPTNO) REFERENCES DEPT (DEPTNO) ON DELETE CASCADE

	);

INSERT INTO DEPT VALUES
	(10,'ACCOUNTING','NEW YORK');
INSERT INTO DEPT VALUES (20,'RESEARCH','DALLAS');
INSERT INTO DEPT VALUES
	(30,'SALES','CHICAGO');
INSERT INTO DEPT VALUES
	(40,'OPERATIONS','BOSTON');

INSERT INTO EMP VALUES
(7369,'SMITH','CLERK',7902,'2000-12-19',800,NULL,20);

INSERT INTO EMP VALUES
(7499,'ALLEN','SALESMAN',7698,'2001-2-22',1600,300,30);
INSERT INTO EMP VALUES
(7521,'WARD','SALESMAN',7698,'2009-12-2',1250,500,30);
INSERT INTO EMP VALUES
(7566,'JONES','MANAGER',7839,'2003-2-4',2975,NULL,20);

INSERT INTO EMP VALUES
(7654,'MARTIN','SALESMAN',7698,'1999-9-9',1250,1400,30);

INSERT INTO EMP VALUES
(7698,'BLAKE','MANAGER',7839,'2003-12-11',2850,NULL,30);

INSERT INTO EMP VALUES
(7782,'CLARK','MANAGER',7839,'2009-1-4',2450,NULL,10);
INSERT INTO EMP VALUES
(7788,'SCOTT','ANALYST',7566,'2013-2-24',3000,NULL,20);
INSERT INTO EMP VALUES
(7839,'KING','PRESIDENT',NULL,'2011-12-4',5000,NULL,10);
INSERT INTO EMP VALUES
(7844,'TURNER','SALESMAN',7698,'2012-2-14',1500,0,30);
INSERT INTO EMP VALUES
(7876,'ADAMS','CLERK',7788,'2003-3-4',1100,NULL,20);
INSERT INTO EMP VALUES
(7900,'JAMES','CLERK',7698,'2009-2-14',950,NULL,30);
INSERT INTO EMP VALUES
(7902,'FORD','ANALYST',7566,'2005-2-4',3000,NULL,20);

INSERT INTO EMP VALUES
(7934,'MILLER','CLERK',7782,'2013-12-4',1300,NULL,10);

drop table if exists BONUS ;
CREATE TABLE BONUS
	(
	ENAME VARCHAR(10)	,
	JOB VARCHAR(9)  ,
	SAL int,
	COMM int
	) ;

drop table if exists SALGRADE ;
CREATE TABLE SALGRADE
      ( GRADE int,
	LOSAL int,
	HISAL int );
INSERT INTO SALGRADE VALUES (1,700,1200);
INSERT INTO SALGRADE VALUES (2,1201,1400);
INSERT INTO SALGRADE VALUES (3,1401,2000);
INSERT INTO SALGRADE VALUES (4,2001,3000);
INSERT INTO SALGRADE VALUES (5,3001,9999);
COMMIT;
