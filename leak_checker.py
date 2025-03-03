import argparse

if __name__ == '__main__':
	parser = argparse.ArgumentParser(
		prog='leak_checker.py',
		description="""
OSINT Credential Leak & Domain Security Scanner

Credential Leaks	Checks if an email or username has been found in data breaches.
Domain Security		Scans a domain for misconfigurations, exposed services, and security risks.

Select specific checks using flags or use --all to run everything.""",
		formatter_class=argparse.RawTextHelpFormatter)

	parser.add_argument('-a', '--all', action='store_true', help="Run all scans")

	args = parser.parse_args()
