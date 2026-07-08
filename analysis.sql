-- Monthly Sales Trend
SELECT DATE_FORMAT(Order_Date, '%Y-%m') AS Month, SUM(Sales) AS Total_Sales
FROM Orders
GROUP BY Month
ORDER BY Month;

-- Top 10 Customers by Sales
SELECT Customer_Name, SUM(Sales) AS Total_Sales
FROM Orders
GROUP BY Customer_Name
ORDER BY Total_Sales DESC
LIMIT 10;

-- Profit Margin by Category
SELECT Category, SUM(Profit)/SUM(Sales)*100 AS Profit_Margin_Percentage
FROM Orders
GROUP BY Category
ORDER BY Profit_Margin_Percentage DESC;
