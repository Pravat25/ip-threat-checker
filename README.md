# IP Threat Intelligence Checker

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Cybersecurity](https://img.shields.io/badge/Tool-Threat%20Intelligence-red)
![Status](https://img.shields.io/badge/Status-Active-success)

## Overview

IP Threat Intelligence Checker is a Python-based cybersecurity tool that retrieves information about an IP address and analyzes basic threat indicators.

The tool queries a public IP intelligence API to gather information such as location, ISP, and network type. It then evaluates whether the IP might be suspicious based on indicators like proxy usage or hosting providers.

This project demonstrates **basic threat intelligence analysis**, a common task performed by **Security Operations Center (SOC) analysts during investigations**.

---

## Features

- Lookup detailed information about an IP address
- Retrieve geolocation data (country, region)
- Identify ISP and hosting providers
- Detect potential suspicious indicators
- Generate a simple threat intelligence report

---

## Technologies Used

- Python
- Requests library
- Public IP Intelligence API

---

## Project Structure


ip-threat-checker
│
├── ip_checker.py
└── README.md


---

## Installation

Clone the repository:


git clone https://github.com/Pravat25/ip-threat-checker.git


Navigate into the project directory:


cd ip-threat-checker


Install required dependency:


pip install requests


---

## How to Run

Run the Python script:


python ip_checker.py


When prompted, enter the IP address you want to analyze.

Example:


Enter IP address to check: 8.8.8.8


---

## Example Output


===== IP Intelligence Report =====

IP: 8.8.8.8
Country: United States
Region: California
ISP: Google LLC

No obvious threat indicators


---

## Learning Purpose

This project was created to practice:

- Python API integration
- Threat intelligence lookups
- Security investigation workflows
- Cybersecurity automation

---

## Disclaimer

This tool is created for **educational purposes only** and should not be used for malicious activities.
