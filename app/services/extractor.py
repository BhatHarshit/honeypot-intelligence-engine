# app/services/extractor.py
import re

def extract_upi(message: str) -> list:
    """Extract UPI IDs like example@upi"""
    pattern = r"[\w.-]+@[\w]+"
    return re.findall(pattern, message)

def extract_bank_accounts(message: str) -> list:
    """Extract bank account numbers (9-18 digits)"""
    pattern = r"\b\d{9,18}\b"
    return re.findall(pattern, message)

def extract_links(message: str) -> list:
    """Extract URLs"""
    pattern = r"https?://\S+"
    return re.findall(pattern, message)

def extract_all(message: str) -> dict:
    """Extract all intelligence in one dict"""
    return {
        "upi_ids": extract_upi(message),
        "bank_accounts": extract_bank_accounts(message),
        "links": extract_links(message)
    }

# Optional local test
if __name__ == "__main__":
    test_msg = "Send ₹5000 to rahul@ybl or 123456789012. Click here: http://fake-kyc.in"
    print(extract_all(test_msg))
