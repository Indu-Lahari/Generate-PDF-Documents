from fpdf import FPDF
import pandas as pd

df = pd.read_csv("topics.csv")

pdf = FPDF(orientation="P", unit="mm", format="A4")

#so pages won't break automatically
pdf.set_auto_page_break(auto=False, margin=0)

for index, row in df.iterrows():
    pdf.add_page()
    #Set the header
    pdf.set_font(family="Times", style="B", size=24)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
    pdf.set_text_color(100, 100, 100)

    #For lined PDF
    for y in range(20, 298, 10):
        pdf.line(10, y, 200, y)
    # Two Lines on top
    pdf.line(10, 21, 200, 21)

    #Set the Footer
    pdf.ln(265)
    pdf.set_font(family="Times", style="I", size=12)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="R")
    pdf.set_text_color(180, 180, 180)

    #nested for-loop
    for i in range(row["Pages"] - 1):
        pdf.add_page()
        # Set the Footer
        pdf.ln(277)
        pdf.set_font(family="Times", style="I", size=12)
        pdf.cell(w=0, h=12, txt=row["Topic"], align="R")
        pdf.set_text_color(180, 180, 180)

        # For lined PDF
        for y in range(20, 298, 10):
            pdf.line(10, y, 200, y)

pdf.output("output.pdf")