select * into #temp1
from [dbo].[EmployeeRecords]

select * from #temp1

select * from EmployeeRecords
where EmployeeID = 3

select EmployeeID,FirstName,Department from EmployeeRecords
where EmployeeID = 3

select * from [dbo].[EmployeeRecords] where Salary>=70000.00

select distinct FirstName,Salary,Department from [dbo].[EmployeeRecords] 
where Salary<70000.00

select * from [dbo].[Employees]

select distinct FirstName,LastName from [dbo].[Employees]