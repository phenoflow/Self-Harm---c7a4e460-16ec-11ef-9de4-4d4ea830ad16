# Matthew J Carr, Sarah Steeg, Roger T Webb, Nav Kapur, Carolyn A Chew-Graham, Kathrym M Abel, Holly Hope, Matthias Pierce, Darren M. Ashcroft, 2024.

import sys, csv, re

codes = [{"code":"SyuFc00","system":"readv2"},{"code":"SyuFH00","system":"readv2"},{"code":"TK3y.00","system":"readv2"},{"code":"TK71.00","system":"readv2"},{"code":"ZX1L900","system":"readv2"},{"code":"TK02.00","system":"readv2"},{"code":"SyuFJ00","system":"readv2"},{"code":"SLX..00","system":"readv2"},{"code":"ZX1L911","system":"readv2"},{"code":"SyuFL00","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('self-harm-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["self-harm-tooth---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["self-harm-tooth---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["self-harm-tooth---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
