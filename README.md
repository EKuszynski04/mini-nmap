# Mini Nmap

A Python-based port scanner built to explore TCP/IP networking and Python socket programming. Mini Nmap replicates basic Nmap functionality TCP and UDP port scanning with custom port ranges using only the Python standard library.

For more in depth documentation read the Mini Nmap Documentation file.

**Authorised use only.** This tool is intended for educational purposes and authorised network testing. Only scan systems you have explicit permission to test. 

---

## What it does

- **TCP port scanning** — open / closed / timeout / error states via `connect_ex`
- **UDP port scanning** — distinguishing replies, ICMP refusals and timeouts
- **Custom port ranges** — user defined min/max with validation
- **Interactive CLI** — step by step prompts with error handling
- **Structured results** — one line per port showing port number and state

**Not included:** vulnerability scanning, scripting, stealth/evasion, packet crafting, OS fingerprinting, service identification, host reachability checks.

---

## How it works

Mini Nmap follows a layered structure:

| Layer | Responsibility |
|---|---|
| `cli/` | Input prompts and output formatting |
| `utils/` | Parsers and validators for user input |
| `models/` | Dataclasses for scan results and configuration |
| `scanner/` | `tcp_scan` and `udp_scan` socket-level scanning logic |
| `controller/` | Orchestrates the flow between CLI, validation, and scanners |

The separation lets the scanner modules be tested in isolation from the CLI, and the validators be tested without touching the network.

### TCP scanning

For each port a TCP socket is created to attempt a connection with connect_ex and classify the outcome:

- `0` → **open**
- `ECONNREFUSED` → **closed**
- `socket.timeout` → **timeout**
- other `errno` → **error**

### UDP scanning

For each port send a ‘MININMAP’ probe and wait for a reply with a timeout:

- reply received → **open**
- `ConnectionRefusedError` (ICMP port unreachable) → **closed**
- `socket.timeout` (no reply) → **timeout**
- other `OSError` → **error**

A new socket is created per port so closed ports and their ICMP responses don't affect subsequent scans.

---

### Requirements

- Python 3.10+
- Windows or Linux

