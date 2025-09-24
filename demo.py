INSERT INTO EmployeeBenefits_Audit (EmployeeID, BenefitType, OldAmount, NewAmount, ChangedOn)
SELECT EmployeeID, BenefitType, CoverageAmount, 600000, GETDATE()
FROM EmployeeBenefits
WHERE BenefitType = 'Health'
  AND Status = 'Active';
