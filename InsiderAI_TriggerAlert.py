def trigger_monique_alert(message):
    from datetime import datetime
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[Monique Alert] {now}: {message}")
    # This is where you'd trigger Monique or send email alert
