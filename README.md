
# Cloud Cost Optimizer

A Python-based FinOps automation tool that scans your AWS account to detect cost inefficiencies including:
- Idle EC2 instances (low CPU usage)
- Unattached EBS volumes (billed but unused)

The tool generates timestamped CSV reports that help FinOps practitioners identify and eliminate cloud waste.

---

## Features

- Scans EC2 instances for low CPU usage (default: < 5% over 24 hours)
- Detects unattached EBS volumes (status: 'available')
- Generates CSV reports with timestamped filenames
- Clean, modular Python structure
- Safe read-only use of AWS APIs (does not delete or modify resources)

---

## How to Run

### 1. Install Python Requirements

```bash
pip install -r requirements.txt
```

### 2. Configure AWS CLI

```bash
aws configure
```

Provide your AWS access key, secret key, and region (e.g., `us-east-1`).

### 3. Run the Tool

```bash
python3 main.py
```

---

## Output

Reports are saved to the `reports/` folder with today's date.

### Example 1: Idle EC2 Instances

`reports/idle_instances_YYYYMMDD.csv`:

```
Instance ID,Avg CPU Usage (%)
i-0123456789abcdef0,2.34
i-0abcdef1234567890,0.97
```

### Example 2: Unattached EBS Volumes

`reports/unattached_volumes_YYYYMMDD.csv`:

```
VolumeId,Size(GiB),CreateTime,AvailabilityZone,Tags
vol-0a1b2c3d4e5f6g7h,50,2024-12-01 14:22:10,us-east-1a,"{'Name': 'backup'}"
```

---

## Tech Stack

- Python 3.12
- boto3 – AWS SDK for Python
- pandas – for data handling
- tabulate – optional

---

## FinOps Relevance

This tool helps cloud teams and FinOps practitioners:
- Gain visibility into underused and forgotten cloud resources
- Reduce waste and improve cost-efficiency
- Automate daily or weekly audits with GitHub Actions

---

## Project Structure

```
cloud-cost-optimizer/
├── main.py                        # Entry point
├── requirements.txt               # Python dependencies
├── utils/
│   ├── idle_finder.py             # EC2 logic
│   └── ebs_checker.py             # EBS logic
├── reports/                       # CSV reports
└── .github/workflows/             # GitHub Actions workflows
```

---

## GitHub Actions Template

This project includes a GitHub Actions workflow for scheduled automation.

- File: `.github/workflows/cost-audit-template.yml`
- Run type: Manual only (does not run automatically)
- Requires: GitHub repository secrets `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`

To use it in your own fork:

1. Go to Settings → Secrets → Actions
2. Add AWS credentials as secrets
3. Go to the Actions tab and trigger the workflow manually

---

## Author

Tamir Kafri  
GitHub: [@tamirkafridjerassi](https://github.com/tamirkafridjerassi)

---

## License

MIT — fork, adapt, and improve.
