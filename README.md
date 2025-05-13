
# Cloud Cost Optimizer

A Python-based FinOps automation tool that scans your AWS account to detect idle EC2 instances by analyzing CloudWatch CPU utilization metrics. It generates a timestamped CSV report you can use to identify cost-saving opportunities and eliminate waste in your cloud environment.

Built to demonstrate FinOps knowledge and cloud automation skills for potential employers.

---

## Features

- Scans all EC2 instances in your AWS account
- Detects underutilized resources (e.g., avg CPU < 5% over 24 hours)
- Outputs clean, timestamped `.csv` reports
- Modular code structure for easy extension (e.g. EBS, S3, tagging)
- Ideal for rightsizing, cost analysis, and reporting in a FinOps role

---

## How to Run

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
reports/idle_instances_YYYYMMDD.csv
```

---

## Sample Output

CSV file contents:

```
Instance ID,Avg CPU Usage (%)
i-0123456789abcdef0,2.34
i-0abcdef1234567890,0.97
```

---

## Tech Stack

- Python 3.12
- boto3 – AWS SDK for Python
- pandas – for data handling
- tabulate – optional, for future CLI reporting

---

## FinOps Relevance

This tool reflects FinOps principles such as:

- Visibility – Automated insight into unused compute
- Optimization – Reduce cloud waste and improve unit economics
- Operationalization – Integrate into CI/CD or schedule via GitHub Actions

---

## Project Structure

```
cloud-cost-optimizer/
├── main.py                # Entry point for scanning EC2 instances
├── requirements.txt       # Python dependencies
├── utils/
│   └── idle_finder.py     # CPU analysis logic
├── reports/               # CSV output saved here
└── README.md              # You're reading it!
```

---

## GitHub Actions Template

This project includes a GitHub Actions workflow for running the EC2 idle scan automatically.

- File: `.github/workflows/cost-audit-template.yml`
- Runs: Only when manually triggered
- Requires: AWS credentials stored in `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`

To use this in your own fork:

1. Go to Settings → Secrets → Actions
2. Add your AWS credentials as secrets
3. Navigate to the Actions tab and run the workflow manually

---

## Roadmap / Next Steps

- [ ] Add EBS and RDS idle checks
- [ ] Integrate Slack or email alerts
- [ ] Schedule daily/weekly runs with GitHub Actions
- [ ] Create dashboard view (Streamlit or Jupyter)

---

## Author

Tamir Kafri  
GitHub: [@tamirkafridjerassi](https://github.com/tamirkafridjerassi)

---

## License

MIT — feel free to fork, adapt, and use for your own FinOps journey.
