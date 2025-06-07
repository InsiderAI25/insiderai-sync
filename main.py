from InsiderAI_SheetsLogger import log_to_google_sheets
from InsiderAI_TriggerAlert import trigger_monique_alert

def main():
    log_to_google_sheets("Daily sync started.")
    trigger_monique_alert("Daily sync completed successfully.")

if __name__ == "__main__":
    main()
