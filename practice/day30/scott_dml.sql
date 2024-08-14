select @@autocommit;
set autocommit = false;

desc DEPT;
desc EMP;

-- 테이블 데이터 조회
select *
from DEPT;
select *
from EMP;

/* Add rows */
-- (50, '교육팀', '서울') 데이터 INSERT
INSERT INTO DEPT(DEPTNO, DNAME, LOC)
VALUES (50, '교육팀', '서울');
-- autocommit = false인 상태라 commit을 해야 데이터가 확정
commit;
-- 동일한 데이터 INSERT 시도, [23000][1062] Duplicate entry '50' for key dept.PRIMARY 에러 발생
-- (51, '기술팀', '서울') 데이터 INSERT
INSERT INTO DEPT(DEPTNO, DNAME, LOC)
VALUES (51, '기술팀', '서울');
INSERT INTO DEPT(DEPTNO, DNAME, LOC)
VALUES (52, '기술팀', '서울');
-- commit 전 롤백 가능
ROLLBACK;
-- 취소

/* Modify existing rows */
UPDATE DEPT
SET DNAME = '영업팀'
-- WHERE LOC = '서울'; -- unique한 PK를 지정해주는게 좋다.
WHERE DEPTNO = 52;
commit;

/* Delete existing rows */
DELETE
FROM DEPT; -- Unsafe Query.
ROLLBACK;
DELETE
FROM DEPT
WHERE LOC = '서울';
commit;

/*INSERT*/
INSERT INTO EMP -- Column 명을 명시하지 않으면 컬럼 순서대로 데이터를 작성해줘야함
VALUES (9000, '김씨', '사원', null, sysdate(), 0, null, 40);
-- INSERT 시 FK가 존재하지 않으면 에러 발생
-- [23000][1452] Cannot add or update a child row: a foreign key constraint fails (`scott`.`emp`, CONSTRAINT `emp_ibfk_1` FOREIGN KEY (`DEPTNO`) REFERENCES `dept` (`DEPTNO`) ON DELETE CASCADE)
INSERT INTO EMP
VALUES (9001, '이씨', '사원', null, now(), 0, null, 50);

-- (50, '교육팀', '서울') 데이터 INSERT
INSERT INTO DEPT(DEPTNO, DNAME, LOC)
VALUES (50, '교육팀', '서울');
INSERT INTO EMP
VALUES (9001, '이씨', '사원', null, now(), 0, null, 50);

SELECT * FROM EMP;

/*Remove existing rows*/
DELETE FROM DEPT WHERE DEPTNO = 50;
-- 제약 조건 추가
-- FOREIGN KEY (DEPTNO) REFERENCES DEPT (DEPTNO) ON DELETE CASCADE;

