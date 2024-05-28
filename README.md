# Python Trading Bot using Ploygon.io

![Project Logo](https://topflightapps.com/wp-content/uploads/2022/03/crypto-trading-bot-concept.png)

## Table of Contents
- [Overview](#overview)
- [Description](#Description)
- [ClientRequirement](#ClientRequirement)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Overview
This repo contains a python script which retrieves realtime trading data from the ploygon.io api and apply some simple strategies on top of it

## ClientRequirement
Could you please ensure that our monitoring system accurately checks for the predefined conditions, such as "Above 2%" for APPLE and "Monthly Low" for QCOM? Additionally, could you provide insights into any buy or sell suggestions based on the current conditions observed for these stocks?

## Description
- The provided text outlines a strategy for monitoring stock performance and making buy or sell decisions based on specific criteria. Using data from polygon.io, the strategy involves tracking stocks listed in an Excel sheet every 10 seconds. Specific conditions are set for stocks like APPLE and QCOM, including percentage increases, weekly highs and lows, monthly lows, and moving averages. If APPLE's value rises above 2% and QCOM hits a monthly low, the strategy suggests buying APPLE stocks and selling QCOM stocks. This approach aims to dynamically update an Excel sheet and guide investment decisions based on real-time data analysis.


```bash
# Clone the repository
git clone https://github.com/your-username/your-repo-name.git

# Navigate to the project directory
cd your-repo-name

# Install dependencies
pip install -r requirements.txt
