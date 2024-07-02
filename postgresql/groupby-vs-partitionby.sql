INSERT INTO transactions (transaction_id, customer_id, account_id, transaction_date, transaction_amount, transaction_type) VALUES (16, 101, 1001, CAST('2024-01-01' AS Date), CAST(-430.00 AS Decimal(10, 2)),'deposit');
SELECT *
FROM transactions

SELECT customer_id, SUM(transaction_amount) AS total_amount
FROM transactions
GROUP BY customer_id;

SELECT account_id, COUNT(*) AS transaction_count
FROM transactions
GROUP BY account_id;

SELECT
    customer_id,
    SUM(transaction_amount) AS total_amount
FROM transactions
GROUP BY customer_id;

SELECT
    customer_id,
    account_id,
    transaction_date,
    transaction_amount,
    transaction_type,
    SUM(transaction_amount) OVER(PARTITION BY customer_id, transaction_type) AS total_amount_per_customer
FROM transactions;

SELECT 
transaction_id, 
customer_id, 
transaction_amount, 
RANK() OVER(PARTITION BY customer_id ORDER BY transaction_amount DESC) AS transaction_rank
FROM transactions;

SELECT 
transaction_id,
customer_id,
transaction_amount, 
SUM(transaction_amount) OVER(PARTITION BY customer_id ORDER BY transaction_date) AS running_total
FROM transactions;