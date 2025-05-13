
# ☁️ Cloud Cost Optimizer

A Python-based FinOps automation tool that scans your AWS account to detect **idle EC2 instances** by analyzing **CloudWatch CPU utilization metrics**. It generates a timestamped CSV report you can use to **identify cost-saving opportunities** and eliminate waste in your cloud environment.

> 💡 Built to demonstrate FinOps knowledge and cloud automation skills for potential employers.

---

## 🔍 Features

- ✅ Scans all EC2 instances in your AWS account
- 📉 Detects underutilized resources (e.g., avg CPU < 5% over 24 hours)
- 🧾 Outputs clean, timestamped `.csv` reports
- 🧰 Modular code structure for easy extension (e.g. EBS, S3, tagging)
- 💡 Ideal for rightsizing, cost analysis, and reporting in a FinOps role

---

## 🚀 How to Run

### 1. Install Python Requirements

Ensure you're in the project folder and virtual environment, then:

```bash
pip install -r requirements.txt
```

### 2. Configure AWS CLI

```bash
aws configure
```

Provide your AWS access key, secret, and a valid region like `us-east-1`.

### 3. Run the Tool

```bash
python3 main.py
```

The script will generate a file in the `reports/` folder:

```
reports/idle_instances_20250513.csv
```

---

##Sample Output

CSV file contents:

```
Instance ID,Avg CPU Usage (%)
i-0123456789abcdef0,2.34
i-0abcdef1234567890,0.97
```

---

##Tech Stack

- **Python 3.12**
- [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) – AWS SDK for Python
- **pandas** – for data handling
- **tabulate** – optional, for future CLI reporting

---

##FinOps Relevance

This tool reflects FinOps principles such as:
- **Visibility** – Automated insight into unused compute
- **Optimization** – Reduce cloud waste and improve unit economics
- **Operationalization** – Integrate into CI/CD or schedule via cron/GitHub Actions

---

##Project Structure

```
cloud-cost-optimizer/
├── main.py                # Entry point for scanning EC2 instances
├── requirements.txt       # Python dependencies
├── utils/
│   └── idle_finder.py     # CPU analysis logic
├── reports/               # CSV output saved here
└── README.md              # You're reading it!
```


##Author

**Tamir Kafri Djerassi**  
GitHub: [@tamirkafridjerassi](https://github.com/tamirkafridjerassi)  


---

##License

MIT — feel free to fork, adapt, and use for your own FinOps journey.
