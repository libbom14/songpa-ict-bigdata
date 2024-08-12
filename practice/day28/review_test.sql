-- page 163 실습문제
-- 그림 5-3의 한빛무역 ERD를 참고하여 SQL문을 작성하시오.
-- 1. 마일리지 등급명별로 고객수를 보이시오.
-- 2. 주문번호 'H0249'를 주문한 고객의 모든 정보를 보이시오.

-- 3. 2020년 4월 9일에 주문한 고객의 모든 정보를 보이시오.
-- ANSI join
SELECT *
FROM 고객
         JOIN 주문 ON 고객.고객번호 = 주문.고객번호
WHERE 주문.주문일 = '2020-04-09';
-- Non-ANSI join
SELECT 고객.*
FROM 고객,
     주문
WHERE 고객.고객번호 = 주문.고객번호
  and 주문.주문일 = '2020-04-09';

-- 4. 도시별로 주문금액합을 보이되 주문금액합이 많은 상위 5개의 도시에 대한 결과만 보이시오.
-- ANSI join
SELECT 도시, SUM(주문수량 * 단가) 주문금액합
FROM 고객
         JOIN 주문 ON 고객.고객번호 = 주문.고객번호
         JOIN 주문세부 ON 주문.주문번호 = 주문세부.주문번호
GROUP BY 고객.도시
ORDER BY 주문금액합 DESC
limit 5;
-- Non-ANSI join
SELECT 고객.도시, SUM(주문세부.주문수량 * 주문세부.단가) 주문금액합
FROM 고객,
     주문,
     주문세부
WHERE 고객.고객번호 = 주문.고객번호
  and 주문.주문번호 = 주문세부.주문번호
GROUP BY 고객.도시
ORDER BY 주문금액합 DESC
limit 5;
