from utils.idle_finder import find_idle_instances
import csv
from datetime import datetime

def main():
    idle = find_idle_instances()
    report_path = f'reports/idle_instances_{datetime.now().strftime("%Y%m%d")}.csv'
    with open(report_path, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['Instance ID', 'Avg CPU Usage (%)'])
        writer.writerows(idle)

if __name__ == "__main__":
    main()
