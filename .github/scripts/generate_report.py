import sys
import datetime
from pathlib import Path

def generate_html_report(log_content):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>FusionPact DevOps Challenge - Execution Report</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            line-height: 1.6;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f5f5f5;
        }}
        .header {{
            background-color: #ffffff;
            padding: 20px;
            border-radius: 5px;
            margin-bottom: 20px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        .log-container {{
            background-color: #272822;
            color: #f8f8f2;
            padding: 20px;
            border-radius: 5px;
            overflow-x: auto;
            white-space: pre-wrap;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        h1 {{
            color: #2c3e50;
            margin-bottom: 10px;
        }}
        .timestamp {{
            color: #7f8c8d;
            font-size: 0.9em;
        }}
        .section {{
            margin: 20px 0;
            padding: 20px;
            background-color: #ffffff;
            border-radius: 5px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        h2 {{
            color: #34495e;
            border-bottom: 2px solid #eee;
            padding-bottom: 10px;
        }}
    </style>
</head>
<body>
    <div class="header">
        <h1>Docker Compose Execution Report</h1>
        <p>Generated at: {current_time}</p>
    </div>
    <div class="log-container">
{log_content}
    </div>
</body>
</html>
"""
    return html_content

def main():
    log_content = sys.stdin.read()
    html_report = generate_html_report(log_content)
    
    output_dir = Path("report")
    output_dir.mkdir(exist_ok=True)
    
    with open(output_dir / "index.html", "w", encoding="utf-8") as f:
        f.write(html_report)

if __name__ == "__main__":
    main()