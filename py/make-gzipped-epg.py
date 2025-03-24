import gzip
f_in = "..\\epg.xml"
f_out = "..\\epg.xml.gz"
with open(f_in, "rb") as f_input, gzip.open(f_out, "wb") as f_output:
    f_output.write(f_input.read())