"""Validated traffic ticket input processing for Lab 7."""

import re


_TICKET_ID = re.compile(r"([A-Za-z]{1,10})-([0-9]{4})-([0-9]{1,10})\Z")


def parse_ticket_id(ticket_id):
    """Parse PREFIX-YYYY-SERIAL; raise ValueError for malformed identifiers."""
    if not isinstance(ticket_id, str):
        raise TypeError("ticket_id must be a string")
    match = _TICKET_ID.fullmatch(ticket_id)
    if match is None:
        raise ValueError("ticket ID must match PREFIX-YYYY-SERIAL")
    prefix, year_text, serial_text = match.groups()
    year = int(year_text)
    serial = int(serial_text)
    if year == 0:
        raise ValueError("ticket year must be greater than zero")
    return prefix.upper(), year, serial


def total_fines(amounts_csv):
    """Sum comma-separated, non-negative integer fines, capped at 10,000.

    An empty or whitespace-only string represents no fines and returns zero.
    """
    if not isinstance(amounts_csv, str):
        raise TypeError("amounts_csv must be a string")
    if not amounts_csv.strip():
        return 0
    parts = amounts_csv.split(",")
    amounts = []
    for part in parts:
        token = part.strip()
        if not token or not re.fullmatch(r"[0-9]+", token):
            raise ValueError("fines must be comma-separated non-negative integers")
        amounts.append(int(token))
    return min(sum(amounts), 10000)


def speed_excess(reading):
    """Return whole percent over the limit from a non-negative SPEED/LIMIT."""
    if not isinstance(reading, str):
        raise TypeError("reading must be a string")
    parts = reading.split("/")
    if len(parts) != 2:
        raise ValueError("reading must be SPEED/LIMIT")
    speed_text, limit_text = (part.strip() for part in parts)
    if not re.fullmatch(r"[0-9]+", speed_text) or not re.fullmatch(
        r"[0-9]+", limit_text
    ):
        raise ValueError("speed and limit must be non-negative integers")
    speed = int(speed_text)
    limit = int(limit_text)
    if limit == 0:
        raise ValueError("speed limit must be greater than zero")
    if speed <= limit:
        return 0
    return (speed - limit) * 100 // limit


def main():
    print("==== Running parse_ticket_id ====")
    user_input = input("Enter a ticket ID (e.g. TF-2024-0456): ")
    result = parse_ticket_id(user_input)
    print("Ticket Prefix, Year and Serial:", result)

    print("\n==== Running total_fines ====")
    user_input = input("Enter fine amounts as CSV (e.g. 500,1200,300): ")
    result = total_fines(user_input)
    print("Total Fines:", result)

    print("\n==== Running speed_excess ====")
    user_input = input("Enter speed/limit (e.g. 72/60): ")
    result = speed_excess(user_input)
    print("Percent Over Limit:", result)


if __name__ == "__main__":
    main()
