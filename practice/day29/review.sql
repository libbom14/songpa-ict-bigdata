-- page 163 실습문제
-- 응용: 도시별 평균 급여 조회

select loc, round(avg(sal)) 평균급여
from emp,
     dept
where emp.deptno = dept.deptno
group by loc;

select loc, round(avg(sal)) 평균급여
from emp
         join dept
              on emp.deptno = dept.deptno
group by loc;