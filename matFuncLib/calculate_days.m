function calculate_days (together, startdate)
% Input: together=1 if true, else if not together then argument = 0
%        start date as string, in the format day-months-year, eg: '25-June-2021'
% Output: Prints the number of days

if together == 1
    d1 = datetime('today');
    days = caldays(between(datetime(startdate),d1,'days'));
    fprintf('Then we are together for: %d days\n', days);
else
    fprintf('Open this next time\n');
end

end