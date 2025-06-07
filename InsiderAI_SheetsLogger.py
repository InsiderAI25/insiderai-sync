def log_to_google_sheets(message):
    from datetime import datetime
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[Sheets Log] {now}: {message}")
    # This is where you'd integrate with Google Sheets API
