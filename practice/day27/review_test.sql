-- page 125 실습문제
USE 한빛무역;
-- 1. 제품번호별로 주문수량합과 주문금액합을 보이시오.
SELECT 제품번호
     , SUM(주문수량)      as 주문수량
     , SUM(단가 * 주문수량) as 주문금액합
FROM 주문세부
GROUP BY 제품번호;

-- 2. 주문번호별로 주문된 제품번호의 목록과 주문금액합을 보이시오.
SELECT 주문번호
     , GROUP_CONCAT(제품번호) as 제품번호
     , SUM(단가 * 주문수량)     as 주문금액합
FROM 주문세부
GROUP BY 주문번호;

-- 3. 2021년 주문내역에 대하여 고객번호별로 주문건수를 보이되, 주문건수가 많은 상위 3건의 고객의 정보만 보이시오.
SELECT 고객번호
     , COUNT(*) as 주문건수
FROM 주문
WHERE YEAR(주문일) = 2021
GROUP BY 고객번호
ORDER BY 주문건수 DESC
LIMIT 3;

-- 4. 직위별로 사원수와 사원이름 목록을 보이시오.
SELECT 직위
     , COUNT(*)         as 사원수
     , GROUP_CONCAT(이름) as 사원이름목록
FROM 사원
GROUP BY 직위;