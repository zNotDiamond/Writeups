What networking constructs are used to direct traffic to the right application on a server?

Answer: `Ports`

How many of these are available on any network-enabled computer?

Answer: `65535`

How many of these are considered "well-known"?

Answer: `1024`

What is the first switch listed in the help menu for a 'Syn Scan'?

Answer: `-sS`

Which switch would you use for a "UDP scan"?

Answer: `-sU`

If you wanted to detect which operating system the target is running on, which switch would you use?

Answer: `-O`

Nmap provides a switch to detect the version of the services running on the target. What is this switch?

Answer: `-sV`

How would you increase the verbosity?

Answer: `-v`

How would you set the verbosity level to two?

Answer: `-vv`

What switch would you use to save the nmap results in three major formats?

Answer: `-oA`

What switch would you use to save the nmap results in a "normal" format?

Answer: `-oN`

How would you save results in a "grepable" format?

Answer: `-oG`

How would you activate aggressive mode?

Answer: `-A`

How would you set the timing template to level 5?

Answer: `-T5`

How would you tell nmap to only scan port 80?

Answer: `-p 80`

How would you tell nmap to scan ports 1000-1500?

Answer: `-p 1000-1500`

How would you tell nmap to scan all ports?

Answer: `-p-`

How would you activate a script from the nmap scripting library?

Answer: `--script`

How would you activate all of the scripts in the "vuln" category?

Answer: `--script=vuln`

Which RFC defines the appropriate behaviour for the TCP protocol?

Answer: `RFC 793`

If a port is closed, which flag should the server send back to indicate this?

Answer: `RST`

There are two other names for a SYN scan, what are they?

Answer: `Half-Open, Stealth`

Can Nmap use a SYN scan without Sudo permissions (Y/N)?

Answer: `N`

If a UDP port doesn't respond to an Nmap scan, what will it be marked as?

Answer: `open|filtered`

When a UDP port is closed, by convention the target should send back a "port unreachable" message. Which protocol would it use to do so?

Answer: `ICMP`

Which of the three shown scan types uses the URG flag?

Answer: `xmas`

Why are NULL, FIN and Xmas scans generally used?

Answer: `Firewall Evasion`

Which common OS may respond to a NULL, FIN or Xmas scan with a RST for every port?

Answer: `Microsoft Windows`

How would you perform a ping sweep on the 172.16.x.x network (Netmask: 255.255.0.0) using Nmap? (CIDR notation)

Answer: `nmap -sn 172.16.0.0/16`

What language are NSE scripts written in

Answer: `Lua`

Which category of scripts would be a very bad idea to run in a production environment?

Answer: `intrusive`

What optional argument can the ftp-anon.nse script take?

Answer: `maxlist`

What is the filename of the script which determines the underlying OS of the SMB server?

Answer: `smb-os-discovery.nse`

What does it depend on?

Answer: `smb-brute`

Which simple (and frequently relied upon) protocol is often blocked, requiring the use of the -Pn switch

Answer: `ICMP`

Which Nmap switch allows you to append an arbitrary length of random data to the end of packets?

Answer: `--data-length`

Does the target respond to ICMP (ping) requests (Y/N)?

Answer: `N`

Perform an Xmas scan on the first 999 ports of the target — how many ports are shown to be open or filtered?

Answer: `999`

There is a reason given for this — what is it?

Answer: `No Response`

Perform a TCP SYN scan on the first 5000 ports of the target — how many ports are shown to be open?

Answer: `5`

Deploy the ftp-anon script against the box. Can Nmap login successfully to the FTP server on port 21? (Y/N)

Answer: `Y`
