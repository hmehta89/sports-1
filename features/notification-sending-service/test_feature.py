import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from src.notification import Notification


def main():
    n1 = Notification(message="Your booking is confirmed!")
    n1.send("alice@example.com")

    n2 = Notification(message="Payment of $120.00 received.")
    n2.send("bob@example.com")

    n3 = Notification(message="Your show starts in 30 minutes.")
    n3.send("carol@example.com")

    print("All notifications sent.")


if __name__ == "__main__":
    main()
