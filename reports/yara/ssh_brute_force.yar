rule SSH_Brute_Force
{
    meta:
        author = "CyberLog AI"
        description = "Automatically generated YARA rule"
        severity = "HIGH"

    strings:
        $ip = "192.168.1.10"
        $attack = "None"

    condition:
        any of them
}
