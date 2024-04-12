# Electricity Bill Calculator

This Python program calculates electricity bills based on the provided rate sheet and user input for past and current kWh usage.

## Description

The electricity bill calculator program takes past and current kWh usage as input from the user and calculates the bill amount using a predefined rate sheet. 
It then displays the calculated bill amount for the specified usage.

**This Program Fuly Based on TNEB CHARGES only ,Not Liable for other Providers**

## Rate Sheet

The rate sheet contains the following information:

| From Unit | To Unit | Rate (Rs.) | Max. Unit |
|-----------|---------|------------|-----------|
| 1         | 100     | 0          | 500       |
| 101       | 200     | 2.25       | 500       |
| 201       | 400     | 4.5        | 500       |
| 401       | 500     | 6          | 500       |
| 1         | 100     | 0          | 9999999   |
| 101       | 400     | 4.5        | 9999999   |
| 401       | 500     | 6          | 9999999   |
| 501       | 600     | 8          | 9999999   |

## Usage

To use the program:

1. Run the Python Program.
2. Enter the past kWh usage when prompted.
3. Enter the current kWh usage when prompted.
4. The program will calculate and display the bill amount for the specified usage.

Example:

Enter past kWh used: 17209
Enter current kWh used: 17596
Bill amount for 387 units: Rs. 1066.50
