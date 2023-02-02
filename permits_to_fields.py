# convert permits*.csv to
# 1. 60ft_fields.csv
# 2. 90ft_fields.csv
import sys
import csv

lw1 = "lw1"
whitman = "whitman"
loyal_heights_1 = "loyal heights 1"
eagle_staff_90 = "eagle staff 90"

fields = {
    "Eagle Staff Middle School Baseball Field": eagle_staff_90,
    "Eagle Staff Middle School Softball Field": "eagle staff 60",
    "Lower Woodland Playfield Ballfield 01": lw1,
    "Lower Woodland Playfield Ballfield 03": "lw3",
    "Lower Woodland Playfield Ballfield 04": "lw4",
    "Lower Woodland Playfield Ballfield 05": "lw5",
    "Lower Woodland Playfield Ballfield 06": "lw5",
    "Loyal Heights Playfield Ballfield 01": loyal_heights_1,
    "Ross Playfield Lower Ballfield": "ross",
    "B F Day Playfield Ballfield": "bfday",
    "Whitman Middle School Baseball": whitman,
}

days = {
    "Monday": "Mon",
    "Tuesday": "Tue",
    "Wednesday": "Wed",
    "Thursday": "Thu",
    "Friday": "Fri",
    "Saturday": "Sat",
    "Sunday": "Sun",
}


def date_without_year(date):
    return date.split(",")[0]


def is_90ft_field(field_name):
    return fields[field_name] in (eagle_staff_90, lw1, whitman, loyal_heights_1)


def create_fields_csvfile(rows, filename):
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f, delimiter=",")
        writer.writerow(["Date", "Day", "Permit", "Field"])
        for row in rows:
            writer.writerow(
                [date_without_year(row[0]), days[row[1]], row[3], fields[row[4]]]
            )


def get_rows_for_both_fields(permits_filename):
    ninety_foot_rows = []
    sixty_foot_rows = []
    with open(permits_filename, "r", newline="") as f:
        reader = csv.reader(f, delimiter="\t")
        next(reader)  # Ignore the first row
        for row in reader:
            field_name = row[4]
            if is_90ft_field(field_name):
                ninety_foot_rows.append(row)
            else:
                sixty_foot_rows.append(row)
    return sixty_foot_rows, ninety_foot_rows


if __name__ == "__main__":
    assert len(sys.argv) == 2
    permits_filename = sys.argv[1]

    sixty_foot_rows, ninety_foot_rows = get_rows_for_both_fields(permits_filename)
    create_fields_csvfile(sixty_foot_rows, "fields/fields_60ft.csv")
    create_fields_csvfile(ninety_foot_rows, "fields/fields_90ft.csv")