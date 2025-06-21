def read_failed_logins():
    import win32evtlog

    log_type = 'Security'
    event_id = 4625
    failed_logins = []

    # Open the event log
    hand = win32evtlog.OpenEventLog(None, log_type)

    # Read the event log
    total_events = win32evtlog.GetNumberOfEventLogRecords(hand)

    for i in range(total_events):
        try:
            events = win32evtlog.ReadEventLog(hand, win32evtlog.EVENTLOG_FORWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ, 0)
            for event in events:
                if event.EventID == event_id:
                    timestamp = event.TimeGenerated.Format()
                    username = event.StringInserts[0] if event.StringInserts else 'Unknown'
                    ip_address = event.StringInserts[1] if len(event.StringInserts) > 1 else 'Unknown'
                    failure_reason = event.StringInserts[2] if len(event.StringInserts) > 2 else 'Unknown'
                    failed_logins.append({
                        'timestamp': timestamp,
                        'username': username,
                        'ip_address': ip_address,
                        'failure_reason': failure_reason
                    })
        except Exception as e:
            break

    return failed_logins