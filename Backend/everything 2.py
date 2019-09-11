#!/usr/bin/python
import daily_announcements
import sports_results
import update_daily_announcements_excel

def main():
    daily_announcements.main()
    update_daily_announcements_excel.main()
    sports_results.main()

if __name__ == '__main__':
    main()
