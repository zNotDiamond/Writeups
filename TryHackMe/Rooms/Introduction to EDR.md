#TryHackMe

Which feature of EDR provides a complete context for all the detections?

Answer: `Visibility`

Which process spawned sc.exe?

Answer: `cmd.exe`

Which component of the EDR is responsible for collecting telemetry from the endpoints?

Answer: `Agent`

An EDR agent is also known as a?

Answer: `Sensor`

Endpoint Detection and Response (EDR) extends beyond traditional antivirus by providing continuous endpoint telemetry, behavioral and anomaly detection, IOC-based matching, ATT&CK mapping, and powerful response actions such as host isolation, process termination, quarantine, remote shell, and artifact collection.

Core idea: EDR continuously monitors endpoints, detects advanced threats, and provides rich context with process trees, timelines, and historical visibility.

Three pillars: Visibility, Detection, Response.

Visibility includes process/registry/file/user activity and process trees to reconstruct the attack story; detections blend signatures, behavior, and ML; response enables isolation, kill, quarantine, remote access.

IOC matching: correlates with known malicious hashes/domains/URLs.
MITRE ATT&CK mapping: contextualizes tactics and techniques.
Machine learning: detects complex/fileless/multi-stage patterns.

Response capabilities:

- Isolate host, terminate process, quarantine files, remote shell, artifact collection (memory, logs, folders, registry hives).
