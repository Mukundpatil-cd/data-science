

select * from [dbo].[Employees] 
where not FirstName = 'jane' and not Department = 'IT'

select  * from [dbo].[EmployeeRecords]
where Salary between 50000 and 60000 or LastName = 'davis' 

select * from [dbo].[EmployeeRecords]
where not Salary between 50000 and 75000

select * from [dbo].[EmployeeRecords]
where Department in ('HR','IT')

select * from [dbo].[EmployeeRecords]
where Department not in ('HR','IT')
