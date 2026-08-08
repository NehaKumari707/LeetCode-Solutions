-- Last updated: 8/8/2026, 5:21:07 PM
# Write your MySQL query statement below
SELECT patient_id, patient_name, conditions
FROM Patients
WHERE conditions LIKE 'DIAB1%' 
   OR conditions LIKE '% DIAB1%';