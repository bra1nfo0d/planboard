import datetime as dt

def main():
	pass

def get_date_str(day=0, language="de"):
	tday = dt.date.today()
	date = str(tday + dt.timedelta(day))
	print(f"{date[8:]}.{date[5:7]}.{date[:4]}")
	if language == "de":
		return f"{date[8:]}.{date[5:7]}.{date[:4]}"

def get_date_str_list(week=0, language="de"):
	date_list = []
	tday = dt.date.today()
	weekday = dt.date.today().weekday()
	date_weekday0 = tday - dt.timedelta(weekday) + dt.timedelta(week * 7)
	if language == "de":
		for i in range(8):
			date = str(date_weekday0 + dt.timedelta(i))
			date_list.append(f"{date[8:]}.{date[5:7]}.{date[:4]}")
		return date_list

def get_callender_week_str(week=0, language="de"):
	tday = dt.date.today()
	week_target = tday + dt.timedelta(week * 7)
	callender_week = week_target.isocalendar().week
	if language == "de":
		return f"KW {callender_week}"


if __name__ == "__main__":
	main()