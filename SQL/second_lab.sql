CREATE TABLE ElevatorServiceLogs (
    ID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique ID for each service
    Elevator_ID VARCHAR(50),                -- Elevator identifier
    Service_Date DATE,                      -- Date of service
    Technician VARCHAR(100),                -- Name of the technician
    Service_Type VARCHAR(50),               -- Type of service (e.g., maintenance, repair)
    Status VARCHAR(50),                     -- Status of the service (e.g., completed, pending)
    Cost DECIMAL(10, 2)                     -- Cost of the service
);


INSERT INTO ElevatorServiceLogs (Elevator_ID, Service_Date, Technician, Service_Type, Status, Cost)
VALUES 
    ('E-001', '2024-10-10', 'John Doe', 'Maintenance', 'Completed', 200.00),
    ('E-002', '2024-10-11', 'Jane Smith', 'Repair', 'Pending', 350.00),
    ('E-003', '2024-10-12', 'Alice Johnson', 'Maintenance', 'Completed', 150.00),
    ('E-004', '2024-10-13', 'Bob Brown', 'Repair', 'Completed', 500.00);

-- Retrieve all data from the ElevatorServiceLogs table
SELECT * FROM ElevatorServiceLogs;

-- Retrieve all services that are still pending
SELECT * FROM ElevatorServiceLogs
WHERE Status = 'Pending';

-- Retrieve the average service cost
SELECT AVG(Cost) AS Average_Service_Cost FROM ElevatorServiceLogs;